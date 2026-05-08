# ppm_viewer.py
# Simple PPM (P3 and P6) image viewer using tkinter + Pillow

import sys
from pathlib import Path
from tkinter import Tk, Label, filedialog
from PIL import Image, ImageTk


def read_token(f):
    token = bytearray()

    while True:
        ch = f.read(1)

        if not ch:
            break

        # Skip comments
        if ch == b'#':
            while ch not in (b'\n', b''):
                ch = f.read(1)
            continue

        # Whitespace handling
        if ch in b' \t\r\n':
            if token:
                break
            continue

        token.extend(ch)

    return token.decode('ascii')

def load_ppm(path):
    with open(path, "rb") as f:
        magic = read_token(f)

        if magic not in ("P3", "P6"):
            raise ValueError("Unsupported PPM format")

        width = int(read_token(f))
        height = int(read_token(f))
        maxval = int(read_token(f))

        if maxval > 255:
            raise ValueError("Only maxval <= 255 supported")

        pixels = []

        if magic == "P3":
            for _ in range(width * height):
                r = int(read_token(f))
                g = int(read_token(f))
                b = int(read_token(f))
                pixels.append((r, g, b))

        elif magic == "P6":
            raw = f.read(width * height * 3)

            for i in range(0, len(raw), 3):
                pixels.append((raw[i], raw[i + 1], raw[i + 2]))

        image = Image.new("RGB", (width, height))
        image.putdata(pixels)

        return image


class PPMViewer:
    def __init__(self, image):
        self.root = Tk()
        self.root.title("PPM Viewer")

        self.tk_image = ImageTk.PhotoImage(image)

        label = Label(self.root, image=self.tk_image)
        label.pack()

    def run(self):
        self.root.mainloop()


def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        root = Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Select PPM File",
            filetypes=[("PPM files", "*.ppm")]
        )

        if not file_path:
            return

        path = Path(file_path)

    image = load_ppm(path)

    viewer = PPMViewer(image)
    viewer.run()


if __name__ == "__main__":
    main()