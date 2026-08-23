# Lesson: Observability And Debugging

## Start With The Problem
A running service is too complex to inspect directly. Operators need evidence that explains behavior across requests and dependencies.

## Core Model
Logs describe events, metrics summarize patterns, and traces connect work across boundaries.

```text
request ID -> API span -> database span
           -> logs + metrics + trace context
```

## Worked Example
A request ID ties a slow API event to its database event. A latency percentile can reveal a problem hidden by a healthy average.

## Think About It
- What evidence distinguishes client slowness from database slowness?
- Which fields are safe to log?
- Which metric dimensions explode cardinality?

## Common Mistakes
Logging secrets, using unbounded IDs as metric labels, and debugging without a falsifiable hypothesis.

## Mastery Check
Write a runbook that diagnoses error rate, latency, saturation, and dependency failure.