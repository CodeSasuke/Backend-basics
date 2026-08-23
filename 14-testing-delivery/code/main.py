"""Behavior-first function ready to test with pytest."""


def normalize_title(title: str) -> str:
    normalized = " ".join(title.split())
    if not normalized:
        raise ValueError("title is required")
    return normalized


if __name__ == "__main__":
    print(normalize_title("  backend   basics "))
