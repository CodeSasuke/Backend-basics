# Exercises: Networking And HTTP

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Protocols](../../03-protocols/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: API Contracts](../../05-api-contracts/exercises/README.md)

- Inspect method, path, headers, body, and status with `curl`.
- Compare read and write requests by their retry behavior.
- Add deliberate delay and failure to a local handler.

## Task

Build a standard-library HTTP service exposing `/health`, `/accounts`, and `/accounts/{id}/balance`. Return explicit status codes and JSON errors. Test it as an external client, not only by calling functions.

## Exit Check

Explain what the client knows after a timeout and what remains unknown.