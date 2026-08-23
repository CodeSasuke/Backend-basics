"""Capstone integration checklist starter."""

CAPSTONE_SLICES = [
    "users and authentication",
    "private notes and authorization",
    "persistence and migrations",
    "background reports",
    "failure handling and idempotency",
    "observability and operations",
]


def show_slices() -> None:
    for number, slice_name in enumerate(CAPSTONE_SLICES, start=1):
        print(f"{number}. {slice_name}")


if __name__ == "__main__":
    show_slices()
