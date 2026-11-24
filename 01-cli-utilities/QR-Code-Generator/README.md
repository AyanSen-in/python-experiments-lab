# 📱 QR Code Generator

A versatile QR Code generator providing both a fast command-line interface with terminal ASCII rendering and an optional desktop GUI.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **CLI & GUI Interfaces**: Run from the command line with instant preview or launch the Tkinter desktop GUI.
- **Terminal ASCII Rendering**: Renders a scannable ASCII QR preview directly inside your terminal.
- **High Error Correction**: Built with high error-correction capability (H level, ~30% recovery).
- **Customizable Output**: Easily save high-resolution PNG outputs for printing or sharing.

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### CLI Usage

```bash
# Interactive mode
python main.py

# Pass argument directly
python main.py "https://github.com/AyanSen-in/python-experiments-lab"
```

### GUI Usage

```bash
python gui.py
```
