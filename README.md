# English Coach App — Fase 1

Plataforma web MVP para el aprendizaje de inglés A1–C2 con fonética aplicada e IA.

## Stack

| Capa | Tecnología |
|------|-----------|
| Base de datos | MySQL 8 (Docker) |
| Backend | Python 3.12 · FastAPI · SQLAlchemy 2 |
| Frontend | Angular 20 · Standalone · SCSS |

---

## Levantar el proyecto en desarrollo

### 1. Pre-requisitos

- Docker Desktop
- Python 3.12+
- Node.js 20+ y `pnpm` v11+

### 2. Iniciar MySQL con Docker

```bash
# Desde la raíz del proyecto
docker-compose up -d db
```

MySQL quedará disponible en `localhost:3306`.

### 3. Backend — FastAPI

```bash
cd backend

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# Instalar dependencias
pip install -r requirements.txt

# Poblar la base de datos — trunca todo y re-siembra desde cero
# ⚠️ COMANDO CORRECTO: python -m scripts.seed no funciona desde la raíz
.venv/bin/python scripts/seed.py

# Iniciar servidor de desarrollo
uvicorn app.main:app --reload --port 8000
```

API disponible en: `http://localhost:8000`
Documentación Swagger: `http://localhost:8000/api/docs`

### 4. Frontend — Angular

```bash
cd frontend

# Instalar dependencias (SOLO pnpm, nunca npm/yarn)
pnpm install

# Iniciar servidor de desarrollo
ng serve
```

App disponible en: `http://localhost:4200`

### Estandarización de Interfaz y Tarjetas (UI Card Standard)

- **Alturas Uniformes (Uniform Heights):** Todas las tarjetas de vista general en cuadrículas (grid overview cards) deben implementar alturas uniformes mediante flexbox o propiedades de CSS Grid (estiramiento `h-full`) para garantizar una alineación perfecta en todos los tamaños de pantalla y evitar saltos de línea asimétricos.

---

## Endpoints disponibles (Fase 1)

```
GET /api/v1/levels/                  → Lista todos los niveles A1-C2
GET /api/v1/levels/{id}              → Nivel por ID
GET /api/v1/levels/code/{code}       → Nivel por código (A1, B2, etc.)
GET /api/v1/lessons/level/{id}       → Lecciones de un nivel (filtro ?type=grammar|phonetics)
GET /api/v1/lessons/{id}             → Lección con ejemplos y ejercicios
GET /health                          → Health check
```

---

## Rutas del Frontend

```
/                  → Home — grid de 6 niveles CEFR
/level/:levelId    → Lista de lecciones del nivel
/lesson/:lessonId  → Lección con ejemplos IPA + ejercicios
```

---

## Estructura del proyecto

```
english-coach-app/
├── docker-compose.yml
├── Makefile
├── backend/
│   ├── app/
│   │   ├── api/v1/endpoints/   # Controladores REST
│   │   ├── core/               # Config, settings
│   │   ├── db/                 # Engine, session
│   │   ├── models/             # SQLAlchemy ORM
│   │   ├── repositories/       # Acceso a datos
│   │   ├── schemas/            # Pydantic I/O
│   │   ├── services/           # Lógica de negocio
│   │   │   └── ai/             # 🔒 Reservado Fases 2-4
│   │   └── main.py
│   └── scripts/seed.py
└── frontend/
    └── src/app/
        ├── core/
        │   ├── models/         # Interfaces TypeScript
        │   ├── services/       # HTTP services
        │   └── interceptors/
        └── features/
            ├── home/
            ├── level/
            └── lesson/
                └── components/
                    ├── example-card/   # Frase + IPA + botones Fase 2/3
                    └── exercise-card/  # Ejercicios + botón Fase 4
```

---

## Seed de datos — Estructura y contrato

### Comando de ejecución

```bash
# Siempre ejecutar desde backend/ con el venv activado
cd backend
.venv/bin/python scripts/seed.py
```

