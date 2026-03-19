# K-Means Clustering: Finding Hidden Patterns

K-Means is an unsupervised learning algorithm that groups unlabeled data into $K$ distinct clusters based on feature similarity.

### 🧮 How the Algorithm Works
1. **Initialization:** Randomly pick $K$ points as the initial "centroids."
2. **Assignment:** Assign each data point to the nearest centroid using **Euclidean Distance**.
3. **Update:** Calculate the new mean of all points in a cluster and move the centroid to that center.
4. **Repeat:** Continue until the centroids stop moving (convergence).

---

### 📐 Choosing the Right 'K': The Elbow Method
To find the optimal number of clusters, we calculate the **Within-Cluster Sum of Squares (WCSS)** for different values of $K$. 
* We look for the "Elbow" in the graph—the point where adding another cluster doesn't significantly decrease the WCSS.

