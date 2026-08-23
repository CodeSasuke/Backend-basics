# 06. Application Structure And Request Lifecycle

[Previous: API Contracts](../../05-api-contracts/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Persistence Modeling](../../07-persistence-modeling/theory/README.md)

Structure isolates change. Transport translates protocol messages, the application layer coordinates a use case, domain code enforces decisions, and infrastructure persists or calls external systems.

```text
HTTP adapter -> use case -> domain rule -> repository interface
```

Ask: Which layer should know an HTTP status? Can a business rule be tested without a socket? Where does a transaction begin and end?

## Exit Check

Name one dependency that can be replaced without changing domain code.