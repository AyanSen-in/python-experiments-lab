# 🌐 Page-as-PDF Downloader

A headless Chromium automation script to render full web pages (including JavaScript and background assets) and download them as formatted A4 PDFs.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **Full JavaScript Rendering**: Uses headless Chromium via `pyppeteer` to wait for DOM completion (`networkidle2`).
- **A4 Format**: Exports pages in standard A4 document layout with background styling enabled.
- **Auto-naming**: Automatically derives clean output file names from URLs if not explicitly specified.
- **Cross-Platform**: Works across Windows, macOS, and Linux.

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
# Basic usage
python main.py -l https://example.com

# Specify custom PDF filename
python main.py --link https://news.ycombinator.com --name hacker_news.pdf
```
