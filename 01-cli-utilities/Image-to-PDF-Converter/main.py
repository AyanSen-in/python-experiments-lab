"""
Image to PDF Converter
Convert individual images or entire directories of images into a single consolidated PDF.
"""
import os
import sys
from pathlib import Path

try:
    import img2pdf
except ImportError:
    print("Error: 'img2pdf' is not installed. Install it via: pip install img2pdf")
    sys.exit(1)

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')


def convert_images_to_pdf(folder_path: str, output_pdf: str = "output.pdf") -> str:
    path = Path(folder_path).resolve()
    if not path.is_dir():
        raise FileNotFoundError(f"Directory not found: {folder_path}")

    # Gather matching image files
    images = [
        f for f in path.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
    images.sort(key=lambda p: p.name.lower())

    if not images:
        raise ValueError(f"No valid images found in {path} with extensions {SUPPORTED_EXTENSIONS}")

    print(f"Found {len(images)} images to convert.")

    # Read bytes and convert
    image_bytes = []
    for img in images:
        try:
            with open(img, "rb") as f:
                image_bytes.append(f.read())
            print(f"  [+] Loaded: {img.name}")
        except Exception as e:
            print(f"  [!] Skipped {img.name}: {e}")

    if not image_bytes:
        raise RuntimeError("No image data could be read.")

    pdf_bytes = img2pdf.convert(image_bytes)
    out_path = Path(output_pdf).resolve()
    with open(out_path, "wb") as f:
        f.write(pdf_bytes)

    return str(out_path)


def main():
    print("=" * 45)
    print("        Image to PDF Converter")
    print("=" * 45)

    default_dir = os.getcwd()
    dir_input = input(f"Enter image folder path [default: current folder]: ").strip().strip('"').strip("'")
    target_dir = dir_input if dir_input else default_dir

    out_name = input("Enter output PDF filename [default: output.pdf]: ").strip().strip('"').strip("'")
    if not out_name:
        out_name = "output.pdf"
    if not out_name.lower().endswith(".pdf"):
        out_name += ".pdf"

    try:
        saved_file = convert_images_to_pdf(target_dir, out_name)
        print(f"\n✅ Success! PDF generated at: {saved_file}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
