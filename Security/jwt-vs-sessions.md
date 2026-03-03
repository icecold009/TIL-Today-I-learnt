# JWT vs. Sessions: Authentication at Scale

Authentication is the process of verifying who a user is. In a distributed system, the challenge is making sure every server recognizes the user without constantly hitting the database.

---

### 1. Session-Based Authentication (Stateful) 🍪
The server is "responsible" for remembering you.

* **How it works:** 1. User logs in.
  2. Server creates a **Session ID** and stores it in memory or a database (like Redis).
  3. Server sends the ID back to the browser in a **Cookie**.
  4. On every request, the browser sends the Cookie; the server looks up the ID to see who you are.
* **The Scaling Problem:** If you have 5 servers, Server A might have your session, but Server B won't. You need a "Shared Session Store" (like Redis) so all servers can see the same data.



---

### 2. JWT Authentication (Stateless) 🎫
The user is "responsible" for carrying their own proof.

* **How it works:** 1. User logs in.
  2. Server creates a **JSON Web Token (JWT)**, signs it with a private key, and sends it to the user.
  3. The user stores it (Local Storage or Cookie).
  4. On every request, the user sends the JWT. The server **verifies the signature** using its key.
* **The Scaling Benefit:** The server doesn't need to look anything up! It just checks the signature. Any server with the secret key can "trust" the token instantly.

---

### 📊 Comparison Table

| Feature | Sessions | JWT |
| :--- | :--- | :--- |
| **State** | Stateful (Stored on server) | Stateless (Stored on client) |
| **Revocation** | Easy (Just delete the session) | Hard (Token is valid until it expires) |
| **Size** | Small (just an ID) | Large (contains user data) |
| **Scaling** | Requires Shared Store | Scales horizontally out-of-the-box |

```mermaid
sequenceDiagram
    participant U as User
    participant S as Server
    U->>S: Login(User, Pass)
    S->>S: Verify & Sign JWT
    S-->>U: Return JWT
    Note over U,S: Subsequent Request
    U->>S: Request + JWT
    S->>S: Verify Signature
    S-->>U: Success (No DB lookup!)