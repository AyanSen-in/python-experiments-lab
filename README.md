# 📚 Library Management System

A Python-based Library Management System demonstrating Object-Oriented Programming (OOP) principles through practical implementation.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 📖 Add, remove, and search books
- 👥 Register and manage members
- 🔄 Issue and return books
- 📊 View library statistics
- 💾 Automatic JSON data persistence
- 🔍 Search by title, author, or ISBN
- 📝 Complete transaction history
- 🛡️ Error handling and validation

## 📁 Project Structure

```
library_management_system/
├── main.py                 # Entry point
├── models/
│   ├── book.py            # Book class
│   ├── member.py          # Member class
│   ├── library.py         # Library management
│   └── transaction.py     # Transaction tracking
├── utils/
│   └── file_handler.py    # JSON operations
└── data/                  # Data storage
    ├── books.json
    ├── members.json
    └── transactions.json
```

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/library-management-system.git

# Navigate to directory
cd library-management-system

# Run application
python main.py
```

No external dependencies required!

## 💻 Usage

### Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add Book |
| 2 | Remove Book |
| 3 | Register Member |
| 4 | Issue Book |
| 5 | Return Book |
| 6 | Search Books |
| 7 | Display All Books |
| 8 | Display All Members |
| 9 | View Statistics |
| 10 | Transaction History |
| 0 | Exit |

### Example Usage

```python
from models.library import Library

# Create library
library = Library("My Library")

# Add books
library.add_book("1984", "George Orwell", "9780451524935")

# Register member
library.register_member("John Doe")

# Issue book
library.issue_book("9780451524935", "M0001")

# Search books
results = library.search_books("Orwell")
```

## 🎓 OOP Concepts Covered

- **Classes & Objects**: Book, Member, Library, Transaction
- **Encapsulation**: Private attributes in Library
- **Inheritance**: Extensible class hierarchy
- **Polymorphism**: Common interfaces across classes
- **Composition**: Library contains Books and Members
- **Magic Methods**: `__init__`, `__str__`, `__eq__`
- **Class Methods**: `from_dict()`, `get_total_books()`
- **Static Methods**: `validate_isbn()`

## 📚 Learning Path

1. **Week 1**: Basic classes and objects
2. **Week 2**: Encapsulation and methods
3. **Week 3**: Composition and relationships
4. **Week 4**: Data persistence and advanced features

## 🧪 Testing

```bash
# Run tests
python -m unittest discover tests

# Run specific test
python -m unittest tests.test_book
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

Distributed under MIT License. See `LICENSE` for details.

## 📞 Contact

Your Name - [@twitter](https://twitter.com/yourname) - email@example.com

Project Link: [https://github.com/yourusername/library-management-system](https://github.com/yourusername/library-management-system)

---

<p align="center">Made with ❤️ for learning OOP</p>
