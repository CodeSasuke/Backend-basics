"""SQLite persistence starter."""

import sqlite3


SCHEMA = """
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    balance INTEGER NOT NULL CHECK (balance >= 0)
);
"""


def open_database(path: str = ":memory:") -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.executescript(SCHEMA)
    return connection


if __name__ == "__main__":
    database = open_database()
    database.execute("INSERT INTO accounts (balance) VALUES (?)", (0,))
    print(database.execute("SELECT id, balance FROM accounts").fetchall())
    database.close()
