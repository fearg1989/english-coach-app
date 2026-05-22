# Copilot Instructions - Project: english-coach-app

At the end of every response, you must always say exactly: "ok, jefecito".
Do not write any code or generate massive files until we reach a conceptual agreement in the chat.
Never suggest or perform merges into the `main` branch without explicitly explaining what changes will be uploaded and obtaining my direct approval.

## 📝 Lesson Seed Data Formatting Rules

- **Language & Length Limit:** The description field in all seed data (Grammar, Phonetics, Specialized) is strictly for the UI Card overview. It MUST be 100% in English, concise, and strictly under 150 characters. It is just a hook/summary.
- **Pedagogical Separation:** Theoretical breakdowns and structural walkthroughs belong exclusively inside the lesson view content, never in the overview card dictionary. Never put theoretical breakdowns, structural walkthroughs, or long phonetic explanations (e.g., strong/weak forms, assimilation rules) inside the description field.

## 🌐 Global Project Context & Roadmap

This project is an MVP of a custom web platform for English learning (A1-C2) and applied phonetics, designed to improve fluency and technical communication through AI. Development is planned incrementally across 4 phases:

- **Phase 1 (Completed):** Full-Stack base architecture. Relational database (MySQL) to store proficiency levels, lessons, examples with IPA transcriptions, and exercises. Dynamic UI with scalable routing.
- **Phase 2 (Current):** Integration of Text-to-Speech (Web Speech API / OpenAI TTS) to listen to English examples interactively.
- **Phase 3 (Future):** Audio capture in the frontend using `MediaRecorder` sent to the backend for speech-to-text transcription via OpenAI Whisper.
- **Phase 4 (Future):** Advanced validation and detailed pronunciation/grammar feedback utilizing GPT-4o-mini and Azure Speech Assessment.
- **Phase 5 (Future):** Gamification & Metrics. Implementation of a study Time Tracker, daily streaks, experience points (XP), and progress dashboards to boost user engagement and retention.

---

## 🔒 Strict Security Guidelines (DevSecOps)

To mitigate supply chain attacks and ensure a fully hardened environment, the following rules are mandatory:

1. **NPM/YARN PROHIBITION:** It is strictly forbidden to use, generate, or recommend commands based on `npm install` or `yarn`. All dependency management must be done exclusively using **pnpm (version 11 or higher)**.
2. **SECURE COMPILATION POLICIES:**
   - Enforce a package quarantine window: `minimum-release-edge=1440` (prevents installing code published less than 24 hours ago).
   - Block exotic or untrusted third-party sub-dependencies: `block-exotic-sub-dependencies=true`.
   - Ignore automatic execution of potentially malicious scripts (`preinstall`/`postinstall`) during dependency setup by always using the `--ignore-scripts` flag.
3. **ZERO HARDCODED CREDENTIALS:** Do not expose API tokens, secret keys, or database credentials within the source code. All configuration must be handled through environment variables using a secured `.env` file.

---

## 🏗️ Architecture & Database (Phase 1)

The backend must act as a robust, decoupled BFF (Backend For Frontend), while the frontend must be modular, highly dynamic, and future-proof.

### Backend & Persistence (MySQL)
- Clean Architecture / DDD patterns with strict typing (TypeScript with Prisma ORM / Python with FastAPI and Pydantic schemas).
- MySQL Relational Database Schema:
  - `Level`: id, name (A1, A2, B1, B2, C1, C2), description.
  - `Lesson`: id, level_id, type ('grammar' or 'phonetics'), title, explanation.
  - `Example`: id, lesson_id, english_phrase, spanish_translation, ipa_transcription (Phonetic symbols using the International Phonetic Alphabet).
  - `Exercise`: id, lesson_id, question, correct_answer.
- Maintain a dedicated directory for future AI integrations (`services/ai/`), modularized but kept empty or commented out for now.

### Frontend (Angular 17+ Standalone / React with Vite)
- Scalable dynamic routing with Lazy Loading per level utilizing route parameters (`/level/:id`). Do not hardcode views for each level; a single dynamic component must render the data provided by the API response.
- **UI Preparation:** Within the English examples cards/lists, display the phrase, translation, and IPA. Leave visual placeholders or disabled buttons for **"Listen"** and **"Record Audio"** to ensure the layout does not break during Phases 2 and 3.
- Keep source files under 200–300 lines of code. If a file exceeds this limit, modularize it into smaller reusable components or utility services.

---

## 🧪 Testing & QA (Quality Assurance)

Code quality and system stability are non-negotiable. This project follows a test-conscious development philosophy (Test-First / TDD).

