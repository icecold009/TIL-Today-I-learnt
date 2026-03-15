# The Evolution of HTTP: 1.1 to 3 (QUIC)

HTTP (Hypertext Transfer Protocol) is the language of the web. Over the last 20 years, it has undergone three major overhauls to keep up with the demands of modern, asset-heavy websites.

### 🐢 1. HTTP/1.1 (The "Sequential" Era)
The classic version we used for decades. 
* **The Problem:** **Head-of-Line (HOL) Blocking**. HTTP/1.1 can only send one request per TCP connection at a time. If the first image is slow, everything behind it waits.
* **The "Hack":** Browsers open 6–8 parallel TCP connections to a single domain to cheat the system, but this consumes massive resources.

### ⚡ 2. HTTP/2 (The "Multiplexed" Era)
Introduced in 2015, it changed the game by staying on a **single TCP connection** but splitting data into "frames."
* **Multiplexing:** You can send multiple requests and responses simultaneously on the same connection.
* **Server Push:** The server can send assets (like CSS) to the client before the client even asks for them.
* **The Problem:** If one TCP packet is lost, the *entire* connection stalls until it's recovered (TCP-level HOL blocking).

### 🚀 3. HTTP/3 (The "UDP/QUIC" Era)
The cutting edge. It throws away TCP entirely and uses **QUIC**, which runs on top of **UDP**.
* **Zero RTT:** It combines the "Handshake" and "Encryption" (TLS) into one step, making connections almost instant.
* **Independent Streams:** Since it's not bound by TCP's rigid order, losing one packet only affects *that* specific stream, not the whole site.
* **Connection Migration:** If you move from Wi-Fi to 5G, your download doesn't break because QUIC uses a "Connection ID" instead of an IP address.

---

### 📊 Comparison Table

| Feature | HTTP/1.1 | HTTP/2 | HTTP/3 |
| :--- | :--- | :--- | :--- |
| **Transport** | TCP | TCP | UDP (QUIC) |
| **Multiplexing** | No (Serial) | Yes (Binary) | Yes (Streams) |
| **Header Compression** | None | HPACK | QPACK |
| **Handshake** | 3-way TCP | 3-way TCP + TLS | 1-way (QUIC + TLS) |

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    
    Note over C,S: HTTP/1.1 + TLS (Slow)
    C->>S: TCP SYN
    S->>C: TCP SYN-ACK
    C->>S: TCP ACK + TLS ClientHello
    S->>C: TLS ServerHello
    
    Note over C,S: HTTP/3 (Fast)
    C->>S: QUIC + TLS Combined Hello
    S->>C: QUIC + TLS Welcome
