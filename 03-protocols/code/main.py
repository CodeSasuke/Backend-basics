"""Strict line protocol starter."""


def parse_message(raw: bytes) -> dict[str, str]:
    text = raw.decode("utf-8")
    fields = text.rstrip("\n").split("|", maxsplit=2)
    if len(fields) != 3 or fields[0] != "CREATE":
        raise ValueError("expected CREATE|title|body")
    _, title, body = fields
    if not title.strip() or not body.strip():
        raise ValueError("title and body are required")
    return {"type": "create", "title": title, "body": body}


def encode_message(message: dict[str, str]) -> bytes:
    if message.get("type") != "create":
        raise ValueError("unsupported message type")
    return f"CREATE|{message['title']}|{message['body']}\n".encode("utf-8")


if __name__ == "__main__":
    raw = encode_message({"type": "create", "title": "First", "body": "Hello"})
    print(raw)
    print(parse_message(raw))
