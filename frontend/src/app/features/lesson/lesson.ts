import { Component, OnInit, OnDestroy, inject, signal, computed, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { LessonDetail } from '../../core/models/lesson.model';
import { LessonService } from '../../core/services/lesson.service';
import { SpeechService } from '../../core/services/speech.service';
import { ApiService } from '../../core/services/api.service';
import { PracticeSession, PracticeExercise } from '../../core/models/practice.model';
import { environment } from '../../../environments/environment';
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
export class LessonComponent implements OnInit, OnDestroy {
  private readonly route = inject(ActivatedRoute);
  private readonly lessonService = inject(LessonService);
  private readonly speechService = inject(SpeechService);
  private readonly apiService = inject(ApiService);

  readonly lesson = signal<LessonDetail | null>(null);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);

  readonly from = signal<string | null>(null);
  readonly fromTopicId = signal<string | null>(null);
  readonly fromLevelId = signal<number | null>(null);
  readonly fromTab = signal<string | null>(null);

  // --- Dynamic Practice Session (Phase 4.5) ---
  readonly practiceState = signal<'idle' | 'generating' | 'active' | 'summary' | 'error'>('idle');
  readonly activePracticeTheme = signal<string | null>(null);
  readonly customTheme = signal<string>('');
  readonly practiceSession = signal<PracticeSession | null>(null);
  readonly currentExerciseIndex = signal<number>(0);
  readonly showHint = signal<boolean>(false);
  readonly userAnswer = signal<string>('');
  readonly selectedOption = signal<string | null>(null);  // For multiple_choice exercises
  readonly isEvaluating = signal<boolean>(false);

  // Exercise verification feedback states
  readonly exerciseChecked = signal<boolean>(false);
  readonly isExerciseCorrect = signal<boolean>(false);
  readonly exerciseAccuracyScore = signal<number | null>(null);
  readonly exerciseWordsFeedback = signal<any[]>([]);
  readonly exerciseSpeechTranscribed = signal<string | null>(null);

  // Total correct counter
  readonly correctCount = signal<number>(0);

  // Whisper / Recording State for Wizard Card
  readonly recordingState = signal<'idle' | 'recording' | 'processing' | 'success' | 'error'>('idle');
  readonly errorMessage = signal<string | null>(null);
  readonly recordingDuration = signal<number>(0);
  readonly interimTranscript = signal<string>('');

  private socket: WebSocket | null = null;
  private mediaRecorder: MediaRecorder | null = null;
  private audioChunks: Blob[] = [];
  private timerInterval: any = null;

  readonly activeExercise = computed<PracticeExercise | null>(() => {
    const session = this.practiceSession();
    if (!session) return null;
    const idx = this.currentExerciseIndex();
    if (idx >= 0 && idx < session.exercises.length) {
      return session.exercises[idx];
    }
    return null;
  });

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

  ngOnDestroy(): void {
    this.cleanupSocket();
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
    }
  }

  // ─── Practice Session Logic ───────────────────────────────────────────────

  startThemedPractice(theme: string): void {
    const lessonData = this.lesson();
    if (!lessonData) return;

    this.activePracticeTheme.set(theme);
    this.practiceState.set('generating');
    this.errorMessage.set(null);
    this.currentExerciseIndex.set(0);
    this.correctCount.set(0);
    this.resetExerciseStates();

    this.apiService.post<PracticeSession>('/practice/generate', {
      lesson_id: lessonData.id,
      theme: theme
    }).subscribe({
      next: (session) => {
        this.practiceSession.set(session);
        this.practiceState.set('active');
      },
      error: (err) => {
        console.error('Failed to generate practice session:', err);
        this.errorMessage.set(err.error?.detail || 'No se pudo contactar al AI Coach para generar la sesión. Por favor, asegúrate de que Ollama esté encendido y vuelve a intentarlo.');
        this.practiceState.set('error');
      }
    });
  }

  resetExerciseStates(): void {
    this.userAnswer.set('');
    this.selectedOption.set(null);
    this.showHint.set(false);
    this.exerciseChecked.set(false);
    this.isExerciseCorrect.set(false);
    this.exerciseAccuracyScore.set(null);
    this.exerciseWordsFeedback.set([]);
    this.exerciseSpeechTranscribed.set(null);
    this.recordingState.set('idle');
    this.interimTranscript.set('');
  }

  /** Handles option click for multiple_choice exercises */
  selectOption(option: string): void {
    if (this.exerciseChecked()) return;  // Don't allow changing after submission
    this.selectedOption.set(option);
    this.userAnswer.set(option);
  }

  checkAnswer(): void {
    const exercise = this.activeExercise();
    if (!exercise) return;

    this.exerciseChecked.set(true);

    const normalize = (s: string) =>
      s.trim().toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?]/g, '').replace(/\s+/g, ' ');

    if (exercise.type === 'multiple_choice') {
      // Exact match against selected option
      const selected = this.selectedOption();
      const correct = normalize(exercise.correct_answer);
      const isCorrect = !!selected && normalize(selected) === correct;
      this.isExerciseCorrect.set(isCorrect);
      if (isCorrect) this.correctCount.update(c => c + 1);
      return;
    }

    const typedAnswer = normalize(this.userAnswer());
    const targetAnswer = normalize(exercise.correct_answer);

    if (exercise.type === 'open_writing' || exercise.type === 'translation') {
      // Flexible matching: accept if typed includes all key words from target
      // or if the target includes the typed text (when typed is long enough)
      const typedWords = typedAnswer.split(' ').filter(w => w.length > 2);
      const targetWords = targetAnswer.split(' ').filter(w => w.length > 2);
      const matchCount = typedWords.filter(w => targetWords.includes(w)).length;
      const matchRatio = targetWords.length > 0 ? matchCount / targetWords.length : 0;
      // Accept if 70%+ of key words match, or if typed is basically the same
      const isCorrect = typedAnswer === targetAnswer ||
                        matchRatio >= 0.7 ||
                        (targetAnswer.includes(typedAnswer) && typedAnswer.length > 4);
      this.isExerciseCorrect.set(isCorrect);
      if (isCorrect) this.correctCount.update(c => c + 1);
      return;
    }

    // Default: fill_in_the_blank & roleplay_response — exact / includes match
    const isCorrect = typedAnswer === targetAnswer ||
                      (targetAnswer.includes(typedAnswer) && typedAnswer.length > 2);
    this.isExerciseCorrect.set(isCorrect);
    if (isCorrect) this.correctCount.update(c => c + 1);
  }

  onRecordClick(): void {
    if (this.recordingState() === 'recording') {
      this.stopRecording();
    } else {
      this.startRecording();
    }
  }

  private startRecording(): void {
    const exercise = this.activeExercise();
    if (!exercise) return;

    this.recordingState.set('recording');
    this.errorMessage.set(null);
    this.recordingDuration.set(0);
    this.interimTranscript.set('');
    this.audioChunks = [];

    if (typeof window === 'undefined' || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      this.errorMessage.set('Tu navegador no soporta la grabación de audio o requiere HTTPS.');
      this.recordingState.set('error');
      return;
    }

    const target = encodeURIComponent(exercise.correct_answer);
    
    let apiBase = environment.apiUrl;
    if (apiBase.startsWith('/')) {
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      apiBase = `${protocol}//${window.location.host}${apiBase}`;
    } else {
      apiBase = apiBase.replace(/^http:/, 'ws:').replace(/^https:/, 'wss:');
    }
    
    const wsUrl = `${apiBase}/audio/stream-evaluation?target_text=${target}`;
    this.socket = new WebSocket(wsUrl);

    this.socket.onopen = () => {
      console.log('WebSocket practice session connection opened');
      
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then((stream) => {
          this.mediaRecorder = new MediaRecorder(stream);
          this.mediaRecorder.ondataavailable = (event) => {
            if (event.data && event.data.size > 0) {
              this.audioChunks.push(event.data);
              
              if (this.socket && this.socket.readyState === WebSocket.OPEN) {
                this.socket.send(event.data);
              }
            }
          };

          this.mediaRecorder.start(1000);

          this.timerInterval = setInterval(() => {
            this.recordingDuration.update((d) => d + 1);
            if (this.recordingDuration() >= 15) {
              this.stopRecording();
            }
          }, 1000);
        })
        .catch((err) => {
          console.error('Error practice mic access:', err);
          this.errorMessage.set('Acceso al micrófono denegado. Activa los permisos en tu navegador.');
          this.recordingState.set('error');
          this.cleanupSocket();
        });
    };

    this.socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.type === 'interim') {
          this.interimTranscript.set(data.text);
        } else if (data.type === 'final') {
          const score = data.accuracy_score;
          const passed = score >= 75;
          this.exerciseAccuracyScore.set(score);
          this.exerciseWordsFeedback.set(data.words);
          this.exerciseSpeechTranscribed.set(data.transcribed_text);
          this.userAnswer.set(data.transcribed_text);
          
          this.exerciseChecked.set(true);
          this.isExerciseCorrect.set(passed);
          if (passed) {
            this.correctCount.update(c => c + 1);
          }
          this.recordingState.set('success');
          this.cleanupSocket();
        } else if (data.type === 'error') {
          this.errorMessage.set(data.detail || 'Error en el procesamiento del flujo.');
          this.recordingState.set('error');
          this.cleanupSocket();
        }
      } catch (err) {
        console.error('Error parsing practice ws data:', err);
      }
    };

    this.socket.onerror = (err) => {
      console.error('Practice WebSocket error:', err);
      this.errorMessage.set('Error en la conexión en tiempo real.');
      this.recordingState.set('error');
      this.stopRecording();
      this.cleanupSocket();
    };

    this.socket.onclose = () => {
      console.log('Practice WebSocket closed');
    };
  }

  private stopRecording(): void {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }

    if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
      this.mediaRecorder.stop();
      if (this.mediaRecorder.stream) {
        this.mediaRecorder.stream.getTracks().forEach((track) => track.stop());
      }
    }

    if (this.recordingState() === 'recording') {
      this.recordingState.set('processing');
    }

    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({ event: 'stop' }));
    }
  }

  private cleanupSocket(): void {
    if (this.socket) {
      this.socket.close();
      this.socket = null;
    }
  }

  nextExercise(): void {
    const session = this.practiceSession();
    if (!session) return;

    const nextIndex = this.currentExerciseIndex() + 1;
    if (nextIndex < session.exercises.length) {
      this.currentExerciseIndex.set(nextIndex);
      this.resetExerciseStates();
    } else {
      this.practiceState.set('summary');
    }
  }

  retryExercise(): void {
    if (this.isExerciseCorrect()) {
      this.correctCount.update(c => Math.max(0, c - 1));
    }
    this.resetExerciseStates();
  }

  closePractice(): void {
    this.cleanupSocket();
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
    }
    this.practiceState.set('idle');
    this.activePracticeTheme.set(null);
    this.customTheme.set('');
    this.practiceSession.set(null);
  }
}
