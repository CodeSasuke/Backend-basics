# 13. Security Fundamentals

[Previous: Observability](../../12-observability/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Testing And Delivery](../../14-testing-delivery/theory/README.md)

Security protects confidentiality, integrity, and availability under adversarial input. Every boundary is untrusted; every privilege should be minimized.

```text
request -> validate -> authenticate identity -> authorize action
```

Authentication asks who. Authorization asks what that identity may do. Hash passwords with a reviewed library, protect secrets, prevent injection, and audit sensitive actions.

## Exit Check

For every endpoint, identify the asset, attacker capability, trust boundary, and control.