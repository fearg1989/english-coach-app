# a2_phonetics.py — A2 Phonetics lessons
# Intermediate phonetic awareness: consonant contrasts, diphthongs, silent letters, and the Flap T.
# Based on Cambridge Phonetics and American English pronunciation norms.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A2_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: /v/ vs /b/ ─────────────────────────────────────────────────
    {
        "level_code": "A2",
        "meta": {
            "title": "The /v/ vs /b/ Sounds — Bites and Vibrations",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the distinction between bilabial /b/ and vibrated "
                "labiodental /v/ sounds to speak English clearly."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The backend developer built a very robust validation library.",
                "translation": "El desarrollador de backend construyó una librería de validación muy robusta.",
                "ipa_notation": "/ðə ˈbækɛnd dɪˈvɛləpər bɪlt ə ˈvɛri roʊˈbʌst ˌvælɪˈdeɪʃən ˈlaɪbrəri/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Please verify the binary version before you build and deploy.",
                "translation": "Por favor verifica la versión binaria antes de compilar y desplegar.",
                "ipa_notation": "/ˈpliːz ˈvɛrɪfaɪ ðə ˈbaɪnəri ˈvɜːrʒən bɪˈfɔːr juː bɪld ænd dɪˈplɔɪ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "We believe the verbose logging broke the build process.",
                "translation": "Creemos que el registro verboso rompió el proceso de compilación.",
                "ipa_notation": "/wiː bɪˈliːv ðə vɜːrˈboʊs ˈlɒɡɪŋ broʊk ðə bɪld ˈproʊsɛs/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which word contains the labiodental /v/ sound (upper teeth touching lower lip)?",
                "correct_answer": "verbose",
                "options": {"a": "build", "b": "batch", "c": "verbose", "d": "blob"},
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: /oʊ/ and /aʊ/ diphthongs ──────────────────────────────────
    {
        "level_code": "A2",
        "meta": {
            "title": "The 'Code' /oʊ/ and the 'Cloud' /aʊ/ — Two Key Diphthongs",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master /oʊ/ and /aʊ/ diphthongs in words like code and "
                "cloud to elevate your technical pronunciation."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Open the remote node and load the component.",
                "translation": "Abre el nodo remoto y carga el componente.",
                "ipa_notation": "/ˈoʊpən ðə rɪˈmoʊt noʊd ænd loʊd ðə kəmˈpoʊnənt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The cloud service is down and the output count is wrong.",
                "translation": "El servicio en la nube está caído y el conteo de salida es incorrecto.",
                "ipa_notation": "/ðə klaʊd ˈsɜːrvɪs ɪz daʊn ænd ðə ˈaʊtpʊt kaʊnt ɪz rɒŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "We scrolled through the code to find the broken flow.",
                "translation": "Desplazamos el código para encontrar el flujo roto.",
                "ipa_notation": "/wiː skroʊld θruː ðə koʊd tə faɪnd ðə ˈbroʊkən floʊ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": "Download the update now from our local host.",
                "translation": "Descarga la actualización ahora desde nuestro host local.",
                "ipa_notation": "/ˈdaʊnloʊd ðə ˈʌpdeɪt naʊ frɒm aʊər ˈloʊkəl hoʊst/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which word contains the /aʊ/ diphthong (as in 'cow' — open jaw then round lips)?",
                "correct_answer": "cloud",
                "options": {"a": "code", "b": "node", "c": "cloud", "d": "scope"},
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 3: /ʃ/ vs /tʃ/ ────────────────────────────────────────────────
    {
        "level_code": "A2",
        "meta": {
            "title": "The /ʃ/ vs /tʃ/ Sounds — 'Sh' vs 'Ch'",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn the critical contrast between smooth /ʃ/ and "
                "explosive /tʃ/ sounds in words like cache and patch."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Flush the cache before you fetch the latest version from the repository.",
                "translation": "Vacía la caché antes de obtener la última versión del repositorio.",
                "ipa_notation": "/flʌʃ ðə kæʃ bɪˈfɔːr juː fɛtʃ ðə ˈleɪtɪst ˈvɜːrʒən frɒm ðə rɪˈpɒzɪtɔːri/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "She chose to chunk the data and ship it in smaller batches.",
                "translation": "Ella decidió dividir en fragmentos los datos y enviarlos en lotes más pequeños.",
                "ipa_notation": "/ʃiː tʃoʊz tə tʃʌŋk ðə ˈdeɪtə ænd ʃɪp ɪt ɪn ˈsmɔːlər ˈbætʃɪz/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Switch off the feature flag and push a fresh patch to production.",
                "translation": "Desactiva el feature flag y sube un parche nuevo a producción.",
                "ipa_notation": "/swɪtʃ ɒf ðə ˈfiːtʃər flæɡ ænd pʊʃ ə frɛʃ pætʃ tə prəˈdʌkʃən/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which word contains the smooth, continuous /ʃ/ sound (as in 'she' — no burst)?",
                "correct_answer": "cache",
                "options": {"a": "fetch", "b": "cache", "c": "chunk", "d": "watch"},
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 4: Silent Letters ──────────────────────────────────────────────
    {
        "level_code": "A2",
        "meta": {
            "title": "Beware of Silent Letters — Words That Trick the Eye",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master spelling-to-sound traps by identifying silent "
                "letters in words like debt, doubt, and write."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "I should walk to the office — it is only half a mile.",
                "translation": "Debería ir caminando a la oficina — solo es media milla.",
                "ipa_notation": "/aɪ ʃʊd wɔːk tə ðə ˈɒfɪs — ɪt ɪz ˈoʊnli hɑːf ə maɪl/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "There is no doubt that the legacy code has a subtle bug.",
                "translation": "No hay duda de que el código heredado tiene un error sutil.",
                "ipa_notation": "/ðɛr ɪz noʊ daʊt ðæt ðə ˈlɛɡəsi koʊd hæz ə ˈsʌtl bʌɡ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "The team talked calmly about the technical debt in the sprint.",
                "translation": "El equipo habló con calma sobre la deuda técnica en el sprint.",
                "ipa_notation": "/ðə tiːm tɔːkt ˈkɑːmli əˈbaʊt ðə ˈtɛknɪkəl dɛt ɪn ðə sprɪnt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": "The dumb algorithm doubled the processing time — a costly design flaw.",
                "translation": "El algoritmo torpe duplicó el tiempo de procesamiento — un defecto de diseño costoso.",
                "ipa_notation": "/ðə dʌm ˈælɡərɪðəm ˈdʌbəld ðə ˈproʊsɛsɪŋ taɪm — ə ˈkɒstli dɪˈzaɪn flɔː/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "In which word is the letter 'b' COMPLETELY SILENT?",
                "correct_answer": "debt",
                "options": {"a": "blob", "b": "binary", "c": "debug", "d": "debt"},
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 5: American Flap T /ɾ/ ────────────────────────────────────────
    {
        "level_code": "A2",
        "meta": {
            "title": "The American Flap T /ɾ/ — Sounding Like a Native",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn the American Flap T sound in water and data using a "
                "quick tongue tap to sound completely natural."
            ),
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The water cooling system keeps the server temperature stable.",
                "translation": "El sistema de refrigeración por agua mantiene la temperatura del servidor estable.",
                "ipa_notation": "/ðə ˈwɔːɾər ˈkuːlɪŋ ˈsɪstəm kiːps ðə ˈsɜːrvər ˈtɛmprɪtʃər ˈsteɪbəl/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Store the data in a structured database before the migration.",
                "translation": "Almacena los datos en una base de datos estructurada antes de la migración.",
                "ipa_notation": "/stɔːr ðə ˈdeɪɾə ɪn ə ˈstrʌktʃərd ˈdeɪɾəbeɪs bɪˈfɔːr ðə maɪˈɡreɪʃən/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Our new testing framework runs even better than the old one.",
                "translation": "Nuestro nuevo framework de pruebas funciona incluso mejor que el antiguo.",
                "ipa_notation": "/aʊər njuː ˈtɛstɪŋ ˈfreɪmwɜːrk rʌnz ˈiːvən ˈbɛɾər ðæn ðə oʊld wʌn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": "The computer processes each request using the automated iterator.",
                "translation": "El ordenador procesa cada solicitud usando el iterador automatizado.",
                "ipa_notation": "/ðə kəmˈpjuːɾər ˈproʊsɛsɪz iːtʃ rɪˈkwɛst ˈjuːzɪŋ ðə ˈɔːɾəmeɪɾɪd ˈɪɾəreɪɾər/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "In American English, how is the word 'better' correctly pronounced?",
                "correct_answer": "/ˈbɛɾər/ — soft flap, like the Spanish 'r' in 'pero'",
                "options": {
                    "a": "/ˈbɛtər/ — hard British T sound",
                    "b": "/ˈbɛɾər/ — soft flap, like the Spanish 'r' in 'pero'",
                    "c": "/ˈbɛθər/ — TH sound as in 'think'",
                    "d": "/ˈbɛdər/ — voiced D sound",
                },
                "order_index": 1,
            },
        ],
    },
]
