# System design

Architecture notes about scaling, resilience, and distributed-system tradeoffs.

## Best notes

* [API communication protocols](./api-communication-protocols.md) - How services exchange data in practice.
* [CAP theorem](./cap-theorem.md) - The tradeoff model that still frames distributed systems thinking.
* [Consistent hashing](./consistent-hashing.md) - A low-churn approach to partitioning data and load.
* [Idempotency](./idempotency.md) - Why safe retries depend on stable request semantics.
* [Microservices vs monoliths](./microservices-vs-monoliths.md) - A tradeoff, not a religion.
* [Rate limiting algorithms](./rate-limiting-algorithms.md) - Guardrails that control traffic and protect systems.
* [Tail latency and percentiles](./tail-latency-and-percentiles.md) - Why the slowest requests define user experience.
* [The circuit breaker pattern](./the-circuit-breaker-pattern.md) - A resilience pattern for unstable dependencies.
* [The SOLID principles](./the-solid-principles.md) - Design guidance that stays useful even at larger scale.

## Related topics

* [Networking](../Networking)
* [Databases](../Databases)