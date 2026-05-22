# a1_vocabulary.py — Enriched plain-text JSON seed data
# Cleaned programmatically to comply with strict Separation of Concerns.

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

A1_VOCABULARY_LESSONS: list[dict] = [
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Numbers, Years & Decimals — Counting & Data',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master numbers, decimals (dots), thousands (commas), and how to read years and phone numbers.',
            "explanation": {
                "intro": 'Master how to read numbers, decimals, and dates in English. In English, punctuation rules are different from Spanish.',
                "sections": [
                    {
                        "title": 'Number Systems & Time',
                        "subsections": [
                            {
                                "title": 'Units (0-9)',
                                "layout": 'grid',
                                "items": [
                                    "**0** zero | /ˈzɪəroʊ/ | (cero)",
                                    "**1** one | /wʌn/ | (uno)",
                                    "**2** two | /tuː/ | (dos)",
                                    "**3** three | /θriː/ | (tres)",
                                    "**4** four | /fɔːr/ | (cuatro)",
                                    "**5** five | /faɪv/ | (cinco)",
                                    "**6** six | /sɪks/ | (seis)",
                                    "**7** seven | /ˈsɛvən/ | (siete)",
                                    "**8** eight | /eɪt/ | (ocho)",
                                    "**9** nine | /naɪn/ | (nueve)"
                                ]
                            },
                            {
                                "title": 'Teens (10-19)',
                                "layout": 'grid',
                                "items": [
                                    "**10** ten | /tɛn/ | (diez)",
                                    "**11** eleven | /ɪˈlɛvən/ | (once)",
                                    "**12** twelve | /twɛlv/ | (doce)",
                                    "**13** thirteen | /ˌθɜːrˈtiːn/ | (trece)",
                                    "**14** fourteen | /ˌfɔːrˈtiːn/ | (catorce)",
                                    "**15** fifteen | /ˌfɪfˈtiːn/ | (quince)",
                                    "**16** sixteen | /ˌsɪksˈtiːn/ | (dieciséis)",
                                    "**17** seventeen | /ˌsɛvənˈtiːn/ | (diecisiete)",
                                    "**18** eighteen | /ˌeɪˈtiːn/ | (dieciocho)",
                                    "**19** nineteen | /ˌnaɪnˈtiːn/ | (diecinueve)"
                                ]
                            },
                            {
                                "title": 'Decades & Larger Scales',
                                "layout": 'table',
                                "headers": ['Scale', 'Number Pattern', 'Pronunciation'],
                                "rows": [
                                    ['Tens / Decades', '`20, 30, 40, 50...`', '`twenty`, `thirty`, `forty`, `fifty`, `sixty`, `seventy`, `eighty`, `ninety`'],
                                    ['Hundreds (100+)', '`100, 150, 900`', '`one hundred`, `one hundred and fifty`, `nine hundred`'],
                                    ['Thousands & Millions', '`1,500 / 1,000,000`', '`one thousand five hundred`, `one million`']
                                ]
                            },
                            {
                                "title": 'Telling the Time',
                                "layout": 'table',
                                "headers": ['Time Pattern', 'Formula / Rule', 'Example in English'],
                                "rows": [
                                    ["O'clock (Exact hour)", "Hour + `o'clock`", "It is `8 o'clock` (Son las 8 en punto)"],
                                    ['Half past (30 mins)', '`half past` + hour', "It is `half past three` (3:30)"],
                                    ['Quarter past (15 mins)', '`quarter past` + hour', "It is `quarter past ten` (10:15)"],
                                    ['Quarter to (15 mins before)', '`quarter to` + next hour', "It is `quarter to five` (4:45)"],
                                    ['AM / PM Conventions', 'Ante / Post Meridiem', '`9:00 AM` (morning) vs `9:00 PM` (night)']
                                ]
                            },
                            {
                                "title": 'Dates & Decimal Conventions',
                                "layout": 'list',
                                "items": [
                                    "Read years in two parts before 2000: `1999` is **nineteen ninety-nine**.",
                                    "For years 2000-2009, say **two thousand and [number]**: `2005` is **two thousand and five**.",
                                    "For years 2010 onwards, say **twenty-ten**, **twenty-twenty-six**, etc.",
                                    "Decimals use a dot (point): `1.5` is **one point five**, while thousands use a comma: `1,500` is **one thousand five hundred**."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 4,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'The system has one thousand, five hundred and twenty-three active users.',
                "translation": 'El sistema tiene mil quinientos veintitrés usuarios activos.',
                "ipa_notation": '/ðə ˈsɪstəm hæz wʌn ˈθaʊzənd faɪv ˈhʌndrəd ænd ˌtwɛnti θriː ˈæktɪv ˈjuːzərz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The average response time is one point five seconds.',
                "translation": 'El tiempo de respuesta promedio es de uno coma cinco segundos.',
                "ipa_notation": '/ðiː ˈævərɪdʒ rɪˈspɑːns taɪm ɪz wʌn pɔɪnt faɪv ˈsɛkəndz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'The Apollo Eleven mission landed on the moon in nineteen sixty-nine.',
                "translation": 'La misión Apolo Once aterrizó en la luna en mil novecientos sesenta y nueve.',
                "ipa_notation": '/ðiː əˈpɑːloʊ ɪˈlɛvən ˈmɪʃən ˈlændɪd ɑːn ðə muːn ɪn ˌnaɪnˈtiːn ˈsɪksti naɪn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "How do you say the year '2005' in English?",
                "correct_answer": 'two thousand and five',
                "options": {
                    "a": 'twenty oh-five',
                    "b": 'two thousand and five',
                    "c": 'two zero zero five',
                    "d": 'twenty hundred five',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Colors — Describing the World (and the UI)',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn essential colors and how to use them as adjectives to describe UI elements and objects.',
            "explanation": {
                "intro": 'Learn essential colors and how to use them as adjectives to describe UI elements and objects.',
                "sections": [
                    {
                        "title": 'Color Systems & Design Conventions',
                        "subsections": [
                            {
                                "title": 'The Didactic Color Wheel',
                                "layout": 'table',
                                "headers": ['Category', 'Colors Included', 'Visual / Meaning Context'],
                                "rows": [
                                    ['Primary Colors', '`Red` / `Yellow` / `Blue`', 'Foundational base colors of any design palette.'],
                                    ['Secondary Colors', '`Green` / `Orange` / `Purple`', 'Created by mixing primary colors (e.g. Blue + Yellow = Green).'],
                                    ['Tertiary Colors', '`Teal` / `Amber` / `Indigo` / `Violet` / `Magenta`', 'Mix of primary and secondary; very common in modern SaaS branding.']
                                ]
                            },
                            {
                                "title": 'UI/UX Semantic Color System',
                                "layout": 'table',
                                "headers": ['UI Color', 'SaaS Convention', 'Example Application'],
                                "rows": [
                                    ['`Red`', 'Error / Danger / Destructive', 'Delete buttons, form validation alerts, connection drop warnings.'],
                                    ['`Green`', 'Success / Saved / Positive', 'Active user badges, database synced confirmations, success popups.'],
                                    ['`Blue`', 'Primary Action / Info', 'Primary hyperlinks, active navigation tabs, informative tooltips.'],
                                    ['`Yellow` / `Gold`', 'Warning / Alert / Pending', 'Pending review badges, storage limits, deprecation notices.'],
                                    ['`Gray` / `Slate`', 'Neutral / Disabled / Inactive', 'Secondary buttons, inactive fields, placeholder texts.']
                                ]
                            },
                            {
                                "title": 'Color Grammar Rules',
                                "layout": 'list',
                                "items": [
                                    "Colors act as adjectives and always go **BEFORE the noun**: '*a blue screen*', '*three red buttons*'.",
                                    "Adjectives in English are **never pluralized**: '*five red buttons*' (NOT *five reds buttons*).",
                                    "Use **light** and **dark** modifiers to specify tone: '*light blue*' (azul claro) or '*dark green*' (verde oscuro)."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 5,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'The button is blue and the background is white.',
                "translation": 'El botón es azul y el fondo es blanco.',
                "ipa_notation": '/ðə ˈbʌtən ɪz bluː ænd ðə ˈbækˌɡraʊnd ɪz waɪt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The error messages are red, and the success messages are green.',
                "translation": 'Los mensajes de error son rojos y los mensajes de éxito son verdes.',
                "ipa_notation": '/ðiː ˈɛrər ˈmɛsɪdʒɪz ɑːr rɛd ænd ðə səkˈsɛs ˈmɛsɪdʒɪz ɑːr ɡriːn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Is the loading spinner yellow or orange?',
                "translation": '¿El ícono de carga es amarillo o naranja?',
                "ipa_notation": '/ɪz ðə ˈloʊdɪŋ ˈspɪnər ˈjɛloʊ ɔːr ˈɔːrɪndʒ/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Complete the sentence: 'Stop signs are ___ and warning signs are ___.'",
                "correct_answer": 'red / yellow',
                "options": None,
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Countries, Nationalities & Languages — Global Teams',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": "Learn origins, nationalities, and the rule for 'the' with republic/plural country names.",
            "explanation": {
                "intro": 'Learn how to refer to origins, nationalities, and languages, which is essential for working in global tech teams.',
                "sections": [
                    {
                        "title": 'Global Teams Directory',
                        "subsections": [
                            {
                                "title": 'Europe Directory (Europe — Demonym: European / Europeo)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**Austria**', '`German`', '`Austrian`'],
                                    ['**Belgium**', '`Dutch / French`', '`Belgian`'],
                                    ['**France**', '`French`', '`French`'],
                                    ['**Germany**', '`German`', '`German`'],
                                    ['**Greece**', '`Greek`', '`Greek`'],
                                    ['**Ireland**', '`English / Irish`', '`Irish`'],
                                    ['**Italy**', '`Italian`', '`Italian`'],
                                    ['**Netherlands**', '`Dutch`', '`Dutch`'],
                                    ['**Norway**', '`Norwegian`', '`Norwegian`'],
                                    ['**Poland**', '`Polish`', '`Polish`'],
                                    ['**Portugal**', '`Portuguese`', '`Portuguese`'],
                                    ['**Spain**', '`Spanish`', '`Spanish`'],
                                    ['**Sweden**', '`Swedish`', '`Swedish`'],
                                    ['**Switzerland**', '`German / French / Italian`', '`Swiss`'],
                                    ['**The United Kingdom**', '`English`', '`British`']
                                ]
                            },
                            {
                                "title": 'North America Directory (North America — Demonym: North American / Norteamericano)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**Canada**', '`English / French`', '`Canadian`'],
                                    ['**Mexico**', '`Spanish`', '`Mexican`'],
                                    ['**The United States**', '`English`', '`American`']
                                ]
                            },
                            {
                                "title": 'Central America & Caribbean Directory (Central America — Demonym: Central American / Centroamericano)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**Costa Rica**', '`Spanish`', '`Costa Rican`'],
                                    ['**Cuba**', '`Spanish`', '`Cuban`'],
                                    ['**Dominican Republic**', '`Spanish`', '`Dominican`'],
                                    ['**El Salvador**', '`Spanish`', '`Salvadoran`'],
                                    ['**Guatemala**', '`Spanish`', '`Guatemalan`'],
                                    ['**Honduras**', '`Spanish`', '`Honduran`'],
                                    ['**Jamaica**', '`English`', '`Jamaican`'],
                                    ['**Nicaragua**', '`Spanish`', '`Nicaraguan`'],
                                    ['**Panama**', '`Spanish`', '`Panamanian`']
                                ]
                            },
                            {
                                "title": 'South America Directory (South America — Demonym: South American / Sudamericano)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**Argentina**', '`Spanish`', '`Argentine / Argentinian`'],
                                    ['**Bolivia**', '`Spanish`', '`Bolivian`'],
                                    ['**Brazil**', '`Portuguese`', '`Brazilian`'],
                                    ['**Chile**', '`Spanish`', '`Chilean`'],
                                    ['**Colombia**', '`Spanish`', '`Colombian`'],
                                    ['**Ecuador**', '`Spanish`', '`Ecuadorian`'],
                                    ['**Paraguay**', '`Spanish`', '`Paraguayan`'],
                                    ['**Peru**', '`Spanish`', '`Peruvian`'],
                                    ['**Uruguay**', '`Spanish`', '`Uruguayan`'],
                                    ['**Venezuela**', '`Spanish`', '`Venezuelan`']
                                ]
                            },
                            {
                                "title": 'Asia Directory (Asia — Demonym: Asian / Asiático)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**China**', '`Mandarin`', '`Chinese`'],
                                    ['**India**', '`Hindi / English`', '`Indian`'],
                                    ['**Indonesia**', '`Indonesian`', '`Indonesian`'],
                                    ['**Israel**', '`Hebrew`', '`Israeli`'],
                                    ['**Japan**', '`Japanese`', '`Japanese`'],
                                    ['**Malaysia**', '`Malay`', '`Malaysian`'],
                                    ['**Pakistan**', '`Urdu / English`', '`Pakistani`'],
                                    ['**Philippines**', '`Tagalog / English`', '`Filipino`'],
                                    ['**Saudi Arabia**', '`Arabic`', '`Saudi / Saudi Arabian`'],
                                    ['**Singapore**', '`English / Malay / Mandarin`', '`Singaporean`'],
                                    ['**South Korea**', '`Korean`', '`Korean`'],
                                    ['**Thailand**', '`Thai`', '`Thai`'],
                                    ['**Turkey**', '`Turkish`', '`Turkish`'],
                                    ['**United Arab Emirates**', '`Arabic`', '`Emirati`'],
                                    ['**Vietnam**', '`Vietnamese`', '`Vietnamese`']
                                ]
                            },
                            {
                                "title": 'Africa & Oceania Directory (Africa & Oceania — Demonyms: African / Africano, Oceanian / Oceánico)',
                                "layout": 'table',
                                "headers": ['Country', 'Language Spoken', 'Nationality (Demonym)'],
                                "rows": [
                                    ['**Algeria**', '`Arabic / Berber`', '`Algerian`'],
                                    ['**Australia**', '`English`', '`Australian`'],
                                    ['**Egypt**', '`Arabic`', '`Egyptian`'],
                                    ['**Ethiopia**', '`Amharic`', '`Ethiopian`'],
                                    ['**Fiji**', '`English / Fijian`', '`Fijian`'],
                                    ['**Ghana**', '`English`', '`Ghanaian`'],
                                    ['**Kenya**', '`Swahili / English`', '`Kenyan`'],
                                    ['**Madagascar**', '`Malagasy / French`', '`Madagasy`'],
                                    ['**Morocco**', '`Arabic / Berber`', '`Moroccan`'],
                                    ['**New Zealand**', '`English / Māori`', '`New Zealander`'],
                                    ['**Nigeria**', '`English`', '`Nigerian`'],
                                    ['**Papua New Guinea**', '`English / Tok Pisin`', '`Papua New Guinean`'],
                                    ['**Senegal**', '`French`', '`Senegalese`'],
                                    ['**South Africa**', '`English / Zulu / Xhosa`', '`South African`'],
                                    ['**Uganda**', '`English / Swahili`', '`Ugandan`']
                                ]
                            },
                            {
                                "title": 'Grammar Rules: Plural Countries & The Article',
                                "layout": 'list',
                                "items": [
                                    "Always capitalize country names, nationalities, and languages: **German**, **Spanish**, **the United States**.",
                                    "Use the article **the** for countries that are plural unions, collections of islands, or contain *Kingdom*, *Republic*, or *States*: **The United States**, **The United Kingdom**, **The Netherlands**.",
                                    "Do not use **the** for single-word country names: **Germany**, **France**, **Japan**, **Brazil**."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 6,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'She is Venezuelan, but she works for a company in the United States.',
                "translation": 'Ella es venezolana, pero trabaja para una compañía en los Estados Unidos.',
                "ipa_notation": '/ʃiː ɪz ˌvɛnɪˈzweɪlən bʌt ʃiː wɜːrks fər ə ˈkʌmpəni ɪn ðiː jʊˈnaɪtɪd steɪts/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The developer is Spanish, but the documentation is in English.',
                "translation": 'El desarrollador es español, pero la documentación está en inglés.',
                "ipa_notation": '/ðə dɪˈvɛləpər ɪz ˈspænɪʃ bʌt ðə ˌdɑːkjʊmɛnˈteɪʃən ɪz ɪn ˈɪŋɡlɪʃ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Do you speak any language other than English and Spanish?',
                "translation": '¿Hablas algún idioma además del inglés y el español?',
                "ipa_notation": '/duː juː spiːk ˈɛni ˈlæŋɡwɪdʒ ˈʌðər ðæn ˈɪŋɡlɪʃ ænd ˈspænɪʃ/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Which sentence uses the article 'the' correctly with a country name?",
                "correct_answer": 'She lives in the United Kingdom.',
                "options": {
                    "a": 'She lives in the France.',
                    "b": 'She lives in the United Kingdom.',
                    "c": 'She lives in the Venezuela.',
                    "d": 'She lives in the Japan.',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Jobs & Professions — Tech Roles & More',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": "Learn job titles and the golden rule: always use 'a/an' before a profession in English.",
            "explanation": {
                "intro": 'Learn common job roles and titles, and the absolute grammatical rules for introducing professions in English.',
                "sections": [
                    {
                        "title": 'Tech Roles & Professional Grammar',
                        "subsections": [
                            {
                                "title": 'Classic & Modern IT Roles',
                                "layout": 'table',
                                "headers": ['Tech Role', 'Primary Responsibilities', 'SaaS Context'],
                                "rows": [
                                    ['**Software Engineer (SWE)**', 'Writes backend/frontend code, designs databases, maintains systems.', '`I am a Software Engineer at Stripe.`'],
                                    ['**Product Manager (PM)**', 'Defines product features, roadmaps, coordinates engineering and design.', '`She is a PM for the checkout team.`'],
                                    ['**UX/UI Designer**', 'Creates visual designs, wireframes, conducts user research and tests.', '`Our UX designer created the visual prototype.`'],
                                    ['**DevOps Specialist**', 'Manages server deployments, CI/CD pipelines, cloud architectures.', '`He works as a DevOps specialist on AWS.`'],
                                    ['**QA Tester**', 'Tests applications for bugs, writes automated end-to-end tests.', '`The QA tester caught the rendering issue.`']
                                ]
                            },
                            {
                                "title": 'Professional Grammar (A vs. An)',
                                "layout": 'list',
                                "items": [
                                    "Rule: Singular job titles must always be preceded by an indefinite article: '*I am a developer*' (NOT *I am developer*).",
                                    "Use **a** before consonant sounds: '*a developer*', '*a designer*', '*a product manager*'.",
                                    "Use **an** before vowel sounds: '*an engineer*', '*an analyst*', '*an IT specialist*'."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 7,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I am a software engineer at a fintech startup in Caracas.',
                "translation": 'Soy ingeniero de software en una startup fintech en Caracas.',
                "ipa_notation": '/aɪ æm ə ˈsɒftˌwɛr ˌɛndʒɪˈnɪər æt ə ˈfɪntɛk ˈstɑːrtʌp ɪn kəˈrækəs/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She is not a QA engineer; she is a DevOps specialist.',
                "translation": 'Ella no es ingeniera QA; es especialista en DevOps.',
                "ipa_notation": '/ʃiː ɪz nɒt ə ˌkjuːˈeɪ ˌɛndʒɪˈnɪər ʃiː ɪz ə ˈdɛvɒps ˈspɛʃəlɪst/',
                "sentence_type": SentenceType.NEGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Are you a full-stack developer or a data scientist?',
                "translation": '¿Eres desarrollador full-stack o científico de datos?',
                "ipa_notation": '/ɑːr juː ə ˈfʊlstæk dɪˈvɛləpər ɔːr ə ˈdeɪtə ˈsaɪəntɪst/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Complete with the correct article: 'My brother is ___ architect and my sister is ___ UX designer.'",
                "correct_answer": 'an / a',
                "options": None,
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Food & Drinks — Fuel for the Day',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn essential vocabulary for meals, fruits, vegetables, meat, and common drinks.',
            "explanation": {
                "intro": 'Learn everyday food and drink vocabulary to help you navigate tech offices, cafeterias, and social lunches.',
                "sections": [
                    {
                        "title": 'Office Catering & Countability',
                        "subsections": [
                            {
                                "title": 'Office Snack & Beverage Directory',
                                "layout": 'table',
                                "headers": ['Snack / Beverage', 'Category', 'Countable?', 'Common Office Saying'],
                                "rows": [
                                    ['**Coffee**', 'Drink / Beverage', 'Uncountable', '`I need a cup of coffee before the standup.`'],
                                    ['**Water**', 'Drink / Hydration', 'Uncountable', '`Keep some water on your desk to stay hydrated.`'],
                                    ['**Apple / Banana**', 'Food / Fruit', 'Countable', '`I took an apple from the office kitchen.`'],
                                    ['**Sandwich**', 'Food / Lunch', 'Countable', '`Let\'s grab a sandwich during the lunch break.`'],
                                    ['**Salad**', 'Food / Healthy Option', 'Countable / Uncountable', '`She brought a fresh salad for lunch.`']
                                ]
                            },
                            {
                                "title": 'Countable vs. Uncountable Rules',
                                "layout": 'list',
                                "items": [
                                    "Use **a/an** or numbers with Countable foods: '*a sandwich*', '*an apple*', '*three cookies*'.",
                                    "Do NOT use **a/an** or numbers with Uncountable foods/drinks: '*some water*', '*some coffee*', '*some bread*'.",
                                    "To quantify uncountable items, use container phrases: '*a bottle of water*', '*a cup of tea*', '*a slice of bread*'."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 8,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I have coffee and two eggs for breakfast every morning.',
                "translation": 'Tomo café y dos huevos en el desayuno cada mañana.',
                "ipa_notation": '/aɪ hæv ˈkɒfi ænd tuː ɛɡz fər ˈbrɛkfəst ˈɛvri ˈmɔːrnɪŋ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'She drinks water and orange juice at the office.',
                "translation": 'Ella toma agua y jugo de naranja en la oficina.',
                "ipa_notation": '/ʃiː drɪŋks ˈwɔːtər ænd ˈɔːrɪndʒ dʒuːs æt ðə ˈɒfɪs/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Do you want an apple or a banana as a snack?',
                "translation": '¿Quieres una manzana o un cambur de merienda?',
                "ipa_notation": '/duː juː wɒnt æn ˈæpəl ɔːr ə bəˈnænə æz ə snæk/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which meal do you typically eat between 12:00 and 2:00 pm?',
                "correct_answer": 'Lunch',
                "options": {
                    "a": 'Breakfast',
                    "b": 'Lunch',
                    "c": 'Dinner',
                    "d": 'Snack',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Everyday Objects — Home & Office',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Master the vocabulary for common items around your house and on your work desk.',
            "explanation": {
                "intro": 'Master vocabulary for common tools, devices, and office equipment used daily in the workplace.',
                "sections": [
                    {
                        "title": 'Workspace Tools & Place Prepositions',
                        "subsections": [
                            {
                                "title": 'The Modern Workspace Directory',
                                "layout": 'table',
                                "headers": ['Object', 'Usage / Practical Purpose', 'Typical Location'],
                                "rows": [
                                    ['**Laptop**', 'Main machine for code, meetings, communication.', '`On the desk` or `in the bag`'],
                                    ['**Monitor**', 'External screen for displaying code and documentation.', '`Mounted on the desk` or `standing`'],
                                    ['**Keyboard & Mouse**', 'Text and cursor input for system control.', '`In front of the monitor`'],
                                    ['**Headphones**', 'Audio output for video calls and music blockout.', '`On your head` or `on the desk`'],
                                    ['**Desk & Chair**', 'Ergonomic workspace setup for long hours.', '`In the home office` or `company office`']
                                ]
                            },
                            {
                                "title": 'Object Pronouns & Location Prepositions',
                                "layout": 'list',
                                "items": [
                                    "Preposition **ON**: '*on the desk*', '*on the wall*' (contact with a surface).",
                                    "Preposition **UNDER**: '*under the desk*', '*under the chair*' (directly below).",
                                    "Singular objects use **it**: '*Where is the keyboard? It is on the desk*'.",
                                    "Plural objects use **they**: '*Where are the headphones? They are under the notebook*'."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 9,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'My laptop is on the desk next to the keyboard and the mouse.',
                "translation": 'Mi laptop está sobre el escritorio junto al teclado y al ratón.',
                "ipa_notation": '/maɪ ˈlæptɒp ɪz ɒn ðə dɛsk ˈnɛkst tə ðə ˈkiːbɔːrd ænd ðə maʊs/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'There is a cup of coffee on the table in the kitchen.',
                "translation": 'Hay una taza de café sobre la mesa en la cocina.',
                "ipa_notation": '/ðɛr ɪz ə kʌp əv ˈkɒfi ɒn ðə ˈteɪbəl ɪn ðə ˈkɪtʃɪn/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": "I can't find my keys. Are they in your bag?",
                "translation": 'No encuentro mis llaves. ¿Están en tu bolso?',
                "ipa_notation": '/aɪ kænt faɪnd maɪ kiːz — ɑːr ðeɪ ɪn jɔːr bæɡ/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.FILL_BLANK,
                "question": "Complete: 'I use a ___ to type code and a ___ to click on buttons.'",
                "correct_answer": 'keyboard / mouse',
                "options": None,
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Animals — Pets, Farm & Wild',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn the names of common animals, from house pets to wild creatures.',
            "explanation": {
                "intro": 'Learn animals vocabulary, useful for general conversations, analogies, and common tech branding.',
                "sections": [
                    {
                        "title": 'Animals in Tech Branding & Mascots',
                        "subsections": [
                            {
                                "title": 'The Tech Mascot Zoo',
                                "layout": 'table',
                                "headers": ['Animal Name', 'Associated Tech Brand / Mascot', 'Description of Brand'],
                                "rows": [
                                    ['**Python / Snake**', 'Python programming language', '`A powerful, clean coding language.`'],
                                    ['**Gopher**', 'Go (Golang) programming language', '`A fast, concurrent language built by Google.`'],
                                    ['**Whale**', 'Docker containerization engine', '`A platform for packaging applications in containers.`'],
                                    ['**Octocat**', 'GitHub version control platform', '`The mascot combining an octopus and a cat.`'],
                                    ['**Penguin (Tux)**', 'Linux operating system', '`The official open-source Linux kernel mascot.`']
                                ]
                            },
                            {
                                "title": 'Everyday Pets & Farm Animals',
                                "layout": 'list',
                                "items": [
                                    "**Dog**: Known as loyal domestic pets (e.g. '*The dog barked*').",
                                    "**Cat**: Independent household pet (e.g. '*The cat is sleeping under the monitor*').",
                                    "**Bird**: Feathered flying animal (e.g. '*A bird is singing outside the office window*').",
                                    "**Fish**: Aquatic animal (e.g. '*He keeps a goldfish in a bowl on his desk*')."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 10,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I have a dog and two cats at home.',
                "translation": 'Tengo un perro y dos gatos en casa.',
                "ipa_notation": '/aɪ hæv ə dɒɡ ænd tuː kæts æt hoʊm/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'The farm has ten cows, five horses, and many chickens.',
                "translation": 'La finca tiene diez vacas, cinco caballos y muchas gallinas.',
                "ipa_notation": '/ðə fɑːrm hæz tɛn kaʊz faɪv ˈhɔːrsɪz ænd ˈmɛni ˈtʃɪkɪnz/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Lions and tigers are wild animals that live in Africa and Asia.',
                "translation": 'Los leones y los tigres son animales salvajes que viven en África y Asia.',
                "ipa_notation": '/ˈlaɪənz ænd ˈtaɪɡərz ɑːr waɪld ˈænɪməlz ðət lɪv ɪn ˈæfrɪkə ænd ˈeɪʃə/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'Which of these is a pet, not a wild animal?',
                "correct_answer": 'rabbit',
                "options": {
                    "a": 'lion',
                    "b": 'bear',
                    "c": 'rabbit',
                    "d": 'snake',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Family & People — Who is in your life?',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": "Learn the vocabulary for family members (parents, siblings, relatives) and stages of life. Understand how to describe people's marital status and relationships.",
            "explanation": {
                "intro": 'Learn how to talk about family members, relatives, marital status, and the different stages of human life in professional and casual settings.',
                "sections": [
                    {
                        "title": 'Core Family & Life Stages',
                        "subsections": [
                            {
                                "title": 'Immediate Family (Parents & Siblings)',
                                "layout": 'table',
                                "headers": ['Family Member', 'Definition / Relationship', 'Example in Context'],
                                "rows": [
                                    ['**Parents**', 'Mother and father combined.', '`My parents live in Madrid.`'],
                                    ['**Mother / Father**', 'Female parent / Male parent.', '`Her mother is an architect; his father is a developer.`'],
                                    ['**Siblings**', 'Brothers and sisters combined.', '`Do you have any siblings?`'],
                                    ['**Brother / Sister**', 'Male sibling / Female sibling.', '`My brother works in QA; my sister is a PM.`'],
                                    ['**Spouse**', 'Husband or wife (formal/legal term).', '`His spouse is also a software engineer.`']
                                ]
                            },
                            {
                                "title": 'Extended Family & Relatives',
                                "layout": 'table',
                                "headers": ['Relative', 'Definition', 'Example'],
                                "rows": [
                                    ['**Grandparents**', 'Grandmother and grandfather.', '`My grandparents are retired.`'],
                                    ['**Uncle / Aunt**', 'Brother of parent / Sister of parent.', '`My uncle is a sysadmin; my aunt is a designer.`'],
                                    ['**Cousin**', 'Child of an uncle or aunt.', '`I have a cousin who lives in Canada.`'],
                                    ['**Nephew / Niece**', 'Son of sibling / Daughter of sibling.', '`My niece is learning Python.`']
                                ]
                            },
                            {
                                "title": 'Stages of Life & Relationships',
                                "layout": 'list',
                                "items": [
                                    "**Baby / Infant**: A very young child (0-1 years old): '*The baby is sleeping.*'",
                                    "**Child / Toddler**: A young human (1-12 years old): '*We have two children.*'",
                                    "**Teenager / Adolescent**: A person aged 13-19: '*She has a teenage son.*'",
                                    "**Adult**: A fully grown person: '*Only adults can access this system.*'",
                                    "**Elderly / Senior**: Polite term for old people: '*My grandfather is elderly but very active.*'"
                                ]
                            },
                            {
                                "title": 'Marital Status Terminology',
                                "layout": 'table',
                                "headers": ['Status', 'Meaning in Spanish', 'Context / Usage'],
                                "rows": [
                                    ['**Single**', 'Soltero/a', '`I am single and live alone.`'],
                                    ['**Married**', 'Casado/a', '`They got married last year.`'],
                                    ['**Divorced**', 'Divorciado/a', '`He is divorced but has a great relationship with his kids.`'],
                                    ['**Widowed**', 'Viudo/a', '`My grandmother is widowed.`']
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 11,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'My spouse and I are planning a trip to Europe next month.',
                "translation": 'Mi cónyuge y yo estamos planeando un viaje a Europa el próximo mes.',
                "ipa_notation": '/maɪ spaʊs ænd aɪ ɑːr ˈplænɪŋ ə trɪp tə ˈjʊərəp ˈnɛkst mʌnθ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'He has three siblings: two brothers and one sister.',
                "translation": 'Él tiene tres hermanos: dos hermanos y una hermana.',
                "ipa_notation": '/hiː hæz θriː ˈsɪblɪŋz — tuː ˈbrʌðərz ænd wʌn ˈsɪstər/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'Are your parents retired or do they still work?',
                "translation": '¿Tus padres están jubilados o todavía trabajan?',
                "ipa_notation": '/ɑːr jɔːr ˈpɛərənts rɪˈtaɪərd ɔːr duː ðeɪ stɪl wɜːrk/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": 'What is the gender-neutral term for husband or wife in a formal context?',
                "correct_answer": 'spouse',
                "options": {
                    "a": 'sibling',
                    "b": 'cousin',
                    "c": 'spouse',
                    "d": 'relative',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Places & Transport — Getting Around the City',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Learn the names of essential places in a city (hospital, bank, airport) and means of transportation (bus, train, flight).',
            "explanation": {
                "intro": 'Learn essential city locations and public transportation terminology to easily navigate urban environments and business travel.',
                "sections": [
                    {
                        "title": 'City Navigation',
                        "subsections": [
                            {
                                "title": 'Essential City Places',
                                "layout": 'table',
                                "headers": ['Place in the City', 'Purpose / Utility', 'Example'],
                                "rows": [
                                    ['**Airport**', 'Where airplanes land and take off for travel.', '`Let\'s meet at the airport terminal.`'],
                                    ['**Hospital**', 'Institution providing medical treatment.', '`There is a hospital near our office.`'],
                                    ['**Bank**', 'A financial institution for keeping money.', '`I need to go to the bank to deposit a check.`'],
                                    ['**Station (Train/Bus)**', 'Where public transport vehicles stop.', '`The train station is in the city center.`'],
                                    ['**Office building**', 'Where professional services are located.', '`Our company office is on the fifth floor.`'],
                                    ['**Supermarket**', 'Large self-service store selling food and household goods.', '`I buy groceries at the local supermarket.`']
                                ]
                            },
                            {
                                "title": 'Means of Transportation',
                                "layout": 'table',
                                "headers": ['Transport Mode', 'Verb Used', 'Typical Context'],
                                "rows": [
                                    ['**Bus**', '`take the bus` / `ride a bus`', '`I take the bus to commute to work every morning.`'],
                                    ['**Train / Subway**', '`take the train` / `catch the subway`', '`The subway is the fastest way to travel during rush hour.`'],
                                    ['**Flight / Airplane**', '`take a flight` / `fly`', '`He booked a direct flight to San Francisco for the tech conference.`'],
                                    ['**Car / Taxi**', '`drive a car` / `hail a taxi`', '`Let\'s hail a taxi; it is starting to rain.`'],
                                    ['**Bicycle / Bike**', '`ride a bike` / `cycle`', '`She rides her bike to the office to stay fit.`']
                                ]
                            },
                            {
                                "title": 'Prepositions with Transport',
                                "layout": 'list',
                                "items": [
                                    "Use **BY** for the mode of transport: '*by bus*', '*by train*', '*by car*', '*by plane*' (exception: '*on foot*').",
                                    "Use **ON** for larger public transport or two-wheelers: '*on a bus*', '*on a train*', '*on a plane*', '*on a bike*'.",
                                    "Use **IN** for enclosed private vehicles: '*in a car*', '*in a taxi*'."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 12,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'I commute to the office by train, but sometimes I take a taxi.',
                "translation": 'Viajo a la oficina en tren, pero a veces tomo un taxi.',
                "ipa_notation": '/aɪ kəˈmjuːt tə ðə ˈɒfɪs baɪ treɪn bʌt ˈsʌmtaɪmz aɪ teɪk ə ˈtæksi/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Is the new hospital close to the airport or the bus station?',
                "translation": '¿El nuevo hospital está cerca del aeropuerto o de la estación de autobuses?',
                "ipa_notation": '/ɪz ðə njuː ˈhɒspɪtəl kloʊs tə ðə ˈeərpɔːrt ɔːr ðə bʌs ˈsteɪʃən/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'We arrived at the airport three hours before our direct flight.',
                "translation": 'Llegamos al aeropuerto tres horas antes de nuestro vuelo directo.',
                "ipa_notation": '/wiː əˈraɪvd æt ðiː ˈeərpɔːrt θriː ˈaʊərz bɪˈfɔːr ˈaʊər dɪˈrɛkt flaɪt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "Complete the sentence: 'We usually travel to the tech conference ___ plane.'",
                "correct_answer": 'by',
                "options": {
                    "a": 'in',
                    "b": 'on',
                    "c": 'by',
                    "d": 'with',
                },
                "order_index": 1,
            },
        ],
    },
    {
        "level_code": 'A1',
        "meta": {
            "title": 'Basic Adjectives — Describing Things (Opposites)',
            "type": LessonType.VOCABULARY,
            "category": LessonCategory.VOCABULARY,
            "description": 'Expand your vocabulary quickly by learning the most common adjectives in opposite pairs: big/small, hot/cold, cheap/expensive, easy/difficult.',
            "explanation": {
                "intro": 'Adjectives allow you to qualify nouns and describe states. Learning them in opposite pairs is the fastest way to build your vocabulary.',
                "sections": [
                    {
                        "title": 'Core Adjective Opposites',
                        "subsections": [
                            {
                                "title": 'Physical Attributes',
                                "layout": 'grid',
                                "items": [
                                    "**Big / Small** | /ˈbɪɡ/ / /smɔːl/ | (Grande / Pequeño)",
                                    "**Hot / Cold** | /ˈhɒt/ / /koʊld/ | (Caliente / Frío)",
                                    "**Heavy / Light** | /ˈhɛvi/ / /laɪt/ | (Pesado / Ligero)",
                                    "**Clean / Dirty** | /ˈkliːn/ / /ˈdɜːrti/ | (Limpio / Sucio)"
                                ]
                            },
                            {
                                "title": 'Value, Cost & Ease',
                                "layout": 'grid',
                                "items": [
                                    "**Cheap / Expensive** | /ˈtʃiːp/ / /ɪkˈspɛnsɪv/ | (Barato / Caro)",
                                    "**Easy / Difficult** | /ˈiːzi/ / /ˈdɪfɪkəlt/ | (Fácil / Difícil)",
                                    "**Fast / Slow** | /ˈfɑːst/ / /sloʊ/ | (Rápido / Lento)",
                                    "**New / Old** | /ˈnjuː/ / /oʊld/ | (Nuevo / Viejo)"
                                ]
                            },
                            {
                                "title": 'Grammar Rules: Adjectives in English',
                                "layout": 'list',
                                "items": [
                                    "Adjectives in English are **never pluralized**: '*They are new laptops*' (NOT *They are news laptops*).",
                                    "Adjectives typically go **BEFORE the noun**: '*This is a difficult test*'.",
                                    "Adjectives go **AFTER the verb TO BE**: '*The server is expensive*'."
                                ]
                            }
                        ]
                    }
                ]
            },
            "order_index": 13,
            "is_published": True,
        },
        "examples": [
            {
                "phrase": 'This cheap keyboard is loud, but that expensive monitor is completely silent.',
                "translation": 'Este teclado barato es ruidoso, pero ese monitor caro es completamente silencioso.',
                "ipa_notation": '/ðɪs tʃiːp ˈkiːbɔːrd ɪz laʊd bʌt ðæt ɪkˈspɛnsɪv ˈmɒnɪtər ɪz kəmˈpliːtli ˈsaɪlənt/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 1,
            },
            {
                "phrase": 'Is the new software release easy to install, or is it difficult?',
                "translation": '¿La nueva versión del software es fácil de instalar o es difícil?',
                "ipa_notation": '/ɪz ðə njuː ˈsɒftwɛr rɪˈliːs ˈiːzi tuː ɪnˈstɔːl ɔːr ɪz ɪt ˈdɪfɪkəlt/',
                "sentence_type": SentenceType.INTERROGATIVE,
                "order_index": 2,
            },
            {
                "phrase": 'We need a fast internet connection because our current one is too slow.',
                "translation": 'Necesitamos una conexión a internet rápida porque la actual es demasiado lenta.',
                "ipa_notation": '/wiː niːd ə fɑːst ˈɪntərnɛt kəˈnɛkʃən bɪˈkɒz ˈaʊər ˈkʌrənt wʌn ɪz tuː sloʊ/',
                "sentence_type": SentenceType.AFFIRMATIVE,
                "order_index": 3,
            },
        ],
        "exercises": [
            {
                "type": ExerciseType.MULTIPLE_CHOICE,
                "question": "What is the opposite of 'expensive' in English?",
                "correct_answer": 'cheap',
                "options": {
                    "a": 'easy',
                    "b": 'clean',
                    "c": 'heavy',
                    "d": 'cheap',
                },
                "order_index": 1,
            },
        ],
    },
]
