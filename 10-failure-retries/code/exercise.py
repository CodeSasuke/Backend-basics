"""Exercise implementation: add bounded retries and a deadline."""

from collections.abc import Callable


def retry(operation: Callable[[], str], attempts: int = 3) -> str:
    """TODO: classify failures, bound attempts, and apply backoff."""
    raise NotImplementedError
