"""
conftest.py — Test database setup using SQLite in-memory.

Strategy:
  • Crea las tablas una vez por sesión de pytest (scope=session).
  • Cada test recibe una sesión fresca; los datos se limpian entre tests
    ejecutando DELETE en todas las tablas (respeta FK order via sorted_tables).
  • Sobreescribe la dependencia `get_db` de FastAPI con la sesión de prueba
    para que los endpoints no toquen el MySQL real.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Importar todos los modelos para que Base.metadata los registre
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models import (Example, Exercise, ExerciseType, GlossaryEntry, GlossaryType, Lesson, LessonType, LessonCategory, Level)  # noqa: F401

SQLALCHEMY_TEST_URL = "sqlite:///:memory:"

_engine = create_engine(
    SQLALCHEMY_TEST_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


@pytest.fixture(scope="session", autouse=True)
def _create_tables():
    """Crea las tablas una sola vez para toda la sesión de pruebas."""
    Base.metadata.create_all(bind=_engine)
    yield
    Base.metadata.drop_all(bind=_engine)


@pytest.fixture
def db(_create_tables):
    """Sesión de BD por test. Limpia todos los datos al finalizar."""
    session = TestingSession()
    try:
        yield session
    finally:
        session.close()
    # Limpiar datos en orden inverso (respeta restricciones de FK)
    with _engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute(table.delete())


@pytest.fixture
def client(db):
    """TestClient de FastAPI con la BD de prueba inyectada."""
    def _override_get_db():
        yield db

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# ── Data factories ────────────────────────────────────────────────────────────

@pytest.fixture
def level_a1(db) -> Level:
    level = Level(
        code="A1",
        name="Beginner",
        description="Basic everyday phrases.",
        order_index=1,
    )
    db.add(level)
    db.commit()
    db.refresh(level)
    return level


@pytest.fixture
def published_lesson(db, level_a1) -> Lesson:
    lesson = Lesson(
        level_id=level_a1.id,
        title="The /θ/ Sound",
        type=LessonType.PHONETICS,
        category=LessonCategory.VERB_TENSES,
        description="Voiceless TH sound.",
        order_index=1,
        is_published=True,
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson


@pytest.fixture
def lesson_with_content(db, published_lesson) -> Lesson:
    """Published lesson with one example and one exercise."""
    example = Example(
        lesson_id=published_lesson.id,
        phrase="Think about it.",
        translation="Piénsalo.",
        ipa_notation="/θɪŋk əˈbaʊt ɪt/",
        order_index=1,
    )
    exercise = Exercise(
        lesson_id=published_lesson.id,
        type=ExerciseType.MULTIPLE_CHOICE,
        question="Which word has the /θ/ sound?",
        correct_answer="tooth",
        options={"a": "this", "b": "tooth", "c": "breathe"},
        order_index=1,
    )
    db.add_all([example, exercise])
    db.commit()
    db.refresh(published_lesson)
    return published_lesson
