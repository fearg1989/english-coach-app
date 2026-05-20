.PHONY: help up down seed logs backend-dev frontend-dev

help:
	@echo ""
	@echo "  English Coach App — Comandos disponibles"
	@echo "  ───────────────────────────────────────────"
	@echo "  make up            Levanta MySQL + Backend en Docker"
	@echo "  make down          Detiene y limpia contenedores"
	@echo "  make seed          Pobla la BD con datos de prueba"
	@echo "  make logs          Ver logs del backend"
	@echo "  make backend-dev   Inicia backend en modo desarrollo local"
	@echo "  make frontend-dev  Inicia frontend Angular"
	@echo ""

up:
	docker-compose up -d

down:
	docker-compose down

seed:
	cd backend && python -m scripts.seed

logs:
	docker-compose logs -f backend

backend-dev:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend-dev:
	cd frontend && ng serve --open
