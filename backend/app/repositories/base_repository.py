from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Generic CRUD repository.
    Concrete repositories extend this class and inject the SQLAlchemy model.
    Following the Repository Pattern keeps service logic decoupled from the ORM.
    """

    def __init__(self, model: type[ModelType], db: Session) -> None:
        self._model = model
        self._db = db

    def get_by_id(self, entity_id: int) -> ModelType | None:
        return self._db.get(self._model, entity_id)

    def get_all(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return self._db.query(self._model).offset(skip).limit(limit).all()

    def create(self, entity: ModelType) -> ModelType:
        self._db.add(entity)
        self._db.commit()
        self._db.refresh(entity)
        return entity

    def delete(self, entity_id: int) -> bool:
        entity = self.get_by_id(entity_id)
        if entity is None:
            return False
        self._db.delete(entity)
        self._db.commit()
        return True
