from tkinter import Tk, filedialog
from PIL import Image

def pilih_gambar_dan_kompres():
    file_path = filedialog.askopenfilename(title="Pilih Gambar")
    if file_path:
        img = Image.open(file_path)
        simpan_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if simpan_path:
            img.save(simpan_path, "JPEG", quality=60, optimize=True)
            print("Gambar berhasil dikompres!")

root = Tk()
root.withdraw()  # Sembunyikan window utama
pilih_gambar_dan_kompres()