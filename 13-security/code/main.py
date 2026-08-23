"""Authorization decision starter. Do not store real passwords in this exercise."""


def can_read_note(user_id: str, owner_id: str, is_admin: bool = False) -> bool:
    return is_admin or user_id == owner_id


if __name__ == "__main__":
    print(can_read_note("alice", "alice"))
    print(can_read_note("bob", "alice"))
    print(can_read_note("operator", "alice", is_admin=True))
