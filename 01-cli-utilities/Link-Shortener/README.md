# 🔗 URL Shortener CLI

A lightweight command-line interface tool to quickly shorten long URLs using the TinyURL provider via `pyshorteners`.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **Interactive Mode**: Continuously shorten URLs in an interactive session.
- **CLI Argument Support**: Pass a URL directly as an argument (`python main.py <url>`).
- **Automatic Protocol Handling**: Prepends `https://` if omitted.
- **Fast & Reliable**: Leverages TinyURL API with no API keys required.

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

**Single Command:**
```bash
python main.py https://github.com/AyanSen-in/python-experiments-lab
```
