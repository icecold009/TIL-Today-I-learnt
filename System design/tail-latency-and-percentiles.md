# Tail Latency: The Slowest Request Usually Wins

One of the most important lessons in distributed systems is that the average response time is often misleading. In real systems, the user experience is dominated by the slowest requests, not the fastest ones.

### Why the tail matters

If an API returns 99 requests in 20 ms but 1 request takes 2 seconds, the average still looks fine. The problem is that any user hitting that slow path experiences the 2 second delay. At scale, those rare outliers become visible very quickly.

This is why teams care about **p95**, **p99**, and even **p99.9** latency:

* **p95** means 95% of requests are faster than this value.
* **p99** means 99% of requests are faster than this value.
* **p99.9** captures the extreme outliers that can wreck a production SLO.

### The “tail at scale” effect

As traffic increases, the probability of hitting a slow dependency, noisy neighbor, GC pause, or network retry also increases. Even if each individual component is reliable, a request that fans out to multiple services can inherit the worst latency from any one of them.

That is why large systems often get slower at the top end even when the median stays stable.

### Common causes of tail latency

* Cache misses that fall back to a slower database.
* Uneven shard distribution where one partition gets hotter than the rest.
* Retries that amplify load during partial failures.
* Lock contention, queue buildup, or stop-the-world garbage collection.
* Shared infrastructure that becomes noisy under bursty traffic.

### How teams fight it

The usual strategies are not just about making the average faster. They are about preventing rare stalls:

* Use timeouts and circuit breakers so one bad dependency does not block everything.
* Add hedged requests carefully when a very small number of slow outliers matters more than extra load.
* Reduce fan-out where possible.
* Measure percentiles, not just averages.
* Keep the critical path small and predictable.

### A useful mental model

Think of latency like a queue at a store. Most customers move quickly, but the slowest customer at the front controls the entire line. In distributed systems, the line is the request path, and tail latency is the customer that makes everyone else wait.