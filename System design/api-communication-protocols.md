# API Paradigms: REST vs. GraphQL vs. gRPC vs. WebSockets

In modern systems, choosing how services talk is just as important as what they say. Each protocol has a specific "superpower."

### 🏎️ The Big Four at a Glance

| Protocol | Style | Best For... | Data Format |
| :--- | :--- | :--- | :--- |
| **REST** | Resource-based | Public APIs, Web Apps | JSON/XML |
| **GraphQL** | Query-based | Complex data, Mobile apps | JSON |
| **gRPC** | Action-based (RPC) | Internal Microservices | Protobuf (Binary) |
| **WebSockets** | Bi-directional | Real-time (Chat, Stocks) | Binary/Text |

```mermaid
graph TD
    Start[New Project] --> Public{Public API?}
    Public -- Yes --> REST[REST]
    Public -- No --> Data{Complex/Mobile?}
    Data -- Yes --> GQL[GraphQL]
    Data -- No --> Performance{High Performance?}
    Performance -- Yes --> gRPC[gRPC]
    Performance -- No --> RealTime{Real-Time?}
    RealTime -- Yes --> WS[WebSockets]
    RealTime -- No --> REST
