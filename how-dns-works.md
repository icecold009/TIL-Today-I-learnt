# How DNS Works: The Internet's Address Book

DNS (Domain Name System) is the protocol that translates human-readable domain names (like `github.com`) into machine-readable IP addresses (like `140.82.112.4`).

### 🗺️ The Recursive Lookup Journey

When you request a website, your computer doesn't know where it is. It follows a 4-step hierarchy to find the answer:

1. **DNS Recursive Resolver:** Your ISP's server receives your request and goes searching on your behalf.
2. **Root Nameservers:** The first stop. It doesn't know the IP, but it knows where the **.com** (TLD) servers are.
3. **TLD Nameservers:** The Top-Level Domain server (for .com, .org, .net). It points the resolver toward the specific **Authoritative Nameserver** for that domain.
4. **Authoritative Nameserver:** The final destination. It holds the actual IP address record. It gives the IP back to the resolver, which gives it to your browser.



---

### ⚡ DNS Caching: Why It's Usually Faster
To avoid doing this "scavenger hunt" every single time, DNS records are cached at multiple levels:
* **Browser Cache:** Your browser remembers sites you've visited recently.
* **OS Cache:** Your computer's operating system keeps a local record.
* **Resolver Cache:** Your ISP keeps popular records saved for all its users.

### 📝 Common DNS Record Types
When you manage a website, you'll encounter these common records:
* **A Record:** Maps a domain to an **IPv4** address.
* **AAAA Record:** Maps a domain to an **IPv6** address.
* **CNAME:** Maps a domain to another domain (an "alias").
* **MX Record:** Directs email to a mail server.

---

### 🧠 The "Propagation" Delay
When you change your DNS settings, it can take up to 48 hours for the change to be visible globally. This is because of **TTL (Time To Live)**—a setting that tells caches how long to hold onto an old record before asking the Authoritative server for a fresh one.
