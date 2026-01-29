# Memory Allocation: The Stack vs. The Heap

Every program uses two primary parts of memory to store data: the **Stack** and the **Heap**. Understanding the difference is crucial for preventing memory leaks and optimizing performance.

---

### 1. The Stack (Static Allocation)
The stack is a "Last-In, First-Out" (LIFO) structure. It is managed automatically by the CPU.

* **What goes there:** Local variables, function parameters, and return addresses.
* **Speed:** Extremely fast. Accessing stack memory is a simple pointer move.
* **Structure:** Linear and organized.
* **Size:** Fixed and limited. If a program uses too much stack memory (e.g., infinite recursion), you get a **Stack Overflow**.

### 2. The Heap (Dynamic Allocation)
The heap is a large pool of memory used for dynamic allocation. Unlike the stack, it has no fixed pattern.

* **What goes there:** Objects, large arrays, and data that needs to stay alive beyond a single function call.
* **Speed:** Slower. The OS has to find a free block of memory and return a pointer.
* **Management:** In languages like C/C++, you must manually `free()` this. In languages like Python/Java, the **Garbage Collector** handles it.
* **Structure:** Fragmented. Data can be scattered anywhere.

---

### 📊 Comparison Table

| Feature | Stack | Heap |
| :--- | :--- | :--- |
| **Size** | Small / Limited | Large / Flexible |
| **Access** | Very Fast | Slower |
| **Management** | Automatic (by OS) | Manual or Garbage Collected |
| **Lifetime** | Temporary (Function scope) | Long-lived (Global or scoped) |

---

### 🧠 The "Why"
If you create a huge array of 1,000,000 integers inside a function:
1. On the **Stack**, you might crash the program immediately.
2. On the **Heap**, you can store it safely, but you must remember to clean it up (or let the garbage collector do its job) to avoid a **Memory Leak**.
