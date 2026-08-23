# 12. Observability And Debugging

[Previous: Concurrency](../../11-concurrency/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Security](../../13-security/theory/README.md)

Logs describe events, metrics summarize behavior, and traces connect work across boundaries. Debugging is hypothesis testing using evidence.

```text
request_id -> API span -> database span
          -> logs + metrics + trace context
```

Ask: What evidence separates a slow database from a slow client? Which metric dimensions are useful? What must never be logged?

## Exit Check

Reconstruct one failed request from telemetry alone.