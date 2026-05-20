"""
Tests para:
  - GET /api/v1/lessons/level/{id}  (lista con filtros)
  - GET /api/v1/lessons/{id}        (detalle con examples y exercises)
"""
from fastapi import status

from app.models import Lesson, LessonCategory, LessonType


class TestListLessonsByLevel:
    def test_returns_empty_list_when_no_lessons(self, client, level_a1):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_excludes_unpublished_lessons(self, client, db, level_a1):
        lesson = Lesson(
            level_id=level_a1.id,
            title="Draft lesson",
            type=LessonType.GRAMMAR,
            is_published=False,
            order_index=1,
        )
        db.add(lesson)
        db.commit()
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}")
        assert response.json() == []

    def test_returns_only_published_lessons(self, client, published_lesson, level_a1):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}")
        data = response.json()
        assert len(data) == 1
        assert data[0]["title"] == published_lesson.title
        assert data[0]["is_published"] is True

    def test_response_contains_required_fields(self, client, published_lesson, level_a1):
        data = client.get(f"/api/v1/lessons/level/{level_a1.id}").json()
        item = data[0]
        for field in ("id", "level_id", "title", "type", "category", "is_published", "order_index"):
            assert field in item, f"Campo '{field}' ausente en la respuesta"

    def test_filter_by_category_returns_irregular_verbs(self, client, db, level_a1):
        lesson = Lesson(
            level_id=level_a1.id,
            title="Irregular verbs overview",
            type=LessonType.GRAMMAR,
            category=LessonCategory.IRREGULAR_VERBS,
            description="Irregular verbs example.",
            order_index=2,
            is_published=True,
        )
        db.add(lesson)
        db.commit()

        response = client.get("/api/v1/lessons/category/irregular_verbs")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1
        assert data[0]["category"] == "irregular_verbs"

    def test_invalid_category_filter_returns_400(self, client):
        response = client.get("/api/v1/lessons/category/invalid_category")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_by_phonetics_returns_matching_lesson(
        self, client, published_lesson, level_a1
    ):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}?type=phonetics")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1
        assert data[0]["type"] == "phonetics"

    def test_filter_by_grammar_returns_empty_for_phonetics_lesson(
        self, client, published_lesson, level_a1
    ):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}?type=grammar")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_invalid_type_filter_returns_400(self, client, level_a1):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}?type=invalid_type")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_invalid_type_detail_lists_valid_options(self, client, level_a1):
        response = client.get(f"/api/v1/lessons/level/{level_a1.id}?type=bad")
        detail = response.json()["detail"].lower()
        assert "grammar" in detail or "phonetics" in detail


class TestGetLessonDetail:
    def test_returns_404_for_nonexistent_lesson(self, client):
        response = client.get("/api/v1/lessons/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_404_detail_contains_not_found(self, client):
        response = client.get("/api/v1/lessons/99999")
        assert "not found" in response.json()["detail"].lower()

    def test_returns_lesson_with_examples_and_exercises(
        self, client, lesson_with_content
    ):
        response = client.get(f"/api/v1/lessons/{lesson_with_content.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == lesson_with_content.id
        assert len(data["examples"]) == 1
        assert len(data["exercises"]) == 1

    def test_example_fields_are_correct(self, client, lesson_with_content):
        data = client.get(f"/api/v1/lessons/{lesson_with_content.id}").json()
        example = data["examples"][0]
        assert example["phrase"] == "Think about it."
        assert example["translation"] == "Piénsalo."
        assert example["ipa_notation"] == "/θɪŋk əˈbaʊt ɪt/"
        assert example["audio_url"] is None  # Fase 2 — no poblado aún

    def test_exercise_fields_are_correct(self, client, lesson_with_content):
        data = client.get(f"/api/v1/lessons/{lesson_with_content.id}").json()
        exercise = data["exercises"][0]
        assert exercise["type"] == "multiple_choice"
        assert exercise["correct_answer"] == "tooth"
        assert "a" in exercise["options"]

    def test_lesson_without_examples_returns_empty_lists(
        self, client, published_lesson
    ):
        """Lección publicada sin ejemplos ni ejercicios aún."""
        response = client.get(f"/api/v1/lessons/{published_lesson.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["examples"] == []
        assert data["exercises"] == []

    def test_lesson_type_is_correct(self, client, lesson_with_content):
        data = client.get(f"/api/v1/lessons/{lesson_with_content.id}").json()
        assert data["type"] == "phonetics"
