# 16. Capstone Theory: Reliable Notes And Jobs Platform

[Previous: Deployment And Scaling](../../15-deployment-scaling/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Build log](../exercises/experiment.md) | [Starter code](../code/main.py)

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