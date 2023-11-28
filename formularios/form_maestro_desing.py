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
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()
        
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title("Python GUI")
        self.iconbitmap("./imagenes/iita-logo.jpeg")
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.center_ventana(self, w, h)
      
        
    def paneles(self):
      self.barra_superior = tk.Frame (
        self,bg=COLOR_BARRA_SUPERIOR, height=50)
      self.barra_superior.pack(side==tk.TOP, fill="both")
      
      self.menu_lateral = tk.frame(self, bg = COLOR_MENU_LATERAL, width = 150)
      self.menu_lateral.pack (side = tk.LEFT, fill = "bolt", expend = False) 
      
      self.cuerpo_principal = tk.Frame(
        self, bg = COLOR_CUERPO_PRINCIPAL)
      self.cuerpo_principal.pack(side=tk.RIGHT, fill = "both", expend = True)
    
    def controles_barra_superior(self):
      # Configuración de la barra superior
      font_awesome = font.Font(family = "FontAwesome", seze=12)
      
      # Etiqueta de Titulo
      self.labelTitulo = tk.Label(self.barra_superior, text = "IITA")
      self.labelTitulo.config(fg="#fff", font=(
        "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width = 16)
      self.labelTitulo.pack(side = tk.LEFT)
      
      # Boton del menpu lateral
      self.buttonMenuLateral = tk.Button(self.barra_superior, text = 'uf0c9', font=font_awesome,
                                        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
      self.buttonMenuLateral.pack(side=tk.LEFT)
      
      # Etiqueta de Informacion
      self.labelTitulo = tk.Label(
        self.barra_superior, text="alexismauriz")
      self.labelTitulo.config(fg="#fff", font=(
        "Roboto", 10), bg = COLOR_BARRA_SUPERIOR, pack = 10, width = 20)
      self.labelTitulo.pack(side=tk.RIGHT)
      
    def controles_menu_lateral(self):
      #Configuración del menpu lateral
      ancho_menu = 20
      alto_manu = 2
      font_awesome = font.Font(family="FontAwesome", size = 15)
      
      # Etiqueta de perfil
      self.labelPerfil = tk.font.Label(
        self.menu_lateral, image = self.perfil, bg = COLOR_MENU_LATERAL)
      self.labelPerfil.pack(side = tk. TOP, pady = 10)
      
      # Botón del menu lateral
      self.buttonDashBoard = tk.Button(self.menu_lateral)
      self.buttonProfile = tk.Button(self.menu_lateral)
      self.buttonPicture = tk.Button(self.menu_lateral)
      self.buttonInfo = tk.Button(self.menu_lateral)
      self.buttonSettings = tk.Button(self.menu_lateral)
      
      button_info = [
        ("DashBoard", "uf109", self.buttonDashBoard),
        ("Profile", "uf109", self.buttonProfile),
        ("Picture", "uf109", self.buttonPicture),
        ("Settings", "uf109", self.buttonSettings)
      ]
      for text, icon, button in buttons_info:
        self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_manu)
        
    def controles_cuerpo(self):
      #Imagen en el cuerpo principal
      label = tk.Label(self.cuerpo_principal, image=self.logo,
                       bg=COLOR_CUERPO_PRINCIPAL)
      label.placa(x=0, y=0, relwidth=1, relheigth=1)
        
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu. alto_menu):
      button.config(text=f" (icon) (text)", ancho = "w", font=font_awesome,
                    bg=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
      button.pck(side=tk.TOP)
      self.bind_hover_events(button)  
      
    def bind_hover_events(self, button):
      #Asociar eventos Entrer y Leave con la función dinamíca
      button.bind("Enter", lambda event, self.on_enter(event, button))
      button.bind("Enter", lambda event, self.on_leave(event, button))
      
      
    def on_ancho(self, event, button):
      #Cambiar estilo al pasar al ratón por encima
      button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")
    
    def on_leave(self, event, button):
      #Restaurar estilo al salir al ratón
      button.config(bg=COLOR_MENU_LATERAL, fg="white")
      
    def tuggle_panel(self):
      # Alternar visibilidad del menpu lateral
      if self.menu_lateral.winfo_ismapped():
        self.menu_lateral.pack_forguet()
      else:
        self.menu_lateral.pack(side=tk.LEFT, fill="y")
      