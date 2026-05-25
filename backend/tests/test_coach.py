import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import httpx
from fastapi import status

from app.services.ai_coach_service import AICoachService

class TestAICoachServiceShortCircuit:
    @pytest.mark.anyio
    async def test_empty_transcription_short_circuit(self):
        """Verify that empty transcription yields fallback message immediately without calling Ollama."""
        service = AICoachService()
        generator = service.generate_feedback_stream(
            target_phrase="Hello",
            user_transcription="",
            score=0.0
        )
        
        chunks = []
        async for chunk in generator:
            chunks.append(chunk)
            
        assert len(chunks) == 2
        # First chunk should contain friendly message
        data_first = json.loads(chunks[0].replace("data: ", "").strip())
        assert "micrófono" in data_first["content"]
        # Second chunk should be done
        data_second = json.loads(chunks[1].replace("data: ", "").strip())
        assert data_second["done"] is True


class TestAICoachEndpoint:
    def test_endpoint_short_circuit(self, client):
        """Test API endpoint directly under the short circuit scenario."""
        response = client.post(
            "/api/v1/coach/feedback",
            json={
                "target_phrase": "Think about it.",
                "user_transcription": "  ",
                "score": 0.0
            }
        )
        assert response.status_code == status.HTTP_200_OK
        assert "text/event-stream" in response.headers["content-type"]
        
        # Collect and parse SSE response text
        lines = response.text.split("\n\n")
        non_empty_lines = [l for l in lines if l.strip()]
        
        assert len(non_empty_lines) >= 2
        # First SSE data event
        assert non_empty_lines[0].startswith("data: ")
        event_1 = json.loads(non_empty_lines[0].replace("data: ", ""))
        assert "micrófono" in event_1["content"]
        
        # Second SSE data event
        event_2 = json.loads(non_empty_lines[1].replace("data: ", ""))
        assert event_2["done"] is True

    @patch("httpx.AsyncClient.stream")
    def test_endpoint_normal_streaming(self, mock_stream, client):
        """Test API endpoint with mocked successful streaming response from Ollama."""
        # Create a mock async context manager for httpx client stream
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # Define mock lines returned by Ollama's SSE chat API
        mock_lines = [
            b'{"message": {"content": "Good"}, "done": false}',
            b'{"message": {"content": " job!"}, "done": false}',
            b'{"message": {}, "done": true}'
        ]
        
        async def mock_aiter_lines():
            for line in mock_lines:
                yield line
                
        mock_response.aiter_lines = mock_aiter_lines
        
        # Setup mock_stream to return the mock_response context manager
        mock_stream.return_value.__aenter__.return_value = mock_response

        response = client.post(
            "/api/v1/coach/feedback",
            json={
                "target_phrase": "Think about it.",
                "user_transcription": "Tink about it.",
                "score": 85.0
            }
        )
        assert response.status_code == status.HTTP_200_OK
        assert "text/event-stream" in response.headers["content-type"]
        
        lines = response.text.split("\n\n")
        non_empty_lines = [l for l in lines if l.strip()]
        
        assert len(non_empty_lines) == 3
        
        event_1 = json.loads(non_empty_lines[0].replace("data: ", ""))
        assert event_1["content"] == "Good"
        
        event_2 = json.loads(non_empty_lines[1].replace("data: ", ""))
        assert event_2["content"] == " job!"
        
        event_3 = json.loads(non_empty_lines[2].replace("data: ", ""))
        assert event_3["done"] is True

    @patch("httpx.AsyncClient.stream")
    def test_endpoint_ollama_error_status(self, mock_stream, client):
        """Test API endpoint when Ollama returns non-200 error code."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        
        async def mock_aread():
            return b"Internal Server Error"
        mock_response.aread = mock_aread
        
        mock_stream.return_value.__aenter__.return_value = mock_response

        response = client.post(
            "/api/v1/coach/feedback",
            json={
                "target_phrase": "Think about it.",
                "user_transcription": "Tink about it.",
                "score": 85.0
            }
        )
        assert response.status_code == status.HTTP_200_OK
        
        lines = response.text.split("\n\n")
        non_empty_lines = [l for l in lines if l.strip()]
        assert len(non_empty_lines) == 1
        
        event = json.loads(non_empty_lines[0].replace("data: ", ""))
        assert "Failed to communicate with AI Coach" in event["error"]

    @patch("httpx.AsyncClient.stream")
    def test_endpoint_ollama_connection_error(self, mock_stream, client):
        """Test API endpoint when connection to Ollama fails."""
        # Make the __aenter__ call raise a RequestError
        mock_stream.return_value.__aenter__.side_effect = httpx.RequestError("Connection refused")

        response = client.post(
            "/api/v1/coach/feedback",
            json={
                "target_phrase": "Think about it.",
                "user_transcription": "Tink about it.",
                "score": 85.0
            }
        )
        assert response.status_code == status.HTTP_200_OK
        
        lines = response.text.split("\n\n")
        non_empty_lines = [l for l in lines if l.strip()]
        assert len(non_empty_lines) == 1
        
        event = json.loads(non_empty_lines[0].replace("data: ", ""))
        assert "currently unavailable" in event["error"]
