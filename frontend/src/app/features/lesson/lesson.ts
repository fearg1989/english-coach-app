import { Component, OnInit, inject, signal, computed } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { LessonDetail } from '../../core/models/lesson.model';
import { LessonService } from '../../core/services/lesson.service';
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
})
export class LessonComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly lessonService = inject(LessonService);

  readonly lesson = signal<LessonDetail | null>(null);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);

  readonly from = signal<string | null>(null);
  readonly fromTopicId = signal<string | null>(null);
  readonly fromLevelId = signal<number | null>(null);

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

  ngOnInit(): void {
    const lessonId = Number(this.route.snapshot.paramMap.get('lessonId'));

    this.from.set(this.route.snapshot.queryParamMap.get('from'));
    this.fromTopicId.set(this.route.snapshot.queryParamMap.get('topicId'));
    const lvlId = this.route.snapshot.queryParamMap.get('levelId');
    this.fromLevelId.set(lvlId ? Number(lvlId) : null);

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
