# Exercises: Security

[Previous: Observability](../../12-observability/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Testing And Delivery](../../14-testing-delivery/exercises/README.md)

- Build an authorization matrix for users, notes, and administrators.
- Send malformed and unexpected input to every public field.
- Search source and logs for secrets, then design a prevention check.

## Task

Add users, password hashing through a reviewed library, authentication, ownership authorization, rate limiting, and security-focused tests. Document the threat model and residual risks.

## Exit Check

Explain why authentication alone does not protect a private note.