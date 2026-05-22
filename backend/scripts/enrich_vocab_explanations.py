import sys
import os
import importlib

sys.path.insert(0, "/Users/ropa/Develop/english-coach-app/backend")

from app.models import ExerciseType, LessonCategory, LessonType, SentenceType

# Helper to format values nicely as Python literal structures
def format_val(val, indent=0):
    spacing = " " * indent
    if isinstance(val, dict):
        if not val:
            return "{}"
        items = []
        for k, v in val.items():
            formatted_v = format_val(v, indent + 4)
            items.append(f'{spacing}    "{k}": {formatted_v},')
        return "{\n" + "\n".join(items) + "\n" + spacing + "}"
    elif isinstance(val, list):
        if not val:
            return "[]"
        
        # If it's a list of primitive values (e.g. headers, items)
        if all(isinstance(x, (str, int, bool)) for x in val):
            items_str = ", ".join(repr(x) for x in val)
            if len(items_str) < 80:
                return f"[{items_str}]"
                
        # If it's a list of lists of strings (e.g. rows)
        if all(isinstance(row, list) and all(isinstance(x, (str, int, bool)) for x in row) for row in val):
            items = []
            for row in val:
                row_str = ", ".join(repr(x) for x in row)
                items.append(f'{spacing}    [{row_str}],')
            return "[\n" + "\n".join(items) + "\n" + spacing + "]"
        
        items = []
        for x in val:
            formatted_x = format_val(x, indent + 4)
            items.append(f'{spacing}    {formatted_x},')
        return "[\n" + "\n".join(items) + "\n" + spacing + "]"
    elif isinstance(val, str):
        # If string matches an Enum, output the Enum code instead of raw string
        if val == "grammar":
            return "LessonType.GRAMMAR"
        elif val == "phonetics":
            return "LessonType.PHONETICS"
        elif val == "vocabulary":
            return "LessonType.VOCABULARY"
        elif val == "verb_tenses":
            return "LessonCategory.VERB_TENSES"
        elif val == "modal_verbs":
            return "LessonCategory.MODAL_VERBS"
        elif val == "phrasal_verbs":
            return "LessonCategory.PHRASAL_VERBS"
        elif val == "prepositions":
            return "LessonCategory.PREPOSITIONS"
        elif val == "irregular_verbs":
            return "LessonCategory.IRREGULAR_VERBS"
        elif val == "general_grammar":
            return "LessonCategory.GENERAL_GRAMMAR"
        elif val == "verb_patterns":
            return "LessonCategory.VERB_PATTERNS"
        elif val == "conditionals":
            return "LessonCategory.CONDITIONALS"
        elif val == "passive_voice":
            return "LessonCategory.PASSIVE_VOICE"
        elif val == "reported_speech":
            return "LessonCategory.REPORTED_SPEECH"
        elif val == "connectors":
            return "LessonCategory.CONNECTORS"
        elif val == "collocations":
            return "LessonCategory.COLLOCATIONS"
        elif val == "multiple_choice":
            return "ExerciseType.MULTIPLE_CHOICE"
        elif val == "fill_blank":
            return "ExerciseType.FILL_BLANK"
        elif val == "pronunciation":
            return "ExerciseType.PRONUNCIATION"
        elif val == "affirmative":
            return "SentenceType.AFFIRMATIVE"
        elif val == "negative":
            return "SentenceType.NEGATIVE"
        elif val == "interrogative":
            return "SentenceType.INTERROGATIVE"
        
        return repr(val)
    elif isinstance(val, bool):
        return "True" if val else "False"
    elif val is None:
        return "None"
    else:
        return repr(val)

