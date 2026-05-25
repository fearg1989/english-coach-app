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

    def transcribe_audio(self, file_bytes: bytes) -> dict:
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
            # We explicitly specify language='en' to speed up inference and prevent language hallucination.
            # We tune parameters to avoid auto-correcting non-native accents and get word-level info.
            result = model.transcribe(
                temp_wav_path,
                language="en",
                temperature=0.0,
                condition_on_previous_text=False,
                initial_prompt=(
                    "This is a literal transcription of English speech spoken with a strong Hispanic / Spanish accent. "
                    "Transcribe exactly what is spoken, word-for-word, including any mispronunciations, "
                    "phonetical variations, slurred words, or mistakes. Do not correct grammar or spelling."
                ),
                word_timestamps=True
            )
            transcribed_text = result.get("text", "").strip()
            transcribed_text = self._convert_digits_to_words(transcribed_text)
            
            # Extract word-level details
            words = []
            for segment in result.get("segments", []):
                for w in segment.get("words", []):
                    word_text = w.get("word", "").strip()
                    if word_text:
                        # Expand numeric words (e.g. "1941" -> "nineteen", "forty-one")
                        if any(char.isdigit() for char in word_text):
                            converted = self._convert_digits_to_words(word_text)
                            for sw in converted.split():
                                words.append({
                                    "word": sw,
                                    "start": w.get("start", 0.0),
                                    "end": w.get("end", 0.0),
                                    "probability": w.get("probability", 1.0)
                                })
                        else:
                            words.append({
                                "word": word_text,
                                "start": w.get("start", 0.0),
                                "end": w.get("end", 0.0),
                                "probability": w.get("probability", 1.0)
                            })
            
            logger.info(f"Successfully transcribed audio: '{transcribed_text}'")
            return {
                "transcribed_text": transcribed_text,
                "words": words
            }

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

    def transcribe_audio_interim(self, file_bytes: bytes) -> str:
        """
        Runs a highly optimized, fast transcription for real-time interim updates
        without word timestamps or deep alignment analysis.
        """
        temp_in_fd, temp_in_path = tempfile.mkstemp()
        temp_wav_fd, temp_wav_path = tempfile.mkstemp(suffix=".wav")
        
        try:
            with os.fdopen(temp_in_fd, "wb") as f:
                f.write(file_bytes)
                
            try:
                audio = AudioSegment.from_file(temp_in_path)
                audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
                audio.export(temp_wav_path, format="wav")
            except Exception as audio_err:
                logger.error(f"Interim normalization failed: {audio_err}")
                return ""
                
            model = self.get_model()
            result = model.transcribe(
                temp_wav_path,
                language="en",
                temperature=0.0,
                word_timestamps=False
            )
            return self._convert_digits_to_words(result.get("text", "").strip())
            
        finally:
            try:
                os.close(temp_wav_fd)
            except OSError:
                pass
            for path in (temp_in_path, temp_wav_path):
                if os.path.exists(path):
                    try:
                        os.remove(path)
                    except Exception:
                        pass

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
        
        # Normalize numeric digits into written English words
        text = self._convert_digits_to_words(text)
        
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

    def _normalize_token(self, token: str) -> str:
        """
        Lowercases a token and strips all non-alphanumeric characters.
        Keeps contractions as single words without expansion for exact token comparison.
        """
        if not token:
            return ""
        return re.sub(r"[^\w]", "", token.lower())

    def align_words(self, target_text: str, transcribed_words: list[dict]) -> list[dict]:
        """
        Aligns words from target_text with words transcribed by Whisper, using SequenceMatcher.
        For each word in target_text, we determine if it was pronounced correctly (green),
        unclearly (orange/yellow), or incorrectly/missed (red) based on text match and Whisper's confidence.
        """
        target_tokens = target_text.split()
        normalized_targets = [self._normalize_token(t) for t in target_tokens]
        normalized_transcribed = [self._normalize_token(w["word"]) for w in transcribed_words]
        
        # Initialize feedback array
        feedback = [None] * len(target_tokens)
        
        matcher = SequenceMatcher(None, normalized_targets, normalized_transcribed)
        opcodes = matcher.get_opcodes()
        
        for tag, i1, i2, j1, j2 in opcodes:
            if tag == "equal":
                # 1-to-1 match
                for offset in range(i2 - i1):
                    t_idx = i1 + offset
                    w_idx = j1 + offset
                    
                    target_word = target_tokens[t_idx]
                    trans_word_dict = transcribed_words[w_idx]
                    prob = trans_word_dict.get("probability", 1.0)
                    
                    if prob >= 0.35:
                        status = "correct"
                    else:
                        status = "unclear"
                        
                    feedback[t_idx] = {
                        "word": target_word,
                        "status": status,
                        "accuracy_score": round(prob * 100, 1),
                        "transcribed_as": trans_word_dict.get("word")
                    }
            elif tag == "replace":
                # Substitution
                target_len = i2 - i1
                trans_len = j2 - j1
                
                for offset in range(target_len):
                    t_idx = i1 + offset
                    target_word = target_tokens[t_idx]
                    
                    if offset < trans_len:
                        trans_word_dict = transcribed_words[j1 + offset]
                        transcribed_as = trans_word_dict.get("word")
                        prob = trans_word_dict.get("probability", 0.0)
                    else:
                        transcribed_as = None
                        prob = 0.0
                        
                    feedback[t_idx] = {
                        "word": target_word,
                        "status": "incorrect",
                        "accuracy_score": round(prob * 100, 1) if transcribed_as else 0.0,
                        "transcribed_as": transcribed_as
                    }
            elif tag == "delete":
                # Omission
                for t_idx in range(i1, i2):
                    feedback[t_idx] = {
                        "word": target_tokens[t_idx],
                        "status": "incorrect",
                        "accuracy_score": 0.0,
                        "transcribed_as": None
                    }
                    
        # Fill any remaining unassigned slots with safe defaults
        for idx in range(len(feedback)):
            if feedback[idx] is None:
                feedback[idx] = {
                    "word": target_tokens[idx],
                    "status": "incorrect",
                    "accuracy_score": 0.0,
                    "transcribed_as": None
                }
                
        return feedback

    def _convert_digits_to_words(self, text: str) -> str:
        """
        Converts any sequences of digits (integers or decimals) in the text to their spoken English word equivalents.
        e.g., "1941" -> "nineteen forty-one"
        e.g., "3.5" -> "three point five"
        e.g., "42" -> "forty-two"
        """
        import re

        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        def convert_below_100(val: int) -> str:
            if val < 10:
                return ones[val]
            elif val < 20:
                return teens[val - 10]
            else:
                tens_part = tens[val // 10]
                ones_part = ones[val % 10]
                if ones_part:
                    return f"{tens_part}-{ones_part}"
                return tens_part

        def convert_integer(val_str: str) -> str:
            # If it looks like a year (4 digits, starting with 1 or 2, e.g. 1000 to 2999)
            if len(val_str) == 4 and val_str[0] in ('1', '2'):
                part1 = int(val_str[:2])
                part2 = int(val_str[2:])
                w1 = convert_below_100(part1)
                if part2 == 0:
                    return f"{w1} hundred"
                elif part2 < 10:
                    return f"{w1} oh-{ones[part2]}"
                else:
                    return f"{w1} {convert_below_100(part2)}"
            
            val = int(val_str)
            if val == 0:
                return "zero"
                
            if val < 100:
                return convert_below_100(val)
                
            if val < 1000:
                hundreds = ones[val // 100]
                remainder = val % 100
                if remainder == 0:
                    return f"{hundreds} hundred"
                else:
                    return f"{hundreds} hundred and {convert_below_100(remainder)}"
            
            return val_str

        def convert_decimal(match) -> str:
            num_str = match.group(0)
            if '.' in num_str:
                parts = num_str.split('.')
                whole = convert_integer(parts[0])
                decimals = " ".join(ones[int(d)] if d != '0' else 'zero' for d in parts[1])
                return f"{whole} point {decimals}"
            else:
                return convert_integer(num_str)

        pattern = r'\b\d+(?:\.\d+)?\b'
        return re.sub(pattern, convert_decimal, text)

# Export a single thread-safe instance
audio_service = AudioService()
