# a1_grammar.py — Pristine plain-text JSON seed data
# Cleaned programmatically to comply with strict Separation of Concerns.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A1_GRAMMAR_LESSONS: list[dict] = [
    {
        "level_code": 'A1',
        "meta": {
            "title": "Verb 'To Be' — States & Descriptions",
            "explanation": {
                "intro": 'Master the verb **to be** to express identities, descriptions, and states in technical contexts.',
                "sections": [
                    {
                        "title": 'Present Tense Forms',
                        "layout": 'table',
                        "headers": ['Subject', 'Form', 'Contraction', 'Example'],
                        "rows": [
                            ['**I**', '`am`', '`I\'m`', '**I** `am` a developer.'],
                            ['**You**', '`are`', '`You\'re`', '**You** `are` the tech lead.'],
                            ['**He / She / It**', '`is`', '`He\'s` / `She\'s`', '**She** `is` the architect.'],
                            ['**We / They**', '`are`', '`We\'re` / `They\'re`', '**They** `are` on call.'],
                        ],
                    },
                    {
                        "title": 'Past Tense Forms',
                        "layout": 'table',
                        "headers": ['Subject', 'Form', 'Example'],
                        "rows": [
                            ['**I / He / She / It**', '`was`', 'The server `was` down.'],
                            ['**You / We / They**', '`were`', 'The tests `were` passing.'],
                        ],
                    },
                    {
                        "title": 'Sentence Construction & Tips',
                        "layout": 'cards',
                        "items": [
                            "**Negative Structure** | **Subject** + **am / is / are** + **not** | Add `not` after the verb to be → **I** `am not` available.",
                            "**Question Structure** | **Am / Is / Are** + **subject**? | Invert the subject and the verb to be → `Is` **the API** live?",
                            "**Contraction Tip** | Contractions are highly preferred in tech teams: **isn't**, **aren't**, **wasn't**."
                        ],
                    },
                ],
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": "Master the verb 'to be' to express identities, descriptions, and states in technical contexts.",
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I am a full-stack developer.',
                "translation": 'Soy un desarrollador full-stack.',
                "ipa_notation": '/aɪ æm ə ˈfʊl stæk dɪˈvɛləpər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She is not the system administrator.',
                "translation": 'Ella no es la administradora del sistema.',
                "ipa_notation": '/ʃiː ɪz nɒt ðə ˈsɪstəm ədˈmɪnɪtreɪtər/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Are you available for the code review?',
                "translation": '¿Estás disponible para la revisión de código?',
                "ipa_notation": '/ɑːr juː əˈveɪləbl fər ðə koʊd rɪˈvjuː/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
            {
                "phrase": 'The API was down for two hours yesterday.',
                "translation": 'La API estuvo caída dos horas ayer.',
                "ipa_notation": '/ðiː ˌeɪpiːˈaɪ wɒz daʊn fər tuː ˈaʊərz ˈjɛstərdeɪ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
            {
                "phrase": 'The test results were not accurate.',
                "translation": 'Los resultados de las pruebas no eran precisos.',
                "ipa_notation": '/ðə tɛst rɪˈzʌlts wɜːr nɒt ˈækjərɪt/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 5,
            },
            {
                "phrase": 'Was the deployment successful last night?',
                "translation": '¿Fue exitoso el despliegue anoche?',
                "ipa_notation": '/wɒz ðə dɪˈplɔɪmənt səkˈsɛsfəl læst naɪt/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 6,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'The server ______ unavailable for 30 minutes last night. (was/were)',
                "correct_answer": 'was',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence is grammatically correct?',
                "correct_answer": 'The developers are tired.',
                "options": {
                    "a": 'The developers is tired.',
                    "b": 'The developers are tired.',
                    "c": 'The developers am tired.',
                    "d": 'The developers be tired.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Present Simple — Habits & Routines',
            "explanation": {
                "intro": 'Learn the **Present Simple** to describe software habits, routines, general truths, and basic processes in technical settings.',
                "sections": [
                    {
                        "title": 'Sentence Construction',
                        "subsections": [
                            {
                                "title": 'Affirmative Rules',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative (I/You/We/They) | **Subject** + **base verb** | `I` **write** unit tests daily.",
                                    "Affirmative (He/She/It) | **Subject** + **verb + -(e)s** | `She` **deploys** every Friday."
                                ]
                            },
                            {
                                "title": 'Negative Rules',
                                "layout": 'cards',
                                "items": [
                                    "Negative (I/You/We/They) | **Subject** + **don't** + **base verb** | `They` **don't have** credentials.",
                                    "Negative (He/She/It) | **Subject** + **doesn't** + **base verb** | `He` **doesn't use** legacy libraries."
                                ]
                            },
                            {
                                "title": 'Question Rules',
                                "layout": 'cards',
                                "items": [
                                    "Question (I/You/We/They) | **Do** + **subject** + **base verb**? | `Do` **you test** your endpoints?",
                                    "Question (He/She/It) | **Does** + **subject** + **base verb**? | `Does` **the server run** locally?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'Spelling Rules for He / She / It',
                        "layout": 'table',
                        "headers": ['Ending Rule', 'Base Verb', 'Verb + -(e)s', 'Technical Example'],
                        "rows": [
                            ['Most verbs: add **-s**', '`run` / `write`', '`runs` / `writes`', 'The background service `runs` hourly.'],
                            ['Ends in **-ch, -sh, -x, -ss, -o**: add **-es**', '`fix` / `push` / `go`', '`fixes` / `pushes` / `goes`', 'She `fixes` the memory leak.'],
                            ['Ends in **consonant + -y**: change -y to **-ies**', '`try` / `modify`', '`tries` / `modifies`', 'He `modifies` the table schema.']
                        ]
                    },
                    {
                        "title": 'Frequency & Routines',
                        "subsections": [
                            {
                                "title": 'Key Time Markers',
                                "layout": 'table',
                                "headers": ['Marker', 'Frequency', 'Technical Example'],
                                "rows": [
                                    ['`always` / `usually` / `often`', 'High frequency', 'We `always` run unit tests before a merge.'],
                                    ['`sometimes` / `rarely` / `never`', 'Low frequency', 'The server `rarely` crashes under normal load.'],
                                    ['`every day / week / sprint`', 'Regular scheduled routines', 'She reviews pull requests `every morning`.']
                                ]
                            }
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Learn the Present Simple to describe software habits, routines, general truths, and basic processes.',
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I write clean code every day.',
                "translation": 'Escribo código limpio todos los días.',
                "ipa_notation": '/aɪ raɪt kliːn koʊd ˈɛvri deɪ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'He does not use legacy libraries.',
                "translation": 'Él no usa librerías obsoletas.',
                "ipa_notation": '/hiː dʌz nɒt juːz ˈlɛɡəsi ˈlaɪbrəriz/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Do you test your endpoints?',
                "translation": '¿Pruebas tus endpoints?',
                "ipa_notation": '/duː juː tɛst jɔːr ˈɛndpɔɪnts/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'She ______ (deploy) the app every Friday. (Present Simple)',
                "correct_answer": 'deploys',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence uses Present Simple correctly?',
                "correct_answer": 'He reviews the pull request every morning.',
                "options": {
                    "a": 'He is reviewing now.',
                    "b": 'He reviewed yesterday.',
                    "c": 'He reviews the pull request every morning.',
                    "d": 'He will review tomorrow.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Present Continuous — Actions Happening Right Now',
            "explanation": {
                "intro": 'Use the **Present Continuous** to express ongoing operations, server deployments, and active events happening in real-time.',
                "sections": [
                    {
                        "title": 'Real-Time Structures',
                        "subsections": [
                            {
                                "title": 'Affirmative & Negative',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative | **Subject** + **am / is / are** + **verb-ing** | `We` **are deploying** the application now.",
                                    "Negative | **Subject** + **am / is / are** + **not** + **verb-ing** | `The server` **is not responding** to requests."
                                ]
                            },
                            {
                                "title": 'Questions',
                                "layout": 'cards',
                                "items": [
                                    "Question | **Am / Is / Are** + **subject** + **verb-ing**? | `Are` **they auditing** the repository?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'Spelling Rules for -ing Forms',
                        "layout": 'table',
                        "headers": ['Spelling Rule', 'Base Verb', '-ing Form', 'Technical Example'],
                        "rows": [
                            ['Most verbs: add **-ing**', '`deploy` / `test`', '`deploying` / `testing`', 'We are `deploying` the changes.'],
                            ['Ends in silent **-e**: drop the **-e**, add **-ing**', '`write` / `configure`', '`writing` / `configuring`', 'He is `writing` a shell script.'],
                            ['Short verbs ending in **CVC**: double final letter', '`run` / `stop`', '`running` / `stopping`', 'Docker is `running` in the background.']
                        ]
                    },
                    {
                        "title": 'Stative Verbs (Actions vs. States)',
                        "subsections": [
                            {
                                "title": 'Verbs that NEVER use -ing',
                                "layout": 'list',
                                "items": [
                                    "✗ The database **is containing** errors. (Incorrect)",
                                    "✓ The database **contains** errors. (Correct: *contain* is a state, not an action)",
                                    "✗ I **am knowing** the API token. (Incorrect)",
                                    "✓ I **know** the API token. (Correct: *know* is state/knowledge)"
                                ]
                            }
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": 'Express ongoing operations, server deployments, and live events in progress using Present Continuous.',
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'We are deploying the application now.',
                "translation": 'Estamos desplegando la aplicación ahora.',
                "ipa_notation": '/wiː ɑːr dɪˈplɔɪɪŋ ðə ˌæplɪˈkeɪʃən naʊ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The server is not responding to requests.',
                "translation": 'El servidor no está respondiendo a las solicitudes.',
                "ipa_notation": '/ðə ˈsɜːrvər ɪz nɒt rɪˈspɒndɪŋ tə rɪˈkwɛsts/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Are they auditing the repository?',
                "translation": '¿Están auditando el repositorio?',
                "ipa_notation": '/ɑːr ðeɪ ˈɔːdɪtɪŋ ðə rɪˈpɒzɪtɔːri/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'The team ______ (fix) the memory leak right now. (Present Continuous)',
                "correct_answer": 'is fixing',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence is in Present Continuous?',
                "correct_answer": 'She is refactoring the module.',
                "options": {
                    "a": 'She refactors daily.',
                    "b": 'She is refactoring the module.',
                    "c": 'She refactored yesterday.',
                    "d": 'She will refactor it.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Have Got — Possession & Characteristics',
            "explanation": {
                "intro": "Express possession, system specifications, and access credentials using the everyday **have got** structure, commonly used in tech teams.",
                "sections": [
                    {
                        "title": 'Possession Structures',
                        "subsections": [
                            {
                                "title": 'Affirmative Structures',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative (I/You/We/They) | **Subject** + **have got** | `I` **have got** a new laptop for remote work.",
                                    "Affirmative (He/She/It) | **Subject** + **has got** | `The laptop` **has got** 16GB of RAM."
                                ]
                            },
                            {
                                "title": 'Negative Structures',
                                "layout": 'cards',
                                "items": [
                                    "Negative (I/You/We/They) | **Subject** + **haven't got** | `We` **haven't got** access to the staging DB.",
                                    "Negative (He/She/It) | **Subject** + **hasn't got** | `She` **hasn't got** permission to merge yet."
                                ]
                            },
                            {
                                "title": 'Question Structures',
                                "layout": 'cards',
                                "items": [
                                    "Question (I/You/We/They) | **Have** + **subject** + **got**? | `Have` **you got** the new API credentials?",
                                    "Question (He/She/It) | **Has** + **subject** + **got**? | `Has` **he got** the SSH key?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'have got (UK) vs. have (US)',
                        "layout": 'table',
                        "headers": ['Sentence Type', "have got (British Style)", "have (American Style)"],
                        "rows": [
                            ['Affirmative', '`I have got` / `I\'ve got` a bug.', '`I have` a bug.'],
                            ['Negative', '`I haven\'t got` credentials.', '`I don\'t have` credentials.'],
                            ['Question', '`Have you got` the token?', '`Do you have` the token?']
                        ]
                    },
                    {
                        "title": 'Crucial Grammar Rules',
                        "layout": 'list',
                        "items": [
                            "**No Auxiliary Do/Does**: With 'have got', never use do/does in questions or negatives (e.g. NOT *Do you have got?*).",
                            "**Contractions are Preferred**: In speech and slack channels, contractions are highly preferred: `I've got`, `he's got`, `we've got`.",
                            "**Past Tense Exception**: 'Have got' has no past tense form. For past possession, use **had** → *I had a slow laptop last year.*"
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": "Express possession, system specifications, and access credentials using the everyday 'have got' structure.",
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I have got a new laptop for remote work.',
                "translation": 'Tengo una laptop nueva para trabajar en remoto.',
                "ipa_notation": '/aɪ hæv ɡɒt ə njuː ˈlæptɒp fər rɪˈmoʊt wɜːrk/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She has not got permission to access that repository.',
                "translation": 'Ella no tiene permiso para acceder a ese repositorio.',
                "ipa_notation": '/ʃiː hæz nɒt ɡɒt pərˈmɪʃən tə ˈækses ðæt rɪˈpɒzɪtɔːri/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Have you got the API credentials for the staging environment?',
                "translation": '¿Tienes las credenciales de la API para el entorno de staging?',
                "ipa_notation": '/hæv juː ɡɒt ðiː ˌeɪpiːˈaɪ krɪˈdɛnʃəlz fər ðə ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'He ______ a valid SSH key to access the remote server. (has/have got)',
                "correct_answer": 'has got',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which question form is correct with 'have got'?",
                "correct_answer": 'Have you got two-factor authentication enabled?',
                "options": {
                    "a": 'Do you have got 2FA?',
                    "b": 'Have you got two-factor authentication enabled?',
                    "c": 'You have got 2FA?',
                    "d": 'Has you got 2FA?',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'There Is / There Are — Existence & Places',
            "explanation": {
                "intro": 'Describe the presence, absence, or existence of database files, servers, bugs, or pull requests in your system using **there is** and **there are**.',
                "sections": [
                    {
                        "title": 'Existence Rules',
                        "subsections": [
                            {
                                "title": 'Singular & Plural Forms',
                                "layout": 'cards',
                                "items": [
                                    "Singular (There is) | **There is** + **singular noun** | `There is` **a critical bug** in the auth module.",
                                    "Plural (There are) | **There are** + **plural noun** | `There are` **three open issues** in Jira."
                                ]
                            },
                            {
                                "title": 'Negatives & Questions',
                                "layout": 'cards',
                                "items": [
                                    "Negative Singular | **There is no** / **There isn't a** | `There is` **no backup** of the staging database.",
                                    "Negative Plural | **There are no** / **There aren't any** | `There are` **no failing tests** in the pipeline.",
                                    "Questions | **Is there** (Sing.) / **Are there** (Plur.)? | `Is there` **a database migration** pending?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'Expressing Existence Across Tenses',
                        "layout": 'table',
                        "headers": ['Tense', 'Singular Form', 'Plural Form', 'Technical Example'],
                        "rows": [
                            ['Present Simple', '`There is`', '`There are`', '`There is` a memory leak / `There are` active logs.'],
                            ['Past Simple', '`There was`', '`There were`', '`There was` a crash yesterday / `There were` multiple warnings.'],
                            ['Future (Will)', '`There will be`', '`There will be`', '`There will be` a release next week (same for plurals).'],
                            ['Present Perfect', '`There has been`', '`There have been`', '`There has been` a security breach / `There have been` latency spikes.']
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": 'Describe the existence, presence, or absence of database files, servers, and bugs in your architecture.',
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'There is a critical bug in the authentication module.',
                "translation": 'Hay un error crítico en el módulo de autenticación.',
                "ipa_notation": '/ðer ɪz ə ˈkrɪtɪkəl bʌɡ ɪn ðiː ɔːˌθɛntɪˈkeɪʃən ˈmɒdjuːl/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'There are no failing tests in the pipeline.',
                "translation": 'No hay pruebas fallidas en el pipeline.',
                "ipa_notation": '/ðer ɑːr noʊ ˈfeɪlɪŋ tɛsts ɪn ðə ˈpaɪplaɪn/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Is there a backup of the production database?',
                "translation": '¿Hay una copia de seguridad de la base de datos de producción?',
                "ipa_notation": '/ɪz ðer ə ˈbækʌp əv ðə prəˈdʌkʃən ˈdeɪtəbeɪs/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": '______ three new pull requests waiting for your review.',
                "correct_answer": 'There are',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence is grammatically correct?',
                "correct_answer": 'There are two open issues.',
                "options": {
                    "a": 'There is two open issues.',
                    "b": 'There are two open issues.',
                    "c": 'There have two open issues.',
                    "d": 'There be two open issues.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": "Modal Verb 'Can' — Ability & Permission",
            "explanation": {
                "intro": 'Learn to express system capacities, developer permissions, and technical constraints using the modal verb **can**.',
                "sections": [
                    {
                        "title": 'Usage & Conjugation',
                        "subsections": [
                            {
                                "title": 'Affirmative & Negative Ability',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative | **Subject** + **can** + **bare verb** | `I` **can run** the Docker container locally.",
                                    "Negative | **Subject** + **cannot (can't)** + **bare verb** | `She` **cannot push** directly to the main branch."
                                ]
                            },
                            {
                                "title": 'Asking for Permission or Assistance',
                                "layout": 'cards',
                                "items": [
                                    "Permission Question | **Can** + **subject** + **bare verb**? | `Can` **I access** the logs?",
                                    "Polite Request | **Could** + **subject** + **bare verb**? | `Could` **you review** my pull request?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'Key Properties of Modals',
                        "layout": 'list',
                        "items": [
                            "**No Third-Person '-s'**: 'Can' never changes its form. E.g., *She can code* (NOT *She cans code*).",
                            "**Followed by Bare Infinitive**: Always use the base verb without 'to' after 'can'. E.g., *I can deploy* (NOT *I can to deploy*).",
                            "**No Auxiliary Do/Does**: Questions and negatives do not use do/does/did. E.g., *Can you help?* (NOT *Do you can help?*)"
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.MODAL_VERBS,
            "description": 'Learn to express logical ability, permission, and system possibilities using the modal verb Can.',
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I can run the Docker container locally.',
                "translation": 'Puedo ejecutar el contenedor Docker localmente.',
                "ipa_notation": '/aɪ kæn rʌn ðə ˈdɒkər kənˈteɪnər ˈloʊkəli/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She cannot push directly to the main branch.',
                "translation": 'Ella no puede hacer push directamente a la rama principal.',
                "ipa_notation": '/ʃiː ˈkænɒt pʊʃ dɪˈrɛktli tə ðə meɪn bræntʃ/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Can you explain the difference between GET and POST?',
                "translation": '¿Puedes explicar la diferencia entre GET y POST?',
                "ipa_notation": '/kæn juː ɪkˈspleɪn ðə ˈdɪfrəns bɪˈtwiːn ɡɛt ænd poʊst/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": '______ you configure the environment variables for the new service? (Can)',
                "correct_answer": 'Can',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence correctly expresses inability?',
                "correct_answer": 'She cannot access the logs.',
                "options": {
                    "a": "She can't accessing the logs.",
                    "b": 'She not can access the logs.',
                    "c": 'She cannot access the logs.',
                    "d": 'She cans not access the logs.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": "Future with 'Going To' — Plans & Intentions",
            "explanation": {
                "intro": 'Plan your project sprints, releases, and upcoming technical upgrades using the **going to** future structure.',
                "sections": [
                    {
                        "title": 'Planning Structures',
                        "subsections": [
                            {
                                "title": 'Affirmative Plans',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative | **Subject** + **be (am/is/are)** + **going to** + **verb** | `I` **am going to clone** the repo and set up.",
                                    "Negative | **Subject** + **be** + **not** + **going to** + **verb** | `We` **are not going to release** on Friday."
                                ]
                            },
                            {
                                "title": 'Questions about Intentions',
                                "layout": 'cards',
                                "items": [
                                    "Question | **Be (Am/Is/Are)** + **subject** + **going to** + **verb**? | `Are` **you going to attend** the retrospective?"
                                ]
                            }
                        ]
                    },
                    {
                        "title": "'Going To' vs. 'Will'",
                        "layout": 'table',
                        "headers": ['Feature', "Going To (Intentions & Plans)", "Will (Decisions & Promises)"],
                        "rows": [
                            ['Core Use', 'Pre-planned intention / plans made before speaking.', 'Spontaneous decision / promise / quick action.'],
                            ['Tech Example', '`We are going to refactor` this class next sprint.', '`I will fix` that typo right now.'],
                            ['Evidence', 'Based on present signs (e.g. server load is at 99%).', 'Based on personal opinion or hope.'],
                            ['Tech Example', 'The server `is going to crash`! Look at the load.', 'I think our app `will be` popular.']
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": "Plan your project sprints, releases, and upcoming technical upgrades using Future with 'going to'.",
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I am going to clone the repository and set up the environment.',
                "translation": 'Voy a clonar el repositorio y configurar el entorno.',
                "ipa_notation": '/aɪ æm ˈɡoʊɪŋ tə kloʊn ðə rɪˈpɒzɪtɔːri ænd sɛt ʌp ðiː ɪnˈvaɪrənmənt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'We are not going to release the feature on Friday.',
                "translation": 'No vamos a lanzar la funcionalidad el viernes.',
                "ipa_notation": '/wiː ɑːr nɒt ˈɡoʊɪŋ tə rɪˈliːs ðə ˈfiːtʃər ɒn ˈfraɪdeɪ/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Are you going to attend the sprint planning tomorrow?',
                "translation": '¿Vas a asistir a la planificación del sprint mañana?',
                "ipa_notation": '/ɑːr juː ˈɡoʊɪŋ tə əˈtɛnd ðə sprɪnt ˈplænɪŋ təˈmɒroʊ/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'We ______ (be going to) refactor the legacy module in the next sprint.',
                "correct_answer": 'are going to',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Choose the grammatically correct future sentence:',
                "correct_answer": 'I am going to update the dependencies.',
                "options": {
                    "a": 'I going to update the dependencies.',
                    "b": 'I am going to update the dependencies.',
                    "c": 'I go to update the dependencies.',
                    "d": 'I be going to update the dependencies.',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Wh- Questions — Asking for Information',
            "explanation": {
                "intro": 'Learn how to ask clear, specific questions about bugs, users, routes, and software systems using **Wh- words**.',
                "sections": [
                    {
                        "title": 'Question Word Directory',
                        "layout": 'table',
                        "headers": ['Question Word', 'Focus of Query', 'Technical Example'],
                        "rows": [
                            ['`What`', 'Information / Thing', '`What` does this endpoint return?'],
                            ['`Who`', 'Person / Agent', '`Who` merged this pull request?'],
                            ['`Where`', 'Place / Location', '`Where` are the error logs stored?'],
                            ['`When`', 'Time / Schedule', '`When` did the background job fail?'],
                            ['`Why`', 'Reason / Purpose', '`Why` is this test suite skipped?'],
                            ['`How`', 'Method / Process', '`How` does the cache invalidate?'],
                            ['`Which`', 'Choice between options', '`Which` Docker image should we use?']
                        ]
                    },
                    {
                        "title": 'Word Order Formula',
                        "subsections": [
                            {
                                "title": 'Standard Question Structure',
                                "layout": 'cards',
                                "items": [
                                    "Standard Wh- Question | **Wh- word** + **auxiliary (do/does/did/is/are)** + **subject** + **verb**? | `Where` **do we define** the port?"
                                ]
                            },
                            {
                                "title": 'Subject Question Structure',
                                "layout": 'cards',
                                "items": [
                                    "Subject Wh- Question | **Wh- word (as subject)** + **verb**? | `Who` **wrote** this spaghetti code? (no auxiliary needed!)"
                                ]
                            }
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": 'Learn how to ask specific questions about bugs, users, routes, and software systems using Wh- words.',
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Who is responsible for the deployment pipeline?',
                "translation": '¿Quién es responsable del pipeline de despliegue?',
                "ipa_notation": '/huː ɪz rɪˈspɒnsɪbl fər ðə dɪˈplɔɪmənt ˈpaɪplaɪn/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'What does this function return when the list is empty?',
                "translation": '¿Qué devuelve esta función cuando la lista está vacía?',
                "ipa_notation": '/wɒt dʌz ðɪs ˈfʌŋkʃən rɪˈtɜːrn wɛn ðə lɪst ɪz ˈɛmpti/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Where are the environment configuration files stored?',
                "translation": '¿Dónde se almacenan los archivos de configuración de entorno?',
                "ipa_notation": '/wer ɑːr ðiː ɪnˈvaɪrənmənt ˌkɒnfɪɡjʊˈreɪʃən faɪlz stɔːrd/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": '______ is the team lead for this microservice? (Who/What/Where)',
                "correct_answer": 'Who',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which question word asks about a PLACE?',
                "correct_answer": 'Where is the bug?',
                "options": {
                    "a": 'Who wrote this code?',
                    "b": 'What is the error?',
                    "c": 'Where is the bug?',
                    "d": 'When did it fail?',
                },
                "order_index": 2,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Imperatives, Articles & Demonstratives',
            "explanation": {
                "intro": 'Master developer commands (imperatives), singular/plural articles (a, an, the), and pointers (this, that, these, those) used in the codebase.',
                "sections": [
                    {
                        "title": 'Developer Commands (Imperatives)',
                        "subsections": [
                            {
                                "title": 'Giving Instructions',
                                "layout": 'cards',
                                "items": [
                                    "Affirmative Command | **Bare verb** (no subject) | `Open` **the terminal** and run the script.",
                                    "Negative Command | **Don't** + **bare verb** | `Don't` **force-push** to the main branch!"
                                ]
                            }
                        ]
                    },
                    {
                        "title": 'Articles: A, An vs. The',
                        "layout": 'table',
                        "headers": ['Article Type', 'Rule & Usage', 'Technical Example'],
                        "rows": [
                            ['Indefinite (**A**)', 'Before consonant sounds; refers to any non-specific item.', 'Please open `a` file.'],
                            ['Indefinite (**An**)', 'Before vowel sounds; refers to any non-specific item.', 'We need to create `an` issue.'],
                            ['Definite (**The**)', 'Refers to a specific, unique, or previously mentioned item.', 'Open `the` file we modified yesterday.']
                        ]
                    },
                    {
                        "title": 'Pointers (Demonstratives)',
                        "layout": 'table',
                        "headers": ['Pointer', 'Distance & Quantity', 'Technical Example'],
                        "rows": [
                            ['`This`', 'Singular & Near (here)', '`This` is the main branch.'],
                            ['`That`', 'Singular & Far (there)', '`That` is the server IP.'],
                            ['`These`', 'Plural & Near (here)', '`These` are my local commits.'],
                            ['`Those`', 'Plural & Far (there)', '`Those` are the staging logs.']
                        ]
                    }
                ]
            },
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": "Master developer commands, singular/plural articles, and pointers like 'this' or 'that' in your codebase.",
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Open the terminal and run the seed script.',
                "translation": 'Abre la terminal y ejecuta el script de seed.',
                "ipa_notation": '/ˈoʊpən ðə ˈtɜːrmɪnəl ænd rʌn ðə siːd skrɪpt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Create an issue before you open a pull request.',
                "translation": 'Crea un issue antes de abrir un pull request.',
                "ipa_notation": '/kriˈeɪt ən ˈɪʃuː bɪˈfɔːr juː ˈoʊpən ə pʊl rɪˈkwɛst/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'This is the main branch; that is a feature branch.',
                "translation": 'Esta es la rama principal; esa es una rama de funcionalidad.',
                "ipa_notation": '/ðɪs ɪz ðə meɪn bræntʃ ðæt ɪz ə ˈfiːtʃər bræntʃ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "______ the README file before starting the project. (imperative of 'read')",
                "correct_answer": 'Read',
                "options": None,
                "order_index": 1,
            },
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which sentence uses articles correctly?',
                "correct_answer": 'Open a file and check the output.',
                "options": {
                    "a": 'Open an file and check a output.',
                    "b": 'Open a file and check the output.',
                    "c": 'Open the file and check an output.',
                    "d": 'Open file and check output.',
                },
                "order_index": 2,
            },
        ],
    },
]
