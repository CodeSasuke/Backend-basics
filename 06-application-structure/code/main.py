"""Small layered application starter."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Note:
    title: str
    body: str


class NoteRepository:
    def __init__(self) -> None:
        self.notes: list[Note] = []

    def save(self, note: Note) -> Note:
        self.notes.append(note)
        return note


def create_note(repository: NoteRepository, title: str, body: str) -> Note:
    if not title.strip() or not body.strip():
        raise ValueError("title and body are required")
    return repository.save(Note(title=title.strip(), body=body.strip()))


if __name__ == "__main__":
    print(create_note(NoteRepository(), "Layered", "Design"))
