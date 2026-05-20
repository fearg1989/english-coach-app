# b2_grammar.py — B2 Grammar lessons
# Cambridge Advanced Grammar in Use (Hewings) — Upper Intermediate level.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B2_GRAMMAR_LESSONS: list[dict] = [
    {
        "level_code": "B2",
        "meta": {
            "title": "Past Perfect Continuous — Duration Before a Past Point",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Emphasize the duration and continuous process of a past "
                "activity before another specific past moment using Past Perfect Continuous."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {"phrase": "They had been building the architecture for months before the cancellation.", "translation": "Llevaban meses construyendo la arquitectura antes de la cancelación.", "ipa_notation": "/ðeɪ hæd biːn ˈbɪldɪŋ ðiː ˈɑːrkɪtɛktʃər fər mʌnθs bɪˈfɔːr ðə ˌkænsəˈleɪʃən/", "order_index": 1},
            {"phrase": "I had not been sleeping well due to the production incidents.",              "translation": "No había estado durmiendo bien a causa de los incidentes en producción.", "ipa_notation": "/aɪ hæd nɒt biːn ˈsliːpɪŋ wɛl djuː tə ðə prəˈdʌkʃən ˈɪnsɪdənts/",           "order_index": 2},
            {"phrase": "Had you been monitoring the traffic before the server failed?",             "translation": "¿Habías estado monitoreando el tráfico antes de que el servidor fallara?", "ipa_notation": "/hæd juː biːn ˈmɒnɪtərɪŋ ðə ˈtræfɪk bɪˈfɔːr ðə ˈsɜːrvər feɪld/",          "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "The server crashed because developers ______ (ignore) memory warnings for weeks. (Past Perfect Continuous)", "correct_answer": "had been ignoring",                                            "options": None, "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence BEST expresses duration of an activity before a past event?",                              "correct_answer": "They had been patching vulnerabilities for a month before the audit.", "options": {"a": "They patched vulnerabilities.", "b": "They had patched vulnerabilities.", "c": "They had been patching vulnerabilities for a month before the audit.", "d": "They were patching vulnerabilities."}, "order_index": 2},
        ],
    },
    {
        "level_code": "B2",
        "meta": {
            "title": "Future Continuous — Actions in Progress at a Future Moment",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Express ongoing actions or planned events in progress "
                "at a specific moment in the future using Future Continuous."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {"phrase": "This time tomorrow, we will be running the performance benchmark.", "translation": "A esta hora mañana, estaremos ejecutando el benchmark de rendimiento.", "ipa_notation": "/ðɪs taɪm təˈmɒroʊ wiː wɪl biː ˈrʌnɪŋ ðə pərˈfɔːrməns ˈbɛntʃmɑːrk/", "order_index": 1},
            {"phrase": "I will not be participating in the scrum meeting next Friday.",    "translation": "No estaré participando en la reunión de scrum el próximo viernes.",   "ipa_notation": "/aɪ wɪl nɒt biː pɑːrˈtɪsɪpeɪtɪŋ ɪn ðə skrʌm ˈmiːtɪŋ nɛkst ˈfraɪdeɪ/", "order_index": 2},
            {"phrase": "Will you be working remotely next sprint?",                       "translation": "¿Estarás trabajando de forma remota el próximo sprint?",              "ipa_notation": "/wɪl juː biː ˈwɜːrkɪŋ rɪˈmoʊtli nɛkst sprɪnt/",                        "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "At 9 PM, the on-call engineer ______ (monitor) the deployment. (Future Continuous)", "correct_answer": "will be monitoring",                          "options": None, "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence expresses an action IN PROGRESS at a specific future time?",          "correct_answer": "At midnight, the backup job will be running.", "options": {"a": "The backup will run at midnight.", "b": "At midnight, the backup job will be running.", "c": "The backup ran at midnight.", "d": "The backup has been running."}, "order_index": 2},
        ],
    },
    {
        "level_code": "B2",
        "meta": {
            "title": "Future Perfect — Completion Before a Future Deadline",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Learn to express completed actions, final results, and "
                "reached milestones before a future deadline using Future Perfect."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {"phrase": "By the end of the sprint, we will have closed all pending tickets.",  "translation": "Para el final del sprint, habremos cerrado todos los tickets pendientes.", "ipa_notation": "/baɪ ðiː ɛnd əv ðə sprɪnt wiː wɪl hæv kloʊzd ɔːl ˈpɛndɪŋ ˈtɪkɪts/",    "order_index": 1},
            {"phrase": "The team will not have finished the migration by tomorrow morning.",  "translation": "El equipo no habrá terminado la migración para mañana por la mañana.",    "ipa_notation": "/ðə tiːm wɪl nɒt hæv ˈfɪnɪʃt ðə maɪˈɡreɪʃən baɪ təˈmɒroʊ ˈmɔːrnɪŋ/",  "order_index": 2},
            {"phrase": "Will you have reviewed the architecture before the deadline?",        "translation": "¿Habrás revisado la arquitectura antes de la fecha límite?",              "ipa_notation": "/wɪl juː hæv rɪˈvjuːd ðiː ˈɑːrkɪtɛktʃər bɪˈfɔːr ðə ˈdɛdlaɪn/",         "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "By next Monday, the QA team ______ (test) all the new features. (Future Perfect)", "correct_answer": "will have tested",                                   "options": None, "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence correctly uses the Future Perfect?",                                "correct_answer": "By 2027, we will have migrated all data to the cloud.", "options": {"a": "By 2027, we migrate the data.", "b": "By 2027, we will be migrating.", "c": "By 2027, we will have migrated all data to the cloud.", "d": "By 2027, we migrated the data."}, "order_index": 2},
        ],
    },
    {
        "level_code": "B2",
        "meta": {
            "title": "Top Tech Phrasal Verbs for Developers",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PHRASAL_VERBS,
            "description": (
                "Master essential tech phrasal verbs like spin up, roll "
                "back, and figure out for everyday developer collaboration."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I will spin up a new Docker container.",   "translation": "Levantaré un nuevo contenedor Docker.",      "ipa_notation": "/aɪ wɪl spɪn ʌp ə njuː ˈdɒkər kənˈteɪnər/",          "order_index": 1},
            {"phrase": "The script did not spin up the server.",   "translation": "El script no levantó el servidor.",          "ipa_notation": "/ðə skrɪpt dɪd nɒt spɪn ʌp ðə ˈsɜːrvər/",             "order_index": 2},
            {"phrase": "Did you spin up the staging environment?", "translation": "¿Levantaste el entorno de staging?",         "ipa_notation": "/dɪd juː spɪn ʌp ðə ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt/",       "order_index": 3},
            {"phrase": "We rolled back the deployment due to a bug.", "translation": "Revertimos el despliegue debido a un error.", "ipa_notation": "/wiː roʊld bæk ðə dɪˈplɔɪmənt djuː tə ə bʌɡ/",      "order_index": 4},
            {"phrase": "You shouldn't roll back without a backup.", "translation": "No deberías revertir sin un respaldo.",     "ipa_notation": "/juː ˈʃʊdnt roʊl bæk wɪˈðaʊt ə ˈbækʌp/",             "order_index": 5},
            {"phrase": "I finally figured out the memory leak issue.", "translation": "Finalmente entendí el problema de fuga de memoria.", "ipa_notation": "/aɪ ˈfaɪnəli ˈfɪɡjərd aʊt ðə ˈmɛməri liːk ˈɪʃuː/", "order_index": 6},
            {"phrase": "Can you figure out why the API is failing?", "translation": "¿Puedes entender por qué falla la API?",  "ipa_notation": "/kæn juː ˈfɪɡjər aʊt waɪ ðiː ˌeɪpiːˈaɪ ɪz ˈfeɪlɪŋ/", "order_index": 7},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "The DevOps engineer will ______ ______ three containers for the load test. (spin)", "correct_answer": "spin up",    "options": None,                                                                                    "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which phrasal verb means 'to revert a release to a previous version'?",            "correct_answer": "roll back",  "options": {"a": "spin up", "b": "roll back", "c": "figure out", "d": "pull down"},               "order_index": 2},
            {"type": ExerciseType.FILL_BLANK,      "question": "We couldn't ______ ______ the root cause of the 503 error until we checked the logs.", "correct_answer": "figure out", "options": None,                                                                               "order_index": 3},
        ],
    },
    # ── Lesson 5: Mixed Conditionals ─────────────────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Mixed Conditionals — Present Results of Past Decisions",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.CONDITIONALS,
            "description": (
                "Analyze past decisions and their present consequences "
                "during technical architecture trade-offs using Mixed Conditionals."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "If we had chosen a monolith, our deployment pipeline would be much simpler now.",
                "translation": "Si hubiéramos elegido un monolito, nuestro pipeline de despliegue sería mucho más simple ahora.",
                "ipa_notation": "/ɪf wiː hæd ˈtʃoʊzən ə ˈmɒnəlɪθ | aʊər dɪˈplɔɪmənt ˈpaɪplaɪn wʊd biː mʌtʃ ˈsɪmplər naʊ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "If the team had adopted TypeScript from the start, we would not be dealing with these type errors today.",
                "translation": "Si el equipo hubiera adoptado TypeScript desde el principio, no estaríamos lidiando con estos errores de tipo hoy.",
                "ipa_notation": "/ɪf ðə tiːm hæd əˈdɒptɪd ˈtaɪpskrɪpt frəm ðə stɑːrt | wiː wʊd nɒt biː ˈdiːlɪŋ wɪð ðiːz taɪp ˈɛrərz təˈdeɪ/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Would we still be on-call every weekend if we had implemented proper alerting back then?",
                "translation": "¿Seguiríamos de guardia todos los fines de semana si hubiéramos implementado alertas adecuadas en ese entonces?",
                "ipa_notation": "/wʊd wiː stɪl biː ɒn kɔːl ˈɛvri ˈwiːkɛnd ɪf wiː hæd ˌɪmplɪˈmɛntɪd ˈprɒpər əˈlɜːrtɪŋ bæk ðɛn/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which sentence is a correct Mixed Conditional (past decision → present result)?"
                ),
                "correct_answer": "If we had set up monitoring, we would know the root cause now.",
                "options": {
                    "a": "If we set up monitoring, we will know the root cause.",
                    "b": "If we had set up monitoring, we would know the root cause now.",
                    "c": "If we had set up monitoring, we would have known the root cause.",
                    "d": "If we set up monitoring, we would know the root cause.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "If we ______ (migrate) to the cloud three years ago, "
                    "our infrastructure ______ (be) far more resilient today. "
                    "(Mixed Conditional — Past Perfect / would + base verb)"
                ),
                "correct_answer": "had migrated / would be",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 6: Modals of Deduction in the Past ────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Modals of Deduction in the Past — Speculating about Events",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.MODAL_VERBS,
            "description": (
                "Express logical conclusions, certainty, and possibilities "
                "about past system events using past modals."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The database must have run out of connection pool slots — all queries are timing out.",
                "translation": "La base de datos debe haber agotado los slots del connection pool — todas las consultas están fallando por tiempo de espera.",
                "ipa_notation": "/ðə ˈdeɪtəbeɪs mʌst hæv rʌn aʊt əv kəˈnɛkʃən puːl slɒts | ɔːl ˈkwɪəriz ɑːr ˈtaɪmɪŋ aʊt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The intern can't have deployed to production — she doesn't have the required permissions.",
                "translation": "La practicante no puede haber desplegado a producción — no tiene los permisos requeridos.",
                "ipa_notation": "/ðə ɪnˈtɜːrn kɑːnt hæv dɪˈplɔɪd tə prəˈdʌkʃən | ʃiː ˈdʌznt hæv ðə rɪˈkwaɪərd pərˈmɪʃənz/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Could the scheduled job have triggered the cascade failure during peak hours?",
                "translation": "¿Podría el job programado haber desencadenado el fallo en cascada durante las horas pico?",
                "ipa_notation": "/kʊd ðə ˈʃɛdjuːld dʒɒb hæv ˈtrɪɡərd ðə kæsˈkeɪd ˈfeɪljər ˈdjʊərɪŋ piːk aʊərz/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "The CI pipeline failed at 3 AM with no code changes. "
                    "Which sentence expresses near-certainty that a network issue caused it?"
                ),
                "correct_answer": "There must have been a transient network error.",
                "options": {
                    "a": "There might have been a network error.",
                    "b": "There must have been a transient network error.",
                    "c": "There can't have been a network error.",
                    "d": "There could have not been a network error.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "The API returned a 200 status but the data was wrong. "
                    "The cache ______ (serve) a stale response — that's the most likely explanation. "
                    "(must have + past participle)"
                ),
                "correct_answer": "must have served",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 7: Advanced Passive & Distancing ──────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Advanced Passive Voice & Distancing — Objective Reporting",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.PASSIVE_VOICE,
            "description": (
                "Use advanced passive structures and objective distancing "
                "to write formal, professional incident reports."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "It is estimated that the new caching layer will reduce latency by 40%.",
                "translation": "Se estima que la nueva capa de caché reducirá la latencia en un 40%.",
                "ipa_notation": "/ɪt ɪz ˈɛstɪmeɪtɪd ðæt ðə njuː ˈkæʃɪŋ ˈleɪər wɪl rɪˈdjuːs ˈleɪtənsi baɪ ˈfɔːrti pɜːrsɛnt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The root cause is not believed to have been a hardware failure.",
                "translation": "No se cree que la causa raíz haya sido un fallo de hardware.",
                "ipa_notation": "/ðə ruːt kɔːz ɪz nɒt bɪˈliːvd tə hæv biːn ə ˈhɑːrdwɛr ˈfeɪljər/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Is it expected that the on-call team will be notified automatically?",
                "translation": "¿Se espera que el equipo de guardia sea notificado automáticamente?",
                "ipa_notation": "/ɪz ɪt ɪkˈspɛktɪd ðæt ðiː ɒn kɔːl tiːm wɪl biː ˈnoʊtɪfaɪd ˌɔːtəˈmætɪkli/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Rewrite actively: 'Engineers found that the config file was corrupted.' "
                    "Which passive distancing sentence best replaces it in a formal incident report?"
                ),
                "correct_answer": "It was found that the config file had been corrupted.",
                "options": {
                    "a": "The config file corrupted.",
                    "b": "It was found that the config file had been corrupted.",
                    "c": "The config file was corrupting.",
                    "d": "It found that the config file was corrupt.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "Complete with the correct distancing structure: "
                    "'______ ______ ______ that the API will reach general availability next quarter.' "
                    "(It / be / expect)"
                ),
                "correct_answer": "It is expected",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 8: Defining vs. Non-Defining Relative Clauses ─────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Defining vs. Non-Defining Relative Clauses — Adding Details",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Learn to add essential details or non-essential commentary "
                "to your system descriptions using Relative Clauses."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The microservice that handles authentication was the one that failed during the outage.",
                "translation": "El microservicio que gestiona la autenticación fue el que falló durante la interrupción.",
                "ipa_notation": "/ðə ˈmaɪkroʊˌsɜːrvɪs ðæt ˈhændlz ɔːˌθɛntɪˈkeɪʃən wɒz ðə wʌn ðæt feɪld ˈdjʊərɪŋ ðiː ˈaʊtɪdʒ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Our staging environment, which does not mirror production traffic, failed to catch the edge case.",
                "translation": "Nuestro entorno de staging, que no refleja el tráfico de producción, no logró detectar el caso extremo.",
                "ipa_notation": "/aʊər ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt | wɪtʃ dʌz nɒt ˈmɪrər prəˈdʌkʃən ˈtræfɪk | feɪld tə kætʃ ðiː ɛdʒ keɪs/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Is the on-call engineer the person whose phone number is listed in the runbook?",
                "translation": "¿Es el ingeniero de guardia la persona cuyo número de teléfono está en el runbook?",
                "ipa_notation": "/ɪz ðiː ɒn kɔːl ˌɛndʒɪˈnɪər ðə ˈpɜːrsən huːz foʊn ˈnʌmbər ɪz ˈlɪstɪd ɪn ðə ˈrʌnbʊk/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which sentence uses a NON-DEFINING relative clause correctly?"
                ),
                "correct_answer": "The new CI server, which we installed last week, runs jobs 3x faster.",
                "options": {
                    "a": "The server that we installed last week runs jobs 3x faster.",
                    "b": "The new CI server, which we installed last week, runs jobs 3x faster.",
                    "c": "The new CI server that we installed last week, runs jobs 3x faster.",
                    "d": "The new CI server, that we installed last week, runs jobs 3x faster.",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "Complete with the correct relative pronoun: "
                    "'The repository ______ stores all our infrastructure-as-code is hosted on GitHub.' "
                    "(defining clause — thing)"
                ),
                "correct_answer": "that",
                "options": None,
                "order_index": 2,
            },
        ],
    },
]
