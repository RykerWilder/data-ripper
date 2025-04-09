# Password Checker

A Python script that checks if a password has been compromised in known data breaches, using the **Have I Been Pwned** API.

---

### Features
- **Anonymous** password verification (using SHA-1 hash).
- Uses the **k-Anonymity** API to preserve privacy.
- Instant results with breach counts.

---

### Prerequisites
- Python 3.x
- `requests` library (for HTTP calls)

```bash
pip install requests
```