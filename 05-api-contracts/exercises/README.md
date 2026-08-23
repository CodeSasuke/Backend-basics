# Exercises: API Contracts

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Networking And HTTP](../../04-networking-http/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Application Structure](../../06-application-structure/exercises/README.md)

- Design JSON success and error shapes for a notes resource.
- Add pagination, filtering, and sorting with explicit ordering rules.
- Send the same create request twice and define the desired result.

## Task

Write a contract for notes before implementation. Include examples, invalid cases, status codes, authentication assumptions, and a backwards-compatibility rule. Test it from an external client.

## Exit Check

Identify one guarantee that belongs in the contract and one detail that should remain private.