> ⚠️ `python -m scripts.seed` **no funciona** desde la raíz del proyecto.  
> El comando correcto es siempre `.venv/bin/python scripts/seed.py` desde `backend/`.

### Comportamiento

- **Trunca completamente** todas las tablas y re-siembra desde cero en cada ejecución.
- Los `id` de los niveles son **auto-increment** — cambian en cada seed. Siempre consultar por `code` (`'A1'`, `'B2'`, etc.), nunca por `id` hardcodeado.

### Módulos de datos (`backend/scripts/seed_data/`)

El orden en `ALL_LESSONS` dentro de `seed.py` es el orden real de inserción:

| Módulo | Contenido |
|--------|----------|
| `a1_phonetics.py` | /θ/ y /ð/ sounds |
| `a1_grammar.py` | Present Simple, Present Continuous |
| `a2_grammar.py` | Past Simple, Past Continuous, Be Going To, Will, Irregular Verbs |
| `a2_phonetics.py` | /v/ vs /b/, Diphthongs, /ʃ/ vs /tʃ/, Silent Letters, Flap T |
| `b1_grammar.py` | Present Perfect Simple/Continuous, Past Perfect Simple |
| `b1_phonetics.py` | Rhythm & Weak Forms, Word Stress, Linking, Assimilation |
| `b2_grammar.py` | Past Perfect Continuous, Future Continuous, Future Perfect, Phrasal Verbs |
| `b2_phonetics.py` | Elision, Chunking, Prosody, Geminates |
| `c1_grammar.py` | Narrative Tenses & Inversion, Cleft Sentences, Participle Clauses, Subjunctive |
| `c1_phonetics.py` | Advanced Prosody (Intonation), Advanced Assimilation (/t/+/j/→/tʃ/) |
| `c2_grammar.py` | Hedging & Distancing, Semantic Precision, Complex Embedded Clauses |
| `c2_phonetics.py` | Decoding Extreme Connected Speech, Sarcasm & Irony |
| `advanced_specialized.py` | Verb Patterns (B1), Connectors (B2), Collocations (C1) |
| `prepositions.py` | To/For/From (B1), By/Until/For/During (B2), Dependent Verbs (B2), Leadership Adj∕Nouns (C1), Space & Data Flow (C1) |

### Contrato de modificación — Cualquier IA o desarrollador DEBE seguir este orden

Cuando se añada, modifique o elimine un módulo de `seed_data/`, es **obligatorio** actualizar los 3 puntos siguientes antes de ejecutar el seed:

1. **`backend/scripts/seed.py`** — docstring interno + import + lista `ALL_LESSONS`
2. **`README.md`** — tabla de módulos en esta sección
3. **`.github/copilot-instructions.md`** — tabla de módulos en la sección « Seed Script — Reglas para IAs »

Ninguna de las tres fuentes debe quedar desincronizada respecto a las otras.

---

## Roadmap

| Fase | Estado | Descripción |
|------|--------|-------------|
| 1 | ✅ **Completada** | BD relacional MySQL, API REST FastAPI, vistas dinámicas Angular A1–C2 |
| 2 | 🚧 **En curso** | **Text-to-Speech — La App Habla:** Web Speech API nativa del navegador para escuchar la pronunciación exacta de frases, vocabulario y fonemas sin APIs de pago externas |
| 3 | 🔜 | **Speech Recognition — La App Escucha:** Captura de audio (micrófono) para que el estudiante lea las frases y el sistema valide si la pronunciación es correcta |
| 4 | 🔜 | **El Cerebro IA (Oracle OCI + Ollama/Gemma):** Conexión del backend con servidor en la nube para generar prácticas dinámicas, simular entrevistas de trabajo (Roleplay) y dar feedback gramatical en tiempo real |
| 5 | 🔜 | **Gamificación y Métricas:** Time Tracker de estudio, rachas (streaks), puntos de experiencia (XP) y dashboards de progreso |
