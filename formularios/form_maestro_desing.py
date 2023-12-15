import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL, COLOR_BARRA_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from util.frame_util import *
class FormularioMaestroDesign(tk.Tk):  
    def __init__(self):
        super().__init__()
        self.logo = util_img.load_image("./imagenes/iita-logo.jpeg", (600, 400))
        self.perfil = util_img.load_image("./imagenes/zyro-image.png", (140, 140))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()
        self.minsize(700, 500)  # Tamaño mínimo (ancho x alto)
        self.maxsize(700, 500)  # Tamaño máximo (ancho x alto)

    def config_window(self):
        self.title("Python GUI")
        self.iconbitmap("./imagenes/iita-logo.jpeg")
        w, h = 700, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.centrar_ventana(self, w, h)
      
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill="both")
      
        self.menu_lateral = tk.Frame(self, bg=COLOR_BARRA_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)
      
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)
    
    def controles_barra_superior(self):
        font_awesome = font.Font(family="FontAwesome", size=12)
      
        self.labelTitulo = tk.Label(self.barra_superior, text="IITA")
        self.labelTitulo.config(fg="#fff", font=(
          "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)
      
        self.buttonMenuLateral = tk.Button(self.barra_superior, text='\uf0c9', font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
      
        self.labelInfo = tk.Label(self.barra_superior, text="maurizalexis@gmail.com")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, pady=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)
      
    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2 
        font_awesome = font.Font(family="FontAwesome", size=15)
      
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_BARRA_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
      
        self.buttonDashBoard = tk.Button(self.menu_lateral,command= lambda : modificar_a_inscribir_en_curso(self.cuerpo_principal) )
        self.buttonProfile = tk.Button(self.menu_lateral, command= lambda: modificar_a_inscribir_alumno(self.cuerpo_principal))
        self.buttonPicture = tk.Button(self.menu_lateral, command= lambda: modificar_a_planilla_del_curso(self.cuerpo_principal) )
        self.buttonSettings = tk.Button(self.menu_lateral, command= lambda: modificar_a_planilla_del_alumno(self.cuerpo_principal))
      
        buttons_info = [
            ("Inscribir Curso", "\uf109", self.buttonDashBoard),
            ("Inscribir Alumno", "\uf109", self.buttonProfile),
            ("Plantilla Curso", "\uf109", self.buttonPicture),
            ("Plantilla Alumno", "\uf109", self.buttonSettings)
        ]
      
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)
        
    def controles_cuerpo(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
      
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f" {icon} {text}", anchor= "w", font=font_awesome, 
                      bd=0, bg=COLOR_BARRA_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)  
      
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event, button=button: self.on_enter(event, button))
        button.bind("<Leave>", lambda event, button=button: self.on_leave(event, button))
      
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")
    
    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg="white")
      
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill="y")

if __name__ == "__main__":
    ventana = FormularioMaestroDesign()
    ventana.mainloop()
      