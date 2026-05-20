# b1_phonetics.py — B1 Phonetics lessons
# Foco en habla conectada y ritmo: weak forms, word stress en pares noun/verb,
# linking consonant-to-vowel, y asimilación fonética.
# Basado en Cambridge Pronunciation in Use (Intermediate) y norms del inglés americano/británico.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B1_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: Sentence Rhythm & Weak Forms ───────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Sentence Rhythm & Weak Forms — The English Beat",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Understand English stress-timed rhythm by mastering content "
                "words and weak forms to improve your listening and speaking speed."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "We need to send the file to the server before the meeting.",
                "translation": "Necesitamos enviar el archivo al servidor antes de la reunión.",
                "ipa_notation": "/wiː niːd tə sɛnd ðə faɪl tə ðə ˈsɜːrvər bɪˈfɔːr ðə ˈmiːtɪŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Can you check the logs and tell me what went wrong?",
                "translation": "¿Puedes revisar los registros y decirme qué salió mal?",
                "ipa_notation": "/kən jə tʃɛk ðə lɒɡz ən tɛl miː wɒt wɛnt rɒŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "She has been working on a new feature for the past week.",
                "translation": "Ella ha estado trabajando en una nueva funcionalidad durante la semana pasada.",
                "ipa_notation": "/ʃiː həz bɪn ˈwɜːrkɪŋ ɒn ə njuː ˈfiːtʃər fər ðə pæst wiːk/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "In the sentence 'She can send the report to the team', which words are most likely "
                    "pronounced with a weak/reduced vowel?"
                ),
                "correct_answer": "can, the, to, the",
                "options": {
                    "a": "she, report, team",
                    "b": "can, the, to, the",
                    "c": "send, report",
                    "d": "all words are equally stressed",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "The function word 'and' is usually reduced to /___/ in natural connected speech, "
                    "as in 'black and white' → /blæk ən waɪt/."
                ),
                "correct_answer": "ən",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 2: Word Stress — Nouns vs. Verbs ──────────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Word Stress: Nouns vs. Verbs — Changing the Meaning",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn how shifting word stress in two-syllable words like "
                "export and record changes their meaning and grammatical function."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": (
                    "The export (/ˈɛkspɔːrt/) figures are up. "
                    "We export (/ɪkˈspɔːrt/) 40% of our output."
                ),
                "translation": (
                    "Las cifras de exportación han subido. "
                    "Exportamos el 40% de nuestra producción."
                ),
                "ipa_notation": "/ðə ˈɛkspɔːrt ˈfɪɡjərz ɑːr ʌp | wiː ɪkˈspɔːrt ˈfɔːrti pɜːrsɛnt əv ˈaʊər ˈaʊtpʊt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": (
                    "Please check the record (/ˈrɛkərd/). "
                    "The team will record (/rɪˈkɔːrd/) the session live."
                ),
                "translation": (
                    "Por favor revisa el registro. "
                    "El equipo grabará la sesión en vivo."
                ),
                "ipa_notation": "/ˈpliːz tʃɛk ðə ˈrɛkərd | ðə tiːm wɪl rɪˈkɔːrd ðə ˈsɛʃən laɪv/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": (
                    "You need a permit (/ˈpɜːrmɪt/) to deploy. "
                    "Will the system permit (/pərˈmɪt/) that action?"
                ),
                "translation": (
                    "Necesitas un permiso para desplegar. "
                    "¿Permitirá el sistema esa acción?"
                ),
                "ipa_notation": "/juː niːd ə ˈpɜːrmɪt tə dɪˈplɔɪ | wɪl ðə ˈsɪstəm pərˈmɪt ðæt ˈækʃən/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "In the sentence 'We need to update the database', 'update' is functioning as a "
                    "VERB. Which IPA transcription is correct?"
                ),
                "correct_answer": "/ʌpˈdeɪt/",
                "options": {
                    "a": "/ˈʌpdeɪt/",
                    "b": "/ʌpˈdeɪt/",
                    "c": "/ˈʌpdɛt/",
                    "d": "/ʌpˈdɛt/",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "The word 'import' as a NOUN is stressed on the ___ syllable, "
                    "so its IPA stress mark appears as /ˈɪmpɔːrt/. (Write: first / second)"
                ),
                "correct_answer": "first",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 3: Linking Sounds — Consonant to Vowel ────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Linking Sounds — Connecting Consonants to Vowels",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Connect consonant endings to vowel beginnings in words "
                "like turn it off to speak English smoothly and naturally."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Turn it off and check it out — it worked on my machine.",
                "translation": "Apágalo y compruébalo — funcionó en mi máquina.",
                "ipa_notation": "/ˈtɜːrnɪtɒf ən ˈtʃɛkɪtaʊt | ɪt ˈwɜːrktɒn maɪ məˈʃiːn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Pick it up, log it out, and set it up again.",
                "translation": "Recógelo, cierra sesión y vuelve a configurarlo.",
                "ipa_notation": "/ˈpɪkɪtʌp | ˈlɒɡɪtaʊt | ænd ˈsɛtɪtʌp əˈɡɛn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Go out and ask an engineer about it.",
                "translation": "Ve afuera y pregúntale a un ingeniero al respecto.",
                "ipa_notation": "/ɡoʊwaʊt ən æsk ən ˌɛndʒɪˈnɪər əˈbaʊtɪt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": "We looked at all available options and ran a quick test.",
                "translation": "Revisamos todas las opciones disponibles y corrimos una prueba rápida.",
                "ipa_notation": "/wiː ˈlʊktæt ɔːl əˈveɪləbl ˈɒpʃənz ən ræn ə kwɪk tɛst/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which IPA transcription best reflects natural linking in 'check it out'?"
                ),
                "correct_answer": "/ˈtʃɛkɪtaʊt/",
                "options": {
                    "a": "/tʃɛk ɪt aʊt/",
                    "b": "/ˈtʃɛkɪtaʊt/",
                    "c": "/tʃɛk ɪˈtaʊt/",
                    "d": "/ˈtʃɛk.ɪt.aʊt/",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "When a word ends in the vowel /uː/ and the next word starts with a vowel, "
                    "native speakers often insert an intrusive /___/ sound to link them smoothly "
                    "(e.g., 'go out' → 'go-w-out')."
                ),
                "correct_answer": "w",
                "options": None,
                "order_index": 2,
            },
        ],
    },
    # ── Lesson 4: Assimilation — When Sounds Change ──────────────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Assimilation — When Sounds Change Each Other",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Discover how native speakers blend and change adjacent sounds "
                "in fast speech for efficient, seamless pronunciation."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Green Park station is closed — ten cases of delay reported.",
                "translation": "La estación Green Park está cerrada — se reportaron diez casos de retraso.",
                "ipa_notation": "/ˈɡriːm pɑːrk ˈsteɪʃən ɪz kloʊzd | tɛŋ ˈkeɪsɪz əv dɪˈleɪ rɪˈpɔːrtɪd/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Would you check the handbag scanner before good morning briefing?",
                "translation": "¿Revisarías el escáner de bolsos antes del briefing de buenos días?",
                "ipa_notation": "/wʊdʒuː tʃɛk ðə ˈhæmbæɡ ˈskænər bɪˈfɔːr ˈɡuːm ˈmɔːrnɪŋ ˈbriːfɪŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Did you merge the branch? That person said it was already done.",
                "translation": "¿Hiciste el merge de la rama? Esa persona dijo que ya estaba hecho.",
                "ipa_notation": "/dɪdʒuː mɜːrdʒ ðə bræntʃ | ðæp ˈpɜːrsən sɛd ɪt wɒz ɔːlˈrɛdi dʌn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "In natural fast speech, 'did you' /dɪd juː/ undergoes coalescent assimilation "
                    "and is pronounced as:"
                ),
                "correct_answer": "/dɪdʒuː/",
                "options": {
                    "a": "/dɪd juː/",
                    "b": "/dɪdʒuː/",
                    "c": "/dɪʃuː/",
                    "d": "/dɪdjuː/",
                },
                "order_index": 1,
            },
            {
                "type": ExerciseType.FILL_BLANK,
                "question": (
                    "The phrase 'good morning' in rapid natural speech often assimilates to "
                    "/ɡu___ ˈmɔːrnɪŋ/ because the /d/ adapts to the following bilabial /m/. "
                    "Fill in the missing IPA symbol."
                ),
                "correct_answer": "m",
                "options": None,
                "order_index": 2,
            },
        ],
    },
]
