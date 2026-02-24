# The Circuit Breaker Pattern

In a microservices architecture, one service often calls another. If the "Service B" is slow or failing, "Service A" might get stuck waiting for it, eventually running out of resources and crashing too. This is called a **Cascading Failure**.

### 🔌 The Three States
The Circuit Breaker acts as a middleman with three states:

1. **Closed (Normal):** The circuit is closed, and requests flow through to the service. We count how many requests fail.
2. **Open (Failing):** If the failure rate hits a threshold (e.g., 50%), the breaker "trips" and opens. All further requests fail immediately without even trying to hit the service. This gives the failing service time to recover.
3. **Half-Open (Testing):** After a "sleep window," the breaker allows a few trial requests through. If they succeed, it closes. If they fail, it opens again.



### 💡 Why it matters
It improves **Resiliency**. Instead of a user seeing a "Loading..." spinner for 30 seconds before a crash, they get an immediate "Service temporarily unavailable" message, and the rest of your app stays functional.
