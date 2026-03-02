# Database Sharding: Horizontal Partitioning

Sharding is the process of breaking up a large database into smaller, more manageable chunks called **shards**. Each shard is stored on a separate database server instance.

### 🧱 Vertical vs. Horizontal
* **Vertical (Scaling Up):** Adding more CPU/RAM to your existing server. (Expensive and has a "ceiling").
* **Horizontal (Scaling Out):** Adding more servers. Sharding is the primary way we do this for databases.

---

### 🔑 The Shard Key
The most critical part of sharding is choosing a **Shard Key**. This is the column (like `user_id` or `zip_code`) used to determine which shard a specific row lives on.



### 🛰️ Sharding Architectures

#### 1. Range-Based Sharding
Data is split based on ranges of a value.
* *Example:* Users with names A-M go to Shard 1, N-Z go to Shard 2.
* **Risk:** "Hot Spots." If everyone's name starts with 'S', Shard 2 will crash while Shard 1 stays idle.

#### 2. Hash-Based Sharding
A hash function is applied to the Shard Key to distribute data evenly.
* *Formula:* $Shard = Hash(UserID) \mod n$ (where $n$ is the number of shards).
* **Pro:** Excellent data distribution.
* **Con:** Adding a new shard requires moving almost all your data ("Re-sharding").

```mermaid
graph TD
    Data["New User (ID: 42)"] --> Hash{"Hash(42) % 3"}
    Hash -- Result: 0 --> S0[(Shard 0)]
    Hash -- Result: 1 --> S1[(Shard 1)]
    Hash -- Result: 2 --> S2[(Shard 2)]
