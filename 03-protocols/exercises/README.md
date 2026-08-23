# Exercises: Protocols

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: OS Resources](../../02-os-resources/exercises/README.md) | [Theory](../theory/README.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Networking And HTTP](../../04-networking-http/exercises/README.md)

- Design a line-delimited job protocol and document its grammar.
- Encode the same message as JSON and as a delimiter format.
- Test empty, truncated, extra-field, and incorrectly typed messages.

## Task

Implement a strict parser and encoder for `CREATE|title|body`. Define valid messages, invalid messages, and the rule for adding a field without breaking old clients.

## Exit Check

Explain why decoding bytes does not prove that a request is valid.