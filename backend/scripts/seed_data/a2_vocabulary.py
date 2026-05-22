# a2_vocabulary.py — Elementary Vocabulary Lessons

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A2_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Travel & Tourism — Surviving Abroad',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn the vocabulary for hotel reservations, airport checks, directions, and common transport verbs.',
            "explanation": {
                "intro": 'Travel requires precise vocabulary to book accommodation, pass security checks, and ask for clear directions in English.',
                "sections": [
                    {
                        "title": 'Airport & Accommodation',
                        "subsections": [
                            {
                                "title": 'At the Airport',
                                "layout": 'table',
                                "headers": ['Airport Term', 'Pronunciation', 'Significance (Spanish)'],
                                "rows": [
                                    ['**Boarding pass**', '`/ˈbɔːrdɪŋ pæs/`', 'Tarjeta de embarque (Document allowing you onto the plane)'],
                                    ['**Luggage / Baggage**', '`/ˈlʌɡɪdʒ/`', 'Equipaje (Suitcases and bags for travel)'],
                                    ['**Gate**', '`/ɡeɪt/`', 'Puerta de embarque (Where you board the plane)'],
                                    ['**Customs**', '`/ˈkʌstəmz/`', 'Aduana (Where goods are declared)'],
                                    ['**Flight attendant**', '`/flaɪt əˈtɛndənt/`', 'Auxiliar de vuelo (Cabin crew member)']
                                ]
                            },
                            {
                                "title": 'At the Hotel',
                                "layout": 'table',
                                "headers": ['Hotel Phrase', 'Pronunciation', 'Meaning (Spanish)'],
                                "rows": [
                                    ['**Check-in**', '`/ˈtʃɛk.ɪn/`', 'Registrarse al llegar (Register upon arrival)'],
                                    ['**Reservation**', '`/ˌrɛzərˈveɪʃən/`', 'Reserva (A booked room or seat)'],
                                    ['**Double room**', '`/ˈdʌbəl ruːm/`', 'Habitación doble (Room with a double bed)'],
                                    ['**Single room**', '`/ˈsɪŋɡəl ruːm/`', 'Habitación individual (Room for one person)'],
                                    ['**Amenities**', '`/əˈmɛnətiz/`', 'Servicios / comodidades (Wifi, pool, breakfast)']
                                ]
                            },
                            {
                                "title": 'Asking for Directions',
                                "layout": 'list',
                                "items": [
                                    "**Excuse me, where is the...?** | Excuse me, where is the nearest subway station?",
                                    "**How do I get to...?** | How do I get to the central square from here?",
                                    "**Go straight / Turn left / Turn right** | Go straight for two blocks, then turn left at the corner."
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
                "phrase": 'I would like to book a double room for three nights, please.',
                "translation": 'Me gustaría reservar una habitación doble por tres noches, por favor.',
                "ipa_notation": '/aɪ wʊd laɪk tə bʊk ə ˈdʌbəl ruːm fɔːr θriː naɪts pliːz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Excuse me, where is the departure gate for flight 402?',
                "translation": 'Disculpe, ¿dónde está la puerta de salida para el vuelo 402?',
                "ipa_notation": '/ɪkˈskjuːz miː weər ɪz ðə dɪˈpɑːrtʃər ɡeɪt fɔːr flaɪt fɔːr-oʊ-tuː/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which document is required to board an airplane?",
                "correct_answer": "boarding pass",
                "options": {
                    "a": "receipt",
                    "b": "boarding pass",
                    "c": "prescription",
                    "d": "menu"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Health & The Body — Going to the Doctor',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn to describe symptoms (pain, fever, cough), body parts, and basic medical advice.',
            "explanation": {
                "intro": 'Knowing how to describe physical symptoms and understand a doctor\'s instructions is vital for working and traveling internationally.',
                "sections": [
                    {
                        "title": 'Medical Symptoms & Treatments',
                        "subsections": [
                            {
                                "title": 'Common Symptoms',
                                "layout": 'table',
                                "headers": ['Symptom', 'Pronunciation', 'Translation (Spanish)'],
                                "rows": [
                                    ['**Headache**', '`/ˈhɛdeɪk/`', 'Dolor de cabeza'],
                                    ['**Sore throat**', '`/sɔːr θroʊt/`', 'Dolor de garganta'],
                                    ['**Fever**', '`/ˈfiːvər/`', 'Fiebre'],
                                    ['**Cough**', '`/kɒf/`', 'Tos'],
                                    ['**Stomachache**', '`/ˈstʌmək.eɪk/`', 'Dolor de estómago']
                                ]
                            },
                            {
                                "title": 'At the Pharmacy',
                                "layout": 'table',
                                "headers": ['Pharmacy Term', 'Pronunciation', 'Significance'],
                                "rows": [
                                    ['**Prescription**', '`/prɪˈskrɪpʃən/`', 'Receta médica (Official note from a doctor for medicine)'],
                                    ['**Painkiller**', '`/ˈpeɪnˌkɪlər/`', 'Analgésico (Medicine that stops pain)'],
                                    ['**Pills / Tablets**', '`/pɪlz/`', 'Pastillas / comprimidos'],
                                    ['**Ointment**', '`/ˈɔɪntmənt/`', 'Pomada / ungüento'],
                                    ['**Bandage**', '`/ˈbændɪdʒ/`', 'Venda / curita']
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
                "phrase": 'I have a sore throat and a high fever today.',
                "translation": 'Tengo dolor de garganta y fiebre alta hoy.',
                "ipa_notation": '/aɪ hæv ə sɔːr θroʊt ænd ə haɪ ˈfiːvər təˈdeɪ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The doctor gave me a prescription for pain medicine.',
                "translation": 'El médico me dio una receta para medicamentos contra el dolor.',
                "ipa_notation": '/ðə ˈdɒktər ɡeɪv miː ə prɪˈskrɪpʃən fɔːr peɪn ˈmɛdsən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the English word for 'fiebre'?",
                "correct_answer": "fever",
                "options": {
                    "a": "cough",
                    "b": "fever",
                    "c": "headache",
                    "d": "bandage"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Shopping & Money — Buying What You Need',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master retail terminology (receipt, discount, cash, card), currency phrases, and size issues.',
            "explanation": {
                "intro": 'Buying products or subscribing to SaaS tools online requires understanding payment modes, discounts, and purchase validation terms.',
                "sections": [
                    {
                        "title": 'Transactions & Pricing',
                        "subsections": [
                            {
                                "title": 'Payment and Sales Terms',
                                "layout": 'table',
                                "headers": ['Retail Term', 'Pronunciation', 'Meaning (Spanish)'],
                                "rows": [
                                    ['**Cash**', '`/kæʃ/`', 'Dinero en efectivo (Paper bills and coins)'],
                                    ['**Receipt**', '`/rɪˈsiːt/`', 'Recibo / ticket (Proof of purchase)'],
                                    ['**Discount**', '`/ˈdɪskaʊnt/`', 'Descuento (Reduced price)'],
                                    ['**Refund**', '`/ˈriːfʌnd/`', 'Reembolso (Getting money back)'],
                                    ['**Price tag**', '`/praɪs tæɡ/`', 'Etiqueta de precio (Label showing the cost)']
                                ]
                            },
                            {
                                "title": 'Shopping Dialogues',
                                "layout": 'list',
                                "items": [
                                    "**How much does this cost?** | Used to ask the price of a physical item.",
                                    "**Do you accept credit cards?** | Used to verify if digital payments are accepted.",
                                    "**I would like to return this item.** | Standard phrase to request a refund."
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
                "phrase": 'Can I pay by credit card or do you only accept cash?',
                "translation": '¿Puedo pagar con tarjeta de crédito o solo aceptan efectivo?',
                "ipa_notation": '/kæn aɪ peɪ baɪ ˈkrɛdɪt kɑːrd ɔːr duː juː ˈoʊnli əkˈsɛpt kæʃ/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Make sure to keep the receipt if you want a refund.',
                "translation": 'Asegúrate de conservar el recibo si deseas un reembolso.',
                "ipa_notation": '/meɪk ʃʊər tə kiːp ðə rɪˈsiːt ɪf juː wɒnt ə ˈriːfʌnd/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which word has a silent 'p' and means 'proof of purchase'?",
                "correct_answer": "receipt",
                "options": {
                    "a": "refund",
                    "b": "receipt",
                    "c": "discount",
                    "d": "cash"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'A2',
        "meta": {
            "title": 'Clothes & Fashion — What are you wearing?',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn clothing articles, adjectives of style/fit (tight, loose, formal), and materials.',
            "explanation": {
                "intro": 'Learn how to describe clothes, fit preferences, and typical materials used in garments.',
                "sections": [
                    {
                        "title": 'Clothing & Attributes',
                        "subsections": [
                            {
                                "title": 'Garment Vocabulary',
                                "layout": 'table',
                                "headers": ['Garment', 'Pronunciation', 'Translation'],
                                "rows": [
                                    ['**Suit**', '`/suːt/`', 'Traje (Formal matching jacket and pants)'],
                                    ['**Coat**', '`/koʊt/`', 'Abrigo (Warm outer garment)'],
                                    ['**Shirt**', '`/ʃɜːrt/`', 'Camisa (Upper body clothing with collar)'],
                                    ['**Shoes**', '`/ʃuːz/`', 'Zapatos'],
                                    ['**Trousers / Pants**', '`/ˈtraʊzərz/`', 'Pantalones']
                                ]
                            },
                            {
                                "title": 'Fit and Material',
                                "layout": 'table',
                                "headers": ['Fit/Material', 'Pronunciation', 'Significance'],
                                "rows": [
                                    ['**Tight**', '`/taɪt/`', 'Ajustado (Close-fitting, small)'],
                                    ['**Loose**', '`/luːs/`', 'Holgado (Not tight, baggier)'],
                                    ['**Cotton**', '`/ˈkɒtən/`', 'Algodón (Soft natural fabric)'],
                                    ['**Wool**', '`/wʊl/`', 'Lana (Thick warm animal hair fabric)'],
                                    ['**Casual**', '`/ˈkæʒuəl/`', 'Informal (Everyday comfortable style)']
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
                "phrase": 'He is wearing a blue suit and a striped tie for the meeting.',
                "translation": 'Él lleva puesto un traje azul y una corbata a rayas para la reunión.',
                "ipa_notation": '/hiː ɪz ˈwɛərɪŋ ə bluː suːt ænd ə straɪpt taɪ fɔːr ðə ˈmiːtɪŋ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'It is freezing outside, so make sure to wear a warm wool coat.',
                "translation": 'Hace un frío helador afuera, así que asegúrate de usar un abrigo de lana abrigado.',
                "ipa_notation": '/ɪt ɪz ˈfriːzɪŋ ˌaʊtˈsaɪd soʊ meɪk ʃʊər tə wɛər ə wɔːrm wʊl koʊt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the opposite of 'tight' clothes?",
                "correct_answer": "loose",
                "options": {
                    "a": "casual",
                    "b": "tight",
                    "c": "loose",
                    "d": "formal"
                },
                "order_index": 1,
            }
        ]
    }
]
