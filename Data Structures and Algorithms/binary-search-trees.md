# Binary Search Trees (BST)

A **Binary Search Tree** is a rooted binary tree data structure where the nodes are arranged in a specific order to allow for fast lookups, additions, and removals.

### 📐 The Fundamental Property
For every node $N$:
* All nodes in the **left** subtree have values **less than** $N$'s value.
* All nodes in the **right** subtree have values **greater than** $N$'s value.



---

### ⏱ Efficiency: Why Trees Win
In a standard unsorted List, finding a specific item takes $O(n)$ time because you might have to check every single element. In a **Balanced BST**, we use a "divide and conquer" approach:

* **Search:** $O(\log n)$
* **Insertion:** $O(\log n)$
* **Deletion:** $O(\log n)$

Every time you move down a level in the tree, you eliminate **half** of the remaining possibilities.

---

### ⚠️ The "Unbalanced" Trap
The $O(\log n)$ speed only holds if the tree is "balanced." If you insert numbers in perfect order (e.g., 1, 2, 3, 4, 5), the tree becomes a straight line, effectively turning back into a Linked List with $O(n)$ performance.



### 🛠 Real-World Use Cases
1. **Database Indexing:** Most SQL databases use B-Trees (a variation of BSTs) to find rows without scanning the whole table.
2. **Pathfinding:** Many AI algorithms use tree structures to map out possible moves.
3. **Symbol Tables:** Compilers use trees to store variable names and look them up quickly.

---

### 🧬 Tree Traversal
To get all the data out of a BST in sorted order, you use an **In-order Traversal**:
1. Visit the Left Subtree.
2. Visit the Root.
3. Visit the Right Subtree.