1. **Minimum Coverage:** All new functional code must maintain or exceed an **80% Test Coverage** threshold (both Line and Branch coverage).
2. **Test-First Generation:** Before generating core business logic, controllers, or complex components, you must provide the corresponding test file (e.g., `.spec.ts`, `.test.ts`, or `test_*.py`).
3. **Continuous Verification:** After suggesting any functional code block, explicitly provide the command required to run the test suite (using `pnpm test`) to verify everything passes successfully.
4. **Regression Protection:** Do not propose code that breaks existing tests. Test cases must include "Happy Paths" (success metrics) and robust edge-case/error handling (e.g., database connection timeouts).
5. **Frameworks:** Rely on ecosystem standards (Jest/Vitest for Node/React, Jasmine/Karma for Angular, PyTest for Python).

---

## 🛠️ Development Workflow

- **Code Suggestions:** Prioritize short responses and concise explanations. While instructions are in English, the user interaction and code comments/explanations should be written in Spanish.
- **Data Generation:** When asked to generate mock study materials or seeds, strictly base the data on Cambridge reference methodologies (Essential/Intermediate/Advanced Grammar and Vocabulary in Use) and official IPA phonetic structures.
- Whenever a new third-party library is required, verify its legitimacy and document the exact installation command using `pnpm add`.

---

## 🌱 Seed Script — Execution Rules for AI Agents

### Exact working command

```bash
# ALWAYS run from inside backend/ using the project venv
cd /Users/ropa/Develop/english-coach-app/backend
.venv/bin/python scripts/seed.py
```

> ⚠️ `python -m scripts.seed` **does not work** from the project root. The only reliable invocation is `.venv/bin/python scripts/seed.py` from `backend/`.

### Behavior contract

- **Full truncate + re-seed** on every run — all rows are deleted first, then re-inserted.
- Level `id` values are **auto-increment and change on every seed**. Never hardcode a level ID. Always look up by `code` column (`'A1'`, `'C2'`, etc.).

### Seed data module map (insertion order)

This table is the source of truth for `ALL_LESSONS` in `seed.py`. Both files must stay in sync.

| Module | Content |
|--------|---------|
| `a1_phonetics.py` | /θ/ and /ð/ sounds |
| `a1_grammar.py` | To Be, Present Simple, Present Continuous |
| `a1_vocabulary.py` | Numbers/Years/Decimals, Colors, Countries/Nationalities, Jobs/Professions |
| `a2_grammar.py` | Past Simple, Past Continuous, Be Going To, Will, Irregular Verbs |
| `a2_phonetics.py` | /v/ vs /b/, Diphthongs, /ʃ/ vs /tʃ/, Silent Letters, Flap T /ɾ/ |
| `b1_grammar.py` | Present Perfect Simple/Continuous, Past Perfect Simple |
| `b1_phonetics.py` | Sentence Rhythm & Weak Forms, Word Stress (Noun/Verb), Linking, Assimilation |
| `b2_grammar.py` | Past Perfect Continuous, Future Continuous, Future Perfect, Phrasal Verbs |
| `b2_phonetics.py` | Elision, Speaking in Chunks, Prosody, Geminates |
| `c1_grammar.py` | Narrative Tenses & Inversion, Cleft Sentences, Participle Clauses, The Subjunctive |
| `c1_phonetics.py` | Advanced Prosody (Intonation for Meaning), Advanced Assimilation (/t/+/j/→/tʃ/) |
| `c2_grammar.py` | Hedging & Distancing, Semantic Precision, Complex Embedded Clauses |
| `c2_phonetics.py` | Decoding Extreme Connected Speech, Sarcasm, Irony & Subtle Tone |
| `advanced_specialized.py` | Verb Patterns (B1), Connectors (B2), Collocations (C1) |
| `prepositions.py` | To/For/From (B1), By/Until/For/During (B2), Dependent Verbs (B2), Leadership Adj∕Nouns (C1), Space & Data Flow (C1) |

### Mandatory update rule — enforced for every AI agent

Any time a seed_data module is added, modified, or removed, the AI **must** update all three locations before running the seed. No exceptions:

1. **`backend/scripts/seed.py`** — module docstring + import block + `ALL_LESSONS` list
2. **`README.md`** — module table in the "Seed de datos" section
3. **`.github/copilot-instructions.md`** — module table in this section

All three must remain synchronized at all times.

### ⚠️ Python script documentation rule — enforced for every AI agent

Any time an AI agent creates, modifies, or removes **any Python file** under `backend/scripts/` or `backend/app/` (models, services, repositories, endpoints, seed data), it **must** document the change. This means:

- If the change affects the seed data set (modules, schema, categories): update the three locations above.
- If the change affects the API, models, or backend logic: add or update the relevant section in `README.md` under the corresponding architecture heading.
- Every new Python module must include a module-level docstring or comment block explaining its purpose, expected inputs/outputs, and any invariants (e.g., insertion order, FK dependencies).

This rule exists so that future AI agents and human developers always have up-to-date, trustworthy documentation to orient themselves without reading raw source code.