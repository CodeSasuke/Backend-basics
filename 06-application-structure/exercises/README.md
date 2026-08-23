# Exercises: Application Structure

[Previous: API Contracts](../../05-api-contracts/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Persistence Modeling](../../07-persistence-modeling/exercises/README.md)

- Extract domain logic from an HTTP handler.
- Replace a real repository with an in-memory fake in tests.
- Draw a sequence diagram for one request.

## Task

Refactor the notes service into transport, application, domain, and persistence modules while keeping its public contract stable.

## Exit Check

Trace data through each layer and state which layer owns each decision.