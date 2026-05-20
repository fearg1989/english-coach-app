# c1_grammar.py — C1 Grammar lessons
# Cambridge Advanced Grammar in Use (Hewings) — Advanced level.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C1_GRAMMAR_LESSONS: list[dict] = [
    {
        "level_code": "C1",
        "meta": {
            "title": "Narrative Tenses & Inversion for Emphasis",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.VERB_TENSES,
            "description": (
                "Master formal inverted structures and negative adverbials "
                "to express urgency and emphasis in engineering reports."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {"phrase": "Hardly had we started the deployment when the environment failed.",         "translation": "Apenas habíamos comenzado el despliegue cuando el entorno falló.",                "ipa_notation": "/ˈhɑːrdli hæd wiː ˈstɑːrtɪd ðə dɪˈplɔɪmənt wɛn ðiː ɪnˈvaɪrənmənt feɪld/",     "order_index": 1},
            {"phrase": "Not until we had patched the vulnerability did the system stabilize.",      "translation": "No fue hasta que parchamos la vulnerabilidad que el sistema se estabilizó.",      "ipa_notation": "/nɒt ənˈtɪl wiː hæd pætʃt ðə ˌvʌlnərəˈbɪlɪti dɪd ðə ˈsɪstəm ˈsteɪbəlaɪz/",   "order_index": 2},
            {"phrase": "Under no circumstances will the team deploy without a full rollback plan.", "translation": "Bajo ninguna circunstancia el equipo desplegará sin un plan de rollback completo.", "ipa_notation": "/ˈʌndər noʊ ˈsɜːrkəmstænsɪz wɪl ðə tiːm dɪˈplɔɪ wɪˈðaʊt ə fʊl ˈroʊlbæk plæn/", "order_index": 3},
        ],
        "exercises": [
            {"type": ExerciseType.MULTIPLE_CHOICE, "question": "Rewrite with inversion: 'We had rarely seen such a complex race condition.'",       "correct_answer": "Rarely had we seen such a complex race condition.",                      "options": {"a": "Rarely we had seen such a complex race condition.", "b": "Rarely had we seen such a complex race condition.", "c": "Had rarely we seen such a complex race condition.", "d": "We had seen rarely such a complex race condition."}, "order_index": 1},
            {"type": ExerciseType.FILL_BLANK,      "question": "______ had the hotfix been merged when a new regression was discovered. (Hardly)",  "correct_answer": "Hardly",                                                                 "options": None, "order_index": 2},
            {"type": ExerciseType.PRONUNCIATION,   "question": "Record: 'Under no circumstances will I push directly to the main branch.'",        "correct_answer": "/ˈʌndər noʊ ˈsɜːrkəmstænsɪz wɪl aɪ pʊʃ dɪˈrɛktli tə ðə meɪn bræntʃ/", "options": None, "order_index": 3},
        ],
    },
    # ─── Lesson 2: Cleft Sentences ────────────────────────────────────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Cleft Sentences — Emphasizing the Solution",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Reorganize sentence structure using cleft sentences to "
                "highlight solutions and place focus on critical elements."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "What our microservices architecture needs is a centralized API gateway.",
                "translation": "Lo que nuestra arquitectura de microservicios necesita es un API gateway centralizado.",
                "ipa_notation": "/wɒt aʊər ˌmaɪkroʊˈsɜːrvɪsɪz ˈɑːrkɪtɛktʃər niːdz ɪz ə ˈsɛntrəlaɪzd ˌeɪ piː aɪ ˈɡeɪtwɛɪ/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "What the pipeline does not include is an automated security scan at the build stage.",
                "translation": "Lo que el pipeline no incluye es un análisis de seguridad automatizado en la etapa de compilación.",
                "ipa_notation": "/wɒt ðə ˈpaɪplaɪn dʌz nɒt ɪnˈkluːd ɪz ən ˌɔːtəˈmeɪtɪd sɪˈkjʊərɪti skæn æt ðə bɪld steɪdʒ/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Is it the lack of observability that is making incidents so hard to diagnose?",
                "translation": "¿Es la falta de observabilidad lo que hace que los incidentes sean tan difíciles de diagnosticar?",
                "ipa_notation": "/ɪz ɪt ðə læk əv ɒbˌzɜːrvəˈbɪlɪti ðæt ɪz ˈmeɪkɪŋ ˈɪnsɪdənts soʊ hɑːrd tə ˌdaɪəɡˈnoʊz/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence is a correct WH-cleft (pseudo-cleft) used to emphasize a solution?",
                "correct_answer": "What we need to do is migrate to a containerized environment.",
                "options": {
                    "a": "We need to migrate to a containerized environment.",
                    "b": "What we need to do is migrate to a containerized environment.",
                    "c": "It was us who need to migrate to a containerized environment.",
                    "d": "What we migrated is a containerized environment.",
                },
                "order_index": 1,
            },
        ],
    },
    # ─── Lesson 3: Participle Clauses ─────────────────────────────────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "Participle Clauses — Efficient Professional Reporting",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Enhance narrative flow and report conciseness using "
                "participle clauses for sophisticated, professional updates."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "Having refactored the authentication service, the team reduced login latency by forty percent.",
                "translation": "Habiendo refactorizado el servicio de autenticación, el equipo redujo la latencia de inicio de sesión en un cuarenta por ciento.",
                "ipa_notation": "/ˈhævɪŋ ˌriːˈfæktərd ðiː ˌɔːθɛntɪˈkeɪʃən ˈsɜːrvɪs | ðə tiːm rɪˈdjuːst ˈlɒɡɪn ˈleɪtənsi baɪ ˈfɔːrti pəˈsɛnt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "Not having integrated a rate limiter, the API was vulnerable to denial-of-service attacks.",
                "translation": "Al no haber integrado un limitador de tasa, la API era vulnerable a ataques de denegación de servicio.",
                "ipa_notation": "/nɒt ˈhævɪŋ ˌɪntɪˈɡreɪtɪd ə reɪt ˈlɪmɪtər | ðiː eɪ piː aɪ wɒz ˈvʌlnərəbl tə dɪˈnaɪəl əv ˈsɜːrvɪs əˈtæks/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Having run the load tests successfully, can we now schedule the production release for Friday?",
                "translation": "Habiendo ejecutado las pruebas de carga exitosamente, ¿podemos ahora programar el lanzamiento a producción para el viernes?",
                "ipa_notation": "/ˈhævɪŋ rʌn ðə loʊd tɛsts səkˈsɛsfəli | kæn wiː naʊ ˈskɛdʒuːl ðə prəˈdʌkʃən rɪˈliːs fər ˈfraɪdeɪ/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence correctly uses a PERFECT participle clause to show a prior completed action?",
                "correct_answer": "Having deployed the hotfix, the on-call engineer closed the incident ticket.",
                "options": {
                    "a": "Deploying the hotfix, the on-call engineer closed the incident ticket.",
                    "b": "Having deployed the hotfix, the on-call engineer closed the incident ticket.",
                    "c": "Deployed the hotfix, the on-call engineer closed the incident ticket.",
                    "d": "To deploy the hotfix, the on-call engineer closed the incident ticket.",
                },
                "order_index": 1,
            },
        ],
    },
    # ─── Lesson 4: The Subjunctive ────────────────────────────────────────────
    {
        "level_code": "C1",
        "meta": {
            "title": "The Subjunctive — Formal Recommendations",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Master formal requirements, recommendations, and security "
                "protocols using the mandative subjunctive in technical writing."
            ),
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The tech lead recommends that every engineer include integration tests in their pull request.",
                "translation": "El líder técnico recomienda que cada ingeniero incluya pruebas de integración en su pull request.",
                "ipa_notation": "/ðə tɛk liːd ˌrɛkəˈmɛndz ðæt ˈɛvri ˌɛndʒɪˈnɪər ɪnˈkluːd ˌɪntɪˈɡreɪʃən tɛsts ɪn ðɛr pʊl rɪˈkwɛst/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The security policy requires that developers not push directly to the main branch under any circumstance.",
                "translation": "La política de seguridad requiere que los desarrolladores no hagan push directamente a la rama principal bajo ninguna circunstancia.",
                "ipa_notation": "/ðə sɪˈkjʊərɪti ˈpɒlɪsi rɪˈkwaɪərz ðæt ˌdɛvəˈlɒpərz nɒt pʊʃ dɪˈrɛktli tə ðə meɪn bræntʃ ˈʌndər ˈɛni ˈsɜːrkəmstəns/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Does the board insist that the CTO be present at every architecture review meeting?",
                "translation": "¿Insiste el consejo en que el CTO esté presente en cada reunión de revisión de arquitectura?",
                "ipa_notation": "/dʌz ðə bɔːrd ɪnˈsɪst ðæt ðə ˌsiː tiː ˈoʊ biː ˈprɛzənt æt ˈɛvri ˈɑːrkɪtɛktʃər rɪˈvjuː ˈmiːtɪŋ/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence correctly uses the mandative subjunctive for a formal recommendation?",
                "correct_answer": "The architect insists that the team adopt trunk-based development.",
                "options": {
                    "a": "The architect insists that the team adopts trunk-based development.",
                    "b": "The architect insists that the team adopted trunk-based development.",
                    "c": "The architect insists that the team adopt trunk-based development.",
                    "d": "The architect insists that the team should adopts trunk-based development.",
                },
                "order_index": 1,
            },
        ],
    },
]
