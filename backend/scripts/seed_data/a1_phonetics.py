# a1_phonetics.py — A1 Phonetics lessons
# Foundational IPA and phonetic awareness for A1 level.
# Cambridge Phonetics — International Phonetic Alphabet (IPA).
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

# ── Legacy single-dict used directly by seed.py for the TH lesson ────────────
PHONETICS: dict = {
    "meta": {
        "title": "The /θ/ and /ð/ Sounds — TH",
        "type": LessonType.PHONETICS,
        "category": LessonCategory.PHONETICS,
        "description": (
            "Master the voiceless /θ/ sound in think and the voiced /ð/ sound "
            "in this to elevate your English pronunciation."
        ),
        "order_index": 1,
        "is_published": True,
    },
    "examples": [
        {"phrase": "I think this is the right path.",             "translation": "Creo que este es el camino correcto.",         "ipa_notation": "/aɪ θɪŋk ðɪs ɪz ðə raɪt pæθ/",             "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
        {"phrase": "The weather there is breathtaking.",          "translation": "El clima allí es impresionante.",              "ipa_notation": "/ðə ˈweðər ðer ɪz ˈbreθˌteɪkɪŋ/",          "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
        {"phrase": "Thank the author for their thoughtful work.", "translation": "Agradece al autor por su reflexivo trabajo.", "ipa_notation": "/θæŋk ðə ˈɔːθər fər ðer ˈθɔːtfəl wɜːrk/",  "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
    ],
    "exercises": [
        {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which word contains the VOICELESS /θ/ sound (as in 'think')?",     "correct_answer": "tooth",   "options": {"a": "this", "b": "those", "c": "tooth", "d": "breathe"}, "order_index": 1},
        {"type": ExerciseType.FILL_BLANK,      "question": "Complete the IPA transcription for 'think': /______ɪŋk/",          "correct_answer": "θ",       "options": None,                                                       "order_index": 2},
        {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which word contains the VOICED /ð/ sound (as in 'this')?",        "correct_answer": "breathe", "options": {"a": "think", "b": "tooth", "c": "breathe", "d": "path"},  "order_index": 3},
        {"type": ExerciseType.PRONUNCIATION,   "question": "Record yourself saying: 'The father thinks about three things.'", "correct_answer": "/ðə ˈfɑːðər θɪŋks əˈbaʊt θriː θɪŋz/",    "options": None,                                                       "order_index": 4},
    ],
}

# ── A1 Phonetics lesson list (processed via ALL_LESSONS in seed.py) ──────────
A1_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: Introduction to the IPA ────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Introduction to the IPA — Your Pronunciation Map",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to decode the International Phonetic Alphabet (IPA) "
                "and master word stress to read pronunciation keys."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Salad",    "translation": "Ensalada",           "ipa_notation": "/ˈsæləd/",    "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "Function", "translation": "Función",            "ipa_notation": "/ˈfʌŋkʃən/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "Enough",   "translation": "Suficiente",         "ipa_notation": "/ɪˈnʌf/",    "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "In the IPA transcription /ˈsæləd/, what does the symbol ˈ mean?", "correct_answer": "Stress — say that syllable louder and higher.", "options": {"a": "Pause between syllables.", "b": "Stress — say that syllable louder and higher.", "c": "The syllable is silent.", "d": "The word has two different meanings."}, "order_index": 1},
        ],
    },
    # ── Lesson 2: The Schwa /ə/ ───────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "The Schwa Sound /ə/ — The Most Common English Sound",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the schwa /ə/, the most common and relaxed vowel "
                "sound in English, to instantly speak more naturally."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {"phrase": "about",    "translation": "acerca de / sobre",       "ipa_notation": "/əˈbaʊt/",      "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "teacher",  "translation": "maestro / maestra",       "ipa_notation": "/ˈtiːtʃər/",   "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "computer", "translation": "computadora / ordenador", "ipa_notation": "/kəmˈpjuːtər/","sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK, "question": "The IPA symbol for the relaxed, neutral vowel found only in unstressed syllables — the schwa — is: /______/", "correct_answer": "ə", "options": None, "order_index": 1},
        ],
    },
    # ── Lesson 3: Short /ɪ/ vs. Long /iː/ ────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Short /ɪ/ vs. Long /iː/ — Sit vs. Seat",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to distinguish short /ɪ/ from long /iː/ in words "
                "like git and release to avoid common pronunciation errors."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Sit — Seat",   "translation": "Sentarse — Asiento",   "ipa_notation": "/sɪt/ — /siːt/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "Hit — Heat",   "translation": "Golpear — Calor",      "ipa_notation": "/hɪt/ — /hiːt/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "Live — Leave", "translation": "Vivir — Irse / Salir", "ipa_notation": "/lɪv/ — /liːv/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Which word contains the LONG /iː/ sound (as in 'seat')?", "correct_answer": "release", "options": {"a": "bit", "b": "git", "c": "release", "d": "fix"}, "order_index": 1},
        ],
    },
    # ── Lesson 4: Explosive Plosives /p/ /t/ /k/ ─────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "Explosive Plosives — The /p/, /t/, and /k/ Sounds",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the aspiration and air release of English plosives "
                "like p, t, and k to speak with clear articulation."
            ),
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Push the code to production.",         "translation": "Sube el código a producción.",            "ipa_notation": "/pʊʃ ðə koʊd tə prəˈdʌkʃən/",          "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "Take time to test the pipeline.",      "translation": "Tómate tiempo para probar el pipeline.",   "ipa_notation": "/teɪk taɪm tə tɛst ðə ˈpaɪplaɪn/",     "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "Compile, commit, and keep iterating.", "translation": "Compila, haz commit y sigue iterando.",   "ipa_notation": "/kəmˈpaɪl kəˈmɪt ænd kiːp ˈɪtəreɪtɪŋ/","sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "In English, /p/, /t/, /k/ at the start of a stressed syllable are 'aspirated'. What does this mean?", "correct_answer": "A small burst of air follows the consonant.", "options": {"a": "The consonant is silent.", "b": "A small burst of air follows the consonant.", "c": "You hold your breath before the sound.", "d": "The following vowel is always long."}, "order_index": 1},
        ],
    },
    # ── Lesson 5: The Aspirated /h/ ───────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "The Aspirated /h/ — Pure Air Friction",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to produce the relaxed, unvoiced aspirated /h/ sound "
                "smoothly without Spanish throat tension."
            ),
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Hello, I am having trouble with this bug.",     "translation": "Hola, tengo problemas con este error.",             "ipa_notation": "/həˈloʊ aɪ æm ˈhævɪŋ ˈtrʌbəl wɪð ðɪs bʌɡ/",        "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "The server is hosted on our hybrid cloud.",     "translation": "El servidor está alojado en nuestra nube híbrida.", "ipa_notation": "/ðə ˈsɜːrvər ɪz ˈhoʊstɪd ɒn ˈaʊər ˈhaɪbrɪd klaʊd/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "How many hours did you spend on this feature?", "translation": "¿Cuántas horas dedicaste a esta funcionalidad?",   "ipa_notation": "/haʊ ˈmɛni ˈaʊərz dɪd juː spɛnd ɒn ðɪs ˈfiːtʃər/",  "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "The English /h/ in 'hello' and 'house' is best described as:", "correct_answer": "A relaxed, gentle rush of air with no throat tension.", "options": {"a": "A guttural, raspy sound similar to the Spanish 'J'.", "b": "A relaxed, gentle rush of air with no throat tension.", "c": "A silent letter, as in 'hour'.", "d": "A nasal sound produced at the back of the mouth."}, "order_index": 1},
        ],
    },
    # ── Lesson 6: The Final /m/ ───────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "The Final /m/ — Closing Your Lips",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Perfect your pronunciation of words ending in m by closing "
                "your lips completely to sound natural."
            ),
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {"phrase": "What is your name and your team?",               "translation": "¿Cuál es tu nombre y tu equipo?",               "ipa_notation": "/wɒt ɪz jɔːr neɪm ænd jɔːr tiːm/",               "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "The program takes time to run.",                 "translation": "El programa tarda tiempo en ejecutarse.",        "ipa_notation": "/ðə ˈproʊɡræm teɪks taɪm tə rʌn/",               "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "Sometimes the algorithm finds a better path.",   "translation": "A veces el algoritmo encuentra un camino mejor.", "ipa_notation": "/ˈsʌmtaɪmz ðiː ˈælɡərɪðəm faɪndz ə ˈbɛtər pæθ/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.FILL_BLANK, "question": "Complete the IPA transcription for 'team': /tiː______/", "correct_answer": "m", "options": None, "order_index": 1},
        ],
    },
    # ── Lesson 7: The -ed Endings ─────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": "The -ed Endings — /t/, /d/, and /ɪd/",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the three pronunciations of regular past simple -ed endings: /t/, /d/, and /ɪd/."
            ),
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {"phrase": "She worked on the API all morning. (worked → /t/)",      "translation": "Ella trabajó en la API toda la mañana. (-ed = /t/ seco)",             "ipa_notation": "/ʃiː wɜːrkt ɒn ðiː ˌeɪpiːˈaɪ ɔːl ˈmɔːrnɪŋ/",          "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "He played the demo video for the client. (played → /d/)", "translation": "Él mostró el vídeo demo al cliente. (-ed = /d/ suave)",              "ipa_notation": "/hiː pleɪd ðə ˈdɛmoʊ ˈvɪdioʊ fər ðə ˈklaɪənt/",        "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "The server wanted more memory. (wanted → /ɪd/)",          "translation": "El servidor necesitaba más memoria. (-ed = /ɪd/ sílaba extra)",      "ipa_notation": "/ðə ˈsɜːrvər ˈwɒntɪd mɔːr ˈmɛməri/",                    "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "How is the '-ed' suffix pronounced in 'started'?", "correct_answer": "/ɪd/ — it adds an extra syllable.", "options": {"a": "/t/ — a dry, unvoiced ending.", "b": "/d/ — a soft, voiced ending.", "c": "/ɪd/ — it adds an extra syllable.", "d": "The '-ed' is completely silent."}, "order_index": 1},
        ],
    },
    # ── Lesson 8: The Dark L ──────────────────────────────────────────────────
    {
        "level_code": "A1",
        "meta": {
            "title": 'The "Dark L" — Pronouncing L after a Vowel',
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the deep, resonant Dark L sound used after vowels in words like call, tool, and full."
            ),
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Please call the backend team.",          "translation": "Por favor llama al equipo de backend.",     "ipa_notation": "/pliːz kɔːl ðə ˈbækˌɛnd tiːm/",         "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 1},
            {"phrase": "This tool is cool and very useful.",    "translation": "Esta herramienta es genial y muy útil.",    "ipa_notation": "/ðɪs tuːl ɪz kuːl ænd ˈvɛri ˈjuːsfəl/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 2},
            {"phrase": "Pull the full version from the remote.", "translation": "Descarga la versión completa del remoto.", "ipa_notation": "/pʊl ðə fʊl ˈvɜːrʒən frɒm ðə rɪˈmoʊt/", "sentence_type": SentenceType.AFFIRMATIVE, "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "In which word does the DARK L (ɫ) appear?", "correct_answer": "call", "options": {"a": "light", "b": "level", "c": "launch", "d": "call"}, "order_index": 1},
        ],
    },
]

