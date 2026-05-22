# a2_grammar.py — Pristine plain-text JSON seed data
# Cleaned programmatically to comply with strict Separation of Concerns.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A2_GRAMMAR_LESSONS: list[dict] = [
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Past Simple — Completed Actions',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Structure',
                        "layout": 'list',
                        "items": [
                            'Regular affirmative: Subject + verb + -ed — I initialized the repo.',
                            "Negative: Subject + didn't + base verb — We didn't find bugs.",
                            'Question: Did + subject + base verb? — Did you commit?',
                        ],
                    },
                    {
                        "title": 'Regular -ed Rules',
                        "layout": 'table',
                        "headers": ['Rule', 'Base', 'Past Simple'],
                        "rows": [
                            ['Most verbs: add -ed', 'deploy', 'deployed'],
                            ['Ends in -e: add -d only', 'initialize', 'initialized'],
                            ['Short CVC: double final consonant + -ed', 'commit', 'committed'],
                            ['Ends in consonant + y: change y → i + -ed', 'carry', 'carried'],
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Use Past Simple for completed actions at specific past times. Regular verbs end in -ed; irregulars have unique past forms.',
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I initialized the repository yesterday.',
                "translation": 'Inicialicé el repositorio ayer.',
                "ipa_notation": '/aɪ ɪˈnɪʃəlaɪzd ðə rɪˈpɒzɪtɔːri ˈjɛstərdeɪ/',
                "order_index": 1,
            },
            {
                "phrase": 'We did not find any critical bugs.',
                "translation": 'No encontramos ningún error crítico.',
                "ipa_notation": '/wiː dɪd nɒt faɪnd ˈɛni ˈkrɪtɪkəl bʌɡz/',
                "order_index": 2,
            },
            {
                "phrase": 'Did you commit your latest changes?',
                "translation": '¿Hiciste commit de tus últimos cambios?',
                "ipa_notation": '/dɪd juː kəˈmɪt jɔːr ˈleɪtɪst ˈtʃeɪndʒɪz/',
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'The CI pipeline ______ (fail) three times last night. (Past Simple)',
                "correct_answer": 'failed',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the correct Past Simple form of 'write'?",
                "correct_answer": 'wrote',
                "options": {
                    "a": 'writed',
                    "b": 'written',
                    "c": 'wrote',
                    "d": 'writ',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Past Continuous — Interrupted Past Actions',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Structure',
                        "layout": 'list',
                        "items": [
                            'Affirmative: Subject + was/were + verb-ing — I was refactoring the logic.',
                            'Negative: Subject + was/were + not + verb-ing — They were not monitoring the logs.',
                            'Question: Was/Were + subject + verb-ing? — Were you working on the backend?',
                        ],
                    },
                    {
                        "title": 'Classic Two-Clause Pattern',
                        "layout": 'table',
                        "headers": ['Clause type', 'Tense', 'Example'],
                        "rows": [
                            ['Background action (ongoing)', 'Past Continuous', 'I was refactoring the logic...'],
                            ['Interrupting event (completed)', 'Past Simple', '...when the database crashed.'],
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Describe ongoing past actions or background events that were interrupted by another action using Past Continuous.',
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I was refactoring the logic when the database crashed.',
                "translation": 'Estaba refactorizando la lógica cuando la base de datos falló.',
                "ipa_notation": '/aɪ wɒz riːˈfæktərɪŋ ðə ˈlɒdʒɪk wɛn ðə ˈdeɪtəbeɪs kræʃt/',
                "order_index": 1,
            },
            {
                "phrase": 'They were not monitoring the logs during the migration.',
                "translation": 'No estaban monitoreando los logs durante la migración.',
                "ipa_notation": '/ðeɪ wɜːr nɒt ˈmɒnɪtərɪŋ ðə lɒɡz ˈdjʊərɪŋ ðə maɪˈɡreɪʃən/',
                "order_index": 2,
            },
            {
                "phrase": 'Were you working on the backend when it happened?',
                "translation": '¿Estabas trabajando en el backend cuando ocurrió?',
                "ipa_notation": '/wɜːr juː ˈwɜːrkɪŋ ɒn ðə ˈbækɛnd wɛn ɪt ˈhæpənd/',
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Choose the correct form: 'The server ______ when I checked the dashboard.'",
                "correct_answer": 'was crashing',
                "options": {
                    "a": 'crashed',
                    "b": 'was crashing',
                    "c": 'is crashing',
                    "d": 'has crashed',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'While the senior dev ______ (review) the PR, the junior pushed a new commit.',
                "correct_answer": 'was reviewing',
                "options": None,
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": "Future with 'Be Going To' — Planned Intentions",
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Structure',
                        "layout": 'list',
                        "items": [
                            'Affirmative: Subject + am/is/are + going to + base verb',
                            'Negative: Subject + am/is/are + not + going to + base verb',
                            'Question: Am/Is/Are + subject + going to + base verb?',
                        ],
                    },
                    {
                        "title": 'Two Core Uses',
                        "layout": 'table',
                        "headers": ['Use', 'Explanation', 'Example'],
                        "rows": [
                            ['Prior plan / intention', 'The decision was made before now', 'We are going to migrate the microservices next week.'],
                            ['Evidence-based prediction', 'Present signs indicate a future outcome', 'The memory leak is getting worse — the app is going to crash.'],
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": "Express planned intentions, prior decisions, and predictions based on visible evidence using 'be going to'.",
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'We are going to migrate the microservices next week.',
                "translation": 'Vamos a migrar los microservicios la próxima semana.',
                "ipa_notation": '/wiː ɑːr ˈɡoʊɪŋ tə maɪˈɡreɪt ðə ˈmaɪkroʊˌsɜːrvɪsɪz nɛkst wiːk/',
                "order_index": 1,
            },
            {
                "phrase": 'Management is not going to approve the budget.',
                "translation": 'La dirección no va a aprobar el presupuesto.',
                "ipa_notation": '/ˈmænɪdʒmənt ɪz nɒt ˈɡoʊɪŋ tə əˈpruːv ðə ˈbʌdʒɪt/',
                "order_index": 2,
            },
            {
                "phrase": 'Are you going to configure the Docker container?',
                "translation": '¿Vas a configurar el contenedor Docker?',
                "ipa_notation": '/ɑːr juː ˈɡoʊɪŋ tə kənˈfɪɡər ðə ˈdɒkər kənˈteɪnər/',
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'Look at the roadmap — they ______ (release) v2.0 next quarter. (be going to)',
                "correct_answer": 'are going to release',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence expresses a PREVIOUSLY PLANNED intention?',
                "correct_answer": 'We are going to refactor the monolith this sprint.',
                "options": {
                    "a": 'I will fix that bug now.',
                    "b": 'We are going to refactor the monolith this sprint.',
                    "c": 'She is fixing the bug.',
                    "d": 'They fixed it yesterday.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": "Future with 'Will' — Spontaneous Decisions & Promises",
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Structure',
                        "layout": 'list',
                        "items": [
                            "Affirmative: Subject + will ('ll) + base verb — I will fix it now.",
                            "Negative: Subject + won't + base verb — It won't scale.",
                            'Question: Will + subject + base verb? — Will the API support this?',
                        ],
                    },
                    {
                        "title": "Four Core Uses of 'Will'",
                        "layout": 'table',
                        "headers": ['Use', 'Example'],
                        "rows": [
                            ['Spontaneous decision (decided right now)', "A bug appears → I'll open a ticket immediately."],
                            ['Promise', "I won't push untested code to main."],
                            ['Offer', "I'll review your PR if you want."],
                            ['Neutral prediction (no visible evidence)', 'AI will change how we write code.'],
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Learn to express spontaneous decisions, offers, promises, and future predictions using the modal verb Will.',
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I will fix this critical security error right away.',
                "translation": 'Voy a corregir este error crítico de seguridad ahora mismo.',
                "ipa_notation": '/aɪ wɪl fɪks ðɪs ˈkrɪtɪkəl sɪˈkjʊərɪti ˈɛrər raɪt əˈweɪ/',
                "order_index": 1,
            },
            {
                "phrase": 'The system will not scale without optimization.',
                "translation": 'El sistema no escalará sin optimización.',
                "ipa_notation": '/ðə ˈsɪstəm wɪl nɒt skeɪl wɪˈðaʊt ˌɒptɪmaɪˈzeɪʃən/',
                "order_index": 2,
            },
            {
                "phrase": 'Will the API support high traffic?',
                "translation": '¿Soportará la API un alto tráfico?',
                "ipa_notation": '/wɪl ðiː ˌeɪ piː ˈaɪ səˈpɔːrt haɪ ˈtræfɪk/',
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Someone reports a production bug. You respond spontaneously: 'I ______ look into it immediately.'",
                "correct_answer": 'will',
                "options": {
                    "a": 'am going to',
                    "b": 'will',
                    "c": 'was',
                    "d": 'have',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Don't worry, I ______ (not / push) untested code to main. (will)",
                "correct_answer": "won't push",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Essential Irregular Verbs Blueprint',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'High-Frequency Irregular Verbs for Tech',
                        "layout": 'table',
                        "headers": ['Base', 'Past Simple', 'Past Participle', 'Tech context'],
                        "rows": [
                            ['write', 'wrote', 'written', 'I wrote / I have written the tests.'],
                            ['build', 'built', 'built', 'We built / have built the API.'],
                            ['run', 'ran', 'run', 'The pipeline ran / has run.'],
                            ['find', 'found', 'found', 'We found / have found the bug.'],
                            ['break', 'broke', 'broken', 'The deploy broke / has broken prod.'],
                            ['go', 'went', 'gone', 'The server went / has gone down.'],
                            ['begin', 'began', 'begun', 'The migration began / has begun.'],
                            ['bring', 'brought', 'brought', 'She brought / has brought new ideas.'],
                        ],
                    },
                    {
                        "title": 'Three Verb Patterns',
                        "layout": 'list',
                        "items": [
                            'A-B-C: All three forms are different — write / wrote / written.',
                            'A-B-B: Past Simple = Participle — build / built / built.',
                            'A-A-A: All three forms are the same — cut / cut / cut.',
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.IRREGULAR_VERBS,
            "description": 'Build a reliable blueprint for the most common irregular verbs, mastering their base, past, and participle forms.',
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I write clean code every day.',
                "translation": 'Escribo código limpio todos los días.',
                "ipa_notation": '/aɪ raɪt kliːn koʊd ˈɛvri deɪ/',
                "order_index": 1,
            },
            {
                "phrase": 'Yesterday, I wrote the implementation tests.',
                "translation": 'Ayer escribí las pruebas de implementación.',
                "ipa_notation": '/ˈjɛstərdeɪ, aɪ roʊt ði ˌɪmplɪmɛnˈteɪʃən tɛsts/',
                "order_index": 2,
            },
            {
                "phrase": 'I have written the API endpoints.',
                "translation": 'He escrito los endpoints de la API.',
                "ipa_notation": '/aɪ hæv ˈrɪtən ði ˌeɪpiːaɪ ˈɛndˌpɔɪnts/',
                "order_index": 3,
            },
            {
                "phrase": 'She is writing the documentation right now.',
                "translation": 'Ella está escribiendo la documentación ahora mismo.',
                "ipa_notation": '/ʃiː ɪz ˈraɪtɪŋ ðə ˌdɒkjʊmɛnˈteɪʃən raɪt naʊ/',
                "order_index": 4,
            },
            {
                "phrase": 'They go to the office on Mondays.',
                "translation": 'Ellos van a la oficina los lunes.',
                "ipa_notation": '/ðeɪ ɡoʊ tə ði ˈɒfɪs ɒn ˈmʌndeɪz/',
                "order_index": 5,
            },
            {
                "phrase": 'We went live with the project last night.',
                "translation": 'Salimos en vivo con el proyecto anoche.',
                "ipa_notation": '/wiː wɛnt laɪv wɪð ðə ˈprɒdʒɛkt læst naɪt/',
                "order_index": 6,
            },
            {
                "phrase": 'The team has gone to the deployment briefing.',
                "translation": 'El equipo ha ido a la reunión de despliegue.',
                "ipa_notation": '/ðə tiːm hæz ɡɔn tə ðə dɪˈplɔɪmənt ˈbriːfɪŋ/',
                "order_index": 7,
            },
            {
                "phrase": 'The server is going down for maintenance.',
                "translation": 'El servidor se está apagando para mantenimiento.',
                "ipa_notation": '/ðə ˈsɜːrvər ɪz ˈɡoʊɪŋ daʊn fər ˈmeɪntənəns/',
                "order_index": 8,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Complete the Past Simple form: 'Yesterday, I ______ the implementation tests.'",
                "correct_answer": 'wrote',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence uses the Gerund form of 'go'?",
                "correct_answer": 'The server is going down for maintenance.',
                "options": {
                    "a": 'They go to the office on Mondays.',
                    "b": 'The server is going down for maintenance.',
                    "c": 'We went live with the project last night.',
                    "d": 'The team has gone to the deployment briefing.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Present Perfect vs. Past Simple — Life Experiences',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'The Core Contrast',
                        "layout": 'table',
                        "headers": ['Tense', 'When to use', 'Key signals', 'Example'],
                        "rows": [
                            ['Present Perfect', 'Life experience / result matters now / indefinite time', 'ever, never, already, just, yet, recently', 'I have deployed to AWS before.'],
                            ['Past Simple', 'Specific finished time / historical narrative', 'yesterday, last week, in 2021, at 3 PM, ago', 'I deployed to AWS last Tuesday.'],
                        ],
                    },
                    {
                        "title": 'Structure — Present Perfect',
                        "layout": 'list',
                        "items": [
                            'Affirmative: Subject + have/has + past participle — She has configured the cluster.',
                            "Negative: Subject + haven't/hasn't + past participle — I haven't written the tests yet.",
                            'Question: Have/Has + subject + past participle? — Have you ever worked with GraphQL?',
                            "If you can answer 'when?', use Past Simple. If 'when?' is unknown or irrelevant, use Present Perfect.",
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Compare life experiences at indefinite times with specific completed past actions using Present Perfect and Past Simple.',
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I have deployed applications to three different cloud providers in my career.',
                "translation": 'He desplegado aplicaciones en tres proveedores de nube distintos en mi carrera.',
                "ipa_notation": '/aɪ hæv dɪˈplɔɪd ˌæplɪˈkeɪʃənz tə θriː ˈdɪfrənt klaʊd prəˈvaɪdərz ɪn maɪ kəˈrɪər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She has never configured a Kubernetes cluster from scratch.',
                "translation": 'Ella nunca ha configurado un clúster de Kubernetes desde cero.',
                "ipa_notation": '/ʃiː hæz ˈnɛvər kənˈfɪɡərd ə ˌkuːbərˈnɛtɪz ˈklʌstər frɒm skrætʃ/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Did you push the hotfix to the main branch last night?',
                "translation": '¿Subiste el hotfix a la rama principal anoche?',
                "ipa_notation": '/dɪd juː pʊʃ ðə ˈhɒtfɪks tə ðə meɪn bræntʃ læst naɪt/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Choose the correct tense: 'I ______ the API endpoints last Friday at 4 PM.'",
                "correct_answer": 'integrated',
                "options": {
                    "a": 'have integrated',
                    "b": 'integrated',
                    "c": 'had integrated',
                    "d": 'was integrating',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "______ you ever ______ (work) with a GraphQL API? Use Present Perfect with 'ever'.",
                "correct_answer": 'Have you ever worked',
                "options": None,
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Comparatives and Superlatives — Comparing Things',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Formation Rules',
                        "layout": 'table',
                        "headers": ['Adjective type', 'Comparative', 'Superlative', 'Example'],
                        "rows": [
                            ['Short (1 syllable)', '+ -er', 'the + -est', 'fast → faster / the fastest'],
                            ['Ends in -e', '+ -r', 'the + -st', 'safe → safer / the safest'],
                            ['Short CVC', 'double + -er', 'the + double + -est', 'big → bigger / the biggest'],
                            ['Long (2+ syllables)', 'more + adj', 'the most + adj', 'reliable → more reliable / the most reliable'],
                            ['Ends in -y', 'change y→i + -er', 'the + y→i + -est', 'easy → easier / the easiest'],
                        ],
                    },
                    {
                        "title": 'Irregular Forms & Connectors',
                        "layout": 'table',
                        "headers": ['Adjective', 'Comparative', 'Superlative'],
                        "rows": [
                            ['good', 'better', 'the best'],
                            ['bad', 'worse', 'the worst'],
                            ['far', 'further / farther', 'the furthest / farthest'],
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": 'Learn to compare codebase efficiency, system speeds, and language popularity using Comparatives and Superlatives.',
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Python is easier to read than Java for beginners.',
                "translation": 'Python es más fácil de leer que Java para principiantes.',
                "ipa_notation": '/ˈpaɪθən ɪz ˈiːziər tə riːd ðæn ˈdʒɑːvə fɔːr bɪˈɡɪnərz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'TypeScript is not harder to learn than assembly language.',
                "translation": 'TypeScript no es más difícil de aprender que el lenguaje ensamblador.',
                "ipa_notation": '/ˈtaɪpskrɪpt ɪz nɒt ˈhɑːrdər tə lɜːrn ðæn əˈsɛmbli ˈlæŋɡwɪdʒ/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Which programming language is the most popular in the current job market?',
                "translation": '¿Cuál es el lenguaje de programación más popular en el mercado laboral actual?',
                "ipa_notation": '/wɪtʃ ˈproʊɡræmɪŋ ˈlæŋɡwɪdʒ ɪz ðə moʊst ˈpɒpjʊlər ɪn ðə ˈkɜːrənt dʒɒb ˈmɑːrkɪt/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence uses the SUPERLATIVE form correctly?',
                "correct_answer": 'PostgreSQL is the most reliable database we have tested.',
                "options": {
                    "a": 'PostgreSQL is more reliable database.',
                    "b": 'PostgreSQL is the most reliable database we have tested.',
                    "c": 'PostgreSQL is reliablest database.',
                    "d": 'PostgreSQL is most reliable.',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'Our new codebase is ______ (good) than the legacy system. Use the correct irregular comparative.',
                "correct_answer": 'better',
                "options": None,
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Modal Verbs: Must, Have to & Should — Obligation & Advice',
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.MODAL_VERBS,
            "description": 'Master obligation, prohibition, advice, and optional requirements using Must, Have to, and Should in engineering teams.',
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'You must authenticate every API request with a valid token.',
                "translation": 'Debes autenticar cada solicitud de API con un token válido.',
                "ipa_notation": '/juː mʌst ɔːˈθɛntɪkeɪt ˈɛvri ˌeɪpiːˈaɪ rɪˈkwɛst wɪð ə ˈvælɪd ˈtoʊkən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'You must not store plain-text passwords in the database.',
                "translation": 'No debes almacenar contraseñas en texto plano en la base de datos.',
                "ipa_notation": '/juː mʌst nɒt stɔːr pleɪn tɛkst ˈpæswɜːrdz ɪn ðə ˈdeɪtəbeɪs/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'You should write unit tests before merging any new feature.',
                "translation": 'Deberías escribir pruebas unitarias antes de hacer merge de cualquier nueva funcionalidad.',
                "ipa_notation": '/juː ʃʊd raɪt ˈjuːnɪt tɛsts bɪˈfɔːr ˈmɜːrdʒɪŋ ˈɛni njuː ˈfiːtʃər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": 'Junior developers do not have to review architecture decisions alone.',
                "translation": 'Los desarrolladores junior no tienen que revisar las decisiones de arquitectura solos.',
                "ipa_notation": '/ˈdʒuːniər ˌdɛvəˈlɒpərz duː nɒt hæv tə rɪˈvjuː ˈɑːrkɪtɛktʃər dɪˈsɪʒənz əˈloʊn/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence expresses a PROHIBITION?',
                "correct_answer": 'You must not push directly to the main branch.',
                "options": {
                    "a": 'You should review the documentation.',
                    "b": 'You must not push directly to the main branch.',
                    "c": "You don't have to attend the daily standup.",
                    "d": 'You have to update your dependencies.',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'It is just a suggestion — you ______ try the new linting rules, but it is your choice.',
                "correct_answer": 'should',
                "options": {
                    "a": 'must',
                    "b": 'have to',
                    "c": 'should',
                    "d": 'must not',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'First Conditional — Real Future Possibilities',
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.CONDITIONALS,
            "description": 'Learn to express real future possibilities, conditional triggers, and system reactions using the First Conditional.',
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'If you run the migration script, the database schema will update automatically.',
                "translation": 'Si ejecutas el script de migración, el esquema de la base de datos se actualizará automáticamente.',
                "ipa_notation": '/ɪf juː rʌn ðə maɪˈɡreɪʃən skrɪpt, ðə ˈdeɪtəbeɪs ˈskiːmə wɪl ˈʌpdeɪt ˌɔːtəˈmætɪkli/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'If the tests fail, the pipeline will not deploy the new release.',
                "translation": 'Si las pruebas fallan, el pipeline no desplegará la nueva versión.',
                "ipa_notation": '/ɪf ðə tɛsts feɪl, ðə ˈpaɪplaɪn wɪl nɒt dɪˈplɔɪ ðə njuː rɪˈliːs/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Will the server crash if we increase the number of concurrent connections?',
                "translation": '¿Se caerá el servidor si aumentamos el número de conexiones simultáneas?',
                "ipa_notation": '/wɪl ðə ˈsɜːrvər kræʃ ɪf wiː ɪnˈkriːs ðə ˈnʌmbər əv kənˈkʌrənt kəˈnɛkʃənz/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'If we refactor the module, the performance ______ (improve) significantly. (First Conditional)',
                "correct_answer": 'will improve',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence is a correct First Conditional?',
                "correct_answer": 'If you cache the response, the API will be faster.',
                "options": {
                    "a": 'If you will cache the response, the API is faster.',
                    "b": 'If you cache the response, the API will be faster.',
                    "c": 'If you cached the response, the API would be faster.',
                    "d": 'If you cache the response, the API would be faster.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Used to — Past Habits and States',
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": "Describe past developer routines, legacy workflows, and habits that are no longer true using 'used to'.",
            "order_index": 10,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'We used to deploy our apps manually before adopting a CI/CD pipeline.',
                "translation": 'Solíamos desplegar nuestras aplicaciones manualmente antes de adoptar un pipeline CI/CD.',
                "ipa_notation": '/wiː juːst tə dɪˈplɔɪ aʊər æps ˈmænjʊəli bɪˈfɔːr əˈdɒptɪŋ ə siː aɪ siː diː ˈpaɪplaɪn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I did not use to write unit tests until I joined an agile team.',
                "translation": 'No solía escribir pruebas unitarias hasta que me uní a un equipo ágil.',
                "ipa_notation": '/aɪ dɪd nɒt juːz tə raɪt ˈjuːnɪt tɛsts ʌntɪl aɪ dʒɔɪnd ən ˈædʒaɪl tiːm/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Did your team use to work with a monolithic architecture?',
                "translation": '¿Tu equipo solía trabajar con una arquitectura monolítica?',
                "ipa_notation": '/dɪd jɔːr tiːm juːz tə wɜːrk wɪð ə ˌmɒnəˈlɪθɪk ˈɑːrkɪtɛktʃər/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence correctly uses 'used to'?",
                "correct_answer": 'He used to manage servers manually before the cloud era.',
                "options": {
                    "a": 'He use to manage servers.',
                    "b": 'He used to managed servers manually.',
                    "c": 'He used to manage servers manually before the cloud era.',
                    "d": 'He is used to manage servers.',
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'Before Docker, teams ______ (use to) configure environments by hand.',
                "correct_answer": 'used to',
                "options": None,
                "order_index": 2,
            },
        ],
    },
]
