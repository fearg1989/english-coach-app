from fastapi import APIRouter, Depends

from app.api.deps import get_level_service
from app.schemas.level import LevelResponse
from app.services.level_service import LevelService

router = APIRouter(prefix="/levels", tags=["Levels"])


@router.get(
    "/",
    response_model=list[LevelResponse],
    summary="List all CEFR levels",
)
def list_levels(
    service: LevelService = Depends(get_level_service),
) -> list[LevelResponse]:
    """Returns all six CEFR levels ordered by progression (A1 → C2)."""
    return service.get_all_levels()


@router.get(
    "/{level_id}",
    response_model=LevelResponse,
    summary="Get level by ID",
)
def get_level_by_id(
    level_id: int,
    service: LevelService = Depends(get_level_service),
) -> LevelResponse:
    return service.get_level_by_id(level_id)


@router.get(
    "/code/{code}",
    response_model=LevelResponse,
    summary="Get level by CEFR code",
)
def get_level_by_code(
    code: str,
    service: LevelService = Depends(get_level_service),
) -> LevelResponse:
    """Accepts codes like A1, b2, C1 (case-insensitive)."""
    return service.get_level_by_code(code)
