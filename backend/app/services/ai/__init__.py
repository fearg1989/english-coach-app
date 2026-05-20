"""
AI Services — Phase 2, 3 & 4
══════════════════════════════════════════════════════════════════════════════

This package will house all AI integrations as the platform evolves.

┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2 — Text-to-Speech (TTS)                                             │
│  File: tts_service.py                                                       │
│  Description:                                                               │
│    - Web Speech API (browser-side, no backend required)                     │
│    - OpenAI TTS API for server-side audio generation                        │
│    - Stores audio_url in the Example.audio_url column                       │
│    - Endpoint: POST /api/v1/examples/{id}/synthesize                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3 — Speech-to-Text (STT)                                             │
│  File: whisper_service.py                                                   │
│  Description:                                                               │
│    - Frontend captures audio via MediaRecorder API                          │
│    - Audio blob sent to backend as multipart/form-data                      │
│    - Backend calls openai.Audio.transcribe() (Whisper model)                │
│    - Endpoint: POST /api/v1/transcribe                                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4 — Pronunciation & Grammar Validation                               │
│  Files: pronunciation_service.py, grammar_service.py                       │
│  Description:                                                               │
│    - Azure Speech Services: pronunciation assessment scoring                │
│    - GPT-4o-mini: grammar correction and contextual feedback                │
│    - Endpoint: POST /api/v1/exercises/{id}/validate                         │
└─────────────────────────────────────────────────────────────────────────────┘
"""
