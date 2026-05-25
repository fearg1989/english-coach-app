import json
import logging
import uuid
import httpx
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.services.lesson_service import LessonService
from app.schemas.practice import PracticeSessionResponseSchema

logger = logging.getLogger(__name__)


class PracticeService:
    """
    Service responsible for constructing dynamic, context-aware practice sessions
    by querying Ollama with custom themes and grammar contexts, and validating the results.
    Now supports 5 exercise types: fill_in_the_blank, roleplay_response, multiple_choice,
    translation, and open_writing.
    """

    def __init__(self, db: Session) -> None:
        self._db = db
        self._lesson_service = LessonService(db)
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL

    async def generate_practice_session(self, lesson_id: int, theme: str) -> dict:
        """
        Retrieves lesson context, merges it with the custom theme, builds a strict JSON prompt,
        queries the local Ollama instance with JSON format enforcement, validates the schema,
        and returns the parsed practice session with a variety of exercise types.
        """
        # 1. Fetch lesson details to verify existence and grab context
        lesson = self._lesson_service.get_lesson_detail(lesson_id)
        level_code = lesson.level.code if lesson.level else "A1"
        grammar_title = lesson.title

        logger.info(
            f"Generating practice session for Lesson ID: {lesson_id} ('{grammar_title}', Level: {level_code}) "
            f"under the theme: '{theme}'."
        )

        # 2. Local Safety keyword shield to catch blatant inappropriate terms instantly
        blacklist = [
            "sexo", "pornografía", "porno", "porn", "hentai", "droga", "cocaina", "marihuana",
            "asesinar", "violencia", "matar", "violación", "cigarro", "armas", "narco",
            "cartel", "hackear", "hacking", "stealing", "steal", "robbery", "rob", "murder",
            "bomb", "terrorist", "suicide", "prostitución", "prostitutes", "whore", "fuck",
            "shit", "assault", "vulgar", "ilegal", "illegal", "prostituta", "drogas",
            "cocaine", "marijuana", "weapons", "gun", "guns", "assassinate", "prostitute"
        ]
        theme_lower = theme.lower().strip()
        if any(bad_word in theme_lower for bad_word in blacklist):
            logger.warning(f"Practice session theme '{theme}' blocked by local safety shield.")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El tema sugerido contiene términos vulgares, inapropiados o ilegales. Por favor, escribe un tema apto para el aprendizaje educativo."
            )

        # 3. Build the strict prompt enforcing JSON payload structure and all 5 exercise types
        system_prompt = (
            "You are an expert English Language Coach and Curriculum Developer.\n"
            "Your task is to generate a dynamic, structured practice session with 5 exercises of DIFFERENT types.\n"
            "You must output a single, raw, valid JSON object matching the schema below. "
            "Do NOT wrap it in markdown, do NOT use ```json or ```, do NOT add any explanation.\n\n"
            "The JSON schema you must strictly follow:\n"
            "{\n"
            '  "session_id": "string (UUID v4)",\n'
            '  "theme": "string",\n'
            '  "grammar_focus": "string",\n'
            '  "exercises": [\n'
            "    {\n"
            '      "id": number,\n'
            '      "type": "fill_in_the_blank" | "roleplay_response" | "multiple_choice" | "translation" | "open_writing",\n'
            '      "prompt": "string",\n'
            '      "correct_answer": "string",\n'
            '      "hint": "string (in Spanish)",\n'
            '      "options": ["string", "string", "string", "string"] or null\n'
            "    }\n"
            "  ],\n"
            '  "is_rejected": boolean,\n'
            '  "rejection_reason": "string or null"\n'
            "}\n\n"
            "CRITICAL SAFETY DIRECTIVE:\n"
            "If the requested theme is illegal, vulgar, offensive, sexually explicit, violent, or inappropriate "
            "for an educational tool, set 'is_rejected' to true, provide a polite explanation in Spanish in "
            "'rejection_reason', and leave 'exercises' completely empty.\n\n"
            "EXERCISE GENERATION RULES (only if theme is safe):\n"
            f"1. GRAMMAR FOCUS: {grammar_title} ({level_code}). Every exercise MUST practice this exact grammar at this CEFR level.\n"
            f"2. THEME: {theme}. All prompts, scenarios, and vocabulary must revolve around this theme.\n"
            "3. Generate exactly 5 exercises, ONE of each type, in this ORDER:\n"
            "   - Exercise 1: type='fill_in_the_blank'\n"
            "   - Exercise 2: type='multiple_choice'\n"
            "   - Exercise 3: type='translation'\n"
            "   - Exercise 4: type='open_writing'\n"
            "   - Exercise 5: type='roleplay_response'\n"
            "4. Rules per exercise type:\n\n"
            "   FILL_IN_THE_BLANK:\n"
            "   - 'prompt': Start with a brief instruction in Spanish (e.g. 'Completa con la forma correcta del verbo to be:'), "
            "then write the English sentence with a '___' blank.\n"
            "   - 'correct_answer': The single word or short phrase that fills the blank.\n"
            "   - 'options': null (no options needed).\n\n"
            "   MULTIPLE_CHOICE:\n"
            "   - 'prompt': Start with a brief instruction in Spanish (e.g. 'Elige la opción correcta:'), "
            "then write the English sentence or question.\n"
            "   - 'correct_answer': The exact text of the correct option (must match one of the 4 options exactly).\n"
            "   - 'options': A JSON array of exactly 4 strings — the 4 answer choices. "
            "Only one must be correct. Make the distractors plausible but clearly wrong grammatically.\n\n"
            "   TRANSLATION:\n"
            "   - 'prompt': Start with 'Traduce al inglés la siguiente frase:', then write a complete sentence in SPANISH "
            "that the student must translate to English, applying the grammar focus.\n"
            "   - 'correct_answer': The correct English translation of the Spanish sentence.\n"
            "   - 'options': null.\n\n"
            "   OPEN_WRITING:\n"
            "   - 'prompt': Start with a creative writing instruction in Spanish, "
            "asking the student to write a COMPLETE original sentence in English about the theme, using the grammar focus. "
            "Example: 'Escribe en inglés una frase completa describiendo tu película favorita usando el verbo to be:'.\n"
            "   - 'correct_answer': A model answer in English (a valid example sentence) that the student's response will be compared against.\n"
            "   - 'options': null.\n\n"
            "   ROLEPLAY_RESPONSE:\n"
            "   - 'prompt': Describe a roleplay scenario in Spanish, then write the English dialogue line the student must respond to. "
            "Example: 'El director de cine te pregunta: \"Who is the main character?\" Responde en inglés usando el verbo to be:'\n"
            "   - 'correct_answer': A valid English response sentence using the grammar focus.\n"
            "   - 'options': null.\n\n"
            "5. The 'hint' field for every exercise must be in Spanish, offering a pedagogical tip about the grammar rule to apply.\n"
            "6. All prompts, correct_answers, and options content must be relevant to both the GRAMMAR FOCUS and the THEME."
        )

        user_prompt = (
            f"Generate a 5-exercise English practice session with one of each type: "
            f"fill_in_the_blank, multiple_choice, translation, open_writing, roleplay_response. "
            f"Grammar topic: {grammar_title} ({level_code}). Theme: {theme}."
        )

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "stream": False,
            "format": "json"  # Forces Ollama to strictly generate JSON
        }

        # 4. Call the local Ollama instance with timeout
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(90.0)) as client:
                response = await client.post(f"{self.base_url}/api/chat", json=payload)

                if response.status_code != 200:
                    error_detail = response.text
                    logger.error(f"Ollama API error: {response.status_code} - {error_detail}")
                    raise HTTPException(
                        status_code=status.HTTP_502_BAD_GATEWAY,
                        detail="Failed to communicate with local AI service to generate practice session."
                    )

                result_data = response.json()
                raw_content = result_data.get("message", {}).get("content", "").strip()

                if not raw_content:
                    logger.error("Ollama returned an empty response content.")
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="AI Coach generated an empty practice session."
                    )

                # 5. Clean and parse JSON
                try:
                    if raw_content.startswith("```"):
                        lines = raw_content.splitlines()
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines[-1].startswith("```"):
                            lines = lines[:-1]
                        raw_content = "\n".join(lines).strip()

                    parsed_json = json.loads(raw_content)
                except json.JSONDecodeError as decode_err:
                    logger.error(f"Failed to decode Ollama JSON output: {raw_content}. Error: {decode_err}")
                    raise HTTPException(
                        status_code=status.HTTP_502_BAD_GATEWAY,
                        detail="AI Coach returned invalid JSON format. Please try again."
                    )

                # Ensure session_id is a valid UUID, otherwise generate a fallback one
                session_id = parsed_json.get("session_id")
                if not session_id or len(str(session_id)) < 10:
                    parsed_json["session_id"] = str(uuid.uuid4())

                # Force theme and grammar focus alignment in response payload
                parsed_json["theme"] = theme
                parsed_json["grammar_focus"] = f"{grammar_title} ({level_code})"

                # Check if rejected by AI Coach safety moderation
                if parsed_json.get("is_rejected") is True:
                    rejection_reason = parsed_json.get("rejection_reason") or "El tema sugerido no es apto para un contexto educativo."
                    logger.warning(f"Theme '{theme}' was rejected by AI Coach safety filter: {rejection_reason}")
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=rejection_reason
                    )

                # Ensure multiple_choice exercises have valid options list
                for ex in parsed_json.get("exercises", []):
                    if ex.get("type") == "multiple_choice":
                        options = ex.get("options")
                        if not options or not isinstance(options, list) or len(options) < 2:
                            logger.warning(f"Exercise {ex.get('id')} is multiple_choice but has invalid options: {options}. Skipping options validation.")

                # 6. Validate utilizing Pydantic schema
                try:
                    validated_session = PracticeSessionResponseSchema.model_validate(parsed_json)
                    return validated_session.model_dump()
                except Exception as val_err:
                    logger.error(f"Pydantic validation of practice session failed: {val_err}. Content: {parsed_json}")
                    raise HTTPException(
                        status_code=status.HTTP_502_BAD_GATEWAY,
                        detail="AI Coach output structure did not match our curriculum validation schema."
                    )

        except httpx.RequestError as req_err:
            logger.error(f"HTTP request error connecting to Ollama: {req_err}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Local AI service is currently unavailable. Please verify that Ollama is running."
            )
