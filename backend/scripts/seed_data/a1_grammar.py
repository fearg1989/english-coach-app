# a1_grammar.py — A1 Grammar lessons
# Cambridge Essential Grammar in Use (Murphy) — Beginner level.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A1_GRAMMAR_LESSONS: list[dict] = [
    # ── Lesson 1: Verb "To Be" ────────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Verb 'To Be' — States & Descriptions",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Master the verb 'to be' to express identities, "
                "descriptions, and states in technical contexts."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I am a full-stack developer.",                         "translation": "Soy un desarrollador full-stack.",                              "ipa_notation": "/aɪ æm ə ˈfʊl stæk dɪˈvɛləpər/",                         "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "She is not the system administrator.",                 "translation": "Ella no es la administradora del sistema.",                     "ipa_notation": "/ʃiː ɪz nɒt ðə ˈsɪstəm ədˈmɪnɪtreɪtər/",               "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Are you available for the code review?",               "translation": "¿Estás disponible para la revisión de código?",                "ipa_notation": "/ɑːr juː əˈveɪləbl fər ðə koʊd rɪˈvjuː/",                "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
            {"phrase": "The API was down for two hours yesterday.",            "translation": "La API estuvo caída dos horas ayer.",                           "ipa_notation": "/ðiː ˌeɪpiːˈaɪ wɒz daʊn fər tuː ˈaʊərz ˈjɛstərdeɪ/",   "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 4},
            {"phrase": "The test results were not accurate.",                  "translation": "Los resultados de las pruebas no eran precisos.",               "ipa_notation": "/ðə tɛst rɪˈzʌlts wɜːr nɒt ˈækjərɪt/",                  "sentence_type": SentenceType.NEGATIVE,      "order_index": 5},
            {"phrase": "Was the deployment successful last night?",            "translation": "¿Fue exitoso el despliegue anoche?",                           "ipa_notation": "/wɒz ðə dɪˈplɔɪmənt səkˈsɛsfəl læst naɪt/",             "sentence_type": SentenceType.INTERROGATIVE, "order_index": 6},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "The server ______ unavailable for 30 minutes last night. (was/were)", "correct_answer": "was",                          "options": None,                                                                                                                               "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence is grammatically correct?",                            "correct_answer": "The developers are tired.",     "options": {"a": "The developers is tired.", "b": "The developers are tired.", "c": "The developers am tired.", "d": "The developers be tired."}, "order_index": 2},
        ],
    },
    # ── Lesson 2: Present Simple ──────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Present Simple — Habits & Routines",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Learn the Present Simple to describe software habits, "
                "routines, general truths, and basic processes."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I write clean code every day.",      "translation": "Escribo código limpio todos los días.", "ipa_notation": "/aɪ raɪt kliːn koʊd ˈɛvri deɪ/",        "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "He does not use legacy libraries.",  "translation": "Él no usa librerías obsoletas.",        "ipa_notation": "/hiː dʌz nɒt juːz ˈlɛɡəsi ˈlaɪbrəriz/", "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Do you test your endpoints?",        "translation": "¿Pruebas tus endpoints?",               "ipa_notation": "/duː juː tɛst jɔːr ˈɛndpɔɪnts/",         "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "She ______ (deploy) the app every Friday. (Present Simple)",   "correct_answer": "deploys",                              "options": None,                                                                                                                                                    "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence uses Present Simple correctly?",                 "correct_answer": "He reviews the pull request every morning.", "options": {"a": "He is reviewing now.", "b": "He reviewed yesterday.", "c": "He reviews the pull request every morning.", "d": "He will review tomorrow."}, "order_index": 2},
        ],
    },
    # ── Lesson 3: Present Continuous ─────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Present Continuous — Actions Happening Right Now",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Express ongoing operations, server deployments, "
                "and live events in progress using Present Continuous."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {"phrase": "We are deploying the application now.",     "translation": "Estamos desplegando la aplicación ahora.",            "ipa_notation": "/wiː ɑːr dɪˈplɔɪɪŋ ðə ˌæplɪˈkeɪʃən naʊ/",      "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "The server is not responding to requests.", "translation": "El servidor no está respondiendo a las solicitudes.", "ipa_notation": "/ðə ˈsɜːrvər ɪz nɒt rɪˈspɒndɪŋ tə rɪˈkwɛsts/", "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Are they auditing the repository?",         "translation": "¿Están auditando el repositorio?",                   "ipa_notation": "/ɑːr ðeɪ ˈɔːdɪtɪŋ ðə rɪˈpɒzɪtɔːri/",           "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "The team ______ (fix) the memory leak right now. (Present Continuous)", "correct_answer": "is fixing",                    "options": None,                                                                                                                                     "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence is in Present Continuous?",                              "correct_answer": "She is refactoring the module.", "options": {"a": "She refactors daily.", "b": "She is refactoring the module.", "c": "She refactored yesterday.", "d": "She will refactor it."}, "order_index": 2},
        ],
    },
    # ── Lesson 4: Have got ────────────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Have Got — Possession & Characteristics",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Express possession, system specifications, and access "
                "credentials using the everyday 'have got' structure."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I have got a new laptop for remote work.",                    "translation": "Tengo una laptop nueva para trabajar en remoto.",            "ipa_notation": "/aɪ hæv ɡɒt ə njuː ˈlæptɒp fər rɪˈmoʊt wɜːrk/",          "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "She has not got permission to access that repository.",        "translation": "Ella no tiene permiso para acceder a ese repositorio.",       "ipa_notation": "/ʃiː hæz nɒt ɡɒt pərˈmɪʃən tə ˈækses ðæt rɪˈpɒzɪtɔːri/", "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Have you got the API credentials for the staging environment?", "translation": "¿Tienes las credenciales de la API para el entorno de staging?", "ipa_notation": "/hæv juː ɡɒt ðiː ˌeɪpiːˈaɪ krɪˈdɛnʃəlz fər ðə ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt/", "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "He ______ a valid SSH key to access the remote server. (has/have got)", "correct_answer": "has got",                                       "options": None,                                                                                                                                            "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which question form is correct with 'have got'?",                       "correct_answer": "Have you got two-factor authentication enabled?", "options": {"a": "Do you have got 2FA?", "b": "Have you got two-factor authentication enabled?", "c": "You have got 2FA?", "d": "Has you got 2FA?"}, "order_index": 2},
        ],
    },
    # ── Lesson 5: There is / There are ───────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "There Is / There Are — Existence & Places",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Describe the existence, presence, or absence of database "
                "files, servers, and bugs in your architecture."
            ),
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {"phrase": "There is a critical bug in the authentication module.",  "translation": "Hay un error crítico en el módulo de autenticación.",       "ipa_notation": "/ðer ɪz ə ˈkrɪtɪkəl bʌɡ ɪn ðiː ɔːˌθɛntɪˈkeɪʃən ˈmɒdjuːl/", "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "There are no failing tests in the pipeline.",            "translation": "No hay pruebas fallidas en el pipeline.",                   "ipa_notation": "/ðer ɑːr noʊ ˈfeɪlɪŋ tɛsts ɪn ðə ˈpaɪplaɪn/",               "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Is there a backup of the production database?",          "translation": "¿Hay una copia de seguridad de la base de datos de producción?", "ipa_notation": "/ɪz ðer ə ˈbækʌp əv ðə prəˈdʌkʃən ˈdeɪtəbeɪs/",          "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "______ three new pull requests waiting for your review.",              "correct_answer": "There are",   "options": None,                                                                                              "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence is grammatically correct?",                             "correct_answer": "There are two open issues.", "options": {"a": "There is two open issues.", "b": "There are two open issues.", "c": "There have two open issues.", "d": "There be two open issues."}, "order_index": 2},
        ],
    },
    # ── Lesson 6: Modal Verb Can ──────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Modal Verb 'Can' — Ability & Permission",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.MODAL_VERBS,
            "description": (
                "Learn to express logical ability, permission, "
                "and system possibilities using the modal verb Can."
            ),
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I can run the Docker container locally.",                   "translation": "Puedo ejecutar el contenedor Docker localmente.",                     "ipa_notation": "/aɪ kæn rʌn ðə ˈdɒkər kənˈteɪnər ˈloʊkəli/",                 "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "She cannot push directly to the main branch.",              "translation": "Ella no puede hacer push directamente a la rama principal.",          "ipa_notation": "/ʃiː ˈkænɒt pʊʃ dɪˈrɛktli tə ðə meɪn bræntʃ/",               "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Can you explain the difference between GET and POST?",      "translation": "¿Puedes explicar la diferencia entre GET y POST?",                   "ipa_notation": "/kæn juː ɪkˈspleɪn ðə ˈdɪfrəns bɪˈtwiːn ɡɛt ænd poʊst/",    "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "______ you configure the environment variables for the new service? (Can)", "correct_answer": "Can",                          "options": None,                                                                                                                                             "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence correctly expresses inability?",                              "correct_answer": "She cannot access the logs.",  "options": {"a": "She can't accessing the logs.", "b": "She not can access the logs.", "c": "She cannot access the logs.", "d": "She cans not access the logs."}, "order_index": 2},
        ],
    },
    # ── Lesson 7: Future with Going to ───────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Future with 'Going To' — Plans & Intentions",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Plan your project sprints, releases, and upcoming "
                "technical upgrades using Future with 'going to'."
            ),
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {"phrase": "I am going to clone the repository and set up the environment.", "translation": "Voy a clonar el repositorio y configurar el entorno.",       "ipa_notation": "/aɪ æm ˈɡoʊɪŋ tə kloʊn ðə rɪˈpɒzɪtɔːri ænd sɛt ʌp ðiː ɪnˈvaɪrənmənt/", "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "We are not going to release the feature on Friday.",              "translation": "No vamos a lanzar la funcionalidad el viernes.",             "ipa_notation": "/wiː ɑːr nɒt ˈɡoʊɪŋ tə rɪˈliːs ðə ˈfiːtʃər ɒn ˈfraɪdeɪ/",               "sentence_type": SentenceType.NEGATIVE,      "order_index": 2},
            {"phrase": "Are you going to attend the sprint planning tomorrow?",           "translation": "¿Vas a asistir a la planificación del sprint mañana?",       "ipa_notation": "/ɑːr juː ˈɡoʊɪŋ tə əˈtɛnd ðə sprɪnt ˈplænɪŋ təˈmɒroʊ/",               "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "We ______ (be going to) refactor the legacy module in the next sprint.", "correct_answer": "are going to",              "options": None,                                                                                                                                     "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Choose the grammatically correct future sentence:",                       "correct_answer": "I am going to update the dependencies.", "options": {"a": "I going to update the dependencies.", "b": "I am going to update the dependencies.", "c": "I go to update the dependencies.", "d": "I be going to update the dependencies."}, "order_index": 2},
        ],
    },
    # ── Lesson 8: Wh- Questions ───────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Wh- Questions — Asking for Information",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Learn how to ask specific questions about bugs, "
                "users, routes, and software systems using Wh- words."
            ),
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Who is responsible for the deployment pipeline?",       "translation": "¿Quién es responsable del pipeline de despliegue?",       "ipa_notation": "/huː ɪz rɪˈspɒnsɪbl fər ðə dɪˈplɔɪmənt ˈpaɪplaɪn/",    "sentence_type": SentenceType.INTERROGATIVE, "order_index": 1},
            {"phrase": "What does this function return when the list is empty?", "translation": "¿Qué devuelve esta función cuando la lista está vacía?",  "ipa_notation": "/wɒt dʌz ðɪs ˈfʌŋkʃən rɪˈtɜːrn wɛn ðə lɪst ɪz ˈɛmpti/", "sentence_type": SentenceType.INTERROGATIVE, "order_index": 2},
            {"phrase": "Where are the environment configuration files stored?",  "translation": "¿Dónde se almacenan los archivos de configuración de entorno?", "ipa_notation": "/wer ɑːr ðiː ɪnˈvaɪrənmənt ˌkɒnfɪɡjʊˈreɪʃən faɪlz stɔːrd/", "sentence_type": SentenceType.INTERROGATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "______ is the team lead for this microservice? (Who/What/Where)",   "correct_answer": "Who",              "options": None,                                                                                                                           "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which question word asks about a PLACE?",                            "correct_answer": "Where is the bug?", "options": {"a": "Who wrote this code?", "b": "What is the error?", "c": "Where is the bug?", "d": "When did it fail?"}, "order_index": 2},
        ],
    },
    # ── Lesson 9: Imperatives, Articles & Demonstratives ─────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Imperatives, Articles & Demonstratives",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Master developer commands, singular/plural articles, "
                "and pointers like 'this' or 'that' in your codebase."
            ),
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Open the terminal and run the seed script.",                    "translation": "Abre la terminal y ejecuta el script de seed.",                 "ipa_notation": "/ˈoʊpən ðə ˈtɜːrmɪnəl ænd rʌn ðə siːd skrɪpt/",                       "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 1},
            {"phrase": "Create an issue before you open a pull request.",               "translation": "Crea un issue antes de abrir un pull request.",                 "ipa_notation": "/kriˈeɪt ən ˈɪʃuː bɪˈfɔːr juː ˈoʊpən ə pʊl rɪˈkwɛst/",               "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 2},
            {"phrase": "This is the main branch; that is a feature branch.",            "translation": "Esta es la rama principal; esa es una rama de funcionalidad.", "ipa_notation": "/ðɪs ɪz ðə meɪn bræntʃ ðæt ɪz ə ˈfiːtʃər bræntʃ/",                   "sentence_type": SentenceType.AFFIRMATIVE,   "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK,      "question": "______ the README file before starting the project. (imperative of 'read')", "correct_answer": "Read",          "options": None,                                                                                                                             "order_index": 1},
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which sentence uses articles correctly?",                                    "correct_answer": "Open a file and check the output.", "options": {"a": "Open an file and check a output.", "b": "Open a file and check the output.", "c": "Open the file and check an output.", "d": "Open file and check output."}, "order_index": 2},
        ],
    },
]
