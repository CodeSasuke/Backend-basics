"""Atomic transfer starter using SQLite transactions."""

import sqlite3


def transfer(database: sqlite3.Connection, source: int, target: int, amount: int) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")
    with database:
        source_balance = database.execute(
            "SELECT balance FROM accounts WHERE id = ?", (source,)
        ).fetchone()
        if source_balance is None or source_balance[0] < amount:
            raise ValueError("insufficient funds")
        database.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, source))
        database.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, target))


if __name__ == "__main__":
    database = sqlite3.connect(":memory:")
    database.executescript("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL);")
    database.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 100), (2, 0)])
    transfer(database, 1, 2, 25)
    print(database.execute("SELECT * FROM accounts").fetchall())
