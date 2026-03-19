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

```mermaid
graph TD
    Start([Start]) --> Init[Initialize K Centroids<br/>Randomly pick K points]
    Init --> Assign[Assignment Step<br/>Assign each data point to the<br/>nearest centroid using Euclidean Distance]
    Assign --> Update[Update Step<br/>Calculate the mean of all points<br/>in each cluster]
    Update --> Move[Move Centroids<br/>Relocate centroids to the new mean]
    Move --> Check{Converged?}
    Check -- No --> Assign
    Check -- Yes --> End([End<br/>Clusters Finalized])

    style Init fill:#f9f,stroke:#333,stroke-width:2px
    style Check fill:#fff4dd,stroke:#d4a017,stroke-width:2px
    style End fill:#ccffcc,stroke:#333,stroke-width:2px
