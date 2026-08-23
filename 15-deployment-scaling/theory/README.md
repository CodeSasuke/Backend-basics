# 15. Deployment, Scaling And System Design

[Previous: Testing And Delivery](../../14-testing-delivery/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Capstone](../../16-capstone/theory/README.md)

Deployment places a service in an environment with finite resources and operational ownership. Scaling means finding and relieving bottlenecks while managing state, coordination, consistency, and cost.

```text
clients -> load balancer -> service instances -> database
                              +-> cache / queue / workers
```

Ask: What does stateless mean? Which component saturates first at ten times traffic? What can be eventually consistent? How does rollback work?

## Exit Check

Defend one scaling decision with an estimate and name its uncertainty.