# Tries (Prefix Trees)

A **Trie** (derived from "retrieval") is a type of search tree used to store an associative array where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated.

### 🔑 Key Characteristics
* **Root Node:** Always represents an empty string.
* **Edges:** Each edge represents a character of the alphabet.
* **Nodes:** A node marks the end of a valid word (often using a boolean flag `isEndOfWord`).
* **Time Complexity:** * **Insert:** $O(L)$, where $L$ is the length of the word.
    * **Search:** $O(L)$.
    * **Space:** $O(AL \cdot N)$, where $A$ is the alphabet size and $N$ is the number of words.

---

### 📊 Trie Structure Visualization
This diagram shows a Trie containing the words: **"CAT"**, **"CAP"**, and **"CAR"**.

```mermaid
graph TD
    Root(( )) --> C[C]
    C --> A[A]
    A --> T[T*]
    A --> P[P*]
    A --> R[R*]

    style T* stroke:#333
    style P* stroke:#333
    style R* stroke:#333
