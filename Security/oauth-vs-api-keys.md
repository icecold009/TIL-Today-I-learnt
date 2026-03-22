# OAuth vs API Keys

## The Core Idea

| | API Key | OAuth |
|---|---|---|
| What it is | A static secret string | A protocol for delegated access |
| Who it represents | The **app** | The **user** (via the app) |
| Best for | Server-to-server, internal tools | Apps acting on behalf of a user |
| Revocable? | Yes (manually) | Yes (token expiry + refresh) |
| User consent needed? | No | Yes |

---

## API Keys

An API key is a simple token — a long random string — that you attach to every request.

```
GET https://api.weather.com/forecast
Headers:
  x-api-key: ab12cd34ef56gh78
```

The server sees the key, looks it up, and knows **which app** is making the call.

**Used by:** Stripe, OpenAI, Google Maps, AudD

### When to use API Keys
- Your app is calling an API on its own behalf (no user involved)
- Internal microservices talking to each other
- Quick prototypes and scripts
- The API doesn't have sensitive user data

### Risks
- If leaked, anyone can use it — treat like a password
- No built-in expiry (you must rotate manually)
- No granular permissions per user

---

## OAuth 2.0

OAuth is a **protocol**, not just a token. It lets a user grant your app limited access to their account on another service — without giving you their password.

You've seen this flow:

```
1. User clicks "Login with Google"
2. Redirected to Google's consent screen
3. User approves: "Allow this app to read your Gmail"
4. Google sends back an access token
5. Your app uses that token to call Gmail API
```

The key insight: **the user is in control**. They can revoke access anytime without changing their password.

### When to use OAuth
- Your app needs to act on behalf of a user
- Accessing user data on third-party platforms (Google, GitHub, Spotify)
- You want "Login with X" functionality
- Fine-grained scopes matter (read-only vs full access)

### Key OAuth concepts

| Term | Meaning |
|---|---|
| Access Token | Short-lived token used to make API calls |
| Refresh Token | Long-lived token to get a new access token |
| Scope | What permissions were granted (e.g. `read:email`) |
| Authorization Server | The service that issues tokens (e.g. Google) |
| Client ID / Secret | Your app's identity with the auth server |

---

## Side-by-Side Flow

**API Key flow:**
```
App → API Key in header → API Server → Response
```

**OAuth flow:**
```
User → Consent Screen → Auth Server → Access Token
App → Access Token in header → API Server → Response
```
