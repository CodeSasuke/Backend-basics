"""Bounded concurrency starter."""

from concurrent.futures import ThreadPoolExecutor


def run_bounded(jobs: list[str], workers: int = 2) -> list[str]:
    if workers < 1:
        raise ValueError("workers must be positive")
    with ThreadPoolExecutor(max_workers=workers) as executor:
        return list(executor.map(lambda job: f"done:{job}", jobs))


if __name__ == "__main__":
    print(run_bounded(["a", "b", "c"], workers=2))
