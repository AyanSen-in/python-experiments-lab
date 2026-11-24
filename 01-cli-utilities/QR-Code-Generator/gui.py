"""
Optional Desktop Tkinter GUI for QR Code Generator
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import sys

try:
    import qrcode
    from PIL import Image, ImageTk
except ImportError:
    print("Error: Required packages missing. Run: pip install qrcode[pil] pillow")
    sys.exit(1)


class QRCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator GUI")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        title = tk.Label(root, text="QR Code Generator", font=("Helvetica", 16, "bold"), pady=10)
        title.pack()

        lbl_entry = tk.Label(root, text="Enter Text or URL:", font=("Helvetica", 10))
        lbl_entry.pack(anchor="w", padx=20, pady=(5, 0))

        self.entry_text = tk.Entry(root, font=("Helvetica", 11), width=40)
        self.entry_text.pack(padx=20, pady=5)

        btn_generate = tk.Button(root, text="Generate QR Code", font=("Helvetica", 10, "bold"),
                                 bg="#007acc", fg="white", padx=10, pady=5, command=self.generate)
        btn_generate.pack(pady=10)

        self.qr_label = tk.Label(root, text="[QR Code Preview will appear here]", width=40, height=15, relief="groove")
        self.qr_label.pack(padx=20, pady=10)

        self.current_img = None
        self.photo = None
        self.btn_save = tk.Button(root, text="Save QR Code Image", state="disabled", command=self.save_image)
        self.btn_save.pack(pady=5)

    def generate(self):
        text = self.entry_text.get().strip()
        if not text:
            messagebox.showwarning("Input Required", "Please enter text or URL.")
            return

        qr = qrcode.QRCode(box_size=6, border=2)
        qr.add_data(text)
        qr.make(fit=True)
        self.current_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        preview_img = self.current_img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(preview_img)
        self.qr_label.config(image=self.photo, text="")
        self.btn_save.config(state="normal")

    def save_image(self):
        if not self.current_img:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")])
        if path:
            self.current_img.save(path)
            messagebox.showinfo("Saved", f"QR code successfully saved to:\n{path}")


def main():
    root = tk.Tk()
    app = QRCodeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
