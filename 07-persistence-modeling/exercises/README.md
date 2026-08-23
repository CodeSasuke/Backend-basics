# Exercises: Persistence And Modeling

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Application Structure](../../06-application-structure/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Transactions](../../08-transactions/exercises/README.md)

- Model notes and users as entities and relationships before creating tables.
- Restart at different points and record which facts must survive.
- Add a uniqueness constraint and classify its violation.

## Task

Move the ledger to SQLite. Define schema, constraints, indexes, and an initial migration. Test restart, rollback, uniqueness, and invalid state.

## Exit Check

Explain source-of-truth data versus a convenient in-memory representation.