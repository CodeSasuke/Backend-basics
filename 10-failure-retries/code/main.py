"""Bounded retry starter."""

import time
from collections.abc import Callable


def retry(operation: Callable[[], str], attempts: int = 3, delay: float = 0.01) -> str:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            return operation()
        except Exception as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(delay * (2**attempt))
    raise RuntimeError("operation did not succeed") from last_error


if __name__ == "__main__":
    calls = [0]

    def flaky() -> str:
        calls[0] += 1
        if calls[0] < 3:
            raise TimeoutError("dependency timed out")
        return "ok"

    print(retry(flaky))
