import { Component, Input, inject, computed, signal, OnDestroy } from '@angular/core';

import { Example } from '../../../../core/models/lesson.model';
import { SpeechService } from '../../../../core/services/speech.service';
import { ApiService } from '../../../../core/services/api.service';

@Component({
  selector: 'app-example-card',
  imports: [],
  templateUrl: './example-card.html',
  styleUrl: './example-card.scss',
})
export class ExampleCardComponent implements OnDestroy {
  @Input({ required: true }) example!: Example;

  readonly speechService = inject(SpeechService);
  readonly apiService = inject(ApiService);

  // --- Phase 3 Pronunciation Assessment State ---
  readonly recordingState = signal<'idle' | 'recording' | 'processing' | 'success' | 'error'>('idle');
  readonly evaluationResult = signal<{ transcribed_text: string; accuracy_score: number } | null>(null);
  readonly errorMessage = signal<string | null>(null);
  readonly recordingDuration = signal<number>(0);

  private mediaRecorder: MediaRecorder | null = null;
  private audioChunks: Blob[] = [];
  private timerInterval: any = null;

  /**
   * True only when THIS card's phrase is being spoken.
   * Derived from the service's isSpeaking signal + a local tracking flag.
   */
  private _isThisCardSpeaking = false;

  /** Computed signal: speaking AND this card initiated it. */
  readonly isThisCardSpeaking = computed(
    () => this.speechService.isSpeaking() && this._isThisCardSpeaking
  );

  get sentenceType(): 'affirmative' | 'negative' | 'interrogative' {
    const phrase = this.example?.phrase?.trim() ?? '';
    if (phrase.includes('?')) {
      return 'interrogative';
    }

    const negativePattern =
      /\b(?:do not|does not|did not|didn't|doesn't|don't|cannot|can't|won't|never|no\b|not\b|n't)\b/i;
    if (negativePattern.test(phrase)) {
      return 'negative';
    }

    return 'affirmative';
  }

  get sentenceLabel(): string {
    return {
      affirmative: 'Affirmative',
      negative: 'Negative',
      interrogative: 'Interrogative',
    }[this.sentenceType];
  }

  get sentenceIcon(): string {
    return {
      affirmative: '+',
      negative: '−',
      interrogative: '?',
    }[this.sentenceType];
  }

