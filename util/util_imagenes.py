from PIL import ImageTk, Image

def load_image( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE))  