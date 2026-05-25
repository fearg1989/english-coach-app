import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
from fastapi import status


class TestPracticeEndpoint:
    @pytest.fixture
    def mock_lesson(self):
        """Mock lesson detail dictionary."""
        return {
            "id": 1,
            "title": "Verb To Be",
            "level": {"code": "A1", "name": "Beginner"},
            "level_id": 1,
        }

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    @patch("httpx.AsyncClient.post")
    def test_practice_generate_success(self, mock_post, mock_get_lesson, client, mock_lesson):
        """Test successful dynamic practice session generation."""
        # 1. Mock lesson detail lookup
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        # 2. Mock successful response from local Ollama service
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        exercises_payload = {
            "session_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
            "theme": "Software Development",
            "grammar_focus": "Verb To Be (A1)",
            "exercises": [
                {
                    "id": 1,
                    "type": "fill_in_the_blank",
                    "prompt": "Complete: 'I ___ a software developer.'",
                    "correct_answer": "am",
                    "hint": "Primera persona del singular del verbo to be."
                },
                {
                    "id": 2,
                    "type": "roleplay_response",
                    "prompt": "PM asks: 'Are the servers down?'. Reply 'Yes, they are.'",
                    "correct_answer": "Yes, they are.",
                    "hint": "Tercera persona del plural con respuesta afirmativa."
                }
            ]
        }
        
        mock_response.json.return_value = {
            "message": {
                "role": "assistant",
                "content": json.dumps(exercises_payload)
            }
        }
        
        # httpx post return mock response
        mock_post.return_value = mock_response

        # 3. Post generate payload to practice endpoint
        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Software Development"
            }
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["theme"] == "Software Development"
        assert data["grammar_focus"] == "Verb To Be (A1)"
        assert len(data["exercises"]) == 2
        assert data["exercises"][0]["correct_answer"] == "am"

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    def test_practice_generate_lesson_not_found(self, mock_get_lesson, client):
        """Test generating practice session with invalid/missing lesson ID."""
        from fastapi import HTTPException
        mock_get_lesson.side_effect = HTTPException(
            status_code=404, detail="Lesson with id=999 not found."
        )

        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 999,
                "theme": "Cinema"
            }
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "not found" in response.json()["detail"]

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    @patch("httpx.AsyncClient.post")
    def test_practice_generate_ollama_http_error(self, mock_post, mock_get_lesson, client):
        """Test API endpoint when Ollama returns non-200 error."""
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Cinema"
            }
        )
        assert response.status_code == status.HTTP_502_BAD_GATEWAY
        assert "Failed to communicate with local AI service" in response.json()["detail"]

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    @patch("httpx.AsyncClient.post")
    def test_practice_generate_ollama_invalid_json(self, mock_post, mock_get_lesson, client):
        """Test API endpoint when Ollama content is not valid JSON."""
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {
                "role": "assistant",
                "content": "This is conversational garbage, not a JSON payload!"
            }
        }
        mock_post.return_value = mock_response

        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Cinema"
            }
        )
        assert response.status_code == status.HTTP_502_BAD_GATEWAY
        assert "AI Coach returned invalid JSON format" in response.json()["detail"]

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    @patch("httpx.AsyncClient.post")
    def test_practice_generate_ollama_pydantic_validation_error(self, mock_post, mock_get_lesson, client):
        """Test API endpoint when Ollama returns JSON that fails validation (missing keys)."""
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # exercises has invalid type (string instead of list) to force validation error
        invalid_payload = {
            "session_id": "invalid-uuid",
            "theme": "Cinema",
            "grammar_focus": "Verb To Be",
            "exercises": "not-a-list"
        }
        
        mock_response.json.return_value = {
            "message": {
                "role": "assistant",
                "content": json.dumps(invalid_payload)
            }
        }
        mock_post.return_value = mock_response

        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Cinema"
            }
        )
        assert response.status_code == status.HTTP_502_BAD_GATEWAY
        assert "AI Coach output structure did not match our curriculum validation schema" in response.json()["detail"]

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    def test_practice_generate_local_blacklist_blocked(self, mock_get_lesson, client):
        """Test that themes with vulgar or illegal keywords are immediately blocked by our local safety shield."""
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        # Post generation request with illegal theme containing "droga"
        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Comprar droga en la calle"
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "vulgares, inapropiados o ilegales" in response.json()["detail"]

    @patch("app.services.lesson_service.LessonService.get_lesson_detail")
    @patch("httpx.AsyncClient.post")
    def test_practice_generate_llm_rejection(self, mock_post, mock_get_lesson, client):
        """Test safety rejection triggered semantically by the AI Coach (Ollama)."""
        mock_lesson_obj = MagicMock()
        mock_lesson_obj.id = 1
        mock_lesson_obj.title = "Verb To Be"
        mock_lesson_obj.level = MagicMock()
        mock_lesson_obj.level.code = "A1"
        mock_get_lesson.return_value = mock_lesson_obj

        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # Payload mimicking the Ollama response rejected flag set to true
        rejected_payload = {
            "session_id": "8c2ebd5d-3c7d-4abc-9cdd-2b0d7b3dcb7c",
            "theme": "Something inappropriate",
            "grammar_focus": "Verb To Be (A1)",
            "exercises": [],
            "is_rejected": True,
            "rejection_reason": "El tema sugerido no es apto para un contexto educativo de aprendizaje."
        }
        
        mock_response.json.return_value = {
            "message": {
                "role": "assistant",
                "content": json.dumps(rejected_payload)
            }
        }
        mock_post.return_value = mock_response

        response = client.post(
            "/api/v1/practice/generate",
            json={
                "lesson_id": 1,
                "theme": "Something inappropriate"
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "no es apto para un contexto educativo" in response.json()["detail"]
