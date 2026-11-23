
import json
import csv
import os
from datetime import datetime

DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Health", "Entertainment", "Shopping", "Other"]




### Step 2 — 




def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️ Could not read data file, starting fresh.")
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=2)
    except IOError:
        print("❌ Failed to save data.")

def get_next_id(expenses):
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1



### Step 3 — Add an Expense

# **Logic:** Validate input step by step. Amount must be a positive number →
#  `try/except ValueError`. Category is chosen by number from a fixed list → invalid choice falls back to `"Other"`.


def add_expense():
    print("\n── Add Expense ──")
    description = input("Description: ").strip()
    if not description:
        print("❌ Description cannot be empty.")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("❌ Enter a valid positive number.")
        return

    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    try:
        choice = int(input("Choose category number: "))
        category = CATEGORIES[choice - 1]
    except (ValueError, IndexError):
        category = "Other"

    expenses = load_expenses()
    expense = {
        "id": get_next_id(expenses),
        "date": datetime.now().strftime("%Y-%m-%d"), 
        "description": description,
        "amount": amount,
        "category": category,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added: {description} — {amount:.2f} [{category}]")


### Step 4 — View All Expenses

# **Logic:** Loop through the list, print aligned columns with 
# f-string width formatting. Accepts an optional list so Search can reuse it.


def view_expenses(expenses=None):
    if expenses is None:
        expenses = load_expenses()

    if not expenses:
        print("\n📭 No expenses found.")
        return

    print(f"\n{'ID':<5}{'Date':<12}{'Description':<25}{'Category':<15}{'Amount':>10}")
    print("─" * 67)
    for e in expenses:
        print(f"{e['id']:<5}{e['date']:<12}{e['description']:<25}"
              f"{e['category']:<15}{e['amount']:>10.2f}")
    print("─" * 67)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total:':<57}{total:>10.2f}")

### Step 5 — Delete an Expense

# **Logic:** Show the table so the user can see IDs, then rebuild the 
# list excluding the chosen ID using a list comprehension filter.

# ```python
def delete_expense():
    print("\n── Delete Expense ──")
    view_expenses()
    try:
        target_id = int(input("\nEnter ID to delete (0 to cancel): "))
    except ValueError:
        print("❌ Invalid ID.")
        return
    if target_id == 0:
        return

    expenses = load_expenses()
    new_expenses = [e for e in expenses if e["id"] != target_id]

    if len(new_expenses) == len(expenses):
        print(f"❌ ID {target_id} not found.")
        return

    save_expenses(new_expenses)
    print(f"✅ Deleted expense #{target_id}.")


### Step 6 — Search Expenses

# **Logic:** Three search modes, each a filter over the list. Reuses 
# `view_expenses()` to display results — no duplicated printing code.

# ```python
def search_expenses():
    print("\n── Search ──")
    print("1. By keyword\n2. By category\n3. By date range")
    choice = input("Choose: ").strip()
    expenses = load_expenses()
    results = []

    if choice == "1":
        keyword = input("Keyword: ").strip().lower()
        results = [e for e in expenses if keyword in e["description"].lower()]
    elif choice == "2":
        print("Categories:", ", ".join(CATEGORIES))
        cat = input("Category: ").strip().lower()
        results = [e for e in expenses if e["category"].lower() == cat]
    elif choice == "3":
        start = input("Start date (YYYY-MM-DD): ").strip()
        end = input("End date (YYYY-MM-DD): ").strip()
        results = [e for e in expenses if start <= e["date"] <= end]
    else:
        print("❌ Invalid choice.")
        return

    print(f"\n🔍 {len(results)} result(s):")
    view_expenses(results)

### Step 7 — Total & Monthly Spending

# **Logic:** Total = simple sum. Monthly = group into a dict keyed by 
# the first 7 characters of the date (`"YYYY-MM"`), then sum each group.


def total_spending():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total spending: {total:.2f}")

def monthly_spending():
    expenses = load_expenses()
    if not expenses:
        print("📭 No data yet.")
        return

    monthly = {}
    for e in expenses:
        key = e["date"][:7]              # "2026-08"
        monthly.setdefault(key, []).append(e)

    print("\n── Monthly Spending ──")
    for month in sorted(monthly):
        group = monthly[month]
        total = sum(e["amount"] for e in group)
        print(f"{month}: {total:.2f}  ({len(group)} expenses)")

### Step 8 — Export to CSV

# **Logic:** `csv.DictWriter` maps dict keys straight to 
# columns — no manual string building needed.


def export_csv():
    expenses = load_expenses()
    if not expenses:
        print("📭 Nothing to export.")
        return

    filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "date", "description", "amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"✅ Exported to {filename}")

### Step 9 — Main Menu Loop

# **Logic:** Store menu options as `{key: (label, function)}`. The loop reads 
# a choice, looks it up, and calls the matching function — no long `if/elif` chain.


def main():
    menu = {
        "1": ("Add Expense", add_expense),
        "2": ("View All", view_expenses),
        "3": ("Delete Expense", delete_expense),
        "4": ("Search Expenses", search_expenses),
        "5": ("Total Spending", total_spending),
        "6": ("Monthly Spending", monthly_spending),
        "7": ("Export to CSV", export_csv),
        "0": ("Quit", None),
    }

    print("💰 Expense Tracker CLI")
    while True:
        print("\n── Menu ──")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\nChoose: ").strip()

        if choice == "0":
            print("👋 Bye!")
            break
        if choice in menu:
            menu[choice][1]()
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()



