# c2_grammar.py — C2 Grammar lessons
# Cambridge Proficiency in English (CPE) — Mastery level.
# Basado en Cambridge Grammar for Advanced (Hewings) y el marco CEFR C2.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C2_GRAMMAR_LESSONS: list[dict] = [
    # ── Lesson 1: Hedging & Distancing ───────────────────────────────────────
    {
        "level_code": "C2",
        "meta": {
            "title": "Hedging & Distancing — Diplomatic Communication",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Master C2 hedging and epistemic precision to express "
                "diplomatically softened, objective claims in formal architectural reviews."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "It could arguably be stated that the current microservices architecture tends to introduce unnecessary operational complexity.",
                "translation": "Podría argumentarse que la arquitectura actual de microservicios tiende a introducir una complejidad operativa innecesaria.",
                "ipa_notation": "/ɪt kʊd ˈɑːɡjuəbli biː ˈsteɪtɪd ðæt ðə ˈkɜːrənt ˌmaɪkroʊˈsɜːrvɪsɪz ˌɑːrkɪˈtɛktʃər tɛndz tə ɪntrəˈduːs ˌʌnnɛsɪˈsɛri ˌɒpəˈreɪʃənl kəmˈplɛksɪti/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "It would not be entirely accurate to suggest that the system's scalability limitations stem solely from the database layer.",
                "translation": "No sería del todo exacto sugerir que las limitaciones de escalabilidad del sistema provienen únicamente de la capa de base de datos.",
                "ipa_notation": "/ɪt wʊd nɒt biː ɪnˈtaɪərli ˈækjərɪt tə səˈdʒɛst ðæt ðə ˈsɪstɪmz ˌskeɪləˈbɪlɪti ˌlɪmɪˈteɪʃənz stɛm ˈsoʊlli frəm ðə ˈdeɪtəˌbeɪs ˈleɪər/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Could it not be argued that there tends to be a degree of over-engineering in the proposed solution?",
                "translation": "¿No podría argumentarse que tiende a haber un cierto grado de sobreingeniería en la solución propuesta?",
                "ipa_notation": "/kʊd ɪt nɒt biː ˈɑːɡjuːd ðæt ðɛr tɛndz tə biː ə dɪˈɡriː əv ˌoʊvər ˈɛndʒɪnɪərɪŋ ɪn ðə prəˈpoʊzd səˈluːʃən/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which sentence best demonstrates C2-level hedging to soften a critical observation "
                    "in a code review?"
                ),
                "correct_answer": "It could arguably be contended that this implementation tends to compromise the separation of concerns principle.",
                "options": {
                    "a": "This implementation is wrong and breaks separation of concerns.",
                    "b": "It could arguably be contended that this implementation tends to compromise the separation of concerns principle.",
                    "c": "Maybe this implementation is a bit wrong.",
                    "d": "I think there might be a possible issue with the separation of concerns.",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Semantic Precision — Mastering Nuances ─────────────────────
    {
        "level_code": "C2",
        "meta": {
            "title": "Semantic Precision — Mastering Nuances",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Master highly precise vocabulary, differentiating close "
                "near-synonyms like undermine and inhibit in executive messaging."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The accumulation of technical debt does not merely inhibit delivery speed; it actively undermines the team's ability to respond to critical incidents.",
                "translation": "La acumulación de deuda técnica no solo inhibe la velocidad de entrega; mina activamente la capacidad del equipo para responder a incidentes críticos.",
                "ipa_notation": "/ðiː əˌkjuːmjʊˈleɪʃən əv ˈtɛknɪkəl dɛt dʌz nɒt ˈmɪərli ɪnˈhɪbɪt dɪˈlɪvəri spiːd | ɪt ˈæktɪvli ˌʌndərˈmaɪnz ðə tiːmz əˈbɪlɪti tə rɪˈspɒnd tə ˈkrɪtɪkəl ˈɪnsɪdənts/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "A tight release schedule is a constraint inherent to our SLA, not merely a drawback of our chosen deployment strategy.",
                "translation": "Un calendario de lanzamiento ajustado es una restricción inherente a nuestro SLA, no simplemente un inconveniente de la estrategia de despliegue elegida.",
                "ipa_notation": "/ə taɪt rɪˈliːs ˈskɛdʒuːl ɪz ə kənˈstreɪnt ɪnˈhɪərənt tə aʊər ɛs ɛl eɪ | nɒt ˈmɪərli ə ˈdrɔːbæk əv aʊər ˈtʃoʊzən dɪˈplɔɪmənt ˈstrætɪdʒi/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Does adopting a serverless model truly remove the operational constraint, or does it merely displace the drawback to a different layer of the stack?",
                "translation": "¿Adoptar un modelo serverless elimina realmente la restricción operativa, o simplemente desplaza el inconveniente a otra capa del stack?",
                "ipa_notation": "/dʌz əˈdɒptɪŋ ə ˈsɜːrvərləs ˈmɒdəl ˈtruːli rɪˈmuːv ðiː ˌɒpəˈreɪʃənl kənˈstreɪnt | ɔːr dʌz ɪt ˈmɪərli dɪsˈpleɪs ðə ˈdrɔːbæk tə ə ˈdɪfrənt ˈleɪər əv ðə stæk/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "An architect says: 'Poor observability ___ our ability to pinpoint root causes during incidents.' "
                    "Which word is semantically most precise? The problem restricts the ability but does NOT actively destroy the team."
                ),
                "correct_answer": "inhibits",
                "options": {
                    "a": "undermines",
                    "b": "inhibits",
                    "c": "resolves",
                    "d": "mitigates",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 3: Complex Embedded Clauses ───────────────────────────────────
    {
        "level_code": "C2",
        "meta": {
            "title": "Complex Embedded Clauses — Advanced Sentence Structure",
            "type": LessonType.GRAMMAR,
            "category": LessonCategory.GENERAL_GRAMMAR,
            "description": (
                "Condense complex logical relationships clearly within single "
                "sentences using nested relative and participle clauses."
            ),
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": "The observability protocol, which, despite initial resistance from the infrastructure team, was implemented across all critical services, has demonstrably reduced mean time to recovery.",
                "translation": "El protocolo de observabilidad, que, a pesar de la resistencia inicial del equipo de infraestructura, fue implementado en todos los servicios críticos, ha reducido de manera demostrable el tiempo medio de recuperación.",
                "ipa_notation": "/ðiː ˌɒbzɜːrvəˈbɪlɪti ˈproʊtəˌkɒl | wɪtʃ | dɪˈspaɪt ɪˈnɪʃəl rɪˈzɪstəns frəm ðiː ˌɪnfrəˈstrʌktʃər tiːm | wəz ˌɪmplɪˈmɛntɪd əˈkrɒs ɔːl ˈkrɪtɪkəl ˈsɜːrvɪsɪz | hæz dɪˈmɒnstrəbli rɪˈduːst miːn taɪm tə rɪˈkʌvəri/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": "The decision to migrate, which the board, having reviewed the risk assessment submitted by the CTO, ultimately approved, did not account for the downstream dependencies that would later trigger a cascade failure.",
                "translation": "La decisión de migrar, que el consejo, habiendo revisado la evaluación de riesgos presentada por el CTO, aprobó en última instancia, no consideró las dependencias downstream que más tarde desencadenarían un fallo en cascada.",
                "ipa_notation": "/ðə dɪˈsɪʒən tə maɪˈɡreɪt | wɪtʃ ðə bɔːrd | ˈhævɪŋ rɪˈvjuːd ðə rɪsk əˈsɛsmənt səbˈmɪtɪd baɪ ðə siː tiː ˈoʊ | ˈʌltɪmɪtli əˈpruːvd | dɪd nɒt əˈkaʊnt fər ðə ˈdaʊnstriːm dɪˈpɛndənsɪz ðæt wʊd ˈleɪtər ˈtrɪɡər ə kæsˈkeɪd ˈfeɪljər/",
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": "Can it truly be claimed that the architecture, which the team, having spent three quarters on its design, released ahead of schedule, is sufficiently documented to allow independent onboarding?",
                "translation": "¿Puede realmente afirmarse que la arquitectura, que el equipo, habiendo dedicado tres trimestres a su diseño, lanzó antes de lo previsto, está suficientemente documentada para permitir un onboarding independiente?",
                "ipa_notation": "/kæn ɪt ˈtruːli biː kleɪmd ðæt ðiː ˌɑːrkɪˈtɛktʃər | wɪtʃ ðə tiːm | ˈhævɪŋ spɛnt θriː ˈkwɔːrtərz ɒn ɪts dɪˈzaɪn | rɪˈliːst əˈhɛd əv ˈskɛdʒuːl | ɪz səˈfɪʃəntli ˈdɒkjʊmɛntɪd tə əˈlaʊ ˌɪndɪˈpɛndənt ˈɒnbɔːrdɪŋ/",
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "Which sentence correctly uses a complex embedded clause structure "
                    "(non-restrictive relative + nested participle clause) in a professional IT context?"
                ),
                "correct_answer": "The refactoring plan, which the team, having assessed the full impact, finally agreed upon, will be executed over two sprints.",
                "options": {
                    "a": "The refactoring plan that the team agreed upon will be executed over two sprints.",
                    "b": "The refactoring plan, which the team, having assessed the full impact, finally agreed upon, will be executed over two sprints.",
                    "c": "The team assessed the impact and agreed on the refactoring plan, and it will be executed over two sprints.",
                    "d": "Having assessed the impact, the refactoring plan will be executed over two sprints by the team.",
                },
                "order_index": 1,
            },
        ],
    },
]
