# 🐍 Python Experiments Lab

A curated monorepo consolidating practical Python utilities, command-line interfaces, terminal games, object-oriented systems, and AI learning experiments.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Author](https://img.shields.io/badge/Author-Ayan%20Sen-00f5ff.svg)](https://github.com/AyanSen-in)

---

## 📂 Repository Structure

The projects in this repository are organized into four distinct functional domains:

```text
python-experiments-lab/
├── 01-cli-utilities/        # Automation, audio, PDFs, QR, web tools & calculations
├── 02-games/                # Terminal-based quiz, trivia, canvas art & strategy games
├── 03-systems-and-oop/      # Production architecture, OOP patterns, auth & analytics
└── 04-ai-and-learning/      # Interactive AI and Streamlit educational tools
```

---

## 🛠️ Project Index

### 📁 01. CLI Utilities
Practical terminal tools and single-purpose utilities built using Python's standard library and external APIs.

| Project | Description | Core Stack |
| :--- | :--- | :--- |
| **[Expense-Tracker-CLI](./01-cli-utilities/Expense-Tracker-CLI/)** | Dependency-free CLI application for tracking daily personal expenses with JSON persistence. | Python, `json`, `datetime` |
| **[Image-to-PDF-Converter](./01-cli-utilities/Image-to-PDF-Converter/)** | Batch image to PDF conversion utility supporting multi-format loss-free document packing. | Python, `img2pdf` |
| **[Link-Shortener](./01-cli-utilities/Link-Shortener/)** | CLI URL shortener leveraging the TinyURL API for immediate link compression. | Python, `pyshorteners` |
| **[Page-as-PDF-Downloader](./01-cli-utilities/Page-as-PDF-Downloader/)** | Headless browser automation script rendering full web pages into styled A4 PDFs. | Python, `pyppeteer`, `asyncio` |
| **[Password-Manager](./01-cli-utilities/Password-Manager/)** | Credential vault and customizable password generator with local text persistence. | Python, `random`, `string` |
| **[PDF-Merger](./01-cli-utilities/PDF-Merger/)** | Multi-document PDF concatenation tool supporting dynamic file inputs and error handling. | Python, `pypdf` / `PyPDF2` |
| **[QR-Code-Generator](./01-cli-utilities/QR-Code-Generator/)** | Dual CLI/GUI QR code generator with instant terminal ASCII preview and PNG export. | Python, `qrcode`, `pillow`, `tkinter` |
| **[Secret-code_Language](./01-cli-utilities/Secret-code_Language/)** | Cipher encoding and decoding utility for secret message encryption. | Python, String manipulation |
| **[simple_calculator](./01-cli-utilities/simple_calculator/)** | Arithmetic calculation utility handling basic and multi-step math operations. | Python, Functional Design |
| **[Text_To_Voice-](./01-cli-utilities/Text_To_Voice-/)** | Text-to-speech audio converter converting written scripts into natural audio. | Python, `gTTS` / `pyttsx3` |
| **[TIK_TIK-Time_App](./01-cli-utilities/TIK_TIK-Time_App/)** | Desktop live clock with time-of-day greetings and hourly notifications. | Python, `tkinter`, Desktop UI |

---

### 🎮 02. Games
Interactive command-line games and canvas applications focused on control flow, game loops, and graphics.

| Project | Description | Core Stack |
| :--- | :--- | :--- |
| **[Kaun_Banega_Crorepati](./02-games/Kaun_Banega_Crorepati/)** | KBC-inspired trivia game with progressive cash prizes and multiple-choice questions. | Python, CLI loops, State management |
| **[Pixel-Art-Generator](./02-games/Pixel-Art-Generator/)** | Interactive drawing canvas for geometric shapes, polygons, and pixel art. | Python, `turtle`, `tkinter` |
| **[quize_game](./02-games/quize_game/)** | Interactive quiz game featuring score tracking and dynamic validation. | Python, Terminal I/O |
| **[snake_water_gun.game](./02-games/snake_water_gun.game/)** | Classic Indian variant of Rock-Paper-Scissors featuring randomized computer opponents. | Python, `random` module |

---

### 🏛️ 03. Systems & Object-Oriented Programming (OOP)
Structured software architectures demonstrating modular design, data modeling, security, and persistence.

| Project | Description | Core Stack |
| :--- | :--- | :--- |
| **[Authentication_system](./03-systems-and-oop/Authentication_system/)** | Secure user authentication and credential validation engine utilizing bcrypt hashing. | Python, `bcrypt`, Security & Hashing |
| **[Library-Management-System](./03-systems-and-oop/Library-Management-System/)** | Full OOP implementation with models, data persistence, and administrative controls. | Python, Classes, Inheritance, Modular architecture |
| **[Student-Result-Manager](./03-systems-and-oop/Student-Result-Manager/)** | Academic grading, performance tracking, and statistical analytics engine with JSON storage. | Python, OOP, Properties, `json` |

---

### 🤖 04. AI & Interactive Learning
Interactive applications bridging core software development and modern artificial intelligence concepts.

| Project | Description | Core Stack |
| :--- | :--- | :--- |
| **[ai-terminology-explorer](./04-ai-and-learning/ai-terminology-explorer/)** | Interactive Streamlit web application explaining LLMs, RAG, embeddings, and autonomous agents. | Streamlit, Python, Web UI |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher installed on your system.
* (Optional) `pip` package manager.

### Running a Specific Project
Navigate into the respective project folder and execute its entry file:

```bash
# Example 1: Run the QR Code Generator (CLI)
cd "01-cli-utilities/QR-Code-Generator"
python main.py

# Example 2: Run the Student Result Manager (OOP)
cd "03-systems-and-oop/Student-Result-Manager"
python main.py

# Example 3: Launch the AI Terminology Explorer
cd "04-ai-and-learning/ai-terminology-explorer"
streamlit run app.py
```

---

## 👤 Author
**Ayan Sen**  
* GitHub: [@AyanSen-in](https://github.com/AyanSen-in)
* LinkedIn: [linkedin.com/in/ayanseninf](https://www.linkedin.com/in/ayanseninf/)
