# b2_vocabulary.py — Upper-Intermediate Vocabulary Lessons

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B2_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'B2',
        "meta": {
            "title": 'Abstract Nouns — Corporate & Business',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn high-frequency abstract nouns for the modern corporate workplace (deadline, consensus, resource, feedback).',
            "explanation": {
                "intro": 'Professional corporate communication relies heavily on abstract nouns to discuss processes, results, and strategy.',
                "sections": [
                    {
                        "title": 'Corporate Abstract Terminology',
                        "subsections": [
                            {
                                "title": 'Workplace Abstract Nouns',
                                "layout": 'table',
                                "headers": ['Noun', 'Pronunciation', 'Significance / Meaning (Spanish)'],
                                "rows": [
                                    ['**Consensus**', '`/kənˈsɛn.səs/`', 'Consenso (General agreement among a group)'],
                                    ['**Deadline**', '`/ˈdɛd.laɪn/`', 'Fecha límite (The latest time by which something must be done)'],
                                    ['**Feedback**', '`/ˈfiːd.bæk/`', 'Comentarios / retroalimentación (Evaluative information about work)'],
                                    ['**Resource**', '`/rɪˈzɔːs/`', 'Recurso (A stock or supply of money, materials, or staff)'],
                                    ['**Efficiency**', '`/ɪˈfɪʃ.ən.si/`', 'Eficiencia (The state of achieving maximum productivity with minimum wasted effort)']
                                ]
                            },
                            {
                                "title": 'Strategy Nouns',
                                "layout": 'table',
                                "headers": ['Noun', 'Pronunciation', 'Explanation'],
                                "rows": [
                                    ['**Outcome**', '`/ˈaʊt.kʌm/`', 'Resultado / consecuencia (The final consequence or result)'],
                                    ['**Implementation**', '`/ˌɪm.plɪ.mɛnˈteɪ.ʃən/`', 'Implementación (The process of putting a decision or plan into effect)'],
                                    ['**Feasibility**', '`/ˌfiː.zəˈbɪl.ə.ti/`', 'Viabilidad (The state of being easily or conveniently done)'],
                                    ['**Collaboration**', '`/kəˌlæb.əˈreɪ.ʃən/`', 'Colaboración (The action of working with someone to produce something)'],
                                    ['**Innovation**', '`/ˌɪn.əˈveɪ.ʃən/`', 'Innovación (The action or process of innovating new ideas or products)']
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
                "phrase": 'We need to reach a consensus before we make the final product decision.',
                "translation": 'Necesitamos llegar a un consenso antes de tomar la decisión final sobre el producto.',
                "ipa_notation": '/wiː niːd tuː riːtʃ ə kənˈsɛnsəs bɪˈfɔːr wiː meɪk ðə ˈfaɪnəl ˈprɒdʌkt dɪˈsɪʒən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Please provide your feedback on the new user interface mockups by Friday.',
                "translation": 'Por favor, proporciona tus comentarios sobre las nuevas maquetas de la interfaz de usuario para el viernes.',
                "ipa_notation": '/pliːz prəˈvaɪd jɔːr ˈfiːdbæk ɒn ðə njuː ˈjuːzər ˈɪntərfeɪs ˈmɒkʌps baɪ ˈfraɪdeɪ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the corporate noun that means 'general agreement among a group of people'?",
                "correct_answer": "consensus",
                "options": {
                    "a": "deadline",
                    "b": "feasibility",
                    "c": "consensus",
                    "d": "outcome"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B2',
        "meta": {
            "title": 'Advanced Collocations — Words that go together',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master standard verb-noun and adverb-adjective patterns (make a decision, deeply concerned, highly recommend).',
            "explanation": {
                "intro": 'Collocations are pairs or groups of words that naturally go together. Using them makes your English sound native and fluent.',
                "sections": [
                    {
                        "title": 'Natural Word Pairs',
                        "subsections": [
                            {
                                "title": 'Verb-Noun Collocations',
                                "layout": 'table',
                                "headers": ['Verb + Noun', 'Pronunciation', 'Significance (Spanish)'],
                                "rows": [
                                    ['**Make a decision**', '`/meɪk ə dɪˈsɪʒ.ən/`', 'Tomar una decisión (Avoid: "take a decision" in US English)'],
                                    ['**Take into account**', '`/teɪk ˈɪn.tuː əˈkaʊnt/`', 'Tener en cuenta (Consider details during planning)'],
                                    ['**Conduct an analysis**', '`/kənˈdʌkt ən əˈnæl.ə.sɪs/`', 'Realizar un análisis (Perform a systematic study)'],
                                    ['**Meet a requirement**', '`/miːt ə rɪˈkwaɪə.mənt/`', 'Cumplir con un requisito (Satisfy a need or rule)'],
                                    ['**Solve a problem**', '`/sɒlv ə ˈprɒb.ləm/`', 'Resolver un problema (Find a solution)']
                                ]
                            },
                            {
                                "title": 'Adverb-Adjective Collocations',
                                "layout": 'table',
                                "headers": ['Adverb + Adjective', 'Pronunciation', 'Meaning'],
                                "rows": [
                                    ['**Highly recommend**', '`/ˈhaɪ.li ˌrɛk.əˈmɛnd/`', 'Recomendar encarecidamente (Strong recommendation)'],
                                    ['**Deeply concerned**', '`/ˈdiːp.li kənˈsɜːnd/`', 'Profundamente preocupado (Sincere worry)'],
                                    ['**Widely accepted**', '`/ˈwaɪd.li əkˈsɛp.tɪd/`', 'Ampliamente aceptado (Believed by many)'],
                                    ['**Vastly improved**', '`/ˈvɑːst.li ɪmˈpruːvd/`', 'Enormemente mejorado (Much better)'],
                                    ['**Strictly prohibited**', '`/ˈstrɪkt.li prəˈhɪb.ɪ.tɪd/`', 'Estrictamente prohibido (Completely forbidden)']
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
                "phrase": 'I highly recommend updating our security dependencies immediately.',
                "translation": 'Recomiendo encarecidamente actualizar nuestras dependencias de seguridad de inmediato.',
                "ipa_notation": '/aɪ ˈhaɪli ˌrɛkəˈmɛnd ʌpˈdeɪtɪŋ ˈaʊər sɪˈjʊərəti dɪˈpɛndənsiz ɪˈmiːdiətli/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'We must take into account the budget constraints when planning the project.',
                "translation": 'Debemos tener en cuenta las limitaciones presupuestarias al planificar el proyecto.',
                "ipa_notation": '/wiː mʌst teɪk ˈɪntuː əˈaʊnt ðə ˈbʌdʒɪt kənˈstreɪnts wɛn ˈplænɪŋ ðə ˈprɒdʒɛkt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which verb collocates naturally with 'decision' in professional English?",
                "correct_answer": "make",
                "options": {
                    "a": "do",
                    "b": "make",
                    "c": "have",
                    "d": "get"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B2',
        "meta": {
            "title": 'Politics, Society & Global Issues',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Discuss elections, fiscal policy, socioeconomic issues, and welfare systems.',
            "explanation": {
                "intro": 'Professional teams discuss socio-economic trends, corporate policies, and global issues using accurate terms.',
                "sections": [
                    {
                        "title": 'Socio-Political Terminology',
                        "subsections": [
                            {
                                "title": 'Politics & Governance',
                                "layout": 'table',
                                "headers": ['Political Term', 'Pronunciation', 'Significance (Spanish)'],
                                "rows": [
                                    ['**Election**', '`/iˈlɛk.ʃən/`', 'Elecciones (Process of voting to choose representatives)'],
                                    ['**Policy**', '`/ˈpɒl.ə.si/`', 'Política / norma (A course or principle of action adopted by a government or business)'],
                                    ['**Legislation**', '`/ˌlɛdʒ.ɪsˈleɪ.ʃən/`', 'Legislación / leyes (Laws, considered collectively)'],
                                    ['**Regulation**', '`/ˌrɛɡ.jəˈleɪ.ʃən/`', 'Regulaciones (Rule maintained by an authority)'],
                                    ['**Government**', '`/ˈɡʌv.ən.mənt/`', 'Gobierno']
                                ]
                            },
                            {
                                "title": 'Global Socioeconomic Issues',
                                "layout": 'table',
                                "headers": ['Issue Term', 'Pronunciation', 'Explanation'],
                                "rows": [
                                    ['**Inflation**', '`/ɪnˈfleɪ.ʃən/`', 'Inflación (Increase in prices and fall in purchasing value of money)'],
                                    ['**Immigration**', '`/ˌɪm.ɪˈɡreɪ.ʃən/`', 'Inmigración (The action of coming to live permanently in a foreign country)'],
                                    ['**Welfare**', '`/ˈwɛl.feər/`', 'Bienestar social (Financial support given to people in need)'],
                                    ['**Unemployment**', '`/ˌʌn.ɪmˈplɔɪ.mənt/`', 'Desempleo (The state of not having a job)'],
                                    ['**Sustainability**', '`/səˌsteɪ.nəˈbɪl.ə.ti/`', 'Sostenibilidad (The ability to be maintained at a certain rate without depletion)']
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
                "phrase": 'The government is implementing a new fiscal policy to combat rising inflation.',
                "translation": 'El gobierno está implementando una nueva política fiscal para combatir el aumento de la inflación.',
                "ipa_notation": '/ðə ˈɡʌvərnmənt ɪz ˈɪmplɪmɛntɪŋ ə njuː ˈfɪskəl ˈpɒlɪsi tuː kəmˈbæt ˈraɪzɪŋ ɪnˈfleɪʃən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Stable regulatory environments are required for economic growth.',
                "translation": 'Se requieren entornos regulatorios estables para el crecimiento económico.',
                "ipa_notation": '/ˈsteɪbəl ˈrɛɡjələtɔːri ɪnˈvaɪrənmənts ɑːr rɪˈkwaɪərd fɔːr ˌiːkəˈnɒmɪk ɡroʊθ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the economic term for the general increase in prices and fall in purchasing power?",
                "correct_answer": "inflation",
                "options": {
                    "a": "welfare",
                    "b": "sustainability",
                    "c": "inflation",
                    "d": "regulation"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B2',
        "meta": {
            "title": 'Register & Pragmatics — Formal vs. Casual',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn to shift tones between formal client emails and casual peer messaging.',
            "explanation": {
                "intro": 'Register refers to the level of formality in language. Shifting register correctly protects professional relationships.',
                "sections": [
                    {
                        "title": 'Formality Shifts',
                        "subsections": [
                            {
                                "title": 'Register Equivalents',
                                "layout": 'table',
                                "headers": ['Casual (Peers / Slack)', 'Formal (Clients / Emails)', 'Context / Meaning'],
                                "rows": [
                                    ['**ask for**', '`request`', 'Solicitar (Could you request additional access?)'],
                                    ['**tell**', '`inform`', 'Informar (I am writing to inform you...)'],
                                    ['**check**', '`verify / ensure`', 'Verificar (Please verify that the server is online)'],
                                    ['**get in touch**', '`contact`', 'Contactar (Please contact support for billing issues)'],
                                    ['**give**', '`provide`', 'Proporcionar (We will provide the updated documentation)']
                                ]
                            },
                            {
                                "title": 'Tone Alignment Examples',
                                "layout": 'cards',
                                "items": [
                                    "**Formal Email** | I am writing to **request** additional details regarding the API specifications. We will **verify** them today.",
                                    "**Casual Slack** | Just wanted to **ask for** some more info on the API. We'll **check** it out today.",
                                    "**Formal Email** | Please **inform** the team that we will **provide** the update tomorrow.",
                                    "**Casual Slack** | Let the guys know we'll **give** them the update tomorrow."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 53,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I am writing to request additional details regarding the API specifications.',
                "translation": 'Le escribo para solicitar detalles adicionales sobre las especificaciones de la API.',
                "ipa_notation": '/aɪ æm ˈraɪtɪŋ tuː rɪˈkwɛst əˈdɪʃənəl dɪˈteɪlz rɪˈɡɑːrdɪŋ ði eɪ-pi-aɪ ˌspɛsɪfɪˈkeɪʃənz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Just wanted to ask for some more info on the API.',
                "translation": 'Solo quería pedir un poco más de información sobre la API.',
                "ipa_notation": '/dʒʌst ˈwɒntɪd tuː ɑːsk fɔːr sʌm mɔːr ˈɪnfoʊ ɒn ði eɪ-pi-aɪ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which formal verb corresponds to the casual expression 'ask for'?",
                "correct_answer": "request",
                "options": {
                    "a": "verify",
                    "b": "inform",
                    "c": "request",
                    "d": "provide"
                },
                "order_index": 1,
            }
        ]
    }
]
