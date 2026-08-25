# 16. Capstone Theory: Reliable Notes And Jobs Platform

[Previous: Deployment And Scaling](../../15-deployment-scaling/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Build log](../exercises/experiment.md) | [Starter code](../code/main.py)

## Lesson Orientation

This capstone integrates the earlier boundaries into one reliable notes and jobs platform. Read the theory and inspect the starter code before running it.

The capstone combines the earlier boundaries: API contract, domain invariants, durable state, transactions, asynchronous work, failure handling, security, observability, testing, and deployment.

```text
client -> API -> use case -> database
                    |
                    +-> queue -> worker -> derived report
```

## Socratic Review

- What is the source of truth for each fact?
- What happens when every dependency is slow, duplicated, or unavailable?
- Which operations are safe to retry?
- Which guarantee did you intentionally not provide?

## Completion Standard

A design is complete only when its normal path, failure path, evidence, security boundary, and recovery path are documented.

## Complete Lesson

A production backend combines API contracts, domain invariants, durable state, transactions, asynchronous work, failure handling, security, observability, testing, and deployment.

A note request validates its contract, checks ownership, commits durable state, emits work, and returns an answer safe to retry. Ask what is the source of truth for each fact, which operations are safe to retry, and what the client observes during deployment.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Trace one request across the API, domain, database, queue, worker, security, and observability boundaries. Before executing the program, record your predictions and observations in the [build log](../exercises/experiment.md).

Run the capstone experiment only after making your predictions. Then answer the Socratic review questions using both the code and the evidence you recorded.

## Dialogue Check

**You:** How do all these ideas work together?

**Guide:** Follow one request across contract, domain, storage, queue, security, failure handling, and telemetry.

**You:** How do I prove the design is complete?

**Guide:** Show the normal path, failure path, evidence, recovery path, and guarantee you intentionally do not provide.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
