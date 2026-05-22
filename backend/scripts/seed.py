"""
Seed Script — English Coach App
════════════════════════════════
Core Grammar Path: 12 Active Verb Tenses (A1 → B2) + C1 Narrative Tenses bonus.
Includes the original A1 Phonetics lesson (/θ/ and /ð/ sounds).

Lesson data is modularised under scripts/seed_data/:
  core_levels        → CEFR level definitions
  a1_phonetics       → Phonetics lesson (/θ/ and /ð/ sounds)
  a1_grammar         → To Be, Present Simple, Present Continuous
  a1_vocabulary      → Numbers/Years/Decimals, Colors, Countries/Nationalities, Jobs/Professions
  a2_grammar         → Past Simple, Past Continuous, Be Going To, Will, Irregular Verbs
  a2_phonetics       → /v/ vs /b/, Diphthongs /oʊ/ & /aʊ/, /ʃ/ vs /tʃ/, Silent Letters, Flap T /ɾ/
  b1_grammar         → Present Perfect Simple/Continuous, Past Perfect Simple
  prepositions       → To/For/From (B1), By/Until/For/During (B2), Dependent Verbs (B2), Leadership Adj/Nouns (C1), Space & Data Flow (C1)
  b1_phonetics       → Sentence Rhythm & Weak Forms, Word Stress Noun/Verb, Linking, Assimilation
  b2_grammar         → Past Perfect Continuous, Future Continuous, Future Perfect, Phrasal Verbs
  b2_phonetics       → Elision, Speaking in Chunks, Prosody, Geminates
  c1_grammar         → Narrative Tenses & Inversion, Cleft Sentences, Participle Clauses, The Subjunctive
  c1_phonetics       → Advanced Prosody (Intonation for Meaning), Advanced Assimilation (/t/+/j/→/tʃ/)
  c2_grammar         → Hedging & Distancing, Semantic Precision, Complex Embedded Clauses
  c2_phonetics       → Decoding Extreme Connected Speech, Sarcasm, Irony & Subtle Tone
  advanced_specialized → Verb Patterns (B1), Connectors (B2), Collocations (C1)

Behavior: ALWAYS truncates existing data and re-seeds from scratch.

Usage:
  cd backend
  python -m scripts.seed
"""

import os
import sys

from sqlalchemy import text

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.base import Base, engine
from app.db.session import SessionLocal
from app.models import (  # noqa: F401
    Example,
    Exercise,
    ExerciseType,
    GlossaryEntry,
    GlossaryType,
    Lesson,
    LessonCategory,
    LessonType,
    Level,
    SentenceType,
)
from scripts.seed_data.a1_grammar import A1_GRAMMAR_LESSONS
from scripts.seed_data.a1_phonetics import A1_PHONETICS_LESSONS, PHONETICS
from scripts.seed_data.a1_vocabulary import A1_VOCABULARY_LESSONS
from scripts.seed_data.a2_grammar import A2_GRAMMAR_LESSONS
from scripts.seed_data.a2_phonetics import A2_PHONETICS_LESSONS
from scripts.seed_data.a2_vocabulary import A2_VOCABULARY_LESSONS
from scripts.seed_data.b1_grammar import B1_GRAMMAR_LESSONS
from scripts.seed_data.b1_phonetics import B1_PHONETICS_LESSONS
from scripts.seed_data.b1_vocabulary import B1_VOCABULARY_LESSONS
from scripts.seed_data.b2_grammar import B2_GRAMMAR_LESSONS
from scripts.seed_data.b2_phonetics import B2_PHONETICS_LESSONS
from scripts.seed_data.b2_vocabulary import B2_VOCABULARY_LESSONS
from scripts.seed_data.c1_grammar import C1_GRAMMAR_LESSONS
from scripts.seed_data.c1_phonetics import C1_PHONETICS_LESSONS
from scripts.seed_data.c1_vocabulary import C1_VOCABULARY_LESSONS
from scripts.seed_data.c2_grammar import C2_GRAMMAR_LESSONS
from scripts.seed_data.c2_phonetics import C2_PHONETICS_LESSONS
from scripts.seed_data.c2_vocabulary import C2_VOCABULARY_LESSONS
from scripts.seed_data.advanced_specialized import ADVANCED_SPECIALIZED_LESSONS
from scripts.seed_data.prepositions import PREPOSITIONS_LESSONS
from scripts.seed_data.core_levels import LEVELS

