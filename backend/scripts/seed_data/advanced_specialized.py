# advanced_specialized.py — Lecciones especializadas transversales
# Cubre temas que no pertenecen a un único nivel CEFR: B1, B2, C1.
# Referencia: Cambridge Grammar in Use (Murphy/Hewings) + IT professional context.
# NOTE: sys.path es configurado por seed.py antes de importar este módulo.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

ADVANCED_SPECIALIZED_LESSONS: list[dict] = [
    # ── Lesson 1: Verb Patterns — Gerunds & Infinitives (B1) ─────────────────
    {
        "level_code": "B1",
        "meta": {
            "title": "Verb Patterns — Gerunds & Infinitives",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_PATTERNS,
            "description": (
                "Master the rules of using gerunds (-ing) and infinitives "
                "(to + verb) after specific verbs to sound completely natural."
            ),
            "order_index": 20,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "I recommend considering a microservices architecture for this use case.",
                "translation": "Recomiendo considerar una arquitectura de microservicios para este caso de uso.",
                "ipa_notation": "/aɪ ˌrɛkəˈmɛnd kənˈsɪdərɪŋ ə ˈmaɪkroʊˌsɜːrvɪsɪz ˈɑːrkɪtɛktʃər fər ðɪs juːs keɪs/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "We cannot afford to neglect the security requirements in this release.",
                "translation": "No podemos permitirnos descuidar los requisitos de seguridad en esta versión.",
                "ipa_notation": "/wiː kænɒt əˈfɔːrd tə nɪˈɡlɛkt ðə sɪˈkjʊərɪti rɪˈkwaɪərments ɪn ðɪs rɪˈliːs/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Did you manage to resolve the dependency conflict before the deployment?",
                "translation": "¿Lograste resolver el conflicto de dependencias antes del despliegue?",
                "ipa_notation": "/dɪd juː ˈmænɪdʒ tə rɪˈzɒlv ðə dɪˈpɛndənsi ˈkɒnflɪkt bɪˈfɔːr ðə dɪˈplɔɪmənt/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Choose the correct verb pattern: 'I avoid ______ secrets directly in the source code.'",
                "correct_answer": "hardcoding",
                "options": {
                    "a": "to hardcode",
                    "b": "hardcoding",
                    "c": "hardcoded",
                    "d": "to hardcoding",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Discourse Markers & Connectors (B2) ─────────────────────────
    {
        "level_code": "B2",
        "meta": {
            "title": "Discourse Markers & Connectors — Linking Ideas",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.CONNECTORS,
            "description": (
                "Learn to link ideas and clarify technical arguments using "
                "formal connectors for contrast, consequence, and concession."
            ),
            "order_index": 20,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The new caching layer reduced latency; furthermore, it significantly decreased the database load.",
                "translation": "La nueva capa de caché redujo la latencia; además, disminuyó significativamente la carga de la base de datos.",
                "ipa_notation": "/ðə njuː ˈkæʃɪŋ ˈleɪər rɪˈdjuːst ˈleɪtənsi | ˈfɜːðəmɔːr ɪt sɪɡˈnɪfɪkəntli dɪˈkriːst ðə ˈdeɪtəbeɪs loʊd/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The architecture is scalable; however, it does not eliminate the single point of failure.",
                "translation": "La arquitectura es escalable; sin embargo, no elimina el punto único de fallo.",
                "ipa_notation": "/ðiː ˈɑːrkɪtɛktʃər ɪz ˈskeɪləbəl | haʊˈɛvər ɪt dʌz nɒt ɪˈlɪmɪneɪt ðə ˈsɪŋɡəl pɔɪnt əv ˈfeɪljər/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Does the proposed refactor improve readability, or does it, on the other hand, introduce unnecessary complexity?",
                "translation": "¿La refactorización propuesta mejora la legibilidad, o, por otro lado, introduce complejidad innecesaria?",
                "ipa_notation": "/dʌz ðə prəˈpoʊzd ˌriːˈfæktər ɪmˈpruːv ˌriːdəˈbɪlɪti | ɔːr dʌz ɪt | ɒn ðiː ˈʌðər hænd | ɪntrəˈdjuːs ʌnˈnɛsəsɛri kəmˈplɛksɪti/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Choose the best connector: 'The feature was approved; ______, the team was unable to deliver it within the sprint.'",
                "correct_answer": "nevertheless",
                "options": {
                    "a": "furthermore",
                    "b": "consequently",
                    "c": "nevertheless",
                    "d": "in addition",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 3: Collocations — Words That Go Together (C1) ─────────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Collocations — Words That Go Together",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.COLLOCATIONS,
            "description": (
                "Learn the specific word combinations native speakers use "
                "habitually to elevate your technical and everyday vocabulary."
            ),
            "order_index": 20,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The team will deploy the new feature to production once we achieve full test coverage.",
                "translation": "El equipo desplegará la nueva funcionalidad a producción una vez que alcancemos cobertura total de pruebas.",
                "ipa_notation": "/ðə tiːm wɪl dɪˈplɔɪ ðə njuː ˈfiːtʃər tə prəˈdʌkʃən wʌns wiː əˈtʃiːv fʊl tɛst ˈkʌvərɪdʒ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "We must not accumulate tech debt by skipping code reviews under tight deadlines.",
                "translation": "No debemos acumular deuda técnica saltándonos las revisiones de código bajo plazos ajustados.",
                "ipa_notation": "/wiː mʌst nɒt əˈkjuːmjuleɪt tɛk dɛt baɪ ˈskɪpɪŋ koʊd rɪˈvjuːz ˈʌndər taɪt ˈdɛdlaɪnz/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Did the breaking change in the API trigger a critical failure in the downstream services?",
                "translation": "¿El cambio incompatible en la API provocó un fallo crítico en los servicios dependientes?",
                "ipa_notation": "/dɪd ðə ˈbreɪkɪŋ tʃeɪndʒ ɪn ðiː ˌeɪpiːˈaɪ ˈtrɪɡər ə ˈkrɪtɪkəl ˈfeɪljər ɪn ðə ˈdaʊnstriːm ˈsɜːrvɪsɪz/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which verb correctly collocates with 'an error' in professional engineering English: 'We need to ______ the error before it propagates to the client.'",
                "correct_answer": "handle",
                "options": {
                    "a": "manage",
                    "b": "handle",
                    "c": "do",
                    "d": "fix",
                },
                "order_index": 1,
            },
        ],
    },
]
