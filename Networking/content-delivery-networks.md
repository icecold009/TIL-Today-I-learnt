# Content Delivery Networks (CDN)

A **CDN** is a geographically distributed group of servers (called "Edge Servers") that work together to provide fast delivery of internet content.

### 🌎 The Latency Problem
Information can only travel as fast as the speed of light. If your server is in New York and your user is in Tokyo, the "round trip" for data takes a noticeable amount of time (latency). 

### ⚡ How CDNs Fix This: Caching at the Edge
Instead of every user hitting your **Origin Server** (the main server), the CDN stores a copy of your static files (images, JS, CSS, HTML) on **Edge Servers** located all over the world.

1. **User requests a file.**
2. **DNS routes them to the closest Edge Server.**
3. **If the Edge Server has the file (a "Cache Hit"), it serves it instantly.**
4. **If not (a "Cache Miss"), it fetches it from the Origin, saves a copy, and then serves it.**

```mermaid
graph LR
    User((User in Tokyo)) -- 1. Request --> Edge[Tokyo Edge Server]
    Edge -- 2. Cache Hit? --> User
    Edge -- 3. Cache Miss? --> Origin[NY Origin Server]
    Origin -- 4. Fetch & Cache --> Edge
