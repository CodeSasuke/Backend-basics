"""A tiny in-memory backend state machine."""


def apply_command(balance: int, command: str) -> tuple[int, str]:
    """Return next balance and output for one command."""
    parts = command.split()
    if not parts:
        return balance, "error: empty command"

    operation = parts[0]
    if operation == "balance" and len(parts) == 1:
        return balance, str(balance)
    if operation in {"deposit", "withdraw"} and len(parts) == 2:
        try:
            amount = int(parts[1])
        except ValueError:
            return balance, "error: amount must be an integer"
        if amount <= 0:
            return balance, "error: amount must be positive"
        if operation == "withdraw" and amount > balance:
            return balance, "error: insufficient funds"
        next_balance = balance + amount if operation == "deposit" else balance - amount
        return next_balance, str(next_balance)
    return balance, "error: invalid command"


def main() -> None:
    balance = 0
    print("Commands: deposit N, withdraw N, balance, quit")
    while True:
        command = input("> ").strip()
        if command == "quit":
            break
        balance, output = apply_command(balance, command)
        print(output)


if __name__ == "__main__":
    main()
