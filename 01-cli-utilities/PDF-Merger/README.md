# 📑 PDF Merger

A lightweight Python utility to concatenate and merge multiple PDF documents into a single unified file.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **Multi-File Merging**: Merge 2, 3, or more PDF files in any desired order.
- **CLI & Argument Modes**: Provide filenames interactively or as command-line arguments.
- **Robust Error Handling**: Skips unreadable or corrupted files without crashing the merge process.
- **Supports Modern `pypdf` and `PyPDF2`**: Seamless fallback across both libraries.

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Usage

**Interactive Prompt:**
```bash
python main.py
```

**Command-line Arguments:**
```bash
python main.py <output_file.pdf> <input1.pdf> <input2.pdf> ...
```
