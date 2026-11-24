"""
Password Manager CLI
Manage and generate credentials locally with file persistence.
"""
import random
import string
import os
from pathlib import Path

PASSWORD_FILE = Path(__file__).parent / "passwords.txt"


def load_passwords() -> dict:
    passwords = {}
    if not PASSWORD_FILE.exists():
        return passwords

    try:
        with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                parts = line.split(":", 1)
                site = parts[0].strip()
                pwd = parts[1].strip()
                passwords[site] = pwd
    except Exception as e:
        print(f"Warning: Could not read passwords file: {e}")
    return passwords


def save_password(site: str, pwd: str, passwords: dict):
    passwords[site] = pwd
    with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
        for s, p in sorted(passwords.items()):
            f.write(f"{s} : {p}\n")


def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(random.choice(chars) for _ in range(max(6, length)))


def main():
    passwords = load_passwords()

    while True:
        print("\n" + "=" * 35)
        print("       🔐 PASSWORD MANAGER")
        print("=" * 35)
        print("1. Save New Password")
        print("2. View Saved Passwords")
        print("3. Generate Strong Password")
        print("4. Search Website Password")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            site = input("Enter website or service name: ").strip()
            if not site:
                print("Error: Website name cannot be empty.")
                continue

            auto = input("Generate random password? (y/n) [default: n]: ").strip().lower()
            if auto == "y":
                pwd = generate_password()
                print(f"Generated Password: {pwd}")
            else:
                pwd = input("Enter password: ").strip()

            if not pwd:
                print("Error: Password cannot be empty.")
                continue

            save_password(site, pwd, passwords)
            print(f"✅ Saved credentials for '{site}' successfully!")

        elif choice == "2":
            if not passwords:
                print("\n[i] No saved passwords found.")
            else:
                print("\n" + "-" * 40)
                print(f"{'Website / Service':<25} | {'Password'}")
                print("-" * 40)
                for s, p in sorted(passwords.items()):
                    print(f"{s:<25} | {p}")
                print("-" * 40)

        elif choice == "3":
            try:
                length_in = input("Enter desired length [default: 12]: ").strip()
                length = int(length_in) if length_in else 12
            except ValueError:
                length = 12
            generated = generate_password(length)
            print(f"\n🔑 Generated Password ({length} chars): {generated}")

        elif choice == "4":
            query = input("Enter website to search: ").strip().lower()
            matches = {s: p for s, p in passwords.items() if query in s.lower()}
            if matches:
                print("\nSearch Results:")
                for s, p in matches.items():
                    print(f"  {s}: {p}")
            else:
                print(f"No entries found matching '{query}'.")

        elif choice == "5":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
