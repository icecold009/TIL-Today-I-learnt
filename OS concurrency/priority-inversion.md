# Priority Inversion

Priority inversion is a scheduling anomaly where a high-priority task is forced to wait on a low-priority task, because the low-priority task holds a resource the high one needs.

---

### How It Happens

Imagine three tasks: High (H), Medium (M), and Low (L).

1. **L** acquires a shared lock
2. **H** starts and needs the same lock — so it waits
3. **M** becomes runnable and preempts L (since M > L in priority)
4. Now **H** is stuck waiting on L, which can't even run because M is in the way

H is effectively blocked by M — a task it should outrank. This is the inversion.

---

### Why It's Dangerous

In real-time systems, tasks have strict deadlines. If a high-priority task misses its window because a lower one held it up, the consequences can be severe.

The most famous real-world case was the **Mars Pathfinder mission (1997)** — the spacecraft's software kept resetting mid-mission due to an undetected priority inversion between its tasks.

---

### Solutions

**Priority Inheritance**
When L holds a lock that H is waiting on, L temporarily inherits H's priority. This lets L finish and release the lock faster, unblocking H.

**Priority Ceiling Protocol**
Every lock is assigned a ceiling — the highest priority of any task that might acquire it. A task can only acquire the lock if its priority is higher than all currently held ceilings. Prevents inversion entirely rather than reacting to it.

**Lock-free Design**
Avoid shared locks altogether using atomic operations or lock-free data structures. No lock means no inversion.

---

### Quick Example

```
Without fix:         With Priority Inheritance:

H  ──waiting──►      H  ──waiting──►
M  ────runs────      M  ──blocked── (L now runs at H's priority)
L  ──blocked───      L  ──runs────► releases lock → H unblocked
```
