import { Component, Input, inject, computed } from '@angular/core';

import { Example } from '../../../../core/models/lesson.model';
import { SpeechService } from '../../../../core/services/speech.service';

@Component({
  selector: 'app-example-card',
  imports: [],
  templateUrl: './example-card.html',
  styleUrl: './example-card.scss',
})
export class ExampleCardComponent {
  @Input({ required: true }) example!: Example;

  readonly speechService = inject(SpeechService);

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
    // TODO Phase 3 — activate MediaRecorder and send blob to /api/v1/transcribe
    console.info('[Phase 3] Audio recording not yet implemented.');
  }
}
