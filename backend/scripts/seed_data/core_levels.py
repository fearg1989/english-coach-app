# core_levels.py — CEFR level definitions (A1 → C2)
# Cambridge CEFR framework — 6 proficiency levels.

LEVELS: list[dict] = [
    {
        "code": "A1",
        "name": "Beginner",
        "description": "Can understand and use familiar everyday expressions and very basic phrases.",
        "order_index": 1,
    },
    {
        "code": "A2",
        "name": "Elementary",
        "description": "Can understand sentences and frequently-used expressions related to immediate relevance.",
        "order_index": 2,
    },
    {
        "code": "B1",
        "name": "Intermediate",
        "description": "Can understand the main points of clear standard input on familiar matters.",
        "order_index": 3,
    },
    {
        "code": "B2",
        "name": "Upper Intermediate",
        "description": "Can understand the main ideas of complex text on both concrete and abstract topics.",
        "order_index": 4,
    },
    {
        "code": "C1",
        "name": "Advanced",
        "description": "Can understand a wide range of demanding, longer texts and recognise implicit meaning.",
        "order_index": 5,
    },
    {
        "code": "C2",
        "name": "Mastery",
        "description": "Can understand with ease virtually everything heard or read.",
        "order_index": 6,
    },
]
