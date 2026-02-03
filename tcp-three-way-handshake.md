# The TCP Three-Way Handshake

Transmission Control Protocol (TCP) is "connection-oriented." Before a single byte of application data (like a website's HTML) is sent, the client and server must perform a three-step synchronization process.

### 🤝 The Process (SYN, SYN-ACK, ACK)

1. **SYN (Synchronize):** The client sends a packet with a random Sequence Number ($x$) to the server. It’s essentially saying, "I want to talk, and let's start counting our data from $x$."
2. **SYN-ACK (Synchronize-Acknowledge):** The server responds with its own random Sequence Number ($y$) and an Acknowledgement Number ($x + 1$). It says, "I hear you! I’m ready too. Start at $y$, and I’m expecting your next packet to be $x + 1$."
3. **ACK (Acknowledge):** The client sends back an Acknowledgement Number ($y + 1$). It says, "Got it! Let's go."



---

### 🔍 Why This Matters

* **Reliability:** Unlike UDP (which just "fires and forgets"), TCP ensures both parties are awake and have agreed on how to track the data packets.
* **Sequence Numbers:** These prevent data from arriving out of order. If packet 500 arrives before packet 499, TCP uses these numbers to reassemble them correctly.

### ⚠️ The "SYN Flood" Attack
Because the server must commit resources (memory) to keep track of a connection after the first **SYN**, attackers can overwhelm a server by sending thousands of SYN packets and never sending the final **ACK**. This is a classic Denial of Service (DoS) technique.

---

### 🧬 Mathematical View
If $Seq$ is the sequence number and $Ack$ is the acknowledgment:
1. Client $\to$ Server: $Seq = x$
2. Server $\to$ Client: $Seq = y, Ack = x + 1$
3. Client $\to$ Server: $Seq = x + 1, Ack = y + 1$
