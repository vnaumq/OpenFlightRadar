"""OpenFlightRadar — точка входа сервиса.

Минимальная заготовка: подключение к PostgreSQL + /health для проверки,
что app и db видят друг друга. Дальше сюда добавляем реальную логику.
"""

from __future__ import annotations

import os

import psycopg
from fastapi import FastAPI

DB_CONFIG = {
    "host": os.getenv("PGHOST", "db"),
    "port": os.getenv("PGPORT", "5432"),
    "user": os.getenv("POSTGRES_USER", "ofr"),
    "password": os.getenv("POSTGRES_PASSWORD", "ofr"),
    "dbname": os.getenv("POSTGRES_DB", "ofr"),
}

app = FastAPI(title="OpenFlightRadar", version="0.1.0")


@app.get("/")
def root() -> dict:
    return {"service": "openflightradar", "status": "ok"}


@app.get("/health")
def health() -> dict:
    """Проверяет, что база отвечает."""
    try:
        with psycopg.connect(**DB_CONFIG, connect_timeout=3) as conn:
            version = conn.execute("select version()").fetchone()[0]
        return {"status": "ok", "db": version.split(",")[0]}
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "db": str(exc)}
