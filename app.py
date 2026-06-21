#!/usr/bin/env python3
"""Servidor FastAPI para el curso interactivo de sistemas multi-agente."""
import asyncio
import json
import os
import queue
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from courses.content import LESSONS
from courses.executor import run_code_streaming

app = FastAPI(title="Aprende Multi-Agentes — Curso Interactivo")
executor = ThreadPoolExecutor(max_workers=4)
sessions: dict[str, dict] = {}
PROGRESS_FILE = Path("progress.json")

# Monta archivos estáticos si la carpeta existe
static_dir = Path("static")
if static_dir.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")


# ── Rutas ────────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    """Sirve el index.html original de medlit (lector de literatura médica)."""
    p = Path("index.html")
    if not p.exists():
        return HTMLResponse("<h1>MedLit</h1>")
    return HTMLResponse(p.read_text(encoding="utf-8"))


@app.get("/tutorial", response_class=HTMLResponse)
async def tutorial():
    """Sirve la SPA del curso interactivo."""
    p = Path("static/index.html")
    if not p.exists():
        raise HTTPException(404, "SPA no encontrada. Verifica que static/index.html existe.")
    return HTMLResponse(p.read_text(encoding="utf-8"))


@app.get("/api/lessons")
async def list_lessons():
    """Retorna la lista de lecciones con metadatos (sin el código completo)."""
    return [
        {
            "id": l["id"],
            "module": l["module"],
            "module_title": l["module_title"],
            "step": l["step"],
            "title": l["title"],
            "description": l["description"],
            "requires_api_key": l["requires_api_key"],
        }
        for l in LESSONS
    ]


@app.get("/api/lessons/{lesson_id}")
async def get_lesson(lesson_id: str):
    """Retorna una lección completa con código inicial, solución y contenido."""
    lesson = next((l for l in LESSONS if l["id"] == lesson_id), None)
    if not lesson:
        raise HTTPException(404, f"Lección '{lesson_id}' no encontrada")
    return lesson


class RunRequest(BaseModel):
    lesson_id: str = "m1s1"
    code: str


@app.post("/api/run-code")
async def run_code(req: RunRequest):
    """Inicia la ejecución del código en sandbox y retorna un exec_id para el stream."""
    if not req.code.strip():
        raise HTTPException(400, "Código vacío")
    exec_id = str(uuid.uuid4())
    q: queue.Queue = queue.Queue()
    sessions[exec_id] = {"queue": q, "status": "running"}
    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, run_code_streaming, req.code, exec_id, q, 10)
    return {"exec_id": exec_id}


@app.get("/api/stream/{exec_id}")
async def stream(exec_id: str):
    """SSE stream de la ejecución — mismo patrón que Bruno."""
    session = sessions.get(exec_id)
    if not session:
        raise HTTPException(404, "Sesión no encontrada")
    q = session["queue"]
    loop = asyncio.get_event_loop()

    async def generate():
        while True:
            try:
                event = await loop.run_in_executor(None, lambda: q.get(timeout=60))
                if event is None:
                    yield 'data: {"type":"stream_end"}\n\n'
                    break
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
            except Exception:
                yield 'data: {"type":"ping"}\n\n'

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


class ProgressRequest(BaseModel):
    lesson_id: str
    completed: bool = True


@app.post("/api/progress")
async def save_progress(req: ProgressRequest):
    """Guarda el progreso de una lección en el servidor."""
    data: dict = {}
    if PROGRESS_FILE.exists():
        try:
            data = json.loads(PROGRESS_FILE.read_text())
        except Exception:
            data = {}
    data[req.lesson_id] = req.completed
    PROGRESS_FILE.write_text(json.dumps(data, indent=2))
    return {"ok": True}


@app.get("/api/progress")
async def get_progress():
    """Lee el progreso guardado en el servidor."""
    if not PROGRESS_FILE.exists():
        return {"completed": []}
    try:
        data = json.loads(PROGRESS_FILE.read_text())
        return {"completed": [k for k, v in data.items() if v]}
    except Exception:
        return {"completed": []}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