# Rich composite explanations matching your precise pedagogical guidelines
ENRICHED_EXPLANATIONS = {
    "Numbers, Years & Decimals — Counting & Data": {
        "intro": "Master how to read numbers, decimals, and dates in English. In English, punctuation rules are different from Spanish.",
        "sections": [
            {
                "title": "Counting System & Time in English",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: The Basics (0-19)",
                        "layout": "table",
                        "headers": ["Category", "Numbers & Forms", "English Words"],
                        "rows": [
                            ["Units (0-9)", "0, 1, 2, 3, 4, 5, 6, 7, 8, 9", "zero / oh, one, two, three, four, five, six, seven, eight, nine"],
                            ["Teens (10-19)", "10, 11, 12, 13, 14, 15, 16, 17, 18, 19", "ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"]
                        ]
                    },
                    {
                        "title": "Section 2: Decades, Hundreds & Large Scales",
                        "layout": "table",
                        "headers": ["Scale", "Number Pattern", "Example Pronunciation"],
                        "rows": [
                            ["Tens / Decades", "20, 30, 40, 50, 60, 70, 80, 90", "twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety"],
                            ["Hundreds (100+)", "100, 150, 900", "one hundred, one hundred and fifty, nine hundred"],
                            ["Thousands & Millions", "1,500 / 1,000,000", "one thousand five hundred, one million"]
                        ]
                    },
                    {
                        "title": "Section 3: Telling the Time",
                        "layout": "table",
                        "headers": ["Time Pattern", "Formula / Rule", "Example in English"],
                        "rows": [
                            ["O'clock (Exact hour)", "Hour + o'clock", "It is 8 o'clock (Son las 8 en punto)"],
                            ["Half past (30 mins)", "half past + hour", "It is half past three (3:30)"],
                            ["Quarter past (15 mins)", "quarter past + hour", "It is quarter past ten (10:15)"],
                            ["Quarter to (15 mins before)", "quarter to + next hour", "It is quarter to five (4:45)"],
                            ["AM / PM Conventions", "Ante / Post Meridiem", "9:00 AM (morning) vs 9:00 PM (night)"]
                        ]
                    },
                    {
                        "title": "Section 4: Dates and Years Rules",
                        "layout": "list",
                        "items": [
                            "Read years in two parts for dates before 2000: 1999 is 'nineteen ninety-nine'.",
                            "For years 2000-2009, say 'two thousand and [number]': 2005 is 'two thousand and five'.",
                            "For years 2010 onwards, you can say 'twenty-ten', 'twenty-twenty-six', etc.",
                            "Decimals use a dot (point): 1.5 is 'one point five', while thousands use a comma: 1,500 is 'one thousand five hundred'."
                        ]
                    }
                ]
            }
        ]
    },
    "Colors — Describing the World (and the UI)": {
        "intro": "Learn essential colors and how to use them as adjectives to describe UI elements and objects.",
        "sections": [
            {
                "title": "Color Theory & Design Conventions",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: The Color Wheel (Primary, Secondary, Tertiary)",
                        "layout": "table",
                        "headers": ["Category", "Colors included", "Visual / Meaning Context"],
                        "rows": [
                            ["Primary Colors", "Red, Yellow, Blue", "The foundational base colors of any design palette"],
                            ["Secondary Colors", "Green, Orange, Purple", "Created by mixing primary colors (e.g. Blue + Yellow = Green)"],
                            ["Tertiary Colors", "Teal, Amber, Indigo, Violet, Magenta", "Mix of a primary and a secondary color; very common in SaaS brandings"]
                        ]
                    },
                    {
                        "title": "Section 2: UI/UX Semantic Color System",
                        "layout": "table",
                        "headers": ["UI Color", "SaaS Convention", "Example Application"],
                        "rows": [
                            ["Red", "Error / Danger / Destructive", "Delete buttons, form validation alerts, connection drop warnings"],
                            ["Green", "Success / Saved / Positive", "Active user badges, database synced confirmations, purchase success"],
                            ["Blue", "Primary Action / Info", "Primary hyper-links, active tabs, information tooltips"],
                            ["Yellow / Gold", "Warning / Alert / Pending", "Pending review badges, storage limit warnings"],
                            ["Gray / Slate", "Neutral / Disabled / Inactive", "Secondary buttons, inactive fields, placeholder texts"]
                        ]
                    },
                    {
                        "title": "Section 3: Color Grammar Rules",
                        "layout": "list",
                        "items": [
                            "Colors act as adjectives and always go BEFORE the noun: 'a blue screen', 'three red buttons'.",
                            "Adjectives in English are never pluralized: 'five red buttons' (not 'reds buttons').",
                            "Light vs Dark modifiers: Use 'light blue' (azul claro) or 'dark green' (verde oscuro)."
                        ]
                    }
                ]
            }
        ]
    },
    "Countries, Nationalities & Languages — Global Teams": {
        "intro": "Learn how to refer to origins, nationalities, and languages, which is essential for working in global tech teams.",
        "sections": [
            {
                "title": "Global Geography & Demonyms",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: Continents & Countries Directory",
                        "layout": "table",
                        "headers": ["Continent", "Country", "Language Spoken", "Nationality (Demonym)"],
                        "rows": [
                            ["Europe", "Spain", "Spanish", "Spanish"],
                            ["Europe", "Germany", "German", "German"],
                            ["Europe", "The United Kingdom", "English", "British"],
                            ["Europe", "France", "French", "French"],
                            ["Americas", "The United States", "English", "American"],
                            ["Americas", "Brazil", "Portuguese", "Brazilian"],
                            ["Americas", "Mexico", "Spanish", "Mexican"],
                            ["Americas", "Colombia", "Spanish", "Colombian"],
                            ["Asia", "Japan", "Japanese", "Japanese"],
                            ["Asia", "India", "Hindi, English", "Indian"],
                            ["Africa", "South Africa", "English, Zulu, Xhosa", "South African"],
                            ["Oceania", "Australia", "English", "Australian"]
                        ]
                    },
                    {
                        "title": "Section 2: Grammar Rules: Plural Countries & The Article",
                        "layout": "list",
                        "items": [
                            "Always capitalize country names, nationalities, and languages: 'German', 'Spanish', 'the United States'.",
                            "Use the article 'the' for countries that are plural unions, collections of islands, or contain 'Kingdom', 'Republic', or 'States': 'The United States', 'The United Kingdom', 'The Netherlands'.",
                            "Do not use 'the' for single-word country names: 'Germany', 'France', 'Japan', 'Brazil'."
                        ]
                    }
                ]
            }
        ]
    },
    "Jobs & Professions — Tech Roles & More": {
        "intro": "Learn common job roles and titles, and the absolute grammatical rules for introducing professions in English.",
        "sections": [
            {
                "title": "Tech Roles & Professional Grammar",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: Classic & Modern IT Roles",
                        "layout": "table",
                        "headers": ["Tech Role", "Primary Responsibilities", "SaaS Context"],
                        "rows": [
                            ["Software Engineer (SWE)", "Writes backend/frontend code, designs databases, maintains systems", "I am a Software Engineer at Stripe."],
                            ["Product Manager (PM)", "Defines product features, roadmaps, coordinates engineering and design", "She is a PM for the checkout team."],
                            ["UX/UI Designer", "Creates visual designs, wireframes, conducts user research and tests", "Our UX designer created the visual prototype."],
                            ["DevOps Specialist", "Manages server deployments, CI/CD pipelines, cloud architectures", "He works as a DevOps specialist on AWS."],
                            ["QA Tester", "Tests applications for bugs, writes automated end-to-end tests", "The QA tester caught the rendering issue."]
                        ]
                    },
                    {
                        "title": "Section 2: Professional Grammar (A vs An)",
                        "layout": "list",
                        "items": [
                            "Rule: Singular job titles must always be preceded by an indefinite article: 'I am a developer' (not 'I am developer').",
                            "Use 'a' before consonant sounds: 'a developer', 'a designer', 'a product manager'.",
                            "Use 'an' before vowel sounds: 'an engineer', 'an analyst', 'an IT specialist'."
                        ]
                    }
                ]
            }
        ]
    },
    "Food & Drinks — Fuel for the Day": {
        "intro": "Learn everyday food and drink vocabulary to help you navigate tech offices, cafeterias, and social lunches.",
        "sections": [
            {
                "title": "Office Catering & Countability",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: Office Catering & Snack Directory",
                        "layout": "table",
                        "headers": ["Snack / Beverage", "Category", "Countable?", "Common Office Saying"],
                        "rows": [
                            ["Coffee", "Drink / Beverage", "Uncountable", "I need a cup of coffee before the standup."],
                            ["Water", "Drink / Hydration", "Uncountable", "Keep some water on your desk to stay hydrated."],
                            ["Apple / Banana", "Food / Fruit", "Countable", "I took an apple from the office kitchen."],
                            ["Sandwich", "Food / Lunch", "Countable", "Let's grab a sandwich during the lunch break."],
                            ["Salad", "Food / Healthy Option", "Countable / Uncountable", "She brought a fresh salad for lunch."]
                        ]
                    },
                    {
                        "title": "Section 2: Countable vs Uncountable Rules",
                        "layout": "list",
                        "items": [
                            "Use 'a/an' or numbers with Countable foods: 'a sandwich', 'an apple', 'three cookies'.",
                            "Do NOT use 'a/an' or numbers with Uncountable foods/drinks: 'some water', 'some coffee', 'some bread'.",
                            "To quantify uncountable items, use container phrases: 'a bottle of water', 'a cup of tea', 'a slice of bread'."
                        ]
                    }
                ]
            }
        ]
    },
    "Everyday Objects — Home & Office": {
        "intro": "Master vocabulary for common tools, devices, and office equipment used daily in the workplace.",
        "sections": [
            {
                "title": "Workspace Tools & Place Prepositions",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: The Modern Workspace Directory",
                        "layout": "table",
                        "headers": ["Object", "Usage / Practical Purpose", "Typical Location"],
                        "rows": [
                            ["Laptop", "Main machine for code, meetings, communication", "On the desk or in the bag"],
                            ["Monitor", "External screen for displaying code and documentation", "Mounted on the desk or standing"],
                            ["Keyboard & Mouse", "Text and cursor input for system control", "In front of the monitor"],
                            ["Headphones", "Audio output for video calls and music blockout", "On your head or on the desk"],
                            ["Desk & Chair", "Ergonomic workspace setup for long hours", "In the home office or company office"]
                        ]
                    },
                    {
                        "title": "Section 2: Object Pronouns & Location Prepositions",
                        "layout": "list",
                        "items": [
                            "Preposition 'ON': 'on the desk', 'on the wall' (contact with a surface).",
                            "Preposition 'UNDER': 'under the desk', 'under the chair' (directly below).",
                            "Singular objects use 'it': 'Where is the keyboard? It is on the desk'.",
                            "Plural objects use 'they': 'Where are the headphones? They are under the notebook'."
                        ]
                    }
                ]
            }
        ]
    },
    "Animals — Pets, Farm & Wild": {
        "intro": "Learn animals vocabulary, useful for general conversations, analogies, and common tech branding.",
        "sections": [
            {
                "title": "Animals in Tech Branding & Mascots",
                "layout": "composite",
                "subsections": [
                    {
                        "title": "Section 1: The Tech Mascot Zoo",
                        "layout": "table",
                        "headers": ["Animal Name", "Associated Tech Brand / Mascot", "Description of Brand"],
                        "rows": [
                            ["Python / Snake", "Python programming language", "A powerful, clean coding language"],
                            ["Gopher", "Go (Golang) programming language", "A fast, concurrent language built by Google"],
                            ["Whale", "Docker containerization engine", "A platform for packaging applications in containers"],
                            ["Octopus + Cat (Octocat)", "GitHub version control platform", "The mascot combining an octopus and a cat"],
                            ["Penguin (Tux)", "Linux operating system", "The official open-source Linux kernel mascot"]
                        ]
                    },
                    {
                        "title": "Section 2: Everyday Pets & Farm Animals",
                        "layout": "list",
                        "items": [
                            "Dog: Known as loyal domestic pets (e.g. 'The dog barked').",
                            "Cat: Independent household pet (e.g. 'The cat is sleeping under the monitor').",
                            "Bird: Feathered flying animal (e.g. 'A bird is singing outside the office window').",
                            "Fish: Aquatic animal (e.g. 'He keeps a goldfish in a bowl on his desk')."
                        ]
                    }
                ]
            }
        ]
    }
}

file_path = "/Users/ropa/Develop/english-coach-app/backend/scripts/seed_data/a1_vocabulary.py"
print(f"Reading and enriching {file_path}...")

import scripts.seed_data.a1_vocabulary as vocab
importlib.invalidate_caches()

lessons = getattr(vocab, "A1_VOCABULARY_LESSONS", [])

for lesson in lessons:
    meta = lesson.get("meta", {})
    title = meta.get("title")
    if title in ENRICHED_EXPLANATIONS:
        print(f"  - Injecting enriched composite explanation for: {title}")
        meta["explanation"] = ENRICHED_EXPLANATIONS[title]

# Write back
formatted_data = f"A1_VOCABULARY_LESSONS: list[dict] = {format_val(lessons)}"
output_lines = [
    "# a1_vocabulary.py — Enriched plain-text JSON seed data",
    "# Cleaned and enriched to show beautiful multi-section tables.",
    "",
    "from app.models import ExerciseType, LessonCategory, LessonType, SentenceType",
    "",
    formatted_data,
    ""
]

with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))
    
print("Successfully enriched all A1 vocabulary seed data!")
