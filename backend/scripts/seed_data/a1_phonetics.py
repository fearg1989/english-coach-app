# a1_phonetics.py — Pristine plain-text JSON seed data
# Cleaned programmatically to comply with strict Separation of Concerns.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

PHONETICS: dict = {
    "meta": {
        "title": 'The /θ/ and /ð/ Sounds — TH',
        "explanation": {
            "intro": '',
            "sections": [
                {
                    "title": 'The Two TH Sounds',
                    "layout": 'table',
                    "headers": ['Symbol', 'Name', 'Voice?', 'Key words'],
                    "rows": [
                        ['/θ/', 'Voiceless TH', 'No vibration', 'think, three, tooth, path, through'],
                        ['/ð/', 'Voiced TH', 'Vocal cords vibrate', 'this, that, the, breathe, father'],
                    ],
                },
                {
                    "title": 'Articulation Guide',
                    "layout": 'list',
                    "items": [
                        'Position: Tongue tip lightly touches the edges of the upper front teeth.',
                        '/θ/ test: Hold your fingers to your throat — you should feel no vibration (like blowing silently).',
                        '/ð/ test: Hold your fingers to your throat — you should feel vibration (like a gentle buzz).',
                        "Common error: Replacing both with /s/ or /d/ — 'sink' instead of 'think', 'dis' instead of 'this'.",
                    ],
                },
            ],
        },
        "type": LessonType.PHONETICS,
        "category": LessonType.PHONETICS,
        "description": 'Master the voiceless /θ/ sound in think and the voiced /ð/ sound in this to elevate your English pronunciation.',
        "order_index": 1,
        "is_published": True,
    },
    "examples": [
        {
            "phrase": 'I think this is the right path.',
            "translation": 'Creo que este es el camino correcto.',
            "ipa_notation": '/aɪ θɪŋk ðɪs ɪz ðə raɪt pæθ/',
            "sentence_type": SentenceType.AFFIRMATIVE,
            "order_index": 1,
        },
        {
            "phrase": 'The weather there is breathtaking.',
            "translation": 'El clima allí es impresionante.',
            "ipa_notation": '/ðə ˈweðər ðer ɪz ˈbreθˌteɪkɪŋ/',
            "sentence_type": SentenceType.AFFIRMATIVE,
            "order_index": 2,
        },
        {
            "phrase": 'Thank the author for their thoughtful work.',
            "translation": 'Agradece al autor por su reflexivo trabajo.',
            "ipa_notation": '/θæŋk ðə ˈɔːθər fər ðer ˈθɔːtfəl wɜːrk/',
            "sentence_type": SentenceType.AFFIRMATIVE,
            "order_index": 3,
        },
    ],
    "exercises": [
        {
            "type": ExerciseType.MULTIPLE_CHOICE,
            "question": "Which word contains the VOICELESS /θ/ sound (as in 'think')?",
            "correct_answer": 'tooth',
            "options": {
                "a": 'this',
                "b": 'those',
                "c": 'tooth',
                "d": 'breathe',
            },
            "order_index": 1,
        },
        {
            "type": ExerciseType.FILL_BLANK,
            "question": "Complete the IPA transcription for 'think': /______ɪŋk/",
            "correct_answer": 'θ',
            "options": None,
            "order_index": 2,
        },
        {
            "type": ExerciseType.MULTIPLE_CHOICE,
            "question": "Which word contains the VOICED /ð/ sound (as in 'this')?",
            "correct_answer": 'breathe',
            "options": {
                "a": 'think',
                "b": 'tooth',
                "c": 'breathe',
                "d": 'path',
            },
            "order_index": 3,
        },
        {
            "type": ExerciseType.PRONUNCIATION,
            "question": "Record yourself saying: 'The father thinks about three things.'",
            "correct_answer": '/ðə ˈfɑːðər θɪŋks əˈbaʊt θriː θɪŋz/',
            "options": None,
            "order_index": 4,
        },
    ],
}

