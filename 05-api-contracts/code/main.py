"""Contract validation starter. Keep transport separate from domain rules."""


def validate_create_note(payload: object) -> tuple[bool, dict[str, str]]:
    if not isinstance(payload, dict):
        return False, {"code": "invalid_json", "message": "object required"}
    title = payload.get("title")
    body = payload.get("body")
    if not isinstance(title, str) or not title.strip():
        return False, {"code": "invalid_title", "message": "title is required"}
    if not isinstance(body, str) or not body.strip():
        return False, {"code": "invalid_body", "message": "body is required"}
    return True, {"title": title.strip(), "body": body.strip()}


if __name__ == "__main__":
    print(validate_create_note({"title": "Learning", "body": "Contracts"}))
    print(validate_create_note({"title": "", "body": "Missing title"}))
