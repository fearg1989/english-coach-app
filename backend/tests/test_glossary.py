"""
Tests para GET /api/v1/glossary/
  - Sin filtro devuelve todas las entradas
  - Filtro type=phrasal_verb devuelve solo phrasal verbs
  - Filtro type=irregular_verb devuelve solo verbos irregulares
  - Tipo inválido devuelve 400
  - La respuesta incluye los campos requeridos
  - Los verbos irregulares incluyen form_past y form_participle
"""
import pytest
from fastapi import status

from app.models.glossary import GlossaryEntry, GlossaryType


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def phrasal_entry(db) -> GlossaryEntry:
    entry = GlossaryEntry(
        type=GlossaryType.PHRASAL_VERB,
        term="spin up",
        meaning="inicializar / levantar un servicio",
        form_past=None,
        form_participle=None,
        order_index=1,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@pytest.fixture
def irregular_entry(db) -> GlossaryEntry:
    entry = GlossaryEntry(
        type=GlossaryType.IRREGULAR_VERB,
        term="go",
        meaning="ir",
        form_past="went",
        form_participle="gone",
        order_index=1,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


# ── GET /api/v1/glossary/ ─────────────────────────────────────────────────────

class TestListGlossaryEntries:
    def test_empty_database_returns_empty_list(self, client):
        response = client.get("/api/v1/glossary/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_returns_all_entries_without_filter(self, client, phrasal_entry, irregular_entry):
        response = client.get("/api/v1/glossary/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2

    def test_filter_by_phrasal_verb_type(self, client, phrasal_entry, irregular_entry):
        response = client.get("/api/v1/glossary/?type=phrasal_verb")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1
        assert data[0]["type"] == "phrasal_verb"
        assert data[0]["term"] == "spin up"

    def test_filter_by_irregular_verb_type(self, client, phrasal_entry, irregular_entry):
        response = client.get("/api/v1/glossary/?type=irregular_verb")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1
        assert data[0]["type"] == "irregular_verb"
        assert data[0]["term"] == "go"

    def test_invalid_type_returns_400(self, client):
        response = client.get("/api/v1/glossary/?type=unknown_type")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_response_contains_required_fields(self, client, phrasal_entry):
        data = client.get("/api/v1/glossary/").json()
        item = data[0]
        for field in ("id", "type", "term", "meaning", "form_past", "form_participle", "order_index"):
            assert field in item, f"Campo '{field}' ausente en la respuesta"

    def test_phrasal_verb_has_null_verb_forms(self, client, phrasal_entry):
        data = client.get("/api/v1/glossary/?type=phrasal_verb").json()
        assert data[0]["form_past"] is None
        assert data[0]["form_participle"] is None

    def test_irregular_verb_has_verb_forms(self, client, irregular_entry):
        data = client.get("/api/v1/glossary/?type=irregular_verb").json()
        assert data[0]["form_past"] == "went"
        assert data[0]["form_participle"] == "gone"

    def test_meaning_is_present(self, client, irregular_entry):
        data = client.get("/api/v1/glossary/?type=irregular_verb").json()
        assert data[0]["meaning"] == "ir"
