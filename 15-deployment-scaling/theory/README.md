# 15. Deployment, Scaling And System Design

[Previous: Testing And Delivery](../../14-testing-delivery/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Capstone](../../16-capstone/theory/README.md)

## Lesson Orientation

This lesson connects deployment, capacity, state, operational ownership, and the trade-offs involved in scaling. Read the theory and inspect the starter code before running it.

Deployment places a service in an environment with finite resources and operational ownership. Scaling means finding and relieving bottlenecks while managing state, coordination, consistency, and cost.

```text
clients -> load balancer -> service instances -> database
                              +-> cache / queue / workers
```

Ask: What does stateless mean? Which component saturates first at ten times traffic? What can be eventually consistent? How does rollback work?

## Exit Check

Defend one scaling decision with an estimate and name its uncertainty.

## Complete Lesson

Production introduces variable traffic, finite resources, dependency failures, and operational ownership. Scaling relieves bottlenecks while managing state, consistency, coordination, and cost.

Adding service instances does not fix a saturated database. Capacity estimates begin with assumptions about concurrency, latency, and resource limits. Health means the process can serve; readiness means dependencies are usable.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the capacity assumptions, state ownership, health conditions, bottleneck, and rollback boundary. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** What is the bottleneck under more traffic?

**Guide:** State assumptions, estimate capacity, and measure before adding more instances.

**You:** What new risk could scaling create?

**Guide:** Consider coordination, shared state, consistency, cost, and rollback.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
