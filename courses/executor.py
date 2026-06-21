#!/usr/bin/env python3
"""Sandbox de ejecución de código Python en subproceso aislado."""
import os
import queue
import subprocess
import sys
import threading


def run_code_streaming(code: str, exec_id: str, q: queue.Queue, timeout: int = 10) -> None:
    """Ejecuta código Python en subproceso restringido y emite eventos al queue."""
    restricted = {
        "PATH": os.environ.get("PATH", ""),
        "PYTHONPATH": "",
        "HOME": "/tmp",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    try:
        proc = subprocess.Popen(
            [sys.executable, "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=restricted,
        )

        def _stream_stdout():
            assert proc.stdout is not None
            total = 0
            for line in proc.stdout:
                total += len(line)
                if total > 50_000:
                    q.put({"type": "output", "text": "\n[Output truncado a 50KB]\n", "stream": "stdout"})
                    break
                q.put({"type": "output", "text": line, "stream": "stdout"})

        t = threading.Thread(target=_stream_stdout, daemon=True)
        t.start()
        t.join(timeout=timeout)

        if t.is_alive():
            proc.kill()
            q.put({"type": "exec_error", "message": f"Timeout: ejecución cancelada a los {timeout}s"})
            return

        assert proc.stderr is not None
        stderr = proc.stderr.read(50_000)
        if stderr:
            q.put({"type": "output", "text": stderr, "stream": "stderr"})

        proc.wait()
        q.put({"type": "exec_done", "exit_code": proc.returncode})

    except Exception as exc:
        q.put({"type": "exec_error", "message": str(exc)})
    finally:
        q.put(None)  # sentinel — mismo patrón que Bruno
