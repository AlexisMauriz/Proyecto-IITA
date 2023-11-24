import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_BARRA_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormunarioMaestroDesing(tk.Tk):  # Corregir la herencia de la clase
    def __init__(self):
        super().__init__()
        self.logo = util_img.lear_imagen("./imagenes/iita-logo.jpeg", (560, 136))
        self.perfil = util_img.lear_imagen("./imagenes/zyro-image.png", (100, 100))
        self.config_window()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title("Python GUI")
        self.iconbitmap("./imagenes/iita-logo.jpeg")
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.center_ventana(self, w, h)
