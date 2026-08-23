# 05. API Design And Contracts

[Previous: Networking And HTTP](../../04-networking-http/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Application Structure](../../06-application-structure/theory/README.md)

An API is a promise between independent programs. A useful contract defines inputs, outputs, errors, guarantees, and how change remains compatible.

```text
contract = schema + errors + guarantees + compatibility rules
```

Ask: What can a client rely on after success? Which errors are retryable? Is this operation idempotent by behavior? What happens to old clients after a server change?

## Exit Check

Change internal storage without changing the API contract and explain why clients continue working.