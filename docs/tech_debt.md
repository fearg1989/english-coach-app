# Technical Debt Register — English Coach App

This document is the authoritative log of known architectural compromises, temporary workarounds, and deferred upgrades. Each entry includes the current state, the required resolution, and the target phase.

> **Rule:** Any AI agent or developer introducing a deliberate workaround **must** add an entry here before merging.

---

## TD-001 · Advanced Prosody TTS — Missing SSML Support

| Field | Detail |
|---|---|
| **Status** | Active — workaround in production |
| **Affected Levels** | C1, C2 (Advanced Prosody & Intonation lessons) |
| **Introduced in** | Phase 2 |
| **Resolution target** | Phase 4 |
| **Owner** | `SpeechService` → `frontend/src/app/core/services/speech.service.ts` |

### Context

The C1/C2 phonetics lessons teach intonation contours using Unicode arrow markers embedded directly in the `phrase` field of the database (e.g., `↘` for falling tone, `↗` for rising tone, `↘↗` for fall-rise). These are pedagogically critical: two sentences with identical words but different contours represent distinct communicative meanings.

### Current Implementation (Phase 2 Workaround)

The `SpeechService` uses the **native browser Web Speech API** (`window.speechSynthesis`), which does not support [SSML (Speech Synthesis Markup Language)](https://www.w3.org/TR/speech-synthesis11/). It is therefore impossible to control syllable-level pitch contours, nuclear stress placement, or tonal movement.

**Workaround applied:** `_detectIntonation()` parses the arrow markers *before* sanitizing the text and applies a global `pitch`/`rate` adjustment to the entire utterance:

```
↘  (falling)   → { pitch: 0.80, rate: 0.85 }   // lower pitch, deliberate pace
↗  (rising)    → { pitch: 1.30, rate: 0.90 }   // higher pitch
↘↗ (fall-rise) → { pitch: 1.10, rate: 0.80 }   // mid-high, slow
—  (neutral)   → { pitch: 1.00, rate: 0.90 }
```

**Limitation:** This is a rough audible differentiator, not linguistically accurate intonation. The entire utterance is shifted to a single pitch level — there is no rise/fall movement within the sentence. A trained English ear will notice the approximation is incorrect.

### Required Upgrade (Phase 4)

When Cloud AI services are integrated, the TTS engine for advanced phonetics lessons **must** be replaced with a server-side API that fully supports SSML. Candidates:

| Provider | SSML Prosody Tags | Notes |
|---|---|---|
| **Azure Cognitive Services TTS** | `<prosody pitch="...">`, `<emphasis>` | Best SSML coverage; Neural voices |
| **Google Cloud TTS** | `<prosody>`, `<say-as>`, `<break>` | WaveNet/Neural2 voices |
| **OpenAI TTS (v2)** | Limited — no SSML | Not suitable for this use case |

**Recommended:** Azure Cognitive Services Neural TTS with SSML `<prosody>` tags allows expressing intonation contours like:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    I didn't
    <prosody pitch="+10%" rate="slow">SAY</prosody>
    the deploy was ready.
    <prosody pitch="-20%" contour="(0%,+10%) (50%,-10%) (100%,+5%)">↘↗</prosody>
  </voice>
</speak>
```

### Migration Checklist (Phase 4)

- [ ] Implement `SsmlTtsService` in `frontend/src/app/core/services/ssml-tts.service.ts`
- [ ] Add backend endpoint `POST /api/v1/tts/synthesize` that receives `{ phrase, intonation_markers }` and returns an audio stream via Azure/Google TTS
- [ ] Remove `_detectIntonation()` pitch hack from `SpeechService`
- [ ] Keep `_sanitizeForSpeech()` — still needed to strip markers from display text
- [ ] Migrate only `type: 'phonetics'` lessons at C1/C2 level to the new engine; grammar lessons at A1–B2 can remain on Web Speech API

---