ALL_LESSONS: list[dict] = (
    A1_PHONETICS_LESSONS
    + A1_GRAMMAR_LESSONS
    + A1_VOCABULARY_LESSONS
    + A2_GRAMMAR_LESSONS
    + A2_PHONETICS_LESSONS
    + A2_VOCABULARY_LESSONS
    + B1_GRAMMAR_LESSONS
    + B1_PHONETICS_LESSONS
    + B1_VOCABULARY_LESSONS
    + B2_GRAMMAR_LESSONS
    + B2_PHONETICS_LESSONS
    + B2_VOCABULARY_LESSONS
    + C1_GRAMMAR_LESSONS
    + C1_PHONETICS_LESSONS
    + C1_VOCABULARY_LESSONS
    + C2_GRAMMAR_LESSONS
    + C2_PHONETICS_LESSONS
    + C2_VOCABULARY_LESSONS
    + ADVANCED_SPECIALIZED_LESSONS
    + PREPOSITIONS_LESSONS
)

# ── Glossary — Phrasal Verbs ──────────────────────────────────────────────────
GLOSSARY_PHRASAL_VERBS: list[dict] = [
    {"term": "spin up",      "meaning": "Inicializar / levantar un servicio o contenedor",  "order_index":  1},
    {"term": "roll back",    "meaning": "Revertir un despliegue o cambio a una versión anterior", "order_index":  2},
    {"term": "figure out",   "meaning": "Entender o resolver un problema",                  "order_index":  3},
    {"term": "set up",       "meaning": "Configurar o instalar un entorno o herramienta",    "order_index":  4},
    {"term": "back up",      "meaning": "Hacer una copia de seguridad",                      "order_index":  5},
    {"term": "shut down",    "meaning": "Apagar o detener un proceso o sistema",             "order_index":  6},
    {"term": "start up",     "meaning": "Arrancar o iniciar un sistema o servicio",          "order_index":  7},
    {"term": "log in",       "meaning": "Iniciar sesión en un sistema",                      "order_index":  8},
    {"term": "log out",      "meaning": "Cerrar sesión en un sistema",                       "order_index":  9},
    {"term": "sign up",      "meaning": "Registrarse en una plataforma o servicio",          "order_index": 10},
    {"term": "sign in",      "meaning": "Autenticarse en una plataforma",                    "order_index": 11},
    {"term": "call off",     "meaning": "Cancelar una reunión o tarea planificada",          "order_index": 12},
    {"term": "look up",      "meaning": "Buscar información en una fuente o documentación",  "order_index": 13},
    {"term": "break down",   "meaning": "Desglosar en partes / fallar un sistema",           "order_index": 14},
    {"term": "hand over",    "meaning": "Transferir o entregar responsabilidad a otro",       "order_index": 15},
    {"term": "point out",    "meaning": "Señalar o indicar algo en una revisión o PR",       "order_index": 16},
    {"term": "opt in",       "meaning": "Activar una funcionalidad o suscribirse",            "order_index": 17},
    {"term": "opt out",      "meaning": "Desactivar una funcionalidad o darse de baja",      "order_index": 18},
    {"term": "carry out",    "meaning": "Ejecutar o llevar a cabo una tarea o proceso",      "order_index": 19},
    {"term": "come up with", "meaning": "Proponer o generar una idea o solución",            "order_index": 20},
    {"term": "go through",   "meaning": "Revisar o recorrer un código, documento o proceso", "order_index": 21},
    {"term": "check in",     "meaning": "Registrar progreso / hacer commit de cambios",      "order_index": 22},
    {"term": "check out",    "meaning": "Revisar rama o código / explorar algo",             "order_index": 23},
    {"term": "run out of",   "meaning": "Quedarse sin recursos (memoria, tiempo, cuota)",    "order_index": 24},
    {"term": "give up",      "meaning": "Rendirse o abandonar una tarea",                    "order_index": 25},
]

