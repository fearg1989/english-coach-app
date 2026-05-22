# b1_vocabulary.py — Intermediate Vocabulary Lessons

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B1_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'B1',
        "meta": {
            "title": 'Technology & Social Media — The Digital World',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn tech verbs (upload, download, scroll, click, post), devices, and account safety terms.',
            "explanation": {
                "intro": 'Technology dominates modern work. Learn how to describe software operations and online accounts in English.',
                "sections": [
                    {
                        "title": 'Digital Operations',
                        "subsections": [
                            {
                                "title": 'Tech Actions & Verbs',
                                "layout": 'table',
                                "headers": ['Software Operation', 'Pronunciation', 'Translation (Spanish)'],
                                "rows": [
                                    ['**Upload**', '`/ˌʌpˈloʊd/`', 'Subir archivos (Transfer data to another computer system)'],
                                    ['**Download**', '`/ˌdaʊnˈloʊd/`', 'Descargar (Copy data from another system to yours)'],
                                    ['**Scroll**', '`/skroʊl/`', 'Desplazarse (Move text/images up, down or across a screen)'],
                                    ['**Browse**', '`/braʊz/`', 'Navegar (Look through information on the internet)'],
                                    ['**Log in**', '`/lɒɡ ɪn/`', 'Iniciar sesión (Gain access to a secured computer system)']
                                ]
                            },
                            {
                                "title": 'Cybersecurity & Terms',
                                "layout": 'table',
                                "headers": ['Term', 'Pronunciation', 'Significance'],
                                "rows": [
                                    ['**Password**', '`/ˈpɑːs.wɜːd/`', 'Contraseña (Secret word or phrase for safety)'],
                                    ['**The Cloud**', '`/ðə klaʊd/`', 'La nube (Remote servers storing data online)'],
                                    ['**Backup**', '`/ˈbæk.ʌp/`', 'Copia de seguridad (A duplicate file for safety)'],
                                    ['**Database**', '`/ˈdeɪ.tə.beɪs/`', 'Base de datos (Structured collection of data)'],
                                    ['**User interface**', '`/ˈjuː.zər ˈɪn.tə.feɪs/`', 'Interfaz de usuario (What the user interacts with)']
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
                "phrase": 'You should upload the backup files to the cloud server.',
                "translation": 'Deberías subir los archivos de copia de seguridad al servidor de la nube.',
                "ipa_notation": '/juː ʃʊd ˌʌpˈloʊd ðə ˈbæk.ʌp faɪlz tə ðə klaʊd ˈsɜːrvər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Do not share your password with anyone to prevent cyber threats.',
                "translation": 'No compartas tu contraseña con nadie para prevenir amenazas cibernéticas.',
                "ipa_notation": '/duː nɒt ʃɛər jɔːr ˈpɑːs.wɜːd wɪð ˈɛni.wʌn tə prɪˈvɛnt ˈsaɪ.bər θrɛts/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the term for copying data from the internet to your own computer?",
                "correct_answer": "download",
                "options": {
                    "a": "upload",
                    "b": "download",
                    "c": "browse",
                    "d": "scroll"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B1',
        "meta": {
            "title": 'Education & Training — Your Background',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Discuss academic subjects, professional courses, university degrees, and resume terminology.',
            "explanation": {
                "intro": 'Describing your educational history and skills accurately on your CV is crucial for job interviews.',
                "sections": [
                    {
                        "title": 'Academic & Professional Training',
                        "subsections": [
                            {
                                "title": 'Educational Terms',
                                "layout": 'table',
                                "headers": ['Academic Term', 'Pronunciation', 'Translation'],
                                "rows": [
                                    ['**Degree**', '`/dɪˈɡriː/`', 'Título universitario (Qualification given by a university)'],
                                    ['**Graduate**', '`/ˈɡrædʒ.u.ət/`', 'Graduarse / Graduado (Successfully complete a university course)'],
                                    ['**Enroll**', '`/ɪnˈroʊl/`', 'Inscribirse / matricularse (Register for a course or class)'],
                                    ['**Major**', '`/ˈmeɪ.dʒər/`', 'Especialidad (Main subject studied at university)'],
                                    ['**Curriculum / CV**', '`/kəˈrɪk.jə.ləm/`', 'Currículum vitae (Document summarizing your education and work)']
                                ]
                            },
                            {
                                "title": 'Study & Skills Nouns',
                                "layout": 'table',
                                "headers": ['Subject/Skill', 'Pronunciation', 'Explanation'],
                                "rows": [
                                    ['**Scholarship**', '`/ˈskɒl.ə.ʃɪp/`', 'Beca de estudio (Financial aid for learning)'],
                                    ['**Internship**', '`/ˈɪn.tɜːn.ʃɪp/`', 'Pasantía / prácticas (Temporary work to gain skills)'],
                                    ['**Assignment**', '`/əˈsaɪn.mənt/`', 'Tarea / proyecto (Task given as study work)'],
                                    ['**Syllabus**', '`/ˈsɪl.ə.bəs/`', 'Programa de estudios (Outline of subjects in a course)'],
                                    ['**Certificate**', '`/səˈtɪf.ɪ.kət/`', 'Certificado (Proof of skill completion)']
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
                "phrase": "She graduated with a bachelor's degree in Computer Science.",
                "translation": 'Ella se graduó con una licenciatura en Ciencias de la Computación.',
                "ipa_notation": '/ʃiː ˈɡrædʒueɪtɪd wɪð ə ˈbætʃələrz dɪˈɡriː ɪn kəmˈpjuːtər ˈsaɪəns/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I decided to enroll in an online course to learn project management.',
                "translation": 'Decidí inscribirme en un curso en línea para aprender gestión de proyectos.',
                "ipa_notation": '/aɪ dɪˈsaɪdɪd tuː ɪnˈroʊl ɪn ən ˈɒnˌlaɪn kɔːrs tuː lɜːrn ˈprɒdʒɛkt ˈmænɪdʒmənt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the academic term for the main subject of study at a university?",
                "correct_answer": "major",
                "options": {
                    "a": "syllabus",
                    "b": "degree",
                    "c": "major",
                    "d": "internship"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B1',
        "meta": {
            "title": 'Environment & Ecology — The Green World',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Discuss weather systems, clean energy, waste management (recycling, carbon footprint), and climates.',
            "explanation": {
                "intro": 'Understand ecological discussions, environmental policies, and climate change vocabulary in English.',
                "sections": [
                    {
                        "title": 'Ecology & Waste Management',
                        "subsections": [
                            {
                                "title": 'Green Terms',
                                "layout": 'table',
                                "headers": ['Environmental Term', 'Pronunciation', 'Significance (Spanish)'],
                                "rows": [
                                    ['**Recycle**', '`/ˌriːˈsaɪ.kəl/`', 'Reciclar (Convert waste into reusable material)'],
                                    ['**Carbon footprint**', '`/ˈkɑː.bən ˈfʊt.prɪnt/`', 'Huella de carbono (Total greenhouse gas emissions)'],
                                    ['**Renewable energy**', '`/rɪˈnjuː.ə.bəl ˈɛn.ər.dʒi/`', 'Energía renovable (Wind, solar, hydro power)'],
                                    ['**Pollution**', '`/pəˈluː.ʃən/`', 'Contaminación (Harmful substances in nature)'],
                                    ['**Global warming**', '`/ˈɡloʊ.bəl ˈwɔː.mɪŋ/`', 'Calentamiento global (Increase in earth temperature)']
                                ]
                            },
                            {
                                "title": 'Climates & Eco Nouns',
                                "layout": 'table',
                                "headers": ['Climate Term', 'Pronunciation', 'Explanation'],
                                "rows": [
                                    ['**Drought**', '`/draʊt/`', 'Sequía (Long period with no rain)'],
                                    ['**Eco-friendly**', '`/ˌiː.koʊˈfrɛnd.li/`', 'Respetuoso con el medio ambiente (Not harmful to nature)'],
                                    ['**Biodiversity**', '`/ˌbaɪ.oʊ.daɪˈvɜːr.sə.ti/`', 'Biodiversidad (Variety of life in the world)'],
                                    ['**Fossil fuels**', '`/ˈfɒs.əl ˌfjuː.əlz/`', 'Combustibles fósiles (Coal, oil, natural gas)'],
                                    ['**Conservation**', '`/ˌkɒn.səˈveɪ.ʃən/`', 'Conservación (Protection of natural resources)']
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
                "phrase": 'Using solar panels can help reduce your carbon footprint.',
                "translation": 'El uso de paneles solares puede ayudar a reducir tu huella de carbono.',
                "ipa_notation": '/ˈjuːzɪŋ ˈsoʊlər ˈpænəlz kæn hɛlp rɪˈdjuːs jɔːr ˈkɑːrbən ˈfʊtprɪnt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'We should recycle paper and plastic to protect the environment.',
                "translation": 'Deberíamos reciclar el papel y el plástico para proteger el medio ambiente.',
                "ipa_notation": '/wiː ʃʊd ˌriːˈsaɪkəl ˈpeɪpər ænd ˈplæstɪk tuː prəˈtɛkt ði ɪnˈvaɪrənmənt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the English word for 'sequía'?",
                "correct_answer": "drought",
                "options": {
                    "a": "pollution",
                    "b": "drought",
                    "c": "conservation",
                    "d": "biodiversity"
                },
                "order_index": 1,
            }
        ]
    },
    {
        "level_code": 'B1',
        "meta": {
            "title": 'Entertainment & Media — Movies, Music & News',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn genres, media review words, news column titles, and journalism vocabulary.',
            "explanation": {
                "intro": 'Express your cultural opinions and read international news columns using accurate vocabulary.',
                "sections": [
                    {
                        "title": 'Entertainment Media',
                        "subsections": [
                            {
                                "title": 'Media Genres & Nouns',
                                "layout": 'table',
                                "headers": ['Term', 'Pronunciation', 'Significance'],
                                "rows": [
                                    ['**Genre**', '`/ˈʒɑːn.rə/`', 'Género (Category of art, music, or literature)'],
                                    ['**Documentary**', '`/ˌdɒk.jəˈmɛn.tər.i/`', 'Documental (Factual film or television program)'],
                                    ['**Journalist**', '`/ˈdʒɜː.nə.lɪst/`', 'Periodista (Person who writes news articles)'],
                                    ['**Headline**', '`/ˈhɛd.laɪn/`', 'Titular (Heading at the top of a newspaper page)'],
                                    ['**Broadcast**', '`/ˈbrɔːd.kɑːst/`', 'Emitir / Transmisión (Transmit a program on TV/radio)']
                                ]
                            },
                            {
                                "title": 'Opinion & Review Words',
                                "layout": 'table',
                                "headers": ['Adjective', 'Pronunciation', 'Translation'],
                                "rows": [
                                    ['**Entertaining**', '`/ˌɛn.təˈteɪ.nɪŋ/`', 'Entretenido'],
                                    ['**Boring**', '`/ˈbɔː.rɪŋ/`', 'Aburrido'],
                                    ['**Informative**', '`/ɪnˈfɔː.mə.tɪv/`', 'Informativo'],
                                    ['**Captivating**', '`/ˈkæp.tɪ.veɪ.tɪŋ/`', 'Cautivador'],
                                    ['**Predictable**', '`/prɪˈdɪk.tə.bəl/`', 'Predecible']
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
                "phrase": 'The journalist wrote a compelling article about the tech startup.',
                "translation": 'El periodista escribió un artículo convincente sobre la startup tecnológica.',
                "ipa_notation": '/ðə ˈdʒɜːrnəlɪst roʊt ə kəmˈpɛlɪŋ ˈɑːrtɪkəl əˈbaʊt ðə tɛk ˈstɑːrtʌp/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'I prefer reading the headlines online instead of buying a physical paper.',
                "translation": 'Prefiero leer los titulares en línea en lugar de comprar un periódico físico.',
                "ipa_notation": '/aɪ prɪˈfɜːr ˈriːdɪŋ ðə ˈhɛdlaɪnz ˈɒnˌlaɪn ɪnˈstɛd ɒv ˈbaɪɪŋ ə ˈfɪzɪkəl ˈpeɪpər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            }
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the word for a category of artistic composition, as in music or literature?",
                "correct_answer": "genre",
                "options": {
                    "a": "headline",
                    "b": "broadcast",
                    "c": "genre",
                    "d": "documentary"
                },
                "order_index": 1,
            }
        ]
    }
]
