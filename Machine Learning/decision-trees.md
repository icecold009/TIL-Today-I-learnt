# Decision Trees: Recursive Partitioning

A Decision Tree is a supervised learning algorithm used for both classification and regression. It works by splitting the data into subsets based on the feature that provides the most "information" at each node.

### 🧮 The Math: Entropy and Information Gain

To decide where to split, we measure **Entropy** (impurity). A dataset with only one class has an entropy of 0.

$$H(S) = - \sum_{i=1}^{c} p_i \log_2 p_i$$

**Information Gain (IG)** is the reduction in entropy after a dataset is split on an attribute $A$:

$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

---

### 💻 Implementation: Calculating Entropy in Python

Instead of using a library, understanding the raw logic helps in optimizing tree depth.

```python
import numpy as np

def calculate_entropy(y):
    # Find the probability of each class
    labels, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    
    # Apply the formula: -sum(p * log2(p))
    entropy = -np.sum([p * np.log2(p) for p in probabilities if p > 0])
    return entropy

# Example: A dataset with 4 'Yes' and 2 'No'
data = ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
print(f"Current Entropy: {calculate_entropy(data):.4f}")
