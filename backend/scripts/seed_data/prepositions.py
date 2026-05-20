# prepositions.py — Specialized Prepositions lessons (B1 → C1)
# Based on Cambridge Grammar in Use (Intermediate & Advanced) and
# "English Prepositions Explained" (Seth Lindstromberg, Benjamins).
#
# ⚠️  MANDATORY UPDATE RULE (enforced for every AI agent)
# Any time this file is added, modified, or removed, the agent MUST update:
#   1. backend/scripts/seed.py        — module docstring + import + ALL_LESSONS
#   2. README.md                      — module table in the "Seed de datos" section
#   3. .github/copilot-instructions.md — module table in the seed section
# All three locations must remain synchronised at all times.
#
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

PREPOSITIONS_LESSONS: list[dict] = [
    # ── Lesson 1: To vs For vs From ──────────────────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "To vs For vs From in Tech Contexts",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PREPOSITIONS,
            "description": (
                "Master the essential uses of To, For, and From to specify "
                "directions, purposes, and origins in technical documentation."
            ),
            "order_index": 20,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "I deployed the latest build to the production cluster successfully.",
                "translation": "Desplegué la última versión al clúster de producción exitosamente.",
                "ipa_notation": "/aɪ dɪˈplɔɪd ðə ˈleɪtɪst bɪld tə ðə prəˈdʌkʃən ˈklʌstər səkˈsɛsfəli/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "We are not using this library for its intended purpose — it causes memory leaks.",
                "translation": "No estamos usando esta librería para su propósito previsto — produce fugas de memoria.",
                "ipa_notation": "/wiː ɑːr nɒt ˈjuːzɪŋ ðɪs ˈlaɪbrəri fər ɪts ɪnˈtɛndɪd ˈpɜːrpəs — ɪt ˈkɔːzɪz ˈmɛməri liːks/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Where does this pipeline import the raw data from?",
                "translation": "¿De dónde importa este pipeline los datos en bruto?",
                "ipa_notation": "/wɛər dʌz ðɪs ˈpaɪplaɪn ɪmˈpɔːrt ðə rɔː ˈdeɪtə frɒm/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "The token is retrieved ______ the database cache layer.",
                "correct_answer": "from",
                "options": {"a": "to", "b": "for", "c": "from", "d": "at"},
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Time & Deadlines — By vs Until vs For vs During ────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Time & Deadlines: By vs Until vs For vs During",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PREPOSITIONS,
            "description": (
                "Learn to specify precise deadlines and continuous durations "
                "using By, Until, For, and During in sprint planning."
            ),
            "order_index": 21,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "We need to merge this pull request by Friday to meet the sprint deadline.",
                "translation": "Necesitamos fusionar este pull request antes del viernes para cumplir con la fecha límite del sprint.",
                "ipa_notation": "/wiː niːd tə mɜːrdʒ ðɪs pʊl rɪˈkwɛst baɪ ˈfraɪdeɪ tə miːt ðə sprɪnt ˈdɛdlaɪn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The staging environment will not be available until the infrastructure team finishes the migration.",
                "translation": "El entorno de staging no estará disponible hasta que el equipo de infraestructura finalice la migración.",
                "ipa_notation": "/ðə ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt wɪl nɒt biː əˈveɪləbl ənˈtɪl ðə ˈɪnfrəstrʌktʃər tiːm ˈfɪnɪʃɪz ðə maɪˈɡreɪʃən/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Did the on-call engineer monitor the alerts during the entire maintenance window?",
                "translation": "¿Monitorizó el ingeniero de guardia las alertas durante toda la ventana de mantenimiento?",
                "ipa_notation": "/dɪd ðiː ɒnˈkɔːl ˌɛndʒɪˈnɪər ˈmɒnɪtər ðiː əˈlɜːrts ˈdjʊərɪŋ ðiː ɪnˈtaɪər ˈmeɪntənəns ˈwɪndoʊ/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Choose the correct preposition: "
                    "'The on-call rotation kept the team awake ______ the entire incident response.'"
                ),
                "correct_answer": "during",
                "options": {
                    "a": "by",
                    "b": "until",
                    "c": "for",
                    "d": "during",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 3: Dependent Prepositions (Verbs) ─────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Dependent Prepositions (Verbs) — The Tech Lead's Arsenal",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PREPOSITIONS,
            "description": (
                "Master essential verb-preposition combinations such as rely on "
                "and succeed in to speak naturally in technical discussions."
            ),
            "order_index": 22,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "This microservice relies on the API gateway to authenticate all incoming requests.",
                "translation": "Este microservicio depende del API gateway para autenticar todas las solicitudes entrantes.",
                "ipa_notation": "/ðɪs ˈmaɪkroʊsɜːrvɪs rɪˈlaɪz ɒn ðiː ˌeɪpiːˈaɪ ˈɡeɪtweɪ tə ɔːˈθɛntɪkeɪt ɔːl ˈɪnkʌmɪŋ rɪˈkwɛsts/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The team has not succeeded in reducing the mean time to recovery below ten minutes yet.",
                "translation": "El equipo aún no ha logrado reducir el tiempo medio de recuperación por debajo de diez minutos.",
                "ipa_notation": "/ðə tiːm hæz nɒt səkˈsiːdɪd ɪn rɪˈdjuːsɪŋ ðə miːn taɪm tə rɪˈkʌvəri bɪˈloʊ tɛn ˈmɪnɪts jɛt/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Does the legacy batch job consist of more than three independent processing stages?",
                "translation": "¿Consiste el job batch heredado en más de tres etapas de procesamiento independientes?",
                "ipa_notation": "/dʌz ðə ˈlɛɡəsi bætʃ dʒɒb kənˈsɪst əv mɔːr ðæn θriː ˌɪndɪˈpɛndənt ˈprɒsɛsɪŋ ˈsteɪdʒɪz/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Choose the grammatically correct sentence using a dependent preposition:"
                ),
                "correct_answer": "The security team dealt with the zero-day vulnerability within the hour.",
                "options": {
                    "a": "The security team dealt about the zero-day vulnerability within the hour.",
                    "b": "The security team dealt with the zero-day vulnerability within the hour.",
                    "c": "The security team dealt for the zero-day vulnerability within the hour.",
                    "d": "The security team dealt on the zero-day vulnerability within the hour.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 4: Leadership Prepositions — Adjectives & Nouns ───────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Leadership Prepositions — Adjectives & Nouns",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PREPOSITIONS,
            "description": (
                "Master critical adjective and noun preposition patterns for "
                "C-level reporting and management."
            ),
            "order_index": 20,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The platform team is responsible for the reliability and uptime of all core services.",
                "translation": "El equipo de plataforma es responsable de la fiabilidad y disponibilidad de todos los servicios core.",
                "ipa_notation": "/ðə ˈplætfɔːm tiːm ɪz rɪˈspɒnsɪbl fər ðə rɪˌlaɪəˈbɪlɪti ænd ˈʌptaɪm əv ɔːl kɔːr ˈsɜːrvɪsɪz/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Senior management was not aware of the critical lack of automated test coverage in Q3.",
                "translation": "La alta dirección no era consciente de la falta crítica de cobertura de pruebas automatizadas en el tercer trimestre.",
                "ipa_notation": "/ˈsiːniər ˈmænɪdʒmənt wɒz nɒt əˈwɛər əv ðə ˈkrɪtɪkl læk əv ˌɔːtəˈmeɪtɪd tɛst ˈkʌvərɪdʒ ɪn ˌkjuːˈθriː/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Is the CTO answerable to the board for the fifteen percent increase in infrastructure costs?",
                "translation": "¿El CTO debe rendir cuentas al consejo por el incremento del quince por ciento en costos de infraestructura?",
                "ipa_notation": "/ɪz ðə ˌsiːtiːˈoʊ ˈɑːnsərəbl tə ðə bɔːrd fər ðə ˈfɪftiːn pɜːrsɛnt ɪnˈkriːs ɪn ˌɪnfrəˈstrʌktʃər kɒsts/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Select the sentence that uses the correct adjective + preposition collocation:"
                ),
                "correct_answer": "The architect is good at identifying single points of failure early.",
                "options": {
                    "a": "The architect is good in identifying single points of failure early.",
                    "b": "The architect is good for identifying single points of failure early.",
                    "c": "The architect is good at identifying single points of failure early.",
                    "d": "The architect is good on identifying single points of failure early.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 5: Space & Data Flow — Through, Across, Over & Under ──────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Space & Data Flow: Through, Across, Over & Under",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PREPOSITIONS,
            "description": (
                "Learn how to describe data movement, layer relationships, "
                "and system topology using Through, Across, Over, and Under."
            ),
            "order_index": 21,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "All client requests pass through the API gateway before reaching the internal services.",
                "translation": "Todas las solicitudes del cliente pasan a través del API gateway antes de llegar a los servicios internos.",
                "ipa_notation": "/ɔːl ˈklaɪənt rɪˈkwɛsts pɑːs θruː ðiː ˌeɪpiːˈaɪ ˈɡeɪtweɪ bɪˈfɔːr ˈriːtʃɪŋ ðiː ɪnˈtɜːrnəl ˈsɜːrvɪsɪz/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The telemetry data is not replicated across all availability zones during a regional outage.",
                "translation": "Los datos de telemetría no se replican en todas las zonas de disponibilidad durante una interrupción regional.",
                "ipa_notation": "/ðə ˌtɛlɪˈmɛtri ˈdeɪtə ɪz nɒt ˈrɛplɪkeɪtɪd əˈkrɒs ɔːl əˌveɪləˈbɪlɪti zoʊnz ˈdjʊərɪŋ ə ˈriːdʒənəl ˈaʊtɪdʒ/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Does the business logic layer operate over the data access layer in your current stack?",
                "translation": "¿Funciona la capa de lógica de negocio por encima de la capa de acceso a datos en tu stack actual?",
                "ipa_notation": "/dʌz ðə ˈbɪznɪs ˈlɒdʒɪk ˈleɪər ˈɒpəreɪt ˈoʊvər ðə ˈdeɪtə ˈækses ˈleɪər ɪn jɔːr ˈkʌrənt stæk/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which preposition best completes this sentence? "
                    "'HTTPS operates ______ TCP/IP, adding an encryption layer on top of the transport protocol.'"
                ),
                "correct_answer": "over",
                "options": {
                    "a": "through",
                    "b": "across",
                    "c": "over",
                    "d": "under",
                },
                "order_index": 1,
            },
        ],
    },
]
