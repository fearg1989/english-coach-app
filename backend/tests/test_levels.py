"""
Tests para GET /api/v1/levels/
  - Lista todos los niveles ordenados
  - GET por ID: happy path y 404
  - GET por código CEFR: happy path, insensible a mayúsculas, 404
"""
from fastapi import status

from app.models import Level


class TestListLevels:
    def test_empty_database_returns_empty_list(self, client):
        response = client.get("/api/v1/levels/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_returns_all_levels(self, client, db):
        db.add_all([
            Level(code="B1", name="Intermediate", order_index=3),
            Level(code="A1", name="Beginner", order_index=1),
        ])
        db.commit()
        response = client.get("/api/v1/levels/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2

    def test_levels_are_ordered_by_order_index(self, client, db):
        db.add_all([
            Level(code="C1", name="Advanced", order_index=5),
            Level(code="A1", name="Beginner", order_index=1),
            Level(code="B2", name="Upper Intermediate", order_index=4),
        ])
        db.commit()
        data = client.get("/api/v1/levels/").json()
        codes = [item["code"] for item in data]
        assert codes == ["A1", "B2", "C1"]

    def test_response_contains_required_fields(self, client, level_a1):
        data = client.get("/api/v1/levels/").json()
        assert len(data) == 1
        item = data[0]
        for field in ("id", "code", "name", "description", "order_index"):
            assert field in item, f"Campo '{field}' ausente en la respuesta"

    def test_code_is_uppercased_in_response(self, client, level_a1):
        data = client.get("/api/v1/levels/").json()
        assert data[0]["code"] == "A1"


class TestGetLevelById:
    def test_returns_level_when_exists(self, client, level_a1):
        response = client.get(f"/api/v1/levels/{level_a1.id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["code"] == "A1"
        assert response.json()["name"] == "Beginner"

    def test_returns_404_for_nonexistent_id(self, client):
        response = client.get("/api/v1/levels/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_404_detail_contains_not_found(self, client):
        response = client.get("/api/v1/levels/99999")
        assert "not found" in response.json()["detail"].lower()

    def test_returns_correct_level_fields(self, client, level_a1):
        data = client.get(f"/api/v1/levels/{level_a1.id}").json()
        assert data["id"] == level_a1.id
        assert data["description"] == "Basic everyday phrases."


class TestGetLevelByCode:
    def test_returns_level_by_uppercase_code(self, client, level_a1):
        response = client.get("/api/v1/levels/code/A1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["code"] == "A1"

    def test_lookup_is_case_insensitive_lowercase(self, client, level_a1):
        response = client.get("/api/v1/levels/code/a1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["code"] == "A1"

    def test_lookup_is_case_insensitive_mixed(self, client, level_a1):
        response = client.get("/api/v1/levels/code/A1")
        assert response.status_code == status.HTTP_200_OK

    def test_returns_404_for_unknown_code(self, client):
        response = client.get("/api/v1/levels/code/Z9")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_404_detail_for_unknown_code(self, client):
        response = client.get("/api/v1/levels/code/Z9")
        assert "not found" in response.json()["detail"].lower()
