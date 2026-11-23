# 💰 Expense Tracker CLI

A simple, dependency-free command-line application for tracking personal expenses — built entirely with Python's standard library.

## Features

- ➕ **Add** an expense (description, amount, category, auto-dated)
- 🗑️ **Delete** an expense by ID
- 📋 **View** all expenses in a formatted table
- 🔍 **Search** expenses by keyword, category, or date range
- 🏷️ **Categorize** expenses (Food, Transport, Health, Entertainment, Shopping, Other)
- 💵 **Calculate** total spending
- 📅 **Show** spending grouped by month
- 💾 **Save** data persistently to JSON, and **export** to CSV

## Demo

```
── Menu ──
  1. Add Expense
  2. View All
  3. Delete Expense
  4. Search Expenses
  5. Total Spending
  6. Monthly Spending
  7. Export to CSV
  0. Quit

Choose: 1

── Add Expense ──
Description: Coffee
Amount: 3.50

Categories:
  1. Food
  2. Transport
  3. Health
  4. Entertainment
  5. Shopping
  6. Other
Choose category number: 1
✅ Added: Coffee — 3.50 [Food]
```

## Getting Started

### Prerequisites

- Python 3.7+
- No external packages required (uses only the standard library: `json`, `csv`, `os`, `datetime`)

### Installation

```bash
git clone https://github.com/<your-username>/expense-tracker-cli.git
cd expense-tracker-cli
```

### Usage

```bash
python expense_tracker.py
```

Follow the on-screen menu to add, view, search, or delete expenses. Data is automatically saved to `expenses.json` in the same directory after every change.

## Project Structure

```
expense-tracker-cli/
├── expense_tracker.py   # main application
├── expenses.json         # auto-generated data store (gitignored)
└── README.md
```

## How It Works

Each expense is stored as a dictionary:

```json
{
  "id": 1,
  "date": "2026-08-25",
  "description": "Coffee",
  "amount": 3.5,
  "category": "Food"
}
```

All expenses are kept as a list of these dictionaries, loaded from and saved back to `expenses.json` on every operation — so your data persists between runs.

## Exporting Data

Choose **Export to CSV** from the menu to generate a timestamped `.csv` file (e.g. `expenses_20260825_143000.csv`) that can be opened in Excel, Google Sheets, or any spreadsheet tool.

## Concepts Demonstrated

This project is a practical walkthrough of core Python fundamentals:

| Concept | Where it's used |
|---|---|
| `if / else` | Input validation, menu routing |
| Functions | One function per feature |
| Loops | Printing tables, grouping by month |
| Lists & dictionaries | Core data model |
| File handling | JSON persistence, CSV export |
| Exceptions | `try / except` around all user input and file I/O |

## Roadmap / Ideas for Extension

- [ ] Set monthly budget limits per category with alerts
- [ ] Recurring expenses
- [ ] Edit existing expenses
- [ ] Simple spending charts (e.g. with `matplotlib`)
- [ ] Multi-currency support

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](LICENSE)
