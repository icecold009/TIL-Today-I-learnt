# Logistic Regression: Binary Classification

Logistic Regression is used to model the probability of a discrete outcome based on input variables. Instead of fitting a straight line, it uses the **Sigmoid Function** to map any real-valued number into a value between 0 and 1.

### 🧮 The Sigmoid Function
The output of a linear equation is passed through the logistic (sigmoid) function:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Where $z = \beta_0 + \beta_1x_1 + ... + \beta_nx_n$. 
* If $\sigma(z) \geq 0.5$, we classify the output as **1**.
* If $\sigma(z) < 0.5$, we classify the output as **0**.

### 💻 Python Implementation (Scikit-Learn)
This snippet demonstrates how to train a classifier and view the predicted probabilities.

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# 1. Sample Data (Hours Studied vs. Pass/Fail)
X = np.array([[0.5], [1.75], [2.25], [3.25], [4.5], [5.25]])
y = np.array([0, 0, 0, 1, 1, 1])

# 2. Fit the model
clf = LogisticRegression()
clf.fit(X, y)

# 3. Predict probability for 3 hours of study
prob = clf.predict_proba([[3.0]])
print(f"Probability of Passing: {prob[0][1]:.2%}")
