from PIL import ImageTk, Image

def lear_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size))
