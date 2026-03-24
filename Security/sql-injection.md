# SQL Injection

SQL Injection is an attack where malicious SQL code is slipped into an input field and executed by the database — potentially exposing, modifying, or deleting data.

---

### How It Works

A vulnerable login query looks like this:

```sql
SELECT * FROM users WHERE username = 'admin' AND password = '1234';
```

If a user inputs `' OR '1'='1` as the password, the query becomes:

```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1';
```

Since `'1'='1'` is always true, the attacker bypasses authentication entirely.

---

### Types

**Classic**
Directly returns data via error messages or query results.

**Blind**
No visible output — the attacker infers data from app behaviour.

**Time-based**
Uses delays like `SLEEP(5)` to confirm true/false conditions.

**Out-of-band**
Exfiltrates data via DNS or HTTP requests.

---

### How to Prevent It

**1. Use parameterised queries**

```python
# ❌ Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"

# ✅ Safe
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

**2. Use an ORM**
SQLAlchemy and Django ORM handle escaping automatically.

**3. Validate and sanitise inputs**
Reject unexpected characters at the application layer before they reach the DB.

**4. Apply least privilege**
DB accounts should only have the permissions they actually need.

**5. Never expose raw DB errors**
Error messages reveal table and column names — hide them from users.

---

> **Key Takeaway** — Never trust user input. Parameterised queries are the single most effective defence against SQL injection.

---


### References

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Labs](https://portswigger.net/web-security/sql-injection)
