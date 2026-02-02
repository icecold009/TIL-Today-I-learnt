# The CAP Theorem (Brewer's Theorem)

The CAP Theorem states that a distributed data store can only provide two out of the following three guarantees at the same time:

### 1. Consistency (C)
Every read receives the most recent write or an error. It’s as if the system acts like a single node, even if it's spread across the world.

### 2. Availability (A)
Every request receives a (non-error) response, without the guarantee that it contains the most recent write. The system stays "up" even if some nodes are failing.

### 3. Partition Tolerance (P)
The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

---

### ⚖️ The Trade-offs (Choose Your Two)

In a distributed network, **Partition Tolerance (P) is a requirement**, not an option, because networks *will* eventually fail. This leaves engineers with two choices:

#### **CP (Consistency + Partition Tolerance)**
The system is consistent but might become unavailable. If a network split occurs, the system will shut down the "out of sync" nodes to ensure no one reads stale data.
* *Example:* **MongoDB**, **HBase**, **Redis**.

#### **AP (Availability + Partition Tolerance)**
The system stays up, but the data might be out of sync for a while. Users can read and write to any available node, and the system will resolve the differences later (**Eventual Consistency**).
* *Example:* **Cassandra**, **DynamoDB**, **CouchDB**.



---

### 🧠 The "Mathematical" Reality
Mathematically, the theorem can be summarized as:
$$C + A + P \implies \text{Impossible}$$
$$\text{In the presence of a Partition (P), you must choose either C or A.}$$

### Why it matters
When designing a system like a **Banking App**, you choose **CP** (you cannot show a wrong balance). When designing a **Social Media Feed**, you choose **AP** (it’s okay if a post takes 2 seconds to appear for everyone, as long as the site doesn't crash).
