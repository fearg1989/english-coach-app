import logging
import os
import re
import tempfile
import threading
from difflib import SequenceMatcher
from typing import Optional

from pydub import AudioSegment
import whisper

from app.core.config import settings

logger = logging.getLogger(__name__)

class AudioService:
    _instance: Optional["AudioService"] = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        """Implement thread-safe Singleton pattern."""
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(AudioService, cls).__new__(cls, *args, **kwargs)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the service and lazy-load the model lock."""
        if self._initialized:
            return
        self._model = None
        self._model_lock = threading.Lock()
        self._initialized = True
        logger.info("AudioService initialized (lazy model loading enabled)")

    def get_model(self) -> whisper.Whisper:
        """Lazy-load the Whisper model in a thread-safe manner."""
        if self._model is None:
            with self._model_lock:
                if self._model is None:
                    model_name = settings.WHISPER_MODEL
                    logger.info(f"Loading Whisper model '{model_name}' into memory...")
                    # This will download the model if not already cached
                    self._model = whisper.load_model(model_name)
                    logger.info(f"Whisper model '{model_name}' loaded successfully")
        return self._model

    def transcribe_audio(self, file_bytes: bytes) -> str:
        """
        Saves incoming audio bytes, normalizes the format using pydub, transcribes using Whisper,
        and cleans up temporary files safely.
        """
        temp_in_fd, temp_in_path = tempfile.mkstemp()
        temp_wav_fd, temp_wav_path = tempfile.mkstemp(suffix=".wav")
        
        try:
            # Write uploaded raw bytes to the input temp file
            with os.fdopen(temp_in_fd, "wb") as f:
                f.write(file_bytes)
            
            logger.debug(f"Temporary input file created at {temp_in_path}")

            # Decode browser audio (webm/ogg/mp4/etc.) and normalize to 16kHz mono WAV
            try:
                audio = AudioSegment.from_file(temp_in_path)
                # 16000 Hz, 1 channel (mono), 16-bit (2 bytes per sample)
                audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
                audio.export(temp_wav_path, format="wav")
                logger.debug(f"Audio normalized and exported to {temp_wav_path}")
            except Exception as audio_err:
                logger.error(f"Failed to normalize audio via pydub: {audio_err}")
                raise ValueError("Could not decode or normalize the uploaded audio format. Ensure it is a valid audio file.")

            # Load model and transcribe
            model = self.get_model()
            logger.debug("Running Whisper transcription...")
            # We explicitly specify language='en' to speed up inference and prevent language hallucination
            result = model.transcribe(temp_wav_path, language="en")
            transcribed_text = result.get("text", "").strip()
            
            logger.info(f"Successfully transcribed audio: '{transcribed_text}'")
            return transcribed_text

        finally:
            # Safely close file descriptors and delete temp files
            try:
                os.close(temp_wav_fd)
            except OSError:
                pass
            
            for path in (temp_in_path, temp_wav_path):
                if os.path.exists(path):
                    try:
                        os.remove(path)
                        logger.debug(f"Cleaned up temporary file: {path}")
                    except Exception as clean_err:
                        logger.warning(f"Failed to clean up temporary file {path}: {clean_err}")

    def calculate_accuracy(self, transcribed_text: str, target_text: str) -> float:
        """
        Calculates pronunciation accuracy score (0-100) using normalized text similarity
        via difflib.SequenceMatcher.
        """
        norm_transcribed = self._normalize_text(transcribed_text)
        norm_target = self._normalize_text(target_text)
        
        logger.debug(f"Calculating accuracy. Normalized Target: '{norm_target}' | Transcribed: '{norm_transcribed}'")
        
        if not norm_target:
            return 0.0
            
        matcher = SequenceMatcher(None, norm_target, norm_transcribed)
        score = matcher.ratio() * 100
        
        # Round to one decimal place
        return round(score, 1)

    def _normalize_text(self, text: str) -> str:
        """
        Converts text to lowercase, expands common contractions, removes punctuation,
        and normalizes spacing.
        """
        if not text:
            return ""
            
        # Convert to lowercase
        text = text.lower()
        
        # Dictionary of standard English contractions
        contractions = {
            "i'm": "i am",
            "you're": "you are",
            "he's": "he is",
            "she's": "she is",
            "it's": "it is",
            "we're": "we are",
            "they're": "they are",
            "i've": "i have",
            "you've": "you have",
            "we've": "we have",
            "they've": "they have",
            "i'd": "i would",
            "you'd": "you would",
            "he'd": "he would",
            "she'd": "she would",
            "we'd": "we would",
            "they'd": "they would",
            "i'll": "i will",
            "you'll": "you will",
            "he'll": "he will",
            "she'll": "she will",
            "we'll": "we will",
            "they'll": "they will",
            "isn't": "is not",
            "aren't": "are not",
            "wasn't": "was not",
            "weren't": "were not",
            "haven't": "have not",
            "hasn't": "has not",
            "hadn't": "had not",
            "won't": "will not",
            "wouldn't": "would not",
            "don't": "do not",
            "doesn't": "does not",
            "didn't": "did not",
            "can't": "can not",
            "couldn't": "could not",
            "shouldn't": "should not",
            "mightn't": "might not",
            "mustn't": "must not"
        }
        
        # Expand contractions (handling boundary matches)
        for contraction, expansion in contractions.items():
            # Match with apostrophe
            text = re.sub(r"\b" + re.escape(contraction) + r"\b", expansion, text)
            # Match apostrophe-less forms (e.g. dont -> do not, im -> i am)
            text = re.sub(r"\b" + re.escape(contraction.replace("'", "")) + r"\b", expansion, text)

        # Remove all punctuation and symbols (keeping only letters, numbers, and spaces)
        text = re.sub(r"[^\w\s]", "", text)
        
        # Collapse multiple spaces and strip ends
        text = " ".join(text.split())
        
        return text

# Export a single thread-safe instance
audio_service = AudioService()
