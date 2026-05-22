import { Component, OnInit, inject, signal, computed, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { LessonDetail } from '../../core/models/lesson.model';
import { LessonService } from '../../core/services/lesson.service';
import { SpeechService } from '../../core/services/speech.service';
import { ExampleCardComponent } from './components/example-card/example-card';
import { ExerciseCardComponent } from './components/exercise-card/exercise-card';

export interface StructureRow {
  /** '+' | '-' | '?' | 'tip' | 'info' | 'pattern' */
  type: string;
  /** Human-readable label: "Affirmative", "Negative", etc. */
  label: string;
  /** The grammatical formula text */
  formula: string;
}

@Component({
  selector: 'app-lesson',
  imports: [RouterModule, ExampleCardComponent, ExerciseCardComponent],
  templateUrl: './lesson.html',
  styleUrl: './lesson.scss',
  encapsulation: ViewEncapsulation.None,
})
export class LessonComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly lessonService = inject(LessonService);
  private readonly speechService = inject(SpeechService);

  readonly lesson = signal<LessonDetail | null>(null);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);

  readonly from = signal<string | null>(null);
  readonly fromTopicId = signal<string | null>(null);
  readonly fromLevelId = signal<number | null>(null);
  readonly fromTab = signal<string | null>(null);

  /**
   * Split the description into segments. We first split by newline,
   * then further split each line by sentence boundaries, so that
   * "Structure (+): … Structure (-): …" on one line becomes two segments.
   */
  private get rawSegments(): string[] {
    const description = this.lesson()?.description;
    if (!description) return [];

    // Split by newline first
    const byNewline = description.split('\n').map((l) => l.trim()).filter(Boolean);

    // For each line, split further on '. ' boundaries but PRESERVE "Structure (?)"
    // We need to split before "Structure" but keep the content together.
    const segments: string[] = [];
    for (const line of byNewline) {
      // Split before "Structure (" so each structure stays on its own segment
      const parts = line.split(/(?=\bStructure\s*\([+\-?]\))/);
      for (const part of parts) {
        // Also split on '. ' boundaries that are NOT inside a Structure segment
        if (/^Structure\s*\([+\-?]\)/i.test(part.trim())) {
          segments.push(part.trim().replace(/\.\s*$/, ''));
        } else {
          // For non-structure parts, split on '. ' to separate individual sentences
          const sentences = part.split(/\.\s+/).map((s) => s.trim()).filter(Boolean);
          segments.push(...sentences);
        }
      }
    }

    return segments;
  }

  // ─── Structure rows parsed from "Structure (+/-/?): …" segments ─────────
  readonly structureRows = computed<StructureRow[]>(() => {
    const rows: StructureRow[] = [];

    for (const seg of this.rawSegments) {
      // Matches: "Structure (+):", "Structure (-):", "Structure (?):"
      const structMatch = seg.match(/^Structure\s*\(([+\-?])\)\s*:\s*(.+)/i);
      if (structMatch) {
        const symbol = structMatch[1];
        const labelMap: Record<string, string> = {
          '+': 'Affirmative',
          '-': 'Negative',
          '?': 'Interrogative',
        };

        // Split off trailing "Key contrast/markers/adverbs" from the formula
        let formula = structMatch[2].trim();
        const tipKeywords = /\b(Key contrast|Key markers|Key adverbs|Key connectors|Contraction):/i;
        const tipSplit = formula.search(tipKeywords);
        let tipText: string | null = null;
        if (tipSplit !== -1) {
          tipText = formula.slice(tipSplit).replace(/\.\s*$/, '');
          formula = formula.slice(0, tipSplit).replace(/\.\s*$/, '').trim();
        }

        rows.push({
          type: symbol,
          label: labelMap[symbol] ?? symbol,
          formula: formula.replace(/\.\s*$/, ''),
        });

        // Emit the trailing key note as a tip row
        if (tipText) {
          rows.push({ type: 'tip', label: 'Key Notes', formula: tipText });
        }
        continue;
      }

      // Verb-form reference rows (Infinitive, Past Participle, etc.)
      if (/\b(Infinitive|Past Participle|Gerund)\b.*\b(Past Simple|base form|verb\s*\+\s*-ing)\b/i.test(seg)) {
        rows.push({ type: 'info', label: 'Verb Forms', formula: seg });
        continue;
      }

      // Inversion / advanced pattern: "Pattern —"
      if (/Pattern\s*[—–-]/i.test(seg)) {
        rows.push({
          type: 'pattern',
          label: 'Pattern',
          formula: seg.replace(/Pattern\s*[—–-]\s*/i, ''),
        });
        continue;
      }

      // Key adverbs / markers / triggers / contrast
      if (/^(?:Common triggers|Key markers|Key adverbs|Key connectors|Key contrast):/i.test(seg)) {
        rows.push({ type: 'tip', label: 'Key Notes', formula: seg });
        continue;
      }

      // Contraction notes e.g. "Contraction: 'll."
      if (/^(?:Contraction):/i.test(seg)) {
        rows.push({ type: 'tip', label: 'Contraction', formula: seg });
      }
    }

    return rows;
  });

  // ─── Plain text blocks (non-structural explanation) ───────────────────────
  readonly textBlocks = computed(() => {
    return this.rawSegments.filter((seg) => {
      // Exclude anything that became a structure row
      if (/^Structure\s*\([+\-?]\)/i.test(seg)) return false;
      if (/\b(Infinitive|Past Participle|Gerund)\b.*\b(Past Simple|base form|verb\s*\+\s*-ing)\b/i.test(seg)) return false;
      if (/Pattern\s*[—–-]/i.test(seg)) return false;
      if (/^(?:Common triggers|Key markers|Key adverbs|Key connectors|Key contrast|Contraction):/i.test(seg)) return false;
      return true;
    });
  });

  /**
   * Safe text parsing to split bold (**), code (`), and italic (*) markers.
   * Completely complies with strict Separation of Concerns, eliminating innerHTML.
   */
  parseTextSegments(text: string): Array<{ text: string; type: 'plain' | 'bold' | 'code' | 'italic' }> {
    if (!text) return [];
    
    // Split text by bold (**...**), code (`...`), and italic (*...*) markers
    const regex = /(\*\*.*?\*\*|`.*?`|\*.*?\*)/g;
    const parts = text.split(regex);
    
    return parts.map(part => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return { text: part.slice(2, -2), type: 'bold' as const };
      } else if (part.startsWith('`') && part.endsWith('`')) {
        return { text: part.slice(1, -1), type: 'code' as const };
      } else if (part.startsWith('*') && part.endsWith('*')) {
        return { text: part.slice(1, -1), type: 'italic' as const };
      } else {
        return { text: part, type: 'plain' as const };
      }
    }).filter(p => p.text !== '');
  }

  /**
   * Splits a structured card string "Title | Formula | Example" into distinct parts.
   */
  splitCardItem(item: string): { title: string; formula?: string; example?: string } {
    if (!item) return { title: '' };
    const parts = item.split('|').map(p => p.trim());
    if (parts.length >= 3) {
      return { title: parts[0], formula: parts[1], example: parts[2] };
    } else if (parts.length === 2) {
      return { title: parts[0], formula: parts[1] };
    } else {
      return { title: parts[0] };
    }
  }

  /**
   * Splits a structured grid card string "Main | Pronunciation | Translation" into distinct parts.
   */
  splitGridItem(item: string): { main: string; pronunciation?: string; translation?: string } {
    if (!item) return { main: '' };
    const parts = item.split('|').map(p => p.trim());
    if (parts.length >= 3) {
      return { main: parts[0], pronunciation: parts[1], translation: parts[2] };
    } else if (parts.length === 2) {
      return { main: parts[0], pronunciation: parts[1] };
    } else {
      return { main: parts[0] };
    }
  }

  /**
   * Cleans text from markdown and custom formatting, handles bracketed placeholders
   * like [number], [year], etc., and pronounces the phrase.
   */
  speakText(text: string): void {
    if (!text) return;
    
    // Clean markdown bold, italic, and code formatting
    let clean = text.replace(/\*\*|`|\*/g, '');
    
    // Replace bracketed placeholders with natural spoken equivalents
    clean = clean.replace(/\[number\]/gi, 'number')
                 .replace(/\[year\]/gi, 'year')
                 .replace(/\[noun\]/gi, 'noun')
                 .replace(/\[verb\]/gi, 'verb');
    
    // Clean any remaining brackets
    clean = clean.replace(/[\[\]]/g, '').trim();
    
    // Filter out redundant numeric prefixes followed by spelling (e.g., "0 zero" -> "zero", "10 ten" -> "ten")
    const numberWordMatch = clean.match(/^(\d+)\s*[-:]?\s*([a-zA-Z\s/]+)$/);
    if (numberWordMatch) {
      clean = numberWordMatch[2];
    }
    
    this.speechService.speak(clean);
  }

  /**
   * Smartly pronounces a table cell's English text, or speaks the row's primary English term
   * if the cell represents a Spanish translation.
   */
  speakTableCell(cellText: string, columnIndex: number, headers: string[], rowCells: string[]): void {
    const header = (headers[columnIndex] || '').toLowerCase();
    
    // If it's a translation or Spanish column, speak the main term (index 0) of the row instead
    if (
      header.includes('spanish') || 
      header.includes('meaning') || 
      header.includes('translation') || 
      header.includes('significance') || 
      header.includes('explanation')
    ) {
      const mainTerm = rowCells[0] || '';
      this.speakText(mainTerm);
    } else {
      this.speakText(cellText);
    }
  }

  ngOnInit(): void {
    const lessonId = Number(this.route.snapshot.paramMap.get('lessonId'));

    this.from.set(this.route.snapshot.queryParamMap.get('from'));
    this.fromTopicId.set(this.route.snapshot.queryParamMap.get('topicId'));
    const lvlId = this.route.snapshot.queryParamMap.get('levelId');
    this.fromLevelId.set(lvlId ? Number(lvlId) : null);
    this.fromTab.set(this.route.snapshot.queryParamMap.get('tab'));

    this.lessonService.getLesson(lessonId).subscribe({
      next: (data) => {
        this.lesson.set(data);
        this.isLoading.set(false);
      },
      error: () => {
        this.error.set('Error al cargar la lección.');
        this.isLoading.set(false);
      },
    });
  }
}
