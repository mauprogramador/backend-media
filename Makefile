#!make
include .env


dev-run:
	uvicorn app.main.server:app

dev-reload:
	uvicorn app.main.server:app --reload

prod-run:
	uvicorn app.main.server:app --host 0.0.0.0 --port ${APP_PORT}

prod-reload:
	uvicorn app.main.server:app --reload --host 0.0.0.0 --port ${APP_PORT}
