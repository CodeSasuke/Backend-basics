# Exercises: Deployment And Scaling

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Testing And Delivery](../../14-testing-delivery/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Capstone](../../16-capstone/exercises/README.md)

- Estimate capacity from measured latency and a concurrency limit.
- Run two instances and find state incorrectly kept local.
- Design health and readiness checks with different meanings.

## Task

Write a deployment design for the notes service including assumptions, limits, failure modes, rollback, backups, migrations, alerts, and cost-aware alternatives.

## Exit Check

Identify the bottleneck, scaling action, and new failure introduced by that action.