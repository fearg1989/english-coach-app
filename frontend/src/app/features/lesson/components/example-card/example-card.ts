import { Component, Input, inject, computed, signal, OnDestroy } from '@angular/core';

import { Example } from '../../../../core/models/lesson.model';
import { SpeechService } from '../../../../core/services/speech.service';
import { ApiService } from '../../../../core/services/api.service';
import { environment } from '../../../../../environments/environment';

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
  readonly evaluationResult = signal<{
    transcribed_text: string;
    accuracy_score: number;
    words: Array<{
      word: string;
      status: 'correct' | 'unclear' | 'incorrect';
      accuracy_score: number;
      transcribed_as: string | null;
    }>;
  } | null>(null);
  readonly errorMessage = signal<string | null>(null);
  readonly recordingDuration = signal<number>(0);

  // --- Phase 4 AI Coach State ---
  readonly coachState = signal<'idle' | 'loading' | 'streaming' | 'done' | 'error'>('idle');
  readonly coachFeedbackText = signal<string>('');

  // --- Streaming Speech-to-Text State ---
  private socket: WebSocket | null = null;
  readonly interimTranscript = signal<string>('');

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
    this.interimTranscript.set('');
    this.audioChunks = [];

    if (typeof window === 'undefined' || !navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      this.errorMessage.set('Tu navegador no soporta la grabación de audio o requiere un contexto seguro (HTTPS).');
      this.recordingState.set('error');
      return;
    }

    // Connect to the streaming websocket
    const target = encodeURIComponent(this.example.phrase);
    
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
      console.log('WebSocket streaming connection opened');
      
      // Start microphone capture and media recording once websocket is open
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then((stream) => {
          this.mediaRecorder = new MediaRecorder(stream);
          this.mediaRecorder.ondataavailable = (event) => {
            if (event.data && event.data.size > 0) {
              this.audioChunks.push(event.data);
              
              // Stream raw chunk directly to WebSocket
              if (this.socket && this.socket.readyState === WebSocket.OPEN) {
                this.socket.send(event.data);
              }
            }
          };

          // Start recording with timeslice of 1000ms (sends data chunk every 1 second)
          this.mediaRecorder.start(1000);

          // Start visual timer
          this.timerInterval = setInterval(() => {
            this.recordingDuration.update((d) => d + 1);
            if (this.recordingDuration() >= 15) {
              this.stopRecording();
            }
          }, 1000);
        })
        .catch((err) => {
          console.error('Error accessing microphone:', err);
          this.errorMessage.set('Acceso al micrófono denegado. Por favor, activa los permisos en tu navegador.');
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
          this.evaluationResult.set(data);
          this.recordingState.set('success');
          this.cleanupSocket();
        } else if (data.type === 'error') {
          this.errorMessage.set(data.detail || 'Error en el procesamiento del flujo.');
          this.recordingState.set('error');
          this.cleanupSocket();
        }
      } catch (err) {
        console.error('Error parsing streaming websocket data:', err);
      }
    };

    this.socket.onerror = (err) => {
      console.error('WebSocket connection error:', err);
      this.errorMessage.set('Error en la conexión en tiempo real con el servidor de voz.');
      this.recordingState.set('error');
      this.stopRecording();
      this.cleanupSocket();
    };

    this.socket.onclose = () => {
      console.log('WebSocket streaming connection closed');
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

    // Set state to processing while waiting for the final evaluation
    if (this.recordingState() === 'recording') {
      this.recordingState.set('processing');
    }

    // Inform the backend that we stopped speaking
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({ event: 'stop' }));
    }
  }

  private cleanupSocket(): void {
    if (this.socket) {
      try {
        this.socket.close();
      } catch (e) {}
      this.socket = null;
    }
  }

  resetState(): void {
    this.recordingState.set('idle');
    this.evaluationResult.set(null);
    this.errorMessage.set(null);
    this.recordingDuration.set(0);
    this.audioChunks = [];
    this.interimTranscript.set('');
    this.coachState.set('idle');
    this.coachFeedbackText.set('');
    this.cleanupSocket();
  }

  async askCoach(): Promise<void> {
    const result = this.evaluationResult();
    if (!result) return;

    this.coachState.set('loading');
    this.coachFeedbackText.set('');

    try {
      const response = await fetch(`${environment.apiUrl}/coach/feedback`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          target_phrase: this.example.phrase,
          user_transcription: result.transcribed_text,
          score: result.accuracy_score,
        }),
      });

      if (!response.ok || !response.body) {
        throw new Error('Network response was not ok');
      }

      this.coachState.set('streaming');
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n\n');
        
        // Keep the last incomplete chunk in the buffer
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const dataStr = line.substring(6);
            try {
              const data = JSON.parse(dataStr);
              if (data.error) {
                this.coachFeedbackText.set(data.error);
                this.coachState.set('error');
                await reader.cancel();
                return;
              }
              if (data.done) {
                this.coachState.set('done');
                await reader.cancel();
                return;
              }
              if (data.content) {
                this.coachFeedbackText.update((text) => text + data.content);
              }
            } catch (e) {
              console.error('Error parsing SSE data:', e);
            }
          }
        }
      }
      if (this.coachState() === 'streaming') {
        this.coachState.set('done');
      }
    } catch (err) {
      console.error('Ask Coach Error:', err);
      this.coachState.set('error');
    }
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
    this.cleanupSocket();
  }
}
