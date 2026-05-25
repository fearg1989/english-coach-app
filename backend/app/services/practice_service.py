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
        and returns the parsed practice session.
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

        # 3. Build the strict prompt enforcing JSON payload structure and safety checks
        system_prompt = (
            "You are an expert English Language Coach and Curriculum Developer.\n"
            "Your task is to generate a dynamic, structured set of practice exercises.\n"
            "You must output a single, raw, valid JSON object matching the requested schema. "
            "Do NOT wrap it in markdown block tags, do NOT use ```json or ```, and do NOT add any conversational explanation, intro, or outro.\n\n"
            "The JSON schema you must strictly follow is:\n"
            "{\n"
            '  "session_id": "string (UUID)",\n'
            '  "theme": "string (The theme provided by the user)",\n'
            '  "grammar_focus": "string (Grammar focus and level code, e.g. Verb To Be (A1))",\n'
            '  "exercises": [\n'
            "    {\n"
            '      "id": 1,\n'
            '      "type": "fill_in_the_blank" | "roleplay_response",\n'
            '      "prompt": "string (complete instruction or developer dialogue context in English)",\n'
            '      "correct_answer": "string (the exact answer targeted in English)",\n'
            '      "hint": "string (a helpful tip about the correct grammatical verb form/marker in Spanish)"\n'
            "    }\n"
            "  ],\n"
            '  "is_rejected": boolean,\n'
            '  "rejection_reason": "string or null"\n'
            "}\n\n"
            "CRITICAL SAFETY DIRECTIVE:\n"
            "If the requested theme is illegal, vulgar, offensive, sexually explicit, violent, related to weapons/drugs, or highly inappropriate for an educational tool, you MUST reject it by setting 'is_rejected' to true, and providing a polite explanation in Spanish in 'rejection_reason' explaining why we cannot practice this topic (e.g., 'El tema sugerido no es apto para un contexto educativo de aprendizaje. Por favor, elige otra temática.'). In this case, leave the 'exercises' list completely empty.\n\n"
            "Key generation rules if the theme is safe:\n"
            "1. Generate exactly 5 diverse and engaging exercises.\n"
            f"2. The grammar_focus is: {grammar_title} ({level_code}). You MUST construct sentences targeting this exact grammar topic at this CEFR proficiency level.\n"
            f"3. The theme is: {theme}. The prompts, scenarios, vocabulary, and dialogues of every exercise must revolve around this theme (e.g., if theme is Software Development, write about pipelines, coding, deployment conversations).\n"
            "4. The prompts, dialogue contents, and correct answers must be entirely in English.\n"
            "5. The 'hint' field must be in Spanish, offering a helpful pedagogical clue about how to solve the exercise.\n"
            "6. For 'fill_in_the_blank', always prefix the 'prompt' with a clear instruction in Spanish explaining what grammar target to use, followed by the English sentence containing a '___' blank (e.g., 'Completa la frase con la forma correcta de 'to be': The movie ___ very long.').\n"
            "7. For 'roleplay_response', always prefix the 'prompt' with a clear, engaging roleplay context in Spanish explaining who speaks and what they ask, followed by the English dialogue prompt (e.g., 'El reclutador te pregunta en tu entrevista de trabajo: 'Who is the lead dev?'. Responde diciendo afirmativamente que tú eres el desarrollador principal:')."
        )

        user_prompt = (
            f"Generate a 5-question English practice session. "
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
            async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
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
                    # In case Ollama wrapped JSON in ```json or markdown block tags despite instructions
                    if raw_content.startswith("```"):
                        # Extract JSON content between ```json and ```
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
