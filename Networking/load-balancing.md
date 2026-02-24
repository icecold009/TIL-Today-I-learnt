# Load Balancing: Distributing the Weight

A **Load Balancer** acts as a "traffic cop" sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests. 

### 🎯 Key Objectives
1. **Scalability:** Add more servers to handle increased traffic.
2. **High Availability:** If one server crashes, the load balancer redirects traffic to the healthy ones.
3. **Efficiency:** Ensures no single server is overworked while others sit idle.



---

### 🚦 Common Algorithms

| Algorithm | Logic | Best Use Case |
| :--- | :--- | :--- |
| **Round Robin** | Requests are sent sequentially (A -> B -> C). | Servers have equal hardware specs. |
| **Least Connections** | Sends traffic to the server with the fewest active sessions. | High-traffic apps where sessions vary in length. |
| **IP Hash** | Uses the client's IP to determine which server they get. | "Sticky sessions" where a user must stay on one server. |
| **Least Response Time** | Sends traffic to the server responding the fastest. | Real-time applications. |

---

### 🥞 Layer 4 vs. Layer 7 Balancing

Tying back to the **OSI Model**, load balancers usually operate at two different levels:

1. **L4 (Transport Layer):** Makes routing decisions based on network data (IP and Port). It’s extremely fast because it doesn't "look" inside the packet.
2. **L7 (Application Layer):** Makes decisions based on the actual content of the request (URLs, Cookies, Headers). This allows for "smarter" routing, like sending `/video` requests to a video-optimized server.

### 🩺 Health Checks
Load balancers don't just blindly send traffic. They perform **Health Checks**—regularly "pinging" servers to see if they are still alive. If a server fails to respond, it is automatically pulled from the rotation until it recovers.