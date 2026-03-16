# Monoliths vs. Microservices

Architectural patterns define how the different parts of an application are bundled and how they communicate. 

### 🏛️ The Monolith (The "All-in-One")
A monolithic application is built as a single, unified unit. All functions (User UI, Business Logic, Database Access) are managed in one place.

* **Pros:** Simple to develop, test, and deploy (one file/container). Great for small teams and new startups.
* **Cons:** Hard to scale specific parts. If the "Video Processing" module crashes, the whole site goes down. The codebase becomes a "Big Ball of Mud" over time.



---

### 🐝 Microservices (The "Distributed Hive")
The application is broken down into small, independent services that communicate over a network (usually via REST, gRPC, or Message Brokers).

* **Pros:** * **Independent Scaling:** Scale only the service that needs it.
  * **Tech Diversity:** Use Python for AI and Go for high-performance networking in the same app.
  * **Fault Tolerance:** If the "Recommendation Service" dies, users can still "Check Out."
* **Cons:** * **The "Microservice Tax":** Massive complexity in networking, security (JWTs everywhere!), and data consistency.
  * **Operational Overhead:** You need robust CI/CD and monitoring (Kubernetes, Docker).



---

### 📊 Comparison Table

| Feature | Monolith | Microservices |
| :--- | :--- | :--- |
| **Deployment** | All at once | Independent |
| **Data** | Single Shared DB | Database per Service |
| **Latency** | Low (Internal calls) | High (Network calls) |
| **Complexity** | Code-level | Infrastructure-level |
