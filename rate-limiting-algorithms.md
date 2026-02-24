# Rate Limiting: Protecting the Gateway

Rate limiting is a strategy used to limit the number of requests a user or client can make to a service within a specific timeframe. It prevents API abuse, DoS attacks, and unintended traffic spikes.

### 🕰️ Common Algorithms

1. **Token Bucket:** Tokens are added to a "bucket" at a fixed rate. Each request costs one token. If the bucket is empty, the request is dropped. This allows for small "bursts" of traffic.
2. **Leaky Bucket:** Requests enter a bucket and are processed at a constant, steady rate. If the bucket overflows, new requests are discarded. This ensures a smooth, consistent flow.
3. **Fixed Window Counter:** A simple counter for a specific timeframe (e.g., 100 requests per minute). 
   * *The Problem:* A user could send 100 requests at 10:00:59 and 100 more at 10:01:01, effectively doubling the allowed rate in two seconds.



### 🛠️ Implementation
Most modern systems implement rate limiting using **Redis** to store counters because it is extremely fast and can handle the high-volume incrementing required to track millions of users.
