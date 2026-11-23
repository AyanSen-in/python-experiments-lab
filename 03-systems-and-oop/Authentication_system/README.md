# Simple Login/Signup System (Python)

A basic authentication system built from scratch in Python — password validation, username validation, email validation, and secure password hashing with `bcrypt`.

This is a learning project. It is **not** production-ready, and that's the point — I'm sharing it in-progress to get feedback instead of waiting until it's "finished."

## What it does

- **Sign up:** validates username, email, and password, checks for duplicates, hashes the password, and creates the account
- **Login:** finds the user and verifies the password against the stored hash
- **Password rules:** minimum 10 characters, at least one uppercase letter, one lowercase letter, one number, and one special character
- **Username rules:** 3–25 characters, letters/numbers/underscores only
- **Email validation:** basic regex pattern check

## What it doesn't do (yet)

- **No persistent storage.** User data is kept in a Python dictionary in memory, so everything is lost when the script stops. This needs to become a real database (SQLite to start).
- No frontend — this is CLI-only for now.
- No session handling or login tokens after a successful login.
- Email validation is a simple regex, not a proper format/deliverability check.

## How it works

```
SIGN UP
  → Enter username / email / password
  → Validate input
  → If invalid: show error
  → If valid: check for duplicates
  → Hash password with bcrypt
  → Save user
  → Account created

LOGIN
  → Enter username / password
  → Find user
  → If not found: reject
  → If found: verify password hash
  → Correct: login successful
  → Wrong: reject
```

## Running it

Requires Python 3 and `bcrypt`:

```bash
pip install bcrypt
python auth_system.py
```

Then follow the CLI prompts to sign up or log in.

## Why I'm posting this unfinished

Most projects I share are the finished version. This one I'm posting mid-build, specifically to get code review from people who've done this properly before — especially around persistent storage, password hashing config, and whether my validation logic is doing anything useful or just adding friction.

If you spot something worth fixing, open an issue or drop a comment. I'll take it.

## License

MIT