# ── Glossary — Irregular Verbs (Top 50 Cambridge) ────────────────────────────
# fmt: off
GLOSSARY_IRREGULAR_VERBS: list[dict] = [
    {"term": "be",          "meaning": "ser / estar",                  "form_past": "was / were", "form_participle": "been",        "order_index":  1},
    {"term": "become",      "meaning": "convertirse en / llegar a ser", "form_past": "became",     "form_participle": "become",     "order_index":  2},
    {"term": "begin",       "meaning": "comenzar / empezar",           "form_past": "began",      "form_participle": "begun",      "order_index":  3},
    {"term": "break",       "meaning": "romper / interrumpir",         "form_past": "broke",      "form_participle": "broken",     "order_index":  4},
    {"term": "bring",       "meaning": "traer",                        "form_past": "brought",    "form_participle": "brought",    "order_index":  5},
    {"term": "build",       "meaning": "construir / compilar",         "form_past": "built",      "form_participle": "built",      "order_index":  6},
    {"term": "buy",         "meaning": "comprar",                      "form_past": "bought",     "form_participle": "bought",     "order_index":  7},
    {"term": "catch",       "meaning": "atrapar / capturar (error)",   "form_past": "caught",     "form_participle": "caught",     "order_index":  8},
    {"term": "choose",      "meaning": "elegir / seleccionar",         "form_past": "chose",      "form_participle": "chosen",     "order_index":  9},
    {"term": "come",        "meaning": "venir",                        "form_past": "came",       "form_participle": "come",       "order_index": 10},
    {"term": "cost",        "meaning": "costar",                       "form_past": "cost",       "form_participle": "cost",       "order_index": 11},
    {"term": "cut",         "meaning": "cortar",                       "form_past": "cut",        "form_participle": "cut",        "order_index": 12},
    {"term": "do",          "meaning": "hacer",                        "form_past": "did",        "form_participle": "done",       "order_index": 13},
    {"term": "draw",        "meaning": "dibujar / trazar",             "form_past": "drew",       "form_participle": "drawn",      "order_index": 14},
    {"term": "drink",       "meaning": "beber",                        "form_past": "drank",      "form_participle": "drunk",      "order_index": 15},
    {"term": "drive",       "meaning": "conducir / impulsar",          "form_past": "drove",      "form_participle": "driven",     "order_index": 16},
    {"term": "eat",         "meaning": "comer",                        "form_past": "ate",        "form_participle": "eaten",      "order_index": 17},
    {"term": "fall",        "meaning": "caer",                         "form_past": "fell",       "form_participle": "fallen",     "order_index": 18},
    {"term": "feel",        "meaning": "sentir",                       "form_past": "felt",       "form_participle": "felt",       "order_index": 19},
    {"term": "find",        "meaning": "encontrar",                    "form_past": "found",      "form_participle": "found",      "order_index": 20},
    {"term": "forget",      "meaning": "olvidar",                      "form_past": "forgot",     "form_participle": "forgotten",  "order_index": 21},
    {"term": "get",         "meaning": "obtener / conseguir",          "form_past": "got",        "form_participle": "got / gotten","order_index": 22},
    {"term": "give",        "meaning": "dar",                          "form_past": "gave",       "form_participle": "given",      "order_index": 23},
    {"term": "go",          "meaning": "ir",                           "form_past": "went",       "form_participle": "gone",       "order_index": 24},
    {"term": "grow",        "meaning": "crecer / desarrollar",         "form_past": "grew",       "form_participle": "grown",      "order_index": 25},
    {"term": "have",        "meaning": "tener",                        "form_past": "had",        "form_participle": "had",        "order_index": 26},
    {"term": "hear",        "meaning": "escuchar / oír",               "form_past": "heard",      "form_participle": "heard",      "order_index": 27},
    {"term": "hold",        "meaning": "sostener / mantener",          "form_past": "held",       "form_participle": "held",       "order_index": 28},
    {"term": "keep",        "meaning": "mantener / conservar",         "form_past": "kept",       "form_participle": "kept",       "order_index": 29},
    {"term": "know",        "meaning": "saber / conocer",              "form_past": "knew",       "form_participle": "known",      "order_index": 30},
    {"term": "leave",       "meaning": "dejar / salir",                "form_past": "left",       "form_participle": "left",       "order_index": 31},
    {"term": "let",         "meaning": "dejar / permitir",             "form_past": "let",        "form_participle": "let",        "order_index": 32},
    {"term": "lose",        "meaning": "perder",                       "form_past": "lost",       "form_participle": "lost",       "order_index": 33},
    {"term": "make",        "meaning": "hacer / crear",                "form_past": "made",       "form_participle": "made",       "order_index": 34},
    {"term": "mean",        "meaning": "significar / querer decir",    "form_past": "meant",      "form_participle": "meant",      "order_index": 35},
    {"term": "meet",        "meaning": "reunirse / conocer",           "form_past": "met",        "form_participle": "met",        "order_index": 36},
    {"term": "put",         "meaning": "poner / colocar",              "form_past": "put",        "form_participle": "put",        "order_index": 37},
    {"term": "read",        "meaning": "leer",                         "form_past": "read",       "form_participle": "read",       "order_index": 38},
    {"term": "run",         "meaning": "correr / ejecutar",            "form_past": "ran",        "form_participle": "run",        "order_index": 39},
    {"term": "say",         "meaning": "decir",                        "form_past": "said",       "form_participle": "said",       "order_index": 40},
    {"term": "see",         "meaning": "ver",                          "form_past": "saw",        "form_participle": "seen",       "order_index": 41},
    {"term": "sell",        "meaning": "vender",                       "form_past": "sold",       "form_participle": "sold",       "order_index": 42},
    {"term": "send",        "meaning": "enviar",                       "form_past": "sent",       "form_participle": "sent",       "order_index": 43},
    {"term": "set",         "meaning": "establecer / configurar",      "form_past": "set",        "form_participle": "set",        "order_index": 44},
    {"term": "show",        "meaning": "mostrar / demostrar",          "form_past": "showed",     "form_participle": "shown",      "order_index": 45},
    {"term": "speak",       "meaning": "hablar",                       "form_past": "spoke",      "form_participle": "spoken",     "order_index": 46},
    {"term": "spend",       "meaning": "gastar / invertir (tiempo)",   "form_past": "spent",      "form_participle": "spent",      "order_index": 47},
    {"term": "take",        "meaning": "tomar / llevar",               "form_past": "took",       "form_participle": "taken",      "order_index": 48},
    {"term": "tell",        "meaning": "decir / contar",               "form_past": "told",       "form_participle": "told",       "order_index": 49},
    {"term": "think",       "meaning": "pensar",                       "form_past": "thought",    "form_participle": "thought",    "order_index": 50},
    {"term": "understand",  "meaning": "entender / comprender",        "form_past": "understood", "form_participle": "understood", "order_index": 51},
    {"term": "wake",        "meaning": "despertar",                    "form_past": "woke",       "form_participle": "woken",      "order_index": 52},
    {"term": "wear",        "meaning": "llevar puesto / usar (ropa)",  "form_past": "wore",       "form_participle": "worn",       "order_index": 53},
    {"term": "win",         "meaning": "ganar",                        "form_past": "won",        "form_participle": "won",        "order_index": 54},
    {"term": "write",       "meaning": "escribir / redactar",          "form_past": "wrote",      "form_participle": "written",    "order_index": 55},
]
# fmt: on


