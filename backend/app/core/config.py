from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ─── Application ─────────────────────────────────────────────────────────
    APP_NAME: str = "English Coach API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ─── Database ────────────────────────────────────────────────────────────
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "english_coach"
    DB_USER: str = "coach_user"
    DB_PASSWORD: str = "coach_pass"

    # ─── CORS ────────────────────────────────────────────────────────────────
    CORS_ORIGINS: list[str] = ["http://localhost:4200"]

    # ─── Speech To Text ──────────────────────────────────────────────────────
    WHISPER_MODEL: str = "small"

    # ─── AI Coach (Ollama) ───────────────────────────────────────────────────
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "gemma4:31b-cloud"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            "?charset=utf8mb4"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",  # Ignora vars Docker (MYSQL_*) presentes en el mismo .env
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
