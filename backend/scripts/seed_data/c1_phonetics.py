# c1_phonetics.py — C1 Phonetics lessons
# Foco en prosodia avanzada y asimilación extrema en habla rápida y natural.
# Basado en Cambridge Pronunciation in Use (Advanced, Hewings) e IPA americano.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C1_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: Advanced Prosody — Intonation for Meaning ──────────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Advanced Prosody — Intonation for Meaning",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn how shifting nuclear stress and intonation completely "
                "changes the implied meaning of your sentences."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                # Nuclear stress en READY → declaración de hecho: el deploy no está listo.
                "phrase": "I didn't say the deploy was READY. ↘",
                "translation": "Yo no dije que el despliegue estuviera listo. (declaración directa, caída definitiva)",
                "ipa_notation": "/aɪ ˈdɪdnt seɪ ðə dɪˈplɔɪ wəz ˈrɛdi ↘/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                # Nuclear stress en SAY → implicación: lo sugerí, no lo dije — fall-rise.
                "phrase": "I didn't SAY the deploy was ready. ↘↗",
                "translation": "Yo no DIJE que el despliegue estuviera listo. (implicación: quizás lo sugerí)",
                "ipa_notation": "/aɪ dɪdnt ˈseɪ ðə dɪˈplɔɪ wəz rɛdi ↘↗/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                # Nuclear stress en THE → contraste con otro deploy; rise indica pregunta implícita.
                "phrase": "I didn't say THE deploy was ready. ↗",
                "translation": "Yo no dije que ESE despliegue estuviera listo. (contraste: hay otros deploys)",
                "ipa_notation": "/aɪ dɪdnt seɪ ðiː dɪˈplɔɪ wəz rɛdi ↗/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "A developer says: 'I didn't say the TESTS were passing ↘↗'. "
                    "What is the most likely implied meaning of this utterance?"
                ),
                "correct_answer": (
                    "The developer implied it but did not state it explicitly — "
                    "perhaps through a gesture or a previous comment."
                ),
                "options": {
                    "a": "The developer is certain the tests are passing.",
                    "b": (
                        "The developer implied it but did not state it explicitly — "
                        "perhaps through a gesture or a previous comment."
                    ),
                    "c": "The developer is asking whether the tests are passing.",
                    "d": "The developer is contrasting these tests with other tests.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Advanced Assimilation — Sound Blending /t/+/j/ and /d/+/j/ ─
    {
        "level_code": "C1",
        "meta": {
            "title": "Advanced Assimilation — Sound Blending (/t/+/j/ → /tʃ/, /d/+/j/ → /dʒ/)",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master coalescent assimilation to blend sounds like t and d "
                "with y for fast, fluent, and native-like speech."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                # /t/ + /j/ → /tʃ/: "Don't you" → /doʊntʃuː/
                "phrase": "Don't you think we should refactor this module before the sprint ends?",
                "translation": "¿No crees que deberíamos refactorizar este módulo antes de que termine el sprint?",
                "ipa_notation": "/ˈdoʊntʃuː θɪŋk wiː ʃʊd ˌriːˈfæktər ðɪs ˈmɒdjuːl bɪˈfɔːr ðə sprɪnt ɛndz/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                # /d/ + /j/ → /dʒ/: "Could you" → /kʊdʒuː/
                "phrase": "Could you review my pull request before the standup?",
                "translation": "¿Podrías revisar mi pull request antes del standup?",
                "ipa_notation": "/ˈkʊdʒuː rɪˈvjuː maɪ pʊl rɪˈkwɛst bɪˈfɔːr ðə ˈstændʌp/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                # /d/ + /j/ → /dʒ/: "Would you" → /wʊdʒuː/
                "phrase": "Would you be able to deploy the fix to staging this afternoon?",
                "translation": "¿Podrías desplegar el arreglo al entorno de staging esta tarde?",
                "ipa_notation": "/ˈwʊdʒuː biː ˈeɪbəl tə dɪˈplɔɪ ðə fɪks tə ˈsteɪdʒɪŋ ðɪs ˌæftərˈnuːn/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                # /d/ + /j/ → /dʒ/: "Did you" → /dɪdʒuː/
                "phrase": "Did you push the latest changes to the feature branch?",
                "translation": "¿Hiciste push de los últimos cambios a la rama de la funcionalidad?",
                "ipa_notation": "/ˈdɪdʒuː pʊʃ ðə ˈleɪtɪst ˈtʃeɪndʒɪz tə ðə ˈfiːtʃər bræntʃ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "A native speaker says /ˈwʊdʒuː ˈoʊpən ə pʊl rɪˈkwɛst/. "
                    "Which written sentence does this correspond to?"
                ),
                "correct_answer": "Would you open a pull request?",
                "options": {
                    "a": "Could you open a pull request?",
                    "b": "Would you open a pull request?",
                    "c": "Did you open a pull request?",
                    "d": "Don't you open a pull request?",
                },
                "order_index": 1,
            },
        ],
    },
]