  /**
   * Returns a concise grammatical anatomy hint for the example phrase.
   * Branches on interrogative vs. affirmative/negative first so the
   * word-order formula is always correct (auxiliary-first for questions).
   */
  get sentenceStructureHint(): string {
    const phrase = this.example?.phrase?.trim() ?? '';
    const isInterrogative = phrase.endsWith('?');

    // ── INTERROGATIVE: auxiliary opens the sentence ─────────────────────────
    if (isInterrogative) {

      // Past Perfect Continuous: Had + S + been + verb-ing?
      if (/^had\b.*\bbeen\s+\w+ing\b/i.test(phrase)) {
        return 'Had + Subject + been + verb-ing?';
      }
      // Past Perfect: Had + S + past participle?
      if (/^had\b/i.test(phrase)) {
        return 'Had + Subject + past participle?';
      }
      // Present Perfect Continuous: Have/Has + S + been + verb-ing?
      if (/^(?:have|has)\b.*\bbeen\s+\w+ing\b/i.test(phrase)) {
        return 'Have/Has + Subject + been + verb-ing?';
      }
      // Present Perfect Simple: Have/Has + S + (adverb) + past participle?
      if (/^(?:have|has)\b/i.test(phrase)) {
        return 'Have/Has + Subject + past participle?';
      }
      // Future Perfect: Will + S + have + past participle?
      if (/^will\b.*\bhave\s+\w+/i.test(phrase)) {
        return 'Will + Subject + have + past participle?';
      }
      // Future Continuous: Will + S + be + verb-ing?
      if (/^will\b.*\bbe\s+\w+ing\b/i.test(phrase)) {
        return 'Will + Subject + be + verb-ing?';
      }
      // Will future simple: Will + S + base verb?
      if (/^will\b/i.test(phrase)) {
        return 'Will + Subject + base verb?';
      }
      // Going to: Am/Is/Are + S + going to + verb?
      if (/^(?:am|is|are)\b.*\bgoing\s+to\b/i.test(phrase)) {
        return 'Am/Is/Are + Subject + going to + base verb?';
      }
      // Continuous: Am/Is/Are/Was/Were + S + verb-ing?
      if (/^(?:am|is|are|was|were)\b/i.test(phrase)) {
        const aux = /^(?:was|were)\b/i.test(phrase) ? 'Was/Were' : 'Am/Is/Are';
        return `${aux} + Subject + verb-ing?`;
      }
      // Past Simple: Did + S + base verb?
      if (/^did\b/i.test(phrase)) {
        return 'Did + Subject + base verb?';
      }
      // Advanced inversion (C1): Adverbial + auxiliary + S + verb
      if (/^(?:hardly|never|not until|under no|rarely|no sooner)\b/i.test(phrase)) {
        return 'Adverbial + Auxiliary + Subject + verb';
      }
      // Generic interrogative fallback
      return 'Auxiliary + Subject + verb?';
    }

    // ── AFFIRMATIVE / NEGATIVE: subject-first word order ───────────────────

    // Perfect Continuous: S + have/has/had + (not) + been + verb-ing
    if (/\b(?:have|has|had)\s+(?:not\s+)?been\s+\w+ing\b/i.test(phrase)) {
      const aux = /\bhad\b/i.test(phrase) ? 'had' : 'have/has';
      return `Subject + ${aux} + been + verb-ing`;
    }
    // Past Perfect: S + had + (not) + past participle
    if (/\bhad\s+(?:not\s+)?\w+/i.test(phrase)) {
      return 'Subject + had + past participle';
    }
    // Future Perfect: S + will + (not) + have + past participle
    if (/\bwill\s+(?:not\s+)?have\s+\w+/i.test(phrase)) {
      return 'Subject + will + have + past participle';
    }
    // Future Continuous: S + will + (not) + be + verb-ing
    if (/\bwill\s+(?:not\s+)?be\s+\w+ing\b/i.test(phrase)) {
      return 'Subject + will + be + verb-ing';
    }
    // Going to: S + am/is/are + (not) + going to + verb
    if (/\b(?:am|is|are)\s+(?:not\s+)?going\s+to\s+\w+/i.test(phrase)) {
      return 'Subject + am/is/are + going to + base verb';
    }
    // Present Perfect Simple: S + have/has + (not) + past participle
    if (/\b(?:have|has)\s+(?:not\s+)?\w+/i.test(phrase)) {
      return 'Subject + have/has + past participle';
    }
    // Continuous: S + am/is/are/was/were + (not) + verb-ing
    if (/\b(?:am|is|are|was|were)\s+(?:not\s+)?\w+ing\b/i.test(phrase)) {
      const aux = /\b(?:was|were)\b/i.test(phrase) ? 'was/were' : 'am/is/are';
      return `Subject + ${aux} + verb-ing`;
    }
    // Will future simple: S + will + (not) + base verb
    if (/\bwill\s+(?:not\s+)?\w+/i.test(phrase)) {
      return 'Subject + will + base verb';
    }
    // Past Simple negative: S + did not + base verb
    if (/\bdid\s+not\b/i.test(phrase) || /\bdidn't\b/i.test(phrase)) {
      return 'Subject + did + not + base verb';
    }
    // Advanced inversion (C1): Adverbial + auxiliary + S + verb
    if (/^(?:hardly|never|not until|under no|rarely|no sooner)\b/i.test(phrase)) {
      return 'Adverbial + Auxiliary + Subject + verb';
    }
    // Default: Present Simple or Past Simple affirmative
    return 'Subject + verb (+ complement)';
  }

