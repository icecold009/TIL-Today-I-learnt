# Optimistic vs. Pessimistic Locking

When multiple users try to update the same record simultaneously, we need a strategy to ensure data integrity. These two patterns solve the problem in opposite ways.

---

### 1. Pessimistic Locking 🔒
**"Assume the worst."**
Before you even start editing a record, you lock it so no one else can even look at it.

* **How it works:** The application places a "Write Lock" on the database row. Anyone else trying to access it must wait until the first user is finished.
* **Best for:** High-contention environments where conflicts are frequent and the cost of an error is huge (e.g., withdrawing money from a bank account).
* **Cons:** Can lead to **Deadlocks** and severely limits performance because everyone is stuck in a queue.



---

### 2. Optimistic Locking 🔓
**"Hope for the best."**
You don't lock anything. You let everyone read and edit freely, but you check for a conflict right at the moment they try to save.

* **How it works:** Each record has a `version` number. 
  1. User A reads the row (Version 1).
  2. User B reads the same row (Version 1).
  3. User A saves; the DB checks if the version is still 1. It is! Save successful, version becomes 2.
  4. User B tries to save; the DB checks the version. It's now 2, but User B expected 1. **Access Denied.**
* **Best for:** Low-contention environments where conflicts are rare (e.g., editing a wiki page or a social media profile).
* **Cons:** The user has to "try again" if they lose the race.



---

### 📊 Strategy Comparison

| Feature | Pessimistic | Optimistic |
| :--- | :--- | :--- |
| **Locking Mechanism** | Physical Lock (DB Level) | Versioning (App Logic) |
| **Performance** | Lower (High Latency) | Higher (Scalable) |
| **User Experience** | "Waiting for resource..." | "Someone else edited this, please refresh." |
| **Data Integrity** | Maximum | High (but requires retry logic) |

---

### 🧠 Real-World Choice
If you are building a **ticket booking system** for a massive concert, you use **Pessimistic Locking** the moment a user puts a seat in their cart. You can't risk two people thinking they bought seat 42A. 

If you are building a **To-Do List app**, you use **Optimistic Locking**. It's unlikely two people are editing the same task at the exact same millisecond, and you want the app to feel fast.
