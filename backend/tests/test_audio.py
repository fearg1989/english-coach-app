import pytest
from unittest.mock import MagicMock, patch
from fastapi import status
from app.services.audio_service import audio_service

def test_text_normalization():
    """Verify that normalize_text removes punctuation, ignores case, and expands standard contractions."""
    # Test lowercase and punctuation stripping
    assert audio_service._normalize_text("Hello, World!") == "hello world"
    assert audio_service._normalize_text("This... is a test; indeed.") == "this is a test indeed"
    
    # Test contraction expansion
    assert audio_service._normalize_text("I'm fine") == "i am fine"
    assert audio_service._normalize_text("don't do it") == "do not do it"
    assert audio_service._normalize_text("We'll meet there") == "we will meet there"
    assert audio_service._normalize_text("dont do it") == "do not do it"  # apostrophe-less contraction

    # Test whitespace collapse
    assert audio_service._normalize_text("   too    many   spaces   ") == "too many spaces"
    
    # Test empty or None input
    assert audio_service._normalize_text("") == ""
    assert audio_service._normalize_text(None) == ""

def test_calculate_accuracy():
    """Verify pronunciation similarity scoring (0-100)."""
    # Exact match
    score = audio_service.calculate_accuracy("I am happy", "I'm happy!")
    assert score == 100.0
    
    # Partial match
    score = audio_service.calculate_accuracy("I am happy", "I am very happy")
    # "i am happy" (11 chars) vs "i am very happy" (15 chars)
    assert 60.0 < score < 95.0
    
    # Complete mismatch (using dog vs cat which have no character overlaps)
    score = audio_service.calculate_accuracy("dog", "cat")
    assert score == 0.0

@patch("app.services.audio_service.AudioSegment.from_file")
@patch("app.services.audio_service.whisper.load_model")
def test_transcribe_audio_success(mock_load_model, mock_from_file):
    """Test that transcribe_audio successfully normalizes format and transcribes."""
    # Setup AudioSegment mocks
    mock_audio = MagicMock()
    mock_from_file.return_value = mock_audio
    mock_audio.set_frame_rate.return_value = mock_audio
    mock_audio.set_channels.return_value = mock_audio
    mock_audio.set_sample_width.return_value = mock_audio
    
    # Setup Whisper model mocks
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model
    mock_model.transcribe.return_value = {"text": "Hello world"}
    
    # Clear any previous loaded model to force lazy loading
    audio_service._model = None
    
    # Run transcription
    result = audio_service.transcribe_audio(b"some audio data")
    
    assert result == "Hello world"
    mock_from_file.assert_called_once()
    mock_audio.export.assert_called_once()
    
    # Check that model was loaded and transcribed
    mock_load_model.assert_called_once()
    mock_model.transcribe.assert_called_once()

@patch("app.services.audio_service.AudioSegment.from_file")
def test_transcribe_audio_conversion_failure(mock_from_file):
    """Test that transcribe_audio raises ValueError if audio decoding fails."""
    mock_from_file.side_effect = Exception("Decoding error")
    
    with pytest.raises(ValueError) as exc_info:
        audio_service.transcribe_audio(b"bad audio data")
        
    assert "Could not decode" in str(exc_info.value)

@patch("app.services.audio_service.AudioService.transcribe_audio")
def test_evaluate_pronunciation_endpoint_success(mock_transcribe, client):
    """Verify endpoint successfully handles file upload, invokes Whisper service, and returns accuracy score."""
    # Setup mocks
    mock_transcribe.return_value = "I think it is a beautiful day"
    
    # Target text is "I think it's a beautiful day"
    # Normalized transcription "i think it is a beautiful day"
    # Normalized target "i think it is a beautiful day"
    # Expecting 100% score due to contraction normalization!
    
    dummy_audio = b"fake audio content"
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        files={"file": ("test.webm", dummy_audio, "audio/webm")},
        data={"target_text": "I think it's a beautiful day"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "transcribed_text" in data
    assert "accuracy_score" in data
    assert data["transcribed_text"] == "I think it is a beautiful day"
    assert data["accuracy_score"] == 100.0
    
    # Verify the transcribe mock was called with the uploaded bytes
    mock_transcribe.assert_called_once_with(dummy_audio)

def test_evaluate_pronunciation_endpoint_missing_params(client):
    """Verify endpoint returns 422 Unprocessable Entity when parameters are missing."""
    # Missing file
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        data={"target_text": "Hello"}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Missing target_text
    dummy_audio = b"fake audio content"
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        files={"file": ("test.webm", dummy_audio, "audio/webm")}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_evaluate_pronunciation_endpoint_empty_target_text(client):
    """Verify endpoint returns 400 Bad Request when target_text is blank."""
    dummy_audio = b"fake audio content"
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        files={"file": ("test.webm", dummy_audio, "audio/webm")},
        data={"target_text": "   "}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Target text cannot be empty" in response.json()["detail"]

@patch("app.services.audio_service.AudioService.transcribe_audio")
def test_evaluate_pronunciation_endpoint_empty_audio(mock_transcribe, client):
    """Verify endpoint returns 400 Bad Request when uploaded audio file is empty."""
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        files={"file": ("test.webm", b"", "audio/webm")},
        data={"target_text": "Hello"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Uploaded audio file is empty" in response.json()["detail"]
    mock_transcribe.assert_not_called()

@patch("app.services.audio_service.AudioService.transcribe_audio")
def test_evaluate_pronunciation_endpoint_value_error(mock_transcribe, client):
    """Verify endpoint returns 400 Bad Request when AudioService raises ValueError."""
    mock_transcribe.side_effect = ValueError("Could not decode or normalize the uploaded audio format.")
    
    dummy_audio = b"corrupted sound bytes"
    response = client.post(
        "/api/v1/audio/evaluate-pronunciation",
        files={"file": ("test.webm", dummy_audio, "audio/webm")},
        data={"target_text": "Hello"}
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Could not decode or normalize the uploaded audio format" in response.json()["detail"]