  /** Phase 2: Speak ONLY the English phrase via Web Speech API. */
  onListenClick(): void {
    if (!this.speechService.isSupported()) return;

    if (this.isThisCardSpeaking()) {
      // Toggle off: stop if already speaking this card
      this._isThisCardSpeaking = false;
      this.speechService.stop();
      return;
    }

    // Mark this card as the active speaker before calling speak()
    this._isThisCardSpeaking = true;
    // ONLY pass the English phrase — never the Spanish translation or IPA
    this.speechService.speak(this.example.phrase);

    // Reset local flag when speech ends naturally
    const stopWatching = setInterval(() => {
      if (!this.speechService.isSpeaking()) {
        this._isThisCardSpeaking = false;
        clearInterval(stopWatching);
      }
    }, 200);
  }

  /** Phase 3: Will open MediaRecorder, capture audio, send to Whisper STT. */
  onRecordClick(): void {
    if (this.recordingState() === 'recording') {
      this.stopRecording();
    } else {
      this.startRecording();
    }
  }

  private startRecording(): void {
    this.recordingState.set('recording');
    this.evaluationResult.set(null);
    this.errorMessage.set(null);
    this.recordingDuration.set(0);
    this.audioChunks = [];

    if (typeof window === 'undefined' || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      this.errorMessage.set('Tu navegador no soporta la grabación de audio o requiere un contexto seguro (HTTPS).');
      this.recordingState.set('error');
      return;
    }

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then((stream) => {
        this.mediaRecorder = new MediaRecorder(stream);
        this.mediaRecorder.ondataavailable = (event) => {
          if (event.data && event.data.size > 0) {
            this.audioChunks.push(event.data);
          }
        };

        this.mediaRecorder.onstop = () => {
          // Compile standard webm/ogg format chunks into a single Blob
          const mimeType = this.mediaRecorder?.mimeType || 'audio/webm';
          const audioBlob = new Blob(this.audioChunks, { type: mimeType });
          this.sendAudioToBackend(audioBlob);
        };

        // Start recording
        this.mediaRecorder.start();

        // Start timer
        this.timerInterval = setInterval(() => {
          this.recordingDuration.update((d) => d + 1);
          // Safety timeout of 15 seconds to prevent extremely large uploads
          if (this.recordingDuration() >= 15) {
            this.stopRecording();
          }
        }, 1000);
      })
      .catch((err) => {
        console.error('Error accessing microphone:', err);
        this.errorMessage.set('Acceso al micrófono denegado. Por favor, activa los permisos en tu navegador.');
        this.recordingState.set('error');
      });
  }

  private stopRecording(): void {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }

    if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
      this.mediaRecorder.stop();
      // Explicitly stop all audio tracks of the stream to turn off microphone usage lights in the browser
      if (this.mediaRecorder.stream) {
        this.mediaRecorder.stream.getTracks().forEach((track) => track.stop());
      }
    }
  }

  private sendAudioToBackend(audioBlob: Blob): void {
    this.recordingState.set('processing');

    const formData = new FormData();
    // Append the file and specify file name (FastAPI audio endpoint expects standard multipart)
    formData.append('file', audioBlob, 'recording.webm');
    formData.append('target_text', this.example.phrase);

    this.apiService.post<{ transcribed_text: string; accuracy_score: number }>('/audio/evaluate-pronunciation', formData)
      .subscribe({
        next: (res) => {
          this.evaluationResult.set(res);
          this.recordingState.set('success');
        },
        error: (err) => {
          console.error('Pronunciation evaluation failed:', err);
          let detail = 'Error de conexión con el servidor de evaluación. Verifica tu conexión de red.';
          if (err.error && err.error.detail) {
            detail = err.error.detail;
          }
          this.errorMessage.set(detail);
          this.recordingState.set('error');
        }
      });
  }

  resetState(): void {
    this.recordingState.set('idle');
    this.evaluationResult.set(null);
    this.errorMessage.set(null);
    this.recordingDuration.set(0);
    this.audioChunks = [];
  }

  ngOnDestroy(): void {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
    }
    if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
      this.mediaRecorder.stop();
      if (this.mediaRecorder.stream) {
        this.mediaRecorder.stream.getTracks().forEach((track) => track.stop());
      }
    }
  }
}
