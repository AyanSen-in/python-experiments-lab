"""
PDF Merger Tool
Merge two or more PDF files into a single consolidated PDF document.
"""
import os
import sys
from pathlib import Path

try:
    from pypdf import PdfMerger
except ImportError:
    try:
        from PyPDF2 import PdfMerger
    except ImportError:
        print("Error: Neither 'pypdf' nor 'PyPDF2' is installed. Run: pip install pypdf")
        sys.exit(1)


def merge_pdfs(output_filename: str, input_files: list) -> bool:
    merger = PdfMerger()
    appended_any = False

    for file_path in input_files:
        p = Path(file_path).resolve()
        if not p.is_file():
            print(f"[!] Warning: File '{file_path}' not found. Skipping...")
            continue
        try:
            merger.append(str(p))
            appended_any = True
            print(f"[+] Added: {p.name}")
        except Exception as e:
            print(f"[!] Error appending '{file_path}': {e}")

    if not appended_any:
        print("[-] No valid PDF files were supplied to merge.")
        merger.close()
        return False

    out = Path(output_filename).resolve()
    try:
        with open(out, 'wb') as f:
            merger.write(f)
        print(f"\n✅ PDFs merged successfully into: {out}")
        return True
    except Exception as e:
        print(f"[!] Error writing output file: {e}")
        return False
    finally:
        merger.close()


def main():
    print("=" * 45)
    print("            PDF Merge Tool")
    print("=" * 45)

    if len(sys.argv) > 2:
        out_name = sys.argv[1]
        inputs = sys.argv[2:]
        merge_pdfs(out_name, inputs)
        return

    print("Enter paths to PDF files (one by one). Leave blank and press Enter when done:")
    pdf_list = []
    while True:
        entry = input(f"PDF #{len(pdf_list) + 1}: ").strip().strip('"').strip("'")
        if not entry:
            if len(pdf_list) >= 2:
                break
            print("Please enter at least 2 PDF files to merge.")
            continue
        pdf_list.append(entry)

    out_name = input("\nEnter output PDF name [default: merged_output.pdf]: ").strip().strip('"').strip("'")
    if not out_name:
        out_name = "merged_output.pdf"
    if not out_name.lower().endswith(".pdf"):
        out_name += ".pdf"

    merge_pdfs(out_name, pdf_list)


if __name__ == "__main__":
    main()
