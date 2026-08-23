# 12. Observability And Debugging

[Previous: Concurrency](../../11-concurrency/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Security](../../13-security/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

Logs describe events, metrics summarize behavior, and traces connect work across boundaries. Debugging is hypothesis testing using evidence.

```text
request_id -> API span -> database span
          -> logs + metrics + trace context
```

Ask: What evidence separates a slow database from a slow client? Which metric dimensions are useful? What must never be logged?

## Exit Check

Reconstruct one failed request from telemetry alone.

## Complete Lesson

A running service is too complex to inspect directly. Logs describe events, metrics summarize patterns, and traces connect work across boundaries. A request ID ties a slow API event to its database event, while a latency percentile can reveal a problem hidden by a healthy average.

Ask what evidence separates client slowness from database slowness and what must never be logged. Debugging should test a falsifiable hypothesis.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
