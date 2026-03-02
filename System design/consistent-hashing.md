# Consistent Hashing: The Scaling Secret

In traditional hashing ($Hash(key) \mod n$), if the number of servers ($n$) changes, almost every key maps to a new location. This causes a "Data Hurricane" where everything has to be moved at once. 

**Consistent Hashing** solves this by mapping both **Servers** and **Data** onto a virtual circle called a **Hash Ring**.

---

### 🎡 The Hash Ring
Imagine a circle with a range of values, say from $0$ to $2^{32}-1$.

1.  **Map Servers:** Each server is hashed and placed at a position on the ring.
2.  **Map Data:** Each data key is hashed and placed on the same ring.
3.  **The Rule:** To find which server holds a piece of data, travel **clockwise** from the data's position until you hit the first server.



### 🏗️ Why it’s "Consistent"
* **When a server is added:** It only "steals" a small portion of data from its immediate neighbor. All other data stays exactly where it is.
* **When a server crashes:** Its data is simply reassigned to the next server clockwise. Only the data from the failed server needs to move.

---

### 🧬 The Problem of "Skew" (Virtual Nodes)
If you only have two servers, one might end up with 90% of the ring by chance. To fix this, we use **Virtual Nodes**. We hash each server multiple times (e.g., `Server_A_1`, `Server_A_2`) so it appears in many places on the ring, ensuring an even distribution of data.

