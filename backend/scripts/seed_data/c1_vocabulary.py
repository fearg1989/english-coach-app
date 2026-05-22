# c1_vocabulary.py — Advanced Vocabulary Lessons

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C1_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'C1',
        "meta": {
            "title": 'Precise Verbs & Abstract Nouns — The Executive Lexicon',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn strategic corporate verbs (streamline, leverage, spearhead, optimize) and executive abstract nouns.',
            "explanation": {
                "intro": 'Advanced executive conversations rely on precise, action-oriented verbs that communicate impact and strategic vision.',
                "sections": [
                    {
                        "title": 'Strategic Lexicon',
                        "subsections": [
                            {
                                "title": 'High-Impact Executive Verbs',
                                "layout": 'table',
                                "headers": ['Action Verb', 'Pronunciation', 'Professional Significance (Spanish)'],
                                "rows": [
                                    ['**Streamline**', '`/ˈstriːm.laɪn/`', 'Optimizar / simplificar (Make a system or organization simpler and more efficient)'],
                                    ['**Leverage**', '`/ˈliː.vər.ɪdʒ/`', 'Aprovechar (Use something to maximum advantage)'],
                                    ['**Spearhead**', '`/ˈspɪə.hɛd/`', 'Liderar / encabezar (Lead an initiative, campaign, or program)'],
                                    ['**Optimize**', '`/ˈɒp.tɪ.maɪz/`', 'Optimizar (Make the best or most effective use of a situation or resource)'],
                                    ['**Consolidate**', '`/kənˈsɒl.ɪ.deɪt/`', 'Consolidar / fusionar (Combine a number of things into a single more effective whole)']
                                ]
                            },
                            {
                                "title": 'Executive Abstract Nouns',
                                "layout": 'table',
                                "headers": ['Executive Noun', 'Pronunciation', 'Meaning'],
                                "rows": [
                                    ['**Synergy**', '`/ˈsɪn.ə.dʒi/`', 'Sinergia (The interaction of elements to produce a greater combined effect)'],
                                    ['**Acquisition**', '`/ˌæk.wɪˈzɪʃ.ən/`', 'Adquisición (An asset or object bought or obtained)'],
                                    ['**Disruption**', '`/dɪsˈrʌp.ʃən/`', 'Disrupción / innovación disruptiva (Disturbance or radical change in an industry)'],
                                    ['**Mitigation**', '`/ˌmɪt.ɪˈɡeɪ.ʃən/`', 'Mitigación (The action of reducing the severity or seriousness of something)'],
                                    ['**Alignment**', '`/əˈlaɪn.mənt/`', 'Alineación (Position of agreement or alliance among departments)']
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
                "phrase": 'We decided to streamline our deployment process to minimize downtime.',
                "translation": 'Decidimos simplificar nuestro proceso de despliegue para minimizar el tiempo de inactividad.',
                "ipa_notation": '/wiː dɪˈsaɪdɪd tuː ˈstriːmlaɪn ˈaʊər dɪˈplɔɪmənt ˈproʊsɛs tuː ˈmɪnɪmaɪz ˈdaʊntaɪm/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She will spearhead the integration of the new authentication system.',
                "translation": 'Ella liderará la integración del nuevo sistema de autenticación.',
                "ipa_notation": '/ʃiː wɪl ˈspɪərhɛd ði ˌɪntɪˈɡreɪʃən ɒv ðə njuː ˌɔːθɛntɪˈkeɪʃən ˈsɪstəm/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which verb means 'to lead an initiative, campaign, or team effort'?",
                "correct_answer": "spearhead",
                "options": {
                    "a": "leverage",
                    "b": "spearhead",
                    "c": "streamline",
                    "d": "consolidate"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'C1',
        "meta": {
            "title": 'Metaphors in Tech & Business',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn idiomatic business metaphors (low-hanging fruit, bandwidth, boil the ocean, pivot).',
            "explanation": {
                "intro": 'Metaphors are figures of speech that describe an action or object in a way that isn\'t literally true, but helps explain an idea.',
                "sections": [
                    {
                        "title": 'Tech Industry Metaphors',
                        "subsections": [
                            {
                                "title": 'Common Metaphors',
                                "layout": 'table',
                                "headers": ['Metaphorical Term', 'Pronunciation', 'Literal & Figurative Meaning (Spanish)'],
                                "rows": [
                                    ['**Low-hanging fruit**', '`/loʊ ˈhæŋ.ɪŋ fruːt/`', 'Fruta al alcance de la mano (Easy-to-achieve targets or quick wins)'],
                                    ['**Bandwidth**', '`/ˈbænd.wɪtθ/`', 'Ancho de banda (Figurative: Cognitive capacity or time to work on something)'],
                                    ['**Boil the ocean**', '`/bɔɪl ði ˈoʊ.ʃən/`', 'Hervir el océano (Attempt an impossible task or overcomplicate a project)'],
                                    ['**Pivot**', '`/ˈpɪv.ət/`', 'Pivotar (Change strategic direction entirely)'],
                                    ['**Silo**', '`/ˈsaɪ.loʊ/`', 'Silo (Isolate system or department from others)']
                                ]
                            },
                            {
                                "title": 'Usage Guidelines',
                                "layout": 'list',
                                "items": [
                                    "Use **bandwidth** in professional discussions: '*I don't have the bandwidth for that right now.*'",
                                    "Avoid **boiling the ocean** when planning: '*Let's start small; we don't want to boil the ocean.*'",
                                    "Identify **low-hanging fruit** during standups: '*Fixing that UI typo is low-hanging fruit.*'"
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
                "phrase": "Let's focus on the low-hanging fruit to show immediate value to stakeholders.",
                "translation": 'Centrémonos en lo más fácil y rápido para mostrar valor inmediato a las partes interesadas.',
                "ipa_notation": '/lɛts ˈfoʊkəs ɒn ðə loʊ-ˈhæŋɪŋ fruːt tuː ʃoʊ ɪˈmiːdiət ˈvæljuː tuː ˈsteɪkhoʊldərz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I do not have the bandwidth to take on another project this quarter.',
                "translation": 'No tengo el tiempo ni la capacidad para asumir otro proyecto este trimestre.',
                "ipa_notation": '/aɪ duː nɒt hæv ðə ˈbændwɪtθ tuː teɪk ɒn əˈnʌðər ˈprɒdʒɛkt ðɪs ˈkwɔːrtər/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What does the tech metaphor 'bandwidth' mean when referring to a person?",
                "correct_answer": "time and cognitive capacity",
                "options": {
                    "a": "internet speed",
                    "b": "time and cognitive capacity",
                    "c": "financial budget",
                    "d": "programming knowledge"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'C1',
        "meta": {
            "title": 'Professional Idioms — Beyond the Literal Meaning',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master advanced workplace idioms (think outside the box, touch base, double down, hit the ground running).',
            "explanation": {
                "intro": 'Idioms are phrases whose meanings cannot be deduced from the literal words. Mastering them is essential for advanced business integration.',
                "sections": [
                    {
                        "title": 'Workplace Idiomatic Phrasing',
                        "subsections": [
                            {
                                "title": 'High-Frequency Office Idioms',
                                "layout": 'table',
                                "headers": ['Idiom', 'Pronunciation', 'Professional Translation (Spanish)'],
                                "rows": [
                                    ['**Think outside the box**', '`/θɪŋk ˌaʊtˈsaɪd ðə bɒks/`', 'Pensar fuera de la caja (Think creatively and unconventionally)'],
                                    ['**Touch base**', '`/tʌtʃ beɪs/`', 'Hacer contacto / ponerse al día (Briefly contact someone to catch up)'],
                                    ['**Double down**', '`/ˈdʌb.əl daʊn/`', 'Duplicar la apuesta (Strengthen your commitment to a strategy or path)'],
                                    ['**Hit the ground running**', '`/hɪt ðə ɡraʊnd ˈrʌn.ɪŋ/`', 'Empezar a tope (Start a new activity with rapid progress and high energy)'],
                                    ['**Keep in the loop**', '`/kiːp ɪn ðə luːp/`', 'Mantener informado (Keep someone fully informed about a project)']
                                ]
                            },
                            {
                                "title": 'Didactic Cards',
                                "layout": 'cards',
                                "items": [
                                    "**Think outside the box** | Creative Problem Solving | We need to **think outside the box** to bypass these performance constraints.",
                                    "**Touch base** | Keep in Contact | I will **touch base** with you tomorrow after the deployment completes.",
                                    "**Double down** | Commitment | We should **double down** on our cloud native strategy this quarter."
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
                "phrase": 'We need to think outside the box to bypass these engineering limitations.',
                "translation": 'Necesitamos pensar de forma no convencional para superar estas limitaciones de ingeniería.',
                "ipa_notation": '/wiː niːd tuː θɪŋk ˌaʊtˈsaɪd ðə bɒks tuː ˈbaɪpæs ðiːz ˌɛndʒɪˈnɪərɪŋ ˌlɪmɪˈteɪʃənz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I will touch base with you tomorrow after I review the pull request.',
                "translation": 'Me pondré en contacto contigo mañana después de revisar la solicitud de extracción.',
                "ipa_notation": '/aɪ wɪl tʌtʃ beɪs wɪð juː təˈmɒroʊ ˈæftər aɪ rɪˈvjuː ðə pʊl rɪˈkwɛst/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the meaning of the idiom 'touch base'?",
                "correct_answer": "briefly contact someone to catch up",
                "options": {
                    "a": "play baseball",
                    "b": "complete a task",
                    "c": "briefly contact someone to catch up",
                    "d": "investigate a bug"
                },
                "order_index": 1,
            }
        ]
    }
]
