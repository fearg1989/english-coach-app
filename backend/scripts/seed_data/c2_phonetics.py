# c2_phonetics.py — C2 Phonetics lessons
# Foco en habla ultra-rápida nativa (extreme connected speech) y comunicación implícita
# (sarcasmo, ironía, tono escéptico). Nivel CPE — comprensión y producción de habla nativa.
# Basado en Cambridge Pronunciation in Use (Advanced, Hewings) y corpus de inglés coloquial.
# NOTE: sys.path is set up by seed.py before this module is imported.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

C2_PHONETICS_LESSONS: list[dict] = [
    # ── Lesson 1: Decoding Extreme Connected Speech ───────────────────────────
    {
        "level_code": "C2",
        "meta": {
            "title": "Decoding Extreme Connected Speech",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Learn to decode fast native speech by identifying vowel "
                "reductions, elisions, and sound mergers in professional contexts."
            ),
            "order_index": 1,
            "is_published": True,
        },
        "examples": [
            {
                # "Are you going to push" → /jə ˈɡʌnə pʊʃ/ — are you → /jə/, going to → /ˈɡʌnə/
                "phrase": "Ya gonna push the hotfix to production tonight, or are we rolling back? [Are you going to push...]",
                "translation": "¿Vas a hacer push del hotfix a producción esta noche, o hacemos rollback? (ya gonna = are you going to)",
                "ipa_notation": "/jə ˈɡʌnə pʊʃ ðə ˈhɒtfɪks tə prəˈdʌkʃən təˈnaɪt | ɔːr ər wiː ˈroʊlɪŋ bæk/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                # "What are you doing" → /ˈwʌtʃə ˈduːɪŋ/ — coalescencia /t/+/j/→/tʃ/ + /r/ elidido + you→/ə/
                "phrase": "Whatcha doing with the migration script? It's been running for twenty minutes. [What are you doing...]",
                "translation": "¿Qué estás haciendo con el script de migración? Lleva veinte minutos ejecutándose. (whatcha = what are you)",
                "ipa_notation": "/ˈwʌtʃə ˈduːɪŋ wɪð ðə maɪˈɡreɪʃən skrɪpt | ɪts bɪn ˈrʌnɪŋ fər ˈtwɛnti ˈmɪnɪts/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                # "I have got to review" → /aɪv ˈɡɒɾə rɪˈvjuː/ — have got to → gotta con flap T
                "phrase": "I've gotta review three pull requests before the standup, and I'm already late. [I have got to...]",
                "translation": "Tengo que revisar tres pull requests antes del standup, y ya llego tarde. (gotta = have got to)",
                "ipa_notation": "/aɪv ˈɡɒɾə rɪˈvjuː θriː pʊl rɪˈkwɛsts bɪˈfɔːr ðə ˈstændʌp | ænd aɪm ɔːlˈrɛdi leɪt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
            {
                # "Do you want to take" → /ˈwʌnə teɪk/ — do you elidido, want to → wanna /ˈwʌnə/
                "phrase": "Wanna take a quick look at the deployment logs before we close the incident? [Do you want to take...]",
                "translation": "¿Quieres echar un vistazo rápido a los logs del despliegue antes de cerrar el incidente? (wanna = want to)",
                "ipa_notation": "/ˈwʌnə teɪk ə kwɪk lʊk ət ðə dɪˈplɔɪmənt lɒɡz bɪˈfɔːr wiː kloʊz ðiː ˈɪnsɪdənt/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 4,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "A senior engineer says quickly: /ˈdɪdʒə ˈmɜːrdʒ ðə ˈfiːtʃər bræntʃ ɔːlˈrɛdi/. "
                    "Which written sentence does this correspond to? "
                    "(Hint: /ˈdɪdʒə/ = coalescent assimilation of 'did' + 'you')"
                ),
                "correct_answer": "Did you merge the feature branch already?",
                "options": {
                    "a": "Do you merge the feature branch already?",
                    "b": "Did you merge the feature branch already?",
                    "c": "Are you going to merge the feature branch already?",
                    "d": "Would you merge the feature branch already?",
                },
                "order_index": 1,
            },
        ],
    },
    # ── Lesson 2: Sarcasm, Irony & Subtle Tone ───────────────────────────────
    {
        "level_code": "C2",
        "meta": {
            "title": "Sarcasm, Irony & Subtle Tone",
            "type": LessonType.PHONETICS,
            "category": LessonCategory.PHONETICS,
            "description": (
                "Master the prosodic cues, vowel lengthenings, and pitch "
                "changes used to convey sarcasm and skepticism in workplace English."
            ),
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                # "great" alargado + flat ↘→ + pausa dramática = el deploy del viernes es una catástrofe anunciada
                "phrase": "Oh, greaat. ↘→ The deploy went to production on Friday evening. Nothing could go wrong.",
                "translation": "Oh, geniiial. El deploy se fue a producción el viernes por la tarde. Nada puede salir mal. (ironía: TODO va a salir mal — regla no escrita: nunca se despliega en viernes)",
                "ipa_notation": "/oʊ | ˈɡreɪːt ↘→ ‖ ðə dɪˈplɔɪ wɛnt tə prəˈdʌkʃən ɒn ˈfraɪdeɪ ˈiːvnɪŋ | ˈnʌθɪŋ kʊd ɡoʊ rɒŋ →/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                # rise exagerado en "sure ↗" + flat monotono = burla velada ante estimación irreal
                "phrase": "Yeah, sure. ↗ Rewriting the entire backend in a weekend sounds totally realistic. →",
                "translation": "Sí, cómo no. Reescribir todo el backend en un fin de semana parece totalmente realista. (imposible — ironía pura ante una estimación absurda)",
                "ipa_notation": "/jeɪ | ʃʊɹ ↗ ‖ ˌriːˈraɪtɪŋ ðiː ɪnˈtaɪər ˈbækɛnd ɪn ə ˈwiːkɛnd saʊndz ˈtoʊːtəli riˈælɪstɪk →/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                # flat monotone + "I'm sure →" = referencia irónica a la Ley de Brooks (añadir ingenieros retrasa proyectos tardíos)
                "phrase": "Oh, I'm sure → adding more engineers to a late project will just speed everything up.",
                "translation": "Oh, estoy seguro de que añadir más ingenieros a un proyecto retrasado va a acelerarlo todo. (Ley de Brooks — lo opuesto es verdad; ironía sofisticada)",
                "ipa_notation": "/oʊ | aɪm ʃʊɹ → ˈædɪŋ mɔːr ˌɛndʒɪˈnɪərz tə ə leɪt ˈprɒdʒɛkt wɪl dʒʌs spiːd ˈɛvriθɪŋ ʌp →/",
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": (
                    "A colleague says in a monotone flat voice with a noticeably elongated vowel: "
                    "'Oh, that's a greeeat plan. → Deploying on a Friday with no rollback strategy.' "
                    "What is the most accurate interpretation?"
                ),
                "correct_answer": "The speaker is being sarcastic and considers the plan dangerously irresponsible.",
                "options": {
                    "a": "The speaker genuinely thinks it is a great and well-considered plan.",
                    "b": "The speaker is being sarcastic and considers the plan dangerously irresponsible.",
                    "c": "The speaker is uncertain and is requesting more information.",
                    "d": "The speaker is enthusiastic but slightly anxious about the timeline.",
                },
                "order_index": 1,
            },
        ],
    },
]
