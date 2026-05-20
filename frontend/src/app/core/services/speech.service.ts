/**
 * speech.service.ts
 *
 * Angular service wrapping the native Web Speech API (SpeechSynthesis).
 *
 * Responsibilities:
 *  - Detect browser support for SpeechSynthesis.
 *  - Resolve and cache a high-quality English voice (en-US preferred, en-GB fallback).
 *  - Expose speak(text), stop(), and an `isSpeaking` signal for reactive UI binding.
 *
 * Invariants:
 *  - Only the english_phrase text must be passed to speak(). The caller is
 *    responsible for NOT passing Spanish translations or IPA transcriptions.
 *  - Voices are loaded asynchronously; the service retries on the
 *    `voiceschanged` event to handle Chrome's deferred voice loading.
 *
 * Phase: 2 (Text-to-Speech)
 */

import { Injectable, OnDestroy, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class SpeechService implements OnDestroy {
  /** Reactive signal — true while the browser is actively speaking. */
  readonly isSpeaking = signal<boolean>(false);

  private _synth: SpeechSynthesis | null = null;
  private _voice: SpeechSynthesisVoice | null = null;
  private readonly _PREFERRED_LANGS = ['en-US', 'en-GB', 'en-AU'];

  constructor() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window && window.speechSynthesis) {
      this._synth = window.speechSynthesis;
      this._loadVoice();

      // Chrome loads voices asynchronously — onvoiceschanged fires when ready.
      this._synth.onvoiceschanged = () => this._loadVoice();
    }
  }

  // ─── Public API ───────────────────────────────────────────────────────────

  /** Returns true if the current browser supports SpeechSynthesis. */
  isSupported(): boolean {
    return this._synth !== null;
  }

  /**
   * Speaks the given English text aloud.
   * Silently does nothing if the browser lacks SpeechSynthesis support
   * or if the text is blank.
   *
   * @param text — MUST be the English phrase only. Never pass Spanish/IPA.
   */
  speak(text: string): void {
    if (!this._synth || !text.trim()) return;

    // Cancel any ongoing speech before starting a new utterance.
    this._synth.cancel();

    const utterance = new SpeechSynthesisUtterance(this._sanitizeForSpeech(text));
    utterance.lang = 'en-US';
    utterance.rate = 0.9;   // Slightly slower for learning context
    utterance.pitch = 1.0;

    if (this._voice) {
      utterance.voice = this._voice;
    }
    utterance.onstart = () => this.isSpeaking.set(true);
    utterance.onend = () => this.isSpeaking.set(false);
    utterance.onerror = () => this.isSpeaking.set(false);

    this._synth.speak(utterance);
  }

  /** Cancels any ongoing speech immediately. */
  stop(): void {
    this._synth?.cancel();
    this.isSpeaking.set(false);
  }

  ngOnDestroy(): void {
    this.stop();
  }

  // ─── Private helpers ──────────────────────────────────────────────────────

  /**
   * Removes prosodic and phonetic annotation symbols that the browser
   * speech engine would mispronounce (e.g. ↘ → "down right arrow").
   *
   * Strips:
   *  - Unicode directional/arrow characters (intonation markers: ↘ ↗ → ← ↑ ↓ etc.)
   *  - IPA stress/length diacritics that may leak into phrase text (ˈ ˌ ː)
   *  - Trailing punctuation left orphaned after stripping
   *  - Extra whitespace
   */
  private _sanitizeForSpeech(text: string): string {
    return text
      // Unicode arrows (intonation markers): U+2190–U+21FF block
      .replace(/[\u2190-\u21FF]/g, '')
      // IPA diacritics that can appear in annotated phrases
      .replace(/[ˈˌː]/g, '')
      // Clean up orphaned trailing punctuation (e.g. ". ↘" → ".")
      .replace(/\s+([.,;])/g, '$1')
      // Collapse multiple spaces into one
      .replace(/\s{2,}/g, ' ')
      .trim();
  }

  /**
   * Resolves the best available English voice using the priority order:
   *   1. "Google US English" (Chrome/Android)
   *   2. Any en-US voice
   *   3. Any en-GB voice
   *   4. Any other en-* voice
   *   5. System default (null — browser decides)
   */
  private _loadVoice(): void {
    if (!this._synth) return;

    const voices = this._synth.getVoices();
    if (!voices.length) return;

    // Priority 1: Google US English (highest quality on Chrome)
    const googleUS = voices.find((v) => v.name === 'Google US English');
    if (googleUS) {
      this._voice = googleUS;
      return;
    }

    // Priority 2–4: Best match by locale order
    for (const lang of this._PREFERRED_LANGS) {
      const match = voices.find((v) => v.lang === lang);
      if (match) {
        this._voice = match;
        return;
      }
    }

    // Priority 5: Any English voice
    const anyEnglish = voices.find((v) => v.lang.startsWith('en'));
    this._voice = anyEnglish ?? null;
  }
}
