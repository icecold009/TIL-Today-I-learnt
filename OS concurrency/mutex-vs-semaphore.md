# Mutex vs. Semaphore: Thread Synchronization

When multiple threads try to access the same resource (like a variable or a file) at the same time, things break. We use **Mutexes** and **Semaphores** to manage this "traffic."

### 🔒 1. Mutex (Mutual Exclusion)
Think of a Mutex as a **lock on a bathroom door**. Only one person can have the key at a time.

* **Key Rule:** The thread that locks the Mutex **must** be the one to unlock it.
* **Ownership:** It has a concept of "ownership."
* **Best Use:** Protecting a single shared variable or a small piece of code (Critical Section).

### 🚦 2. Semaphore
Think of a Semaphore as a **locker room with 5 keys**. 

* **How it works:** It’s essentially a counter. If the counter is 5, five threads can enter. If it hits 0, the next thread must wait until someone leaves and "increments" the counter.
* **Ownership:** No ownership. Any thread can signal (increment) a semaphore.
* **Best Use:** Managing a pool of resources (like a database connection pool with 10 slots).



---

### 📊 Comparison Table

| Feature | Mutex | Semaphore |
| :--- | :--- | :--- |
| **Type** | Locking Mechanism | Signaling Mechanism |
| **Mechanism** | Binary (0 or 1) | Counter (0 to N) |
| **Ownership** | Yes | No |
| **Usage** | Exclusive access to one resource | Access to a pool of resources |


```mermaid
sequenceDiagram
    participant T1 as Thread A
    participant T2 as Thread B
    participant M as Mutex Lock

    T1->>M: Lock Request (Acquire)
    M-->>T1: Success
    Note right of T1: Working on shared data...
    T2->>M: Lock Request (Acquire)
    Note over T2,M: Thread B BLOCKED (Waiting)
    T1->>M: Unlock (Release)
    M-->>T2: Success (Now Thread B can enter)
