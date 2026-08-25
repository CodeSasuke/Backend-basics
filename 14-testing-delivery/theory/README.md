# 14. Testing And Delivery

[Previous: Security](../../13-security/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Deployment And Scaling](../../15-deployment-scaling/theory/README.md)

## Lesson Orientation

This lesson explains how tests make behavioral claims and how delivery processes make those claims repeatable. Read the theory and inspect the starter code before running it.

Tests are executable claims about behavior. Unit tests isolate rules, integration tests verify boundaries, contract tests protect agreements, and end-to-end tests verify workflows.

```text
many fast focused unit tests
fewer integration and contract tests
few broad end-to-end tests
```

Ask: Which behavior is valuable to protect? Which failure gives the best signal? Are tests coupled to implementation details?

## Exit Check

Prove that a refactor preserved behavior, not merely object structure.

## Complete Lesson

Code can appear correct while violating important behavior. Unit tests isolate rules, integration tests verify boundaries, contract tests protect agreements, and end-to-end tests verify workflows.

A unit test proves an overdraft is rejected; an integration test proves the database constraint and transaction behavior. Ask which behavior is worth protecting and what a clean checkout must reproduce.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the behavior under test, the boundary being exercised, and the evidence a clean delivery should reproduce. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** Which behavior must never regress?

**Guide:** Write the smallest test that proves it, then add a boundary test where components meet.

**You:** What makes delivery repeatable?

**Guide:** A clean checkout should run the same checks without relying on your machine.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
