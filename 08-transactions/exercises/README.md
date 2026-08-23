# Exercises: Transactions

[Previous: Persistence Modeling](../../07-persistence-modeling/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Caches And Queues](../../09-caches-queues/exercises/README.md)

- Compare a query plan before and after adding an index.
- Run two withdrawals concurrently against one account.
- Raise an exception midway through a transfer and inspect the database.

## Task

Implement account transfers with transaction boundaries and invariant tests. Demonstrate a naive failure first, then correct it.

## Exit Check

State which operations are atomic and which are merely adjacent.