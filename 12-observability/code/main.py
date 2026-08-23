"""Structured event logging starter."""

import json
import logging
import time
import uuid


logging.basicConfig(level=logging.INFO, format="%(message)s")


def handle_request() -> None:
    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    logging.info(json.dumps({"event": "request.started", "request_id": request_id}))
    duration_ms = round((time.perf_counter() - started) * 1000, 2)
    logging.info(json.dumps({"event": "request.finished", "request_id": request_id, "duration_ms": duration_ms}))


if __name__ == "__main__":
    handle_request()