def seed() -> None:
    print("\n🌱 English Coach — Core Grammar Path Seed")
    print("─" * 45)
    print("  Creating / verifying tables...")
    Base.metadata.create_all(bind=engine)

    with engine.begin() as conn:
        # ── lessons.category column (legacy guard) ────────────────────────────
        category_col = conn.execute(
            text("SHOW COLUMNS FROM lessons LIKE 'category'")
        ).first()
        if not category_col:
            conn.execute(
                text(
                    "ALTER TABLE lessons ADD COLUMN category VARCHAR(50) NOT NULL DEFAULT 'verb_tenses'"
                )
            )
        # ── lessons.category ENUM: extend to include general_grammar ──────────
        category_type_row = conn.execute(
            text(
                "SELECT COLUMN_TYPE FROM information_schema.COLUMNS "
                "WHERE TABLE_SCHEMA = DATABASE() "
                "AND TABLE_NAME = 'lessons' AND COLUMN_NAME = 'category'"
            )
        ).first()
        if category_type_row:
            col_type = category_type_row[0]
            if (
                "general_grammar" not in col_type
                or "modal_verbs" not in col_type
                or "phonetics" not in col_type
                or "verb_patterns" not in col_type
                or "vocabulary" not in col_type
            ):
                conn.execute(
                    text(
                        "ALTER TABLE lessons MODIFY COLUMN category "
                        "ENUM('verb_tenses','modal_verbs','phrasal_verbs','prepositions',"
                        "'irregular_verbs','general_grammar','phonetics','verb_patterns',"
                        "'conditionals','passive_voice','reported_speech','connectors',"
                        "'collocations','vocabulary') "
                        "NOT NULL DEFAULT 'verb_tenses'"
                    )
                )
        # ── lessons.type ENUM: extend to include vocabulary ───────────────────
        type_col_row = conn.execute(
            text(
                "SELECT COLUMN_TYPE FROM information_schema.COLUMNS "
                "WHERE TABLE_SCHEMA = DATABASE() "
                "AND TABLE_NAME = 'lessons' AND COLUMN_NAME = 'type'"
            )
        ).first()
        if type_col_row and "vocabulary" not in type_col_row[0]:
            conn.execute(
                text(
                    "ALTER TABLE lessons MODIFY COLUMN type "
                    "ENUM('grammar','phonetics','vocabulary') NOT NULL"
                )
            )
        # ── lessons.explanation column ─────────────────────────────────────────
        explanation_col = conn.execute(
            text("SHOW COLUMNS FROM lessons LIKE 'explanation'")
        ).first()
        if not explanation_col:
            conn.execute(
                text("ALTER TABLE lessons ADD COLUMN explanation LONGTEXT NULL")
            )
        # ── examples.sentence_type column ─────────────────────────────────────
        sentence_type_col = conn.execute(
            text("SHOW COLUMNS FROM examples LIKE 'sentence_type'")
        ).first()
        if not sentence_type_col:
            conn.execute(
                text(
                    "ALTER TABLE examples ADD COLUMN sentence_type "
                    "ENUM('affirmative','negative','interrogative') NULL"
                )
            )

    db = SessionLocal()
    try:
        existing = db.query(Level).count()
        if existing > 0:
            print(f"  Clearing {existing} existing level(s) (cascade removes all lessons/examples/exercises)...")
            db.query(Level).delete()
            db.commit()

        print("  Inserting 6 CEFR levels (A1 → C2)...")
        level_map: dict[str, Level] = {}
        for data in LEVELS:
            level = Level(**data)
            db.add(level)
            level_map[data["code"]] = level
        db.flush()

        print("  [A1] The /θ/ and /ð/ Sounds (phonetics)")
        phonetics = Lesson(level_id=level_map["A1"].id, **PHONETICS["meta"])
        db.add(phonetics)
        db.flush()
        for e in PHONETICS["examples"]:
            db.add(Example(lesson_id=phonetics.id, **e))
        for e in PHONETICS["exercises"]:
            db.add(Exercise(lesson_id=phonetics.id, **e))

        lesson_count = example_count = exercise_count = 0
        for entry in ALL_LESSONS:
            level_obj = level_map[entry["level_code"]]
            lesson = Lesson(level_id=level_obj.id, **entry["meta"])
            db.add(lesson)
            db.flush()
            print(f"  [{entry['level_code']}] {entry['meta']['title']}")
            for e in entry["examples"]:
                db.add(Example(lesson_id=lesson.id, **e))
                example_count += 1
            for e in entry["exercises"]:
                db.add(Exercise(lesson_id=lesson.id, **e))
                exercise_count += 1
            lesson_count += 1

        db.commit()

        # ── Glossary ─────────────────────────────────────────────────────────
        print("  Clearing existing glossary entries...")
        db.query(GlossaryEntry).delete()
        db.commit()

        print("  Inserting glossary — phrasal verbs...")
        for data in GLOSSARY_PHRASAL_VERBS:
            db.add(GlossaryEntry(type=GlossaryType.PHRASAL_VERB, form_past=None, form_participle=None, **data))

        print("  Inserting glossary — irregular verbs...")
        for data in GLOSSARY_IRREGULAR_VERBS:
            db.add(GlossaryEntry(type=GlossaryType.IRREGULAR_VERB, **data))

        db.commit()

        total_examples  = len(PHONETICS["examples"])  + example_count
        total_exercises = len(PHONETICS["exercises"]) + exercise_count
        print("\n  ✅ Seed completed successfully!")
        print(f"     • 6 levels (A1 → C2)")
        print(f"     • 1 phonetics lesson + {lesson_count} grammar/vocabulary lessons ({lesson_count + 1} total)")
        print(f"     • {total_examples} examples with IPA notation and Spanish translation")
        print(f"     • {total_exercises} exercises (fill_blank, multiple_choice, pronunciation)")
        print(f"     • {len(GLOSSARY_PHRASAL_VERBS)} phrasal verb glossary entries")
        print(f"     • {len(GLOSSARY_IRREGULAR_VERBS)} irregular verb glossary entries")
        print()

    except Exception as exc:
        db.rollback()
        print(f"\n  ❌ Seed failed: {exc}\n")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
