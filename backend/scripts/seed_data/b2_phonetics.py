# b2_phonetics.py — B2 Phonetics lessons
# Foco en habla conectada avanzada y fluidez: elisión, chunking, prosodia y geminadas.
# Basado en Cambridge Pronunciation in Use (Upper-Intermediate) y norms del inglés americano/británico.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

B2_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: Elision ────────────────────────────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Elision — When Sounds Disappear",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to recognize and apply sound deletions in fast speech "
                "to understand native speakers and sound more natural."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The next deployment starts in the test environment.",
                "translation": "El siguiente despliegue comienza en el entorno de pruebas.",
                "ipa_notation": "/ðə nɛks dɪˈplɔɪmənt stɑːrts ɪn ðə tɛs ɪnˈvaɪrənmənt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Just delete the old branch and push the hotfix.",
                "translation": "Simplemente elimina la rama antigua y sube el hotfix.",
                "ipa_notation": "/dʒʌs dɪˈliːt ðə oʊl bræntʃ ænd pʊʃ ðə ˈhɒtfɪks/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Send the credentials before the next sprint planning.",
                "translation": "Envía las credenciales antes de la planificación del próximo sprint.",
                "ipa_notation": "/sɛn ðə krɪˈdɛnʃəlz bɪˈfɔːr ðə nɛks sprɪnt ˈplænɪŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                "phrase": "We must fix the last bug before the product launch.",
                "translation": "Debemos corregir el último error antes del lanzamiento del producto.",
                "ipa_notation": "/wiː mʌs fɪks ðə lɑːs bʌɡ bɪˈfɔːr ðə ˈprɒdʌk lɔːntʃ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "How is 'last commit' most likely pronounced by a native speaker "
                    "in natural fast speech? (Elision of /t/ before /k/)"
                ),
                "correct_answer": "/lɑːs kəˈmɪt/",
                "options": {
                    "a": "/læst kəˈmɪt/",
                    "b": "/lɑːs kəˈmɪt/",
                    "c": "/lɑːst kəˈmɪt/",
                    "d": "/læs kɒmɪt/",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Speaking in Chunks ─────────────────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Speaking in Chunks — Unlocking Natural Fluency",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master chunking to group words into meaningful units, "
                "improving your spoken rhythm and professional delivery."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "I need to review the pull request | before the standup | at ten o'clock.",
                "translation": "Necesito revisar el pull request | antes del standup | a las diez en punto.",
                "ipa_notation": "/aɪ niːd tə rɪˈvjuː ðə pʊl rɪˈkwɛst | bɪˈfɔːr ðə ˈstændʌp | æt tɛn əˈklɒk/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The function accepts two parameters: | a string | and an integer.",
                "translation": "La función acepta dos parámetros: | una cadena | y un entero.",
                "ipa_notation": "/ðə ˈfʌŋkʃən əkˈsɛpts tuː pəˈræmɪtərz | ə strɪŋ | ænd ən ˈɪntɪdʒər/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "If the tests pass | we can merge to main | and deploy to staging.",
                "translation": "Si las pruebas pasan | podemos hacer merge a main | y desplegar a staging.",
                "ipa_notation": "/ɪf ðə tɛsts pɑːs | wiː kən mɜːrdʒ tə meɪn | ænd dɪˈplɔɪ tə ˈsteɪdʒɪŋ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which chunked version of the sentence 'We should probably open a ticket "
                    "for this issue before the sprint ends' uses the most natural pause points?"
                ),
                "correct_answer": "We should probably open a ticket | for this issue | before the sprint ends.",
                "options": {
                    "a": "We should | probably open | a ticket for this | issue before | the sprint ends.",
                    "b": "We should probably open a ticket | for this issue | before the sprint ends.",
                    "c": "We | should probably | open | a ticket for | this issue before the sprint | ends.",
                    "d": "We should probably | open a ticket for this issue before | the sprint ends.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 3: Prosody ────────────────────────────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Prosody — The Rhythm, Stress, and Melody of English",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master English rhythm, nuclear stress, and intonation "
                "patterns to speak with clarity and emotional precision."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The bug was in the AUTH module, not in the payment service.",
                "translation": "El error estaba en el módulo de AUTH, no en el servicio de pagos.",
                "ipa_notation": "/ðə bʌɡ wɒz ɪn ðiː ˈɔːθ ˌmɒdjuːl | nɒt ɪn ðə ˈpeɪmənt ˈsɜːrvɪs↘/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The pipeline was green, but the deployment still failed.",
                "translation": "El pipeline estaba en verde, pero el despliegue aún así falló.",
                "ipa_notation": "/ðə ˈpaɪplaɪn wɒz ɡriːn↘↗ | bʌt ðə dɪˈplɔɪmənt stɪl feɪld↘/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "This is the most critical refactor we have ever shipped.",
                "translation": "Este es el refactor más crítico que hemos desplegado jamás.",
                "ipa_notation": "/ðɪs ɪz ðə moʊst ˈkrɪtɪkəl ˈriːfæktər wiː hæv ˈɛvər ʃɪpt↘/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "A colleague says: 'We fixed the latency, but not the memory issue.' "
                    "Which prosodic pattern on 'latency' and 'memory issue' best conveys "
                    "this contrast in natural spoken English?"
                ),
                "correct_answer": "Falling tone on 'latency', fall-rise on 'memory issue' to signal the contrast.",
                "options": {
                    "a": "Rising tone on both, to show uncertainty.",
                    "b": "Flat, even tone on all words to stay neutral.",
                    "c": "Falling tone on 'latency', fall-rise on 'memory issue' to signal the contrast.",
                    "d": "Nuclear stress on 'fixed', falling tone throughout.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 4: Geminates ───────────────────────────────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Geminates — Merging Twin Sounds",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to link adjacent identical consonants by prolonging "
                "the sound rather than repeating it between words."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "We ran a full load test to verify peak throughput.",
                "translation": "Ejecutamos una prueba de carga completa para verificar el throughput máximo.",
                "ipa_notation": "/wiː ræn ə ˈfʊlˑloʊd tɛst tə ˈvɛrɪfaɪ piːk ˈθruːpʊt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Push the git tag now so the release pipeline can start.",
                "translation": "Sube el git tag ahora para que el pipeline de release pueda comenzar.",
                "ipa_notation": "/pʊʃ ðə ˈɡɪtˑtæɡ naʊ soʊ ðə rɪˈliːs ˈpaɪplaɪn kæn stɑːrt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "The social login component handles third-party OAuth tokens.",
                "translation": "El componente de inicio de sesión social gestiona los tokens OAuth de terceros.",
                "ipa_notation": "/ðə ˈsoʊʃəlˑloʊɡɪn ˈkɒmpənənt ˈhændlz θɜːrd ˈpɑːrti ˈoʊɔːθ ˈtoʊkənz/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "In the phrase 'top performance', there is a geminate /p/ at the word boundary. "
                    "Which IPA transcription correctly represents it?"
                ),
                "correct_answer": "/tɒpˑpərˈfɔːrməns/",
                "options": {
                    "a": "/tɒp pərˈfɔːrməns/",
                    "b": "/tɒpˑpərˈfɔːrməns/",
                    "c": "/tɒ pərˈfɔːrməns/",
                    "d": "/tɒppərˈfɔːrməns/",
                },
                "order_index": 1,
            },
        ],
    },
]
