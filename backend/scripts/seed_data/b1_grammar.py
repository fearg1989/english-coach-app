# b1_grammar.py — B1 Grammar lessons
# Cambridge Intermediate Grammar in Use (Murphy) — Intermediate level.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B1_GRAMMAR_LESSONS: list[dict] = [
    {
        "level_code": "B1",
        "meta": {
            "title": "Present Perfect Simple — Past Events Linked to the Present",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Learn Present Perfect Simple to express recent past "
                "events, life experiences, and tasks with direct present relevance."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I have optimized the database queries successfully.", "translation": "He optimizado las consultas de base de datos exitosamente.", "ipa_notation": "/aɪ hæv ˈɒptɪmaɪzd ðə ˈdeɪtəbeɪs ˈkwɪəriz səkˈsɛsfəli/",  "order_index": 1},
            {"phrase": "She has not written the integration tests yet.",     "translation": "Ella aún no ha escrito las pruebas de integración.",         "ipa_notation": "/ʃiː hæz nɒt ˈrɪtən ðiː ˌɪntɪˈɡreɪʃən tɛsts jɛt/",         "order_index": 2},
            {"phrase": "Have you ever managed a tech team before?",          "translation": "¿Has liderado alguna vez un equipo de tecnología?",          "ipa_notation": "/hæv juː ˈɛvər ˈmænɪdʒd ə tɛk tiːm bɪˈfɔːr/",              "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence correctly uses Present Perfect?",                        "correct_answer": "We have already deployed the hotfix.",    "options": {"a": "We deployed it yesterday.", "b": "We have already deployed the hotfix.", "c": "We are deploying it.", "d": "We will deploy it."}, "order_index": 1},
            {"type": ExerciseType.FILL_BLANK,      "question": "The team ______ (never / miss) a sprint deadline. (Present Perfect)", "correct_answer": "has never missed",                        "options": None, "order_index": 2},
        ],
    },
    {
        "level_code": "B1",
        "meta": {
            "title": "Present Perfect Continuous — Duration Up to Now",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Emphasize the duration and continuous activity of "
                "ongoing tasks or debugging sessions using Present Perfect Continuous."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {"phrase": "We have been debugging this memory leak for three hours.", "translation": "Llevamos tres horas depurando esta fuga de memoria.",  "ipa_notation": "/wiː hæv biːn dɪˈbʌɡɪŋ ðɪs ˈmɛməri liːk fər θriː ˈaʊərz/", "order_index": 1},
            {"phrase": "He has not been performing well lately.",                  "translation": "No ha estado rindiendo bien últimamente.",             "ipa_notation": "/hiː hæz nɒt biːn pərˈfɔːrmɪŋ wɛl ˈleɪtli/",                  "order_index": 2},
            {"phrase": "How long have you been learning TypeScript?",              "translation": "¿Cuánto tiempo llevas aprendiendo TypeScript?",        "ipa_notation": "/haʊ lɒŋ hæv juː biːn ˈlɜːrnɪŋ ˈtaɪpskrɪpt/",                "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "She ______ (work) on this feature since Monday. (Present Perfect Continuous)",            "correct_answer": "has been working",                                       "options": None, "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence BEST emphasizes the duration of an ongoing activity?",                     "correct_answer": "They have been refactoring the codebase for two weeks.", "options": {"a": "They refactored last week.", "b": "They have refactored.", "c": "They have been refactoring the codebase for two weeks.", "d": "They were refactoring."}, "order_index": 2},
        ],
    },
    {
        "level_code": "B1",
        "meta": {
            "title": "Past Perfect Simple — The Earlier of Two Past Actions",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Learn to structure sequences of events by expressing "
                "actions completed before another past action using Past Perfect."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {"phrase": "The system had crashed before I found the root cause.",      "translation": "El sistema se había caído antes de que yo encontrara la causa raíz.", "ipa_notation": "/ðə ˈsɪstəm hæd kræʃt bɪˈfɔːr aɪ faʊnd ðə ruːt kɔːz/",            "order_index": 1},
            {"phrase": "We had not validated the inputs, so the exploit worked.",    "translation": "No habíamos validado las entradas, así que el exploit funcionó.",     "ipa_notation": "/wiː hæd nɒt ˈvælɪdeɪtɪd ðiː ˈɪnpʊts soʊ ðiː ɪkˈsplɔɪt wɜːrkt/", "order_index": 2},
            {"phrase": "Had you tested the script before running it in production?", "translation": "¿Habías probado el script antes de ejecutarlo en producción?",         "ipa_notation": "/hæd juː ˈtɛstɪd ðə skrɪpt bɪˈfɔːr ˈrʌnɪŋ ɪt ɪn prəˈdʌkʃən/",   "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence shows that action A happened BEFORE action B in the past?",                        "correct_answer": "The engineer had reviewed the code before the team merged it.", "options": {"a": "The engineer reviewed the code before the team merged it.", "b": "The engineer had reviewed the code before the team merged it.", "c": "The engineer has reviewed the code.", "d": "The engineer was reviewing the code."}, "order_index": 1},
            {"type": ExerciseType.FILL_BLANK,      "question": "By the time the incident team arrived, the attacker ______ (already / exfiltrate) the data.", "correct_answer": "had already exfiltrated", "options": None, "order_index": 2},
        ],
    },
    # ── Lesson 5: Second Conditional ─────────────────────────────────────────
    # NOTE: "To vs For vs From in Tech Contexts" was moved to
    # scripts/seed_data/prepositions.py where all Prepositions lessons live.
    {
        "level_code": "B1",
        "meta": {
            "title": "Second Conditional — Unreal Present or Future",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.CONDITIONALS,
            "description": (
                "Express hypothetical scenarios, unreal present situations, "
                "and speculative engineering choices using the Second Conditional."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "If we had infinite compute resources, we would run tests on every commit in real time.",
                "translation": "Si tuviéramos recursos de cómputo infinitos, ejecutaríamos pruebas en cada commit en tiempo real.",
                "ipa_notation": "/ɪf wiː hæd ɪnˈfɪnɪt kəmˈpjuːt rɪˈsɔːrsɪz, wiː wʊd rʌn tɛsts ɒn ˈɛvri ˈkɒmɪt ɪn rɪəl taɪm/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "If this algorithm were optimal, we would not need to cache the results.",
                "translation": "Si este algoritmo fuera óptimo, no necesitaríamos cachear los resultados.",
                "ipa_notation": "/ɪf ðɪs ˈælɡərɪðəm wɜːr ˈɒptɪməl, wiː wʊd nɒt niːd tə kæʃ ðə rɪˈzʌlts/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Would you refactor this monolith if you had three months of dedicated time?",
                "translation": "¿Refactorizarías este monolito si tuvieras tres meses de tiempo dedicado?",
                "ipa_notation": "/wʊd juː ˌriːˈfæktər ðɪs ˈmɒnəlɪθ ɪf juː hæd θriː mʌnθs əv ˈdɛdɪkeɪtɪd taɪm/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence is a grammatically correct Second Conditional?",
                "correct_answer": "If I knew Rust, I would rewrite the core engine.",
                "options": {
                    "a": "If I will know Rust, I would rewrite it.",
                    "b": "If I knew Rust, I would rewrite the core engine.",
                    "c": "If I know Rust, I will rewrite the core engine.",
                    "d": "If I had known Rust, I would have rewritten it.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "If the server ______ (have) more RAM, it would not crash under peak load. (Second Conditional)",
                "correct_answer": "had",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 6: Modals of Deduction ────────────────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Modals of Deduction — Must, Might, Can't",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.MODAL_VERBS,
            "description": (
                "Learn to express logical guesses, levels of certainty, "
                "and system deductions using must, might, and can't."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The build must have a configuration error — it passes locally but fails in CI every time.",
                "translation": "La build debe tener un error de configuración — pasa localmente pero falla en CI siempre.",
                "ipa_notation": "/ðə bɪld mʌst hæv ə ˌkɒnfɪɡəˈreɪʃən ˈɛrər — ɪt ˈpæsɪz ˈloʊkəli bʌt feɪlz ɪn siː aɪ ˈɛvri taɪm/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "It can't be a caching issue — we already invalidated the entire cache layer.",
                "translation": "No puede ser un problema de caché — ya hemos invalidado toda la capa de caché.",
                "ipa_notation": "/ɪt kænt biː ə ˈkæʃɪŋ ˈɪʃuː — wiː ɔːlˈrɛdi ɪnˈvælɪdeɪtɪd ðiː ɪnˈtaɪər kæʃ ˈleɪər/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Could it be a race condition in the async thread pool?",
                "translation": "¿Podría ser una condición de carrera en el pool de hilos asíncronos?",
                "ipa_notation": "/kʊd ɪt biː ə reɪs kənˈdɪʃən ɪn ðiː eɪˈsɪŋk θrɛd puːl/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "The API response time is consistently 8 seconds. Which modal expresses the STRONGEST certainty?",
                "correct_answer": "There must be a performance bottleneck in the query layer.",
                "options": {
                    "a": "There might be a performance bottleneck.",
                    "b": "There must be a performance bottleneck in the query layer.",
                    "c": "There can't be a performance bottleneck.",
                    "d": "There could be a performance bottleneck.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Only one person has push access to main — it ______ be anyone else who caused the conflict.",
                "correct_answer": "can't",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 7: Reported Speech ─────────────────────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Reported Speech — Passing on Information",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.REPORTED_SPEECH,
            "description": (
                "Master reporting developer statements, shifts in tenses, "
                "and indirect questions using Reported Speech."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Direct: 'The deployment is ready.' → The tech lead said that the deployment was ready.",
                "translation": "Directo: 'El despliegue está listo.' → El líder técnico dijo que el despliegue estaba listo.",
                "ipa_notation": "/ðə tɛk lɛd sɛd ðæt ðə dɪˈplɔɪmənt wɒz ˈrɛdi/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Direct: 'We will not merge on Fridays.' → The manager said they would not merge on Fridays.",
                "translation": "Directo: 'No haremos merge los viernes.' → El gerente dijo que no harían merge los viernes.",
                "ipa_notation": "/ðə ˈmænɪdʒər sɛd ðeɪ wʊd nɒt mɜːrdʒ ɒn ˈfraɪdeɪz/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Direct: 'Did you run the integration tests?' → She asked whether I had run the integration tests.",
                "translation": "Directo: '¿Ejecutaste las pruebas de integración?' → Ella preguntó si yo había ejecutado las pruebas de integración.",
                "ipa_notation": "/ʃiː ɑːskt ˈwɛðər aɪ hæd rʌn ðiː ˌɪntɪˈɡreɪʃən tɛsts/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Transform to Reported Speech: 'The API is down.' → He said that the API ______ down.",
                "correct_answer": "was",
                "options": {"a": "is", "b": "was", "c": "will be", "d": "would be"},
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "She said: 'I will push the fix tonight.' → She said that she ______ push the fix that night.",
                "correct_answer": "would",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 8: Passive Voice ───────────────────────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Passive Voice (All Tenses) — Focus on the Action",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PASSIVE_VOICE,
            "description": (
                "Focus on system actions, automated events, and "
                "documentation structures using Passive Voice across all tenses."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "All incoming API requests are validated by the authentication middleware.",
                "translation": "Todas las solicitudes de API entrantes son validadas por el middleware de autenticación.",
                "ipa_notation": "/ɔːl ˈɪnkʌmɪŋ ˌeɪpiːˈaɪ rɪˈkwɛsts ɑːr ˈvælɪdeɪtɪd baɪ ðiː ɔːˌθɛntɪˈkeɪʃən ˈmɪdlwɛər/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The legacy module has not been updated since the initial release.",
                "translation": "El módulo heredado no ha sido actualizado desde el lanzamiento inicial.",
                "ipa_notation": "/ðə ˈlɛɡəsi ˈmɒdjuːl hæz nɒt biːn ˈʌpdeɪtɪd sɪns ðiː ɪˈnɪʃəl rɪˈliːs/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Will the new microservice be containerised before the sprint review?",
                "translation": "¿Será el nuevo microservicio contenedorizado antes de la revisión del sprint?",
                "ipa_notation": "/wɪl ðə njuː ˈmaɪkroʊˌsɜːrvɪs biː kənˈteɪnəraɪzd bɪˈfɔːr ðə sprɪnt rɪˈvjuː/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Transform to Passive: 'A senior engineer reviews every pull request.' → Every pull request ______ by a senior engineer.",
                "correct_answer": "is reviewed",
                "options": {"a": "reviews", "b": "is reviewing", "c": "is reviewed", "d": "was reviewed"},
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "The vulnerability ______ (discover — Present Perfect Passive) by the security audit team.",
                "correct_answer": "has been discovered",
                "options": None,
                "order_index": 2,
            },
        ],
    },
]
