# 🎓 Student Result Manager

An Object-Oriented student grading, performance tracking, and analytics system demonstrating encapsulation, property decorators, and JSON persistence.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **OOP Architecture**: Encapsulated `Student` and `StudentResultManager` classes with computed properties.
- **Dynamic Grading Engine**: Computes total marks, subject averages, letter grades (A+, A, B, C, D, F), and pass/fail thresholds.
- **Statistical Analytics**: Instant class performance summaries (pass rates, class average, highest/lowest scores).
- **JSON Data Persistence**: Automatic reading and writing of student records to `data/students.json`.
- **Zero External Dependencies**: Pure Python standard library (`json`, `typing`, `pathlib`).

## 📁 Project Structure

```
Student-Result-Manager/
├── main.py            # OOP Models and CLI Application
├── README.md          # Documentation
└── data/
    └── students.json  # Data store
```

## 🚀 Quick Start

```bash
python main.py
```
