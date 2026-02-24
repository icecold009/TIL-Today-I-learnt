# Merge Sort: The Power of Divide and Conquer

Merge Sort is a stable, comparison-based sorting algorithm. It is significantly faster than simple sorts for large datasets because it uses a recursive strategy to break a problem down into smaller, manageable sub-problems.

### 🏗 How It Works

Merge Sort follows three main steps:
1. **Divide:** Split the unsorted list into $n$ sub-lists, each containing one element (a list of one element is considered sorted).
2. **Conquer:** Repeatedly merge sub-lists to produce new sorted sub-lists.
3. **Combine:** Continue until there is only one sorted list remaining.



---

### ⏱ Complexity Analysis

Merge Sort is famous for its consistent performance regardless of how messy the input data is.

* **Time Complexity:** $O(n \log n)$ for Best, Average, and Worst cases.
  * The $\log n$ comes from the number of times we split the list in half.
  * The $n$ comes from the work required to merge the elements back together at each level.
* **Space Complexity:** $O(n)$
  * Unlike "In-place" sorts (like Quick Sort), Merge Sort requires extra memory to store the temporary sub-lists during the merging process.

---

### 💻 Why it's used
* **Stability:** Merge Sort is "stable," meaning if two elements have the same value, their relative order is preserved. This is vital when sorting complex objects (e.g., sorting a list of students by grade, then by name).
* **External Sorting:** Because it processes data in chunks, it is the go-to algorithm for sorting datasets that are too large to fit into a computer's RAM (sorting data from a hard drive).

### 🧬 The "Merge" Logic
The magic happens in the merge step. You take two sorted arrays and compare the first elements of each, picking the smaller one and moving it into the final array. This continues until all elements are placed.
