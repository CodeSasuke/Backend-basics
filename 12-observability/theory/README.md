# 12. Observability And Debugging

[Previous: Concurrency](../../11-concurrency/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Security](../../13-security/theory/README.md)

## Lesson Orientation

This lesson presents logs, metrics, and traces as evidence for testing explanations about system behavior. Read the theory and inspect the starter code before running it.

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

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the events, measurements, identifiers, and boundaries that would provide evidence during a failure. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** What evidence would prove my hypothesis?

**Guide:** Choose a safe log, metric, or trace that can distinguish the possible causes.

**You:** Is the average enough?

**Guide:** Check the distribution and the slow outliers before deciding what to change.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
