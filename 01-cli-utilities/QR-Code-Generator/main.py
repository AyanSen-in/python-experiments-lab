"""
QR Code Generator
Generate customizable QR codes with instant terminal ASCII preview and PNG file output.
"""
import sys
import os
from pathlib import Path

try:
    import qrcode
except ImportError:
    print("Error: 'qrcode' is not installed. Install via: pip install qrcode[pil]")
    sys.exit(1)


def generate_qr(
    data: str,
    output_filename: str = "qr_output.png",
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white"
) -> str:
    """Generates a QR code image and saves it to disk."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error correction
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    output_path = Path(output_filename).resolve()
    img.save(str(output_path))
    return str(output_path)


def display_ascii_preview(data: str):
    """Prints a terminal-friendly ASCII preview of the QR code."""
    try:
        qr = qrcode.QRCode(border=1)
        qr.add_data(data)
        qr.make(fit=True)
        print("\n── Terminal QR Preview ──")
        qr.print_ascii(invert=True)
    except Exception:
        pass


def main():
    print("=" * 50)
    print("              QR Code Generator")
    print("=" * 50)

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter text or URL to encode: ").strip()

    if not text:
        print("Error: No input text provided.")
        sys.exit(1)

    file_name = input("Enter output image filename [default: qr_output.png]: ").strip()
    if not file_name:
        file_name = "qr_output.png"
    if not file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        file_name += ".png"

    try:
        saved_path = generate_qr(text, file_name)
        print(f"\n✅ QR code saved to: {saved_path}")
        display_ascii_preview(text)
    except Exception as e:
        print(f"Error generating QR code: {e}")


if __name__ == "__main__":
    main()
