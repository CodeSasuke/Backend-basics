"""Resource lifetime experiment: process jobs from a file safely."""

from pathlib import Path
import os


def process_jobs(path: Path) -> tuple[int, list[str]]:
    processed = 0
    errors: list[str] = []
    with path.open(encoding="utf-8") as job_file:
        for line_number, line in enumerate(job_file, start=1):
            job = line.strip()
            if not job:
                continue
            if ":" not in job:
                errors.append(f"line {line_number}: malformed job")
                continue
            name, value = job.split(":", maxsplit=1)
            if not name or not value:
                errors.append(f"line {line_number}: incomplete job")
                continue
            processed += 1
    return processed, errors


def main() -> None:
    path = Path(os.environ.get("JOB_FILE", "jobs.txt"))
    if not path.exists():
        print(f"missing job file: {path}")
        raise SystemExit(2)
    processed, errors = process_jobs(path)
    print(f"processed={processed} errors={len(errors)}")
    for error in errors:
        print(error)


if __name__ == "__main__":
    main()