A1_PHONETICS_LESSONS: list[dict] = [
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Introduction to the IPA — Your Pronunciation Map',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'What Is the IPA & How to Read Stress Marks',
                        "layout": 'list',
                        "items": [
                            'IPA is enclosed in slashes: /ˈsæləd/ = the word salad.',
                            'ˈ (vertical tick) = primary stress: say this syllable louder, longer, and higher in pitch. Example: /ˈsæləd/ → SAL-ad.',
                            'ˌ (low tick) = secondary stress: slightly stressed, but weaker than primary. Example: /ˌɛndzɪˈnɪr/ → end-zo-NEER.',
                            'Wrong stress = miscommunication. REcord (noun) vs reCORD (verb).',
                        ],
                    },
                    {
                        "title": 'All English Vowels — Short, Long & Schwa',
                        "layout": 'table',
                        "headers": ['Symbol', 'Type', 'Sound description', 'Tech examples'],
                        "rows": [
                            ['/ɪ/', 'Short', "Relaxed, short 'i' — NOT the Spanish /i/", 'bit, git, list, script'],
                            ['/e/', 'Short', 'Mouth half open, front of mouth', 'set, REST, header, fetch'],
                            ['/æ/', 'Short', 'Mouth wide open, flat jaw', 'cat, batch, lambda, cache'],
                            ['/ɒ/', 'Short', 'Mouth open, lips unrounded (AmE)', 'dot, not, log, socket'],
                            ['/ʌ/', 'Short', 'Neutral mid vowel, lips unrounded', 'run, bug, function, null'],
                            ['/ʊ/', 'Short', "Short 'oo', lips slightly rounded", 'book, push, could, full'],
                            ['/ə/', 'Schwa', 'The laziest vowel — neutral, unstressed only', 'data, compiler, system'],
                            ['/iː/', 'Long', "Tense, long 'ee' — lips spread", 'see, release, team, field'],
                            ['/ɑː/', 'Long', 'Mouth wide open, back of throat', 'car, start, class, parse'],
                            ['/ɔː/', 'Long', 'Rounded lips, back vowel', 'call, port, all, log (BrE)'],
                            ['/uː/', 'Long', "Tense 'oo', lips fully rounded", 'use, group, loop, root'],
                            ['/ɜː/', 'Long', 'Mid-central, lips neutral', 'bird, server, virtual, merge'],
                        ],
                    },
                    {
                        "title": 'All English Diphthongs',
                        "layout": 'table',
                        "headers": ['Symbol', 'Glide path', 'Keyword', 'Tech examples'],
                        "rows": [
                            ['/eɪ/', '/e/ → /ɪ/', 'face', 'name, state, change, data, scale'],
                            ['/aɪ/', '/a/ → /ɪ/', 'price', 'file, write, pipeline, time, binary'],
                            ['/ɔɪ/', '/ɔ/ → /ɪ/', 'choice', 'void, point, noise, join'],
                            ['/oʊ/', '/o/ → /ʊ/', 'goat', 'code, node, flow, remote, local'],
                            ['/aʊ/', '/a/ → /ʊ/', 'mouth', 'cloud, down, output, count, found'],
                            ['/ɪə/', '/ɪ/ → /ə/', 'near', 'here, clear, engineer, tier'],
                            ['/eə/', '/e/ → /ə/', 'square', 'share, declare, compare, where'],
                            ['/ʊə/', '/ʊ/ → /ə/', 'cure', 'pure, secure, configure'],
                        ],
                    },
                    {
                        "title": 'Tricky Consonants for Spanish Speakers',
                        "layout": 'table',
                        "headers": ['Symbol', 'Sound', 'Problem for Spanish speakers', 'Examples'],
                        "rows": [
                            ['/θ/', 'Voiceless TH', 'Does not exist in Spanish. Tongue between teeth, air flows out.', 'think, three, thread, method'],
                            ['/ð/', 'Voiced TH', 'Same as /θ/ but vocal cords vibrate.', 'the, this, that, there, other'],
                            ['/v/', 'Voiced V', 'Spanish /b/ and /v/ sound the same. English /v/ = lower lip on upper teeth + vibration.', 'version, value, validate, verbose'],
                            ['/z/', 'Voiced Z', 'Often replaced by /s/. Keep vocal cords vibrating through the sound.', 'zero, zip, fuzzy, resize'],
                            ['/h/', 'English H', 'Silent in Spanish; in English it is a real aspirated consonant.', 'host, hash, handler, header'],
                            ['/w/', 'English W', 'Not a vowel — it is a consonant. Lips must be rounded for the start.', 'web, webpack, workflow, while'],
                            ['/ŋ/', 'NG nasal', 'One sound, not N+G. Do not pronounce a hard /g/ at the end.', 'running, testing, string, length'],
                            ['/ʒ/', 'Voiced ZH', 'Like the French J. No equivalent in Spanish.', 'vision, measure, fusion, Azure'],
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Learn to decode the International Phonetic Alphabet (IPA) and master word stress to read pronunciation keys.',
            "order_index": 2,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Salad',
                "translation": 'Ensalada',
                "ipa_notation": '/ˈsæləd/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Function',
                "translation": 'Función',
                "ipa_notation": '/ˈfʌŋkʃən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Enough',
                "translation": 'Suficiente',
                "ipa_notation": '/ɪˈnʌf/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'In the IPA transcription /ˈsæləd/, what does the symbol ˈ mean?',
                "correct_answer": 'Stress — say that syllable louder and higher.',
                "options": {
                    "a": 'Pause between syllables.',
                    "b": 'Stress — say that syllable louder and higher.',
                    "c": 'The syllable is silent.',
                    "d": 'The word has two different meanings.',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'The Schwa Sound /ə/ — The Most Common English Sound',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Why the Schwa Is Critical',
                        "layout": 'list',
                        "items": [
                            'It makes up roughly 10-15% of all sounds in natural English speech.',
                            'Without it, your English sounds stiff and foreign — every unstressed syllable gets over-articulated.',
                            'Native speakers reduce unstressed vowels to /ə/ constantly.',
                        ],
                    },
                    {
                        "title": 'Schwa in Common Technical Words',
                        "layout": 'table',
                        "headers": ['Word', 'IPA', 'Schwa position'],
                        "rows": [
                            ['computer', '/kəmˈpjuːtər/', '1st syllable: cəm, last: tər'],
                            ['develop', '/dɪˈvɛləp/', '3rd syllable: ləp'],
                            ['about', '/əˈbaʊt/', '1st syllable: əbout'],
                            ['parameter', '/pəˈræmɪtər/', '1st and last syllables'],
                        ],
                    },
                    {
                        "title": 'How to Produce It',
                        "layout": 'list',
                        "items": [
                            'Jaw: slightly open, relaxed.',
                            'Tongue: flat, in the middle of the mouth — no tension.',
                            'Lips: unrounded, neutral.',
                            "Duration: very short — it is always in an unstressed, 'thrown away' syllable.",
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Master the schwa /ə/, the most common and relaxed vowel sound in English, to instantly speak more naturally.',
            "order_index": 3,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'about',
                "translation": 'acerca de / sobre',
                "ipa_notation": '/əˈbaʊt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'teacher',
                "translation": 'maestro / maestra',
                "ipa_notation": '/ˈtiːtʃər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'computer',
                "translation": 'computadora / ordenador',
                "ipa_notation": '/kəmˈpjuːtər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": 'The IPA symbol for the relaxed, neutral vowel found only in unstressed syllables — the schwa — is: /______/',
                "correct_answer": 'ə',
                "options": None,
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Short /ɪ/ vs. Long /iː/ — Sit vs. Seat',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'The Two Sounds Side by Side',
                        "layout": 'table',
                        "headers": ['Symbol', 'Name', 'Mouth shape', 'Tech words'],
                        "rows": [
                            ['/ɪ/', 'Short i', 'Relaxed, jaw slightly open, lips loose', 'git, bit, fix, script, build'],
                            ['/iː/', 'Long ee', 'Tense, wide smile, jaw close, hold the sound', 'release, team, feature, clean, read'],
                        ],
                    },
                    {
                        "title": 'Minimal Pairs — Same Word, Different Meaning',
                        "layout": 'table',
                        "headers": ['/ɪ/ (short)', '/iː/ (long)'],
                        "rows": [
                            ['sit /sɪt/', 'seat /siːt/'],
                            ['hit /hɪt/', 'heat /hiːt/'],
                            ['live /lɪv/', 'leave /liːv/'],
                            ['bit /bɪt/', 'beat /biːt/'],
                        ],
                    },
                    {
                        "title": 'Production Tips',
                        "layout": 'list',
                        "items": [
                            '/ɪ/: Think of a quick, relaxed sound — it is short and unstretched.',
                            '/iː/: Stretch your lips into a wide smile and hold the vowel slightly longer.',
                            'Test: Say bit, then beat. You should feel your lips tighten on the second word.',
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Learn to distinguish short /ɪ/ from long /iː/ in words like git and release to avoid common pronunciation errors.',
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Sit — Seat',
                "translation": 'Sentarse — Asiento',
                "ipa_notation": '/sɪt/ — /siːt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Hit — Heat',
                "translation": 'Golpear — Calor',
                "ipa_notation": '/hɪt/ — /hiːt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Live — Leave',
                "translation": 'Vivir — Irse / Salir',
                "ipa_notation": '/lɪv/ — /liːv/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which word contains the LONG /iː/ sound (as in 'seat')?",
                "correct_answer": 'release',
                "options": {
                    "a": 'bit',
                    "b": 'git',
                    "c": 'release',
                    "d": 'fix',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Explosive Plosives — The /p/, /t/, and /k/ Sounds',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'What Is Aspiration?',
                        "layout": 'text',
                        "paragraphs": [
                            'Plosive consonants (also called stops) are sounds where airflow is completely blocked, then released as a small burst. English has three voiceless plosives: /p/, /t/, and /k/.',
                            "When /p/, /t/, /k/ appear at the start of a stressed syllable, a puff of air follows the release. Hold a sheet of paper in front of your mouth: it should move on 'pen' but barely on 'spin'.",
                        ],
                    },
                    {
                        "title": 'The Three Voiceless Plosives',
                        "layout": 'table',
                        "headers": ['Sound', 'Place of articulation', 'Tech words'],
                        "rows": [
                            ['/p/', 'Both lips pressed together (bilabial)', 'push, pull, patch, pipeline'],
                            ['/t/', 'Tongue tip on the ridge behind upper teeth (alveolar)', 'test, token, type, timeout'],
                            ['/k/', 'Back of tongue on soft palate (velar)', 'code, commit, cache, cluster'],
                        ],
                    },
                    {
                        "title": 'Aspiration Rules',
                        "layout": 'list',
                        "items": [
                            'Aspirated (puff of air): at the start of a stressed syllable: push, test, code.',
                            'Unaspirated (no puff): after /s/ — no aspiration: sprint, stack, script.',
                            'Common error: Spanish /p/, /t/, /k/ are never aspirated — English always aspirates them at word/syllable start.',
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Master the aspiration and air release of English plosives like p, t, and k to speak with clear articulation.',
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Push the code to production.',
                "translation": 'Sube el código a producción.',
                "ipa_notation": '/pʊʃ ðə koʊd tə prəˈdʌkʃən/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Take time to test the pipeline.',
                "translation": 'Tómate tiempo para probar el pipeline.',
                "ipa_notation": '/teɪk taɪm tə tɛst ðə ˈpaɪplaɪn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Compile, commit, and keep iterating.',
                "translation": 'Compila, haz commit y sigue iterando.',
                "ipa_notation": '/kəmˈpaɪl kəˈmɪt ænd kiːp ˈɪtəreɪtɪŋ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "In English, /p/, /t/, /k/ at the start of a stressed syllable are 'aspirated'. What does this mean?",
                "correct_answer": 'A small burst of air follows the consonant.',
                "options": {
                    "a": 'The consonant is silent.',
                    "b": 'A small burst of air follows the consonant.',
                    "c": 'You hold your breath before the sound.',
                    "d": 'The following vowel is always long.',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'The Aspirated /h/ — Pure Air Friction',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'English /h/ vs. Spanish J',
                        "layout": 'table',
                        "headers": ['Sound', 'Articulation', 'Voice', 'Example'],
                        "rows": [
                            ['English /h/', 'Open glottis, free airflow, no friction', 'None', 'hello /həˈloʊ/, host /hoʊst/'],
                            ['Spanish J', 'Back of tongue pressed to soft palate, friction', 'None', 'jefe, joven, caja'],
                        ],
                    },
                    {
                        "title": 'Silent H Words',
                        "layout": 'list',
                        "items": [
                            'hour → /ˈaʊər/ — the H is silent.',
                            'honest → /ˈɒnɪst/ — the H is silent.',
                            'heir → /ɛr/ — the H is silent.',
                            'vehicle → /ˈviːɪkəl/ — the H is silent.',
                        ],
                    },
                    {
                        "title": 'Production Guide',
                        "layout": 'list',
                        "items": [
                            'Open your mouth slightly and breathe out, as if you are fogging a mirror.',
                            'Keep your throat completely relaxed — no tension, no rasp.',
                            'Practice: heat, help, hybrid, HTTP — all start with the same gentle breath.',
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Learn to produce the relaxed, unvoiced aspirated /h/ sound smoothly without Spanish throat tension.',
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Hello, I am having trouble with this bug.',
                "translation": 'Hola, tengo problemas con este error.',
                "ipa_notation": '/həˈloʊ aɪ æm ˈhævɪŋ ˈtrʌbəl wɪð ðɪs bʌɡ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The server is hosted on our hybrid cloud.',
                "translation": 'El servidor está alojado en nuestra nube híbrida.',
                "ipa_notation": '/ðə ˈsɜːrvər ɪz ˈhoʊstɪd ɒn ˈaʊər ˈhaɪbrɪd klaʊd/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'How many hours did you spend on this feature?',
                "translation": '¿Cuántas horas dedicaste a esta funcionalidad?',
                "ipa_notation": '/haʊ ˈmɛni ˈaʊərz dɪd juː spɛnd ɒn ðɪs ˈfiːtʃər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "The English /h/ in 'hello' and 'house' is best described as:",
                "correct_answer": 'A relaxed, gentle rush of air with no throat tension.',
                "options": {
                    "a": "A guttural, raspy sound similar to the Spanish 'J'.",
                    "b": 'A relaxed, gentle rush of air with no throat tension.',
                    "c": "A silent letter, as in 'hour'.",
                    "d": 'A nasal sound produced at the back of the mouth.',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'The Final /m/ — Closing Your Lips',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Articulation Steps',
                        "layout": 'list',
                        "items": [
                            'Step 1: Bring both lips together and seal them completely.',
                            'Step 2: Voice the sound from your vocal cords — you should feel a buzzing in your nose and lips.',
                            'Step 3: Hold the lip closure for a brief moment at the end of the word before releasing.',
                            'Common error: Opening the lips too early and adding a vowel sound: team sounds like tee-ma.',
                        ],
                    },
                    {
                        "title": '/m/ in Technical Words',
                        "layout": 'table',
                        "headers": ['Word', 'IPA', 'Final /m/ context'],
                        "rows": [
                            ['team', '/tiːm/', 'Long vowel + sealed lips'],
                            ['program', '/ˈproʊɡræm/', 'Short /æ/ then sealed lips'],
                            ['algorithm', '/ˈælɡərɪðəm/', 'Unstressed /əm/ at end'],
                            ['stream', '/striːm/', 'Consonant cluster + final /m/'],
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Perfect your pronunciation of words ending in m by closing your lips completely to sound natural.',
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'What is your name and your team?',
                "translation": '¿Cuál es tu nombre y tu equipo?',
                "ipa_notation": '/wɒt ɪz jɔːr neɪm ænd jɔːr tiːm/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The program takes time to run.',
                "translation": 'El programa tarda tiempo en ejecutarse.',
                "ipa_notation": '/ðə ˈproʊɡræm teɪks taɪm tə rʌn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Sometimes the algorithm finds a better path.',
                "translation": 'A veces el algoritmo encuentra un camino mejor.',
                "ipa_notation": '/ˈsʌmtaɪmz ðiː ˈælɡərɪðəm faɪndz ə ˈbɛtər pæθ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Complete the IPA transcription for 'team': /tiː______/",
                "correct_answer": 'm',
                "options": None,
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'The -ed Endings — /t/, /d/, and /ɪd/',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'The Three Rules',
                        "layout": 'table',
                        "headers": ['Pronunciation', 'Rule', 'Tech verb examples'],
                        "rows": [
                            ['/t/', 'Base form ends in a voiceless consonant: /p/, /f/, /s/, /ʃ/, /k/, /tʃ/', 'pushed, cached, worked, patched'],
                            ['/d/', 'Base form ends in a voiced consonant or vowel: /b/, /g/, /v/, /z/, /m/, /n/, /l/, /r/, + all vowels', 'pulled, merged, reviewed, cloned, called'],
                            ['/ɪd/', 'Base form already ends in /t/ or /d/ — an extra syllable is added', 'committed, tested, started, uploaded, deleted'],
                        ],
                    },
                    {
                        "title": 'Why Does This Happen?',
                        "layout": 'list',
                        "items": [
                            'push → pushed — ends in /ʃ/ (voiceless) → /t/',
                            'merge → merged — ends in /dʒ/ (voiced) → /d/',
                            'commit → committed — ends in /t/ → /ɪd/',
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Master the three pronunciations of regular past simple -ed endings: /t/, /d/, and /ɪd/.',
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'She worked on the API all morning. (worked → /t/)',
                "translation": 'Ella trabajó en la API toda la mañana. (-ed = /t/ seco)',
                "ipa_notation": '/ʃiː wɜːrkt ɒn ðiː ˌeɪpiːˈaɪ ɔːl ˈmɔːrnɪŋ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'He played the demo video for the client. (played → /d/)',
                "translation": 'Él mostró el vídeo demo al cliente. (-ed = /d/ suave)',
                "ipa_notation": '/hiː pleɪd ðə ˈdɛmoʊ ˈvɪdioʊ fər ðə ˈklaɪənt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'The server wanted more memory. (wanted → /ɪd/)',
                "translation": 'El servidor necesitaba más memoria. (-ed = /ɪd/ sílaba extra)',
                "ipa_notation": '/ðə ˈsɜːrvər ˈwɒntɪd mɔːr ˈmɛməri/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "How is the '-ed' suffix pronounced in 'started'?",
                "correct_answer": '/ɪd/ — it adds an extra syllable.',
                "options": {
                    "a": '/t/ — a dry, unvoiced ending.',
                    "b": '/d/ — a soft, voiced ending.',
                    "c": '/ɪd/ — it adds an extra syllable.',
                    "d": "The '-ed' is completely silent.",
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'The "Dark L" — Pronouncing L after a Vowel',
            "explanation": {
                "intro": '',
                "sections": [
                    {
                        "title": 'Light L vs. Dark L',
                        "layout": 'table',
                        "headers": ['Type', 'Position', 'Mouth shape', 'Examples'],
                        "rows": [
                            ['Light L /l/', 'Before a vowel (word/syllable start)', 'Tongue tip on alveolar ridge, back of tongue low', 'level, launch, link, load'],
                            ['Dark L /ɫ/', 'After a vowel or at syllable end', 'Tongue tip on ridge + back of tongue raised toward soft palate', 'call, tool, pull, null, full, false'],
                        ],
                    },
                    {
                        "title": 'How to Produce the Dark L',
                        "layout": 'list',
                        "items": [
                            'Step 1: Place your tongue tip on the alveolar ridge (same as light L).',
                            'Step 2: Simultaneously pull the back of your tongue upward toward the soft palate (velum). This creates a deep, resonant, vowel-like quality.',
                            'Step 3: Voicing continues throughout.',
                            "Key feeling: The dark L should almost sound like a 'w' or a deep 'oo'. Example: tool → /tuːɫ/.",
                        ],
                    },
                ],
            },
            "type": LessonType.PHONETICS,
            "category": LessonType.PHONETICS,
            "description": 'Master the deep, resonant Dark L sound used after vowels in words like call, tool, and full.',
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'Please call the backend team.',
                "translation": 'Por favor llama al equipo de backend.',
                "ipa_notation": '/pliːz kɔːl ðə ˈbækˌɛnd tiːm/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'This tool is cool and very useful.',
                "translation": 'Esta herramienta es genial y muy útil.',
                "ipa_notation": '/ðɪs tuːl ɪz kuːl ænd ˈvɛri ˈjuːsfəl/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Pull the full version from the remote.',
                "translation": 'Descarga la versión completa del remoto.',
                "ipa_notation": '/pʊl ðə fʊl ˈvɜːrʒən frɒm ðə rɪˈmoʊt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'In which word does the DARK L (ɫ) appear?',
                "correct_answer": 'call',
                "options": {
                    "a": 'light',
                    "b": 'level',
                    "c": 'launch',
                    "d": 'call',
                },
                "order_index": 1,
            },
        ],
    },
]
