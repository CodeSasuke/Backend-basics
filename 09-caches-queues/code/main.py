"""In-process queue and idempotent consumer starter."""

from collections import deque


def run_jobs(jobs: list[str]) -> list[str]:
    queue = deque(jobs)
    completed: set[str] = set()
    output: list[str] = []
    while queue:
        job_id = queue.popleft()
        if job_id in completed:
            continue
        completed.add(job_id)
        output.append(f"completed:{job_id}")
    return output


if __name__ == "__main__":
    print(run_jobs(["report-1", "report-1", "report-2"]))
