# The OSI Model (Open Systems Interconnection)

The OSI model is a conceptual framework used to understand how data moves from one computer to another over a network. It divides the process into **7 distinct layers**.

### 🥞 The 7 Layers

| # | Layer | Purpose | Data Unit | Examples |
| :--- | :--- | :--- | :--- | :--- |
| **7** | **Application** | Human-computer interaction. | Data | HTTP, DNS, SMTP |
| **6** | **Presentation** | Data encryption, compression, and formatting. | Data | SSL/TLS, JPEG, ASCII |
| **5** | **Session** | Managing connections between applications. | Data | NetBIOS, RPC |
| **4** | **Transport** | End-to-end communication and error recovery. | Segments | TCP, UDP |
| **3** | **Network** | Routing and path determination. | Packets | IP, ICMP, Routers |
| **2** | **Data Link** | Physical addressing and MAC addresses. | Frames | Ethernet, Switches |
| **1** | **Physical** | Binary transmission over cables or air. | Bits | Fiber optics, WiFi |



---

### 🛡 Encapsulation: The "Envelope" Metaphor
As data travels down the stack (from Layer 7 to Layer 1), each layer wraps the data from the previous layer in its own "header," much like putting a letter inside seven different envelopes.

1. The **Transport Layer** adds a TCP header (Port numbers).
2. The **Network Layer** adds an IP header (IP addresses).
3. The **Data Link Layer** adds a Frame header (MAC addresses).

When the data reaches the destination, the process is reversed (**Decapsulation**).

---

### 🧠 Why This Matters
* **Troubleshooting:** If you can "Ping" a server but your website won't load, the **Network Layer (3)** is working, but the **Application Layer (7)** is likely broken.
* **Standardization:** It allows a router made by Cisco to talk to a laptop made by Apple. As long as they both follow the OSI standards for each layer, they are compatible.

### 💡 Mnemonics to Remember the Order
(From Layer 7 down to 1):
> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
