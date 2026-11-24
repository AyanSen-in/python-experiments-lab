# 🖼️ Image to PDF Converter

A clean Python CLI utility to merge individual image files or entire directories into a single, high-quality PDF document.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **Batch Conversion**: Converts all images in a folder into a single PDF in alphabetical sequence.
- **Broad Format Support**: Supports `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, and `.tiff`.
- **Zero Loss / Direct Embedding**: Uses `img2pdf` for loss-free image packing into standard PDF specifications.
- **Interactive Prompts**: Easily specify target input directory and custom output filename.

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running the Converter

```bash
python main.py
```

Follow the on-screen prompts:
1. Provide the directory containing your images (press Enter for current working directory).
2. Choose a name for the output PDF (defaults to `output.pdf`).
