# c2_vocabulary.py — Mastery Vocabulary Lessons

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C2_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'C2',
        "meta": {
            "title": 'Semantic Precision — Mastering Nuances',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Discriminate similar words and master subtle semantic differences (elicit/illicit, appraise/apprise).',
            "explanation": {
                "intro": 'C2 mastery requires absolute precision, ensuring you choose the exact word that fits a specific semantic nuance.',
                "sections": [
                    {
                        "title": 'Semantic Nuances',
                        "subsections": [
                            {
                                "title": 'Easily Confused Nuanced Words',
                                "layout": 'table',
                                "headers": ['Nuanced Word Pair', 'Pronunciations', 'Precise Professional Differences (Spanish)'],
                                "rows": [
                                    ['**Elicit / Illicit**', '`/iˈlɪs.ɪt/` / `/ɪˈlɪs.ɪt/`', '**Elicit** (V): Evocar/provocar una respuesta | **Illicit** (Adj): Ilegal/no permitido.'],
                                    ['**Appraise / Apprise**', '`/əˈpreɪz/` / `/əˈpraɪz/`', '**Appraise** (V): Evaluar el valor/calidad | **Apprise** (V): Informar o notificar a alguien.'],
                                    ['**Alternate / Alternative**', '`/ˈɒl.tə.neɪt/` / `/ɒlˈtɜː.nə.tɪv/`', '**Alternate** (Adj): Alterno (uno sí, uno no) | **Alternative** (Adj/N): Alternativa (otra opción).'],
                                    ['**Complement / Compliment**', '`/ˈkɒm.plɪ.mənt/` / `/ˈkɒm.plɪ.mənt/`', '**Complement** (V/N): Complementar (hacer completo) | **Compliment** (V/N): Halagar (dar elogio).'],
                                    ['**Affect / Effect**', '`/əˈfɛkt/` / `/ɪˈfɛkt/`', '**Affect** (V): Afectar (influenciar) | **Effect** (N): Efecto (el resultado de un cambio).']
                                ]
                            },
                            {
                                "title": 'Nuance In Action',
                                "layout": 'list',
                                "items": [
                                    "Use **apprise** to notify: '*Please apprise me of any changes to the deployment schedule.*'",
                                    "Use **elicit** to obtain reactions: '*The manager tried to elicit honest feedback from the developers.*'",
                                    "Select the best **alternative**: '*We need a cost-effective alternative to cloud hosting.*'"
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 50,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'The survey was designed to elicit constructive feedback from the developers.',
                "translation": 'La encuesta fue diseñada para obtener comentarios constructivos de los desarrolladores.',
                "ipa_notation": '/ðə ˈsɜːrveɪ wɒz dɪˈzaɪnd tuː ɪˈlɪsɪt kənˈstrʌktɪv ˈfiːdbæk frɒm ðə dɪˈvɛləpərz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I will apprise the board of directors of our technical progress.',
                "translation": 'Informaré a la junta de directores sobre nuestro progreso técnico.',
                "ipa_notation": '/aɪ wɪl əˈpraɪz ðə bɔːrd ɒv dɪˈrɛktərz ɒv ˈaʊər ˈtɛknɪkəl ˈproʊɡrɛs/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which verb means 'to inform or notify someone about something'?",
                "correct_answer": "apprise",
                "options": {
                    "a": "appraise",
                    "b": "apprise",
                    "c": "elicit",
                    "d": "affect"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'C2',
        "meta": {
            "title": 'Specialist Jargon — Engineering, Finance & Law',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master specialist jargon tables detailing computer engineering systems, capital markets, and contract law.',
            "explanation": {
                "intro": 'C2 practitioners must communicate seamlessly with engineering leads, CFOs, and legal counsels using exact domain terminology.',
                "sections": [
                    {
                        "title": 'Domain Specialist Jargon',
                        "subsections": [
                            {
                                "title": 'Software Systems Engineering',
                                "layout": 'table',
                                "headers": ['Engineering Jargon', 'Pronunciation', 'Significance (Spanish)'],
                                "rows": [
                                    ['**Latency**', '`/ˈleɪ.tən.si/`', 'Latencia (Time delay in data transmission over networks)'],
                                    ['**Microservices**', '`/ˌmaɪ.kroʊˈsɜː.vɪ.sɪz/`', 'Microservicios (Architectural style partitioning an app into small services)'],
                                    ['**Idempotency**', '`/ˌaɪ.dəmˈpoʊ.təns/`', 'Idempotencia (Operations producing the same result regardless of repeated execution)'],
                                    ['**Scalability**', '`/ˌskeɪ.ləˈbɪl.ə.ti/`', 'Escalabilidad (The capacity of a system to handle growing amounts of work)']
                                ]
                            },
                            {
                                "title": 'Finance & Capital Markets',
                                "layout": 'table',
                                "headers": ['Finance Jargon', 'Pronunciation', 'Significance'],
                                "rows": [
                                    ['**Arbitrage**', '`/ˈɑː.bɪ.trɑːʒ/`', 'Arbitraje (Simultaneous purchase and sale of an asset to profit from price differences)'],
                                    ['**Liquidity**', '`/lɪˈkwɪd.ə.ti/`', 'Liquidez (Availability of liquid assets or cash to a market or company)'],
                                    ['**Equity**', '`/ˈɛk.wɪ.ti/`', 'Capital / acciones (Value of shares issued by a company)'],
                                    ['**Amortization**', '`/əˌmɔː.tɪˈzeɪ.ʃən/`', 'Amortización (Spreading payments of loans or intangible assets over time)']
                                ]
                            },
                            {
                                "title": 'Legal & Contract Law',
                                "layout": 'table',
                                "headers": ['Legal Term', 'Pronunciation', 'Translation'],
                                "rows": [
                                    ['**Liability**', '`/ˌlaɪ.əˈbɪl.ə.ti/`', 'Responsabilidad civil / legal (State of being legally responsible for something)'],
                                    ['**Indemnity**', '`/ɪnˈdɛm.nə.ti/`', 'Indemnización (Security or protection against a financial loss or liability)'],
                                    ['**Clause**', '`/klɔːz/`', 'Cláusula (Particular and separate article in a contract or treaty)'],
                                    ['**Breach of contract**', '`/briːtʃ ɒv ˈkɒn.trækt/`', 'Incumplimiento de contrato (Failing to perform any term of a contract without legal excuse)']
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 51,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'The contract contains an indemnity clause to protect the company against liability.',
                "translation": 'El contrato contiene una cláusula de indemnización para proteger a la empresa contra la responsabilidad legal.',
                "ipa_notation": '/ðə ˈkɒntrækt kənˈteɪnz ən ɪnˈdɛmnɪti klɔːz tuː prəˈtɛkt ðə ˈkʌmpəni əˈɡeɪnst ˌlaɪəˈbɪlɪti/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Our microservices architecture has significantly reduced network latency.',
                "translation": 'Nuestra arquitectura de microservicios ha reducido significativamente la latencia de la red.',
                "ipa_notation": '/ˈaʊər ˌmaɪkroʊˈsɜːrvɪsɪz ˈɑːrkətɛktʃər hæz sɪɡˈnɪfɪkəntli rɪˈdjuːst ˈnɛtwɜːrk ˈleɪtənsi/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which legal term refers to 'security or protection against financial loss or legal liability'?",
                "correct_answer": "indemnity",
                "options": {
                    "a": "liability",
                    "b": "indemnity",
                    "c": "arbitrage",
                    "d": "idempotency"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'C2',
        "meta": {
            "title": 'Deep Cultural Idioms & Proverbs',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master sophisticated idiomatic proverbs (bite the bullet, burn the midnight oil, the devil is in the details).',
            "explanation": {
                "intro": 'Sophisticated command of English is demonstrated by using culturally rich proverbs and expressions naturally and effectively.',
                "sections": [
                    {
                        "title": 'Sophisticated Cultural Phrasing',
                        "subsections": [
                            {
                                "title": 'Mastery Proverbs & Sayings',
                                "layout": 'table',
                                "headers": ['Saying / Proverb', 'Pronunciation', 'Significance & Translation (Spanish)'],
                                "rows": [
                                    ['**Bite the bullet**', '`/baɪt ðə ˈbʊl.ɪt/`', 'Morder la bala (Face a painful situation with courage and get it over with)'],
                                    ['**Burn the midnight oil**', '`/bɜːn ðə ˈmɪd.naɪt ɔɪl/`', 'Quemar las pestañas (Work or study late into the night)'],
                                    ['**The devil is in the details**', '`/ðə ˈdɛv.əl ɪz ɪn ðə ˈdiː.teɪlz/`', 'El diablo está en los detalles (Small things in a plan can cause big problems later)'],
                                    ['**Read between the lines**', '`/riːd bɪˈtwiːn ðə laɪnz/`', 'Leer entre líneas (Understand the implicit or hidden meaning behind text/speech)'],
                                    ['**Jump on the bandwagon**', '`/dʒʌmp ɒn ðə ˈbændˌwæɡ.ən/`', 'Subirse al carro / moda (Adopt a popular activity or trend simply because it is popular)']
                                ]
                            },
                            {
                                "title": 'Didactic Cards',
                                "layout": 'cards',
                                "items": [
                                    "**Bite the bullet** | Facing Hard Decisions | We had to **bite the bullet** and deprecate the legacy database schema.",
                                    "**The devil is in the details** | Structural Precision | Pay close attention to the API contract; **the devil is in the details**.",
                                    "**Burn the midnight oil** | Working Late | Our dev team spent last night **burning the midnight oil** to patch the security vulnerability."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 52,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'We decided to bite the bullet and rewrite the legacy codebase entirely.',
                "translation": 'Decidimos morder la bala y reescribir el código heredado por completo.',
                "ipa_notation": '/wiː dɪˈsaɪdɪd tuː baɪt ðə ˈbʊlɪt ænd ˌriːˈraɪt ðə ˈlɛɡəsi ˈkoʊdbeɪs ɪnˈtaɪərli/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'He spent all night burning the midnight oil to fix the production outage.',
                "translation": 'Pasó toda la noche quemándose las pestañas para solucionar la interrupción del servicio de producción.',
                "ipa_notation": '/hiː spɛnt ɔːl naɪt ˈbɜːrnɪŋ ðə ˈmɪdnaɪt ɔɪl tuː fɪks ðə prəˈdʌkʃən ˈaʊtɪdʒ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the meaning of the proverb 'the devil is in the details'?",
                "correct_answer": "small things in a plan can cause big problems later",
                "options": {
                    "a": "programming is evil",
                    "b": "small things in a plan can cause big problems later",
                    "c": "details are not important",
                    "d": "contracts are dangerous"
                },
                "order_index": 1,
            }
        ]
    }
]
