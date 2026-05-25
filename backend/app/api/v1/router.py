from fastapi import APIRouter

from app.api.v1.endpoints import glossary, lessons, levels, audio

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(levels.router)
api_router.include_router(lessons.router)
api_router.include_router(glossary.router)
api_router.include_router(audio.router)
