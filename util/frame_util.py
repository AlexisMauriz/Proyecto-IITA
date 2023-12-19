import tkinter as tk
from alumno import Alumno
import json

def escribir_en_json(data):
    with open("j.json", 'r') as file:
        existing_data = json.load(file)
       
    existing_data.append(data)
    
    with open("j.json", 'w') as file:
        json.dump(existing_data, file, indent=4)
        
        
def modificar_a_inscribir_en_curso(frame):
    def inscribir_en_curso():
        global txt1, txt2, txt3, txt4  # Hacer que las variables sean globales para acceder desde inscribir_en_curso
        PythonI = txt1.get()
        PythonII = txt2.get()
        MarketingDigital = txt3.get()
        Robotica = txt4.get()

        a = Curso(PythonI, PythonII, MarketingDigital, Robotica)
        escribir_en_json(a.to_dict())
        
    for wid in frame.winfo_children():
        wid.destroy()
    
    # Etiquetas, cajas de entrada y botones debajo del botón "Inscribir Curso"
    lbl1 = tk.Label(frame, text="Python I", bg="#1488CC")
    lbl1.place(x=120, y=60, width=100, height=30)
    
    txt1 = tk.Entry(frame, bg="#1488CC")
    txt1.place(x=240, y=60, width=100, height=30)
    
    lbl2 = tk.Label(frame, text="Python II", bg="#1488CC")
    lbl2.place(x=120, y=100, width=100, height=30)
    
    txt2 = tk.Entry(frame, bg="#1488CC")
    txt2.place(x=240, y=100, width=100, height=30)
    
    lbl3 = tk.Label(frame, text="Marketing Digital", bg="#1488CC")
    lbl3.place(x=120, y=140, width=100, height=30)
    
    txt3 = tk.Entry(frame, bg="#1488CC")
    txt3.place(x=240, y=140, width=100, height=30)
    
    lbl4 = tk.Label(frame, text="Robótica", bg="#1488CC")
    lbl4.place(x=120, y=180, width=100, height=30)
    
    txt4 = tk.Entry(frame, bg="#1488CC")
    txt4.place(x=240, y=180, width=100, height=30)
    
    boton = tk.Button(frame, text="Inscribir Curso", command=inscribir_en_curso)
    boton.pack(pady=20)

    
def modificar_a_inscribir_alumno(frame):
    def inscribir_alumno():
        nombre = txt1.get()
        apellido = txt2.get()
        edad = txt3.get()
        dni = txt4.get()
        contacto = txt5.get()

        a = Alumno(nombre, apellido, edad, dni, contacto)
        escribir_en_json(a.to_dict())

    for wid in frame.winfo_children():
        wid.destroy()
    
    boton = tk.Button(frame, text="Inscribir Alumno", command=inscribir_alumno)
    boton.pack(pady=20)
  
    # Coordenada inicial en y
    y_coordinate = 60
    
    lbl1 = tk.Label(frame, text="Nombre", bg="#1488CC")
    lbl1.place(x=120, y=y_coordinate, width=100, height=30)
    
    txt1 = tk.Entry(frame, bg="#1488CC")
    txt1.place(x=240, y=y_coordinate, width=100, height=30)
    
    lbl2 = tk.Label(frame, text="Apellido", bg="#1488CC")
    lbl2.place(x=120, y=y_coordinate + 40, width=100, height=30)
    
    txt2 = tk.Entry(frame, bg="#1488CC")
    txt2.place(x=240, y=y_coordinate + 40, width=100, height=30)
    
    lbl3 = tk.Label(frame, text="Edad", bg="#1488CC")
    lbl3.place(x=120, y=y_coordinate + 80, width=100, height=30)
    
    txt3 = tk.Entry(frame, bg="#1488CC")
    txt3.place(x=240, y=y_coordinate + 80, width=100, height=30)
    
    lbl4 = tk.Label(frame, text="DNI", bg="#1488CC")
    lbl4.place(x=120, y=y_coordinate + 120, width=100, height=30)
    
    txt4 = tk.Entry(frame, bg="#1488CC")
    txt4.place(x=240, y=y_coordinate + 120, width=100, height=30)
    
    lbl5 = tk.Label(frame, text="Contacto", bg="#1488CC")
    lbl5.place(x=120, y=y_coordinate + 160, width=100, height=30)
    
    txt5 = tk.Entry(frame, bg="#1488CC")
    txt5.place(x=240, y=y_coordinate + 160, width=100, height=30)
    
    
def modificar_a_planilla_del_curso(frame):
    for wid in frame.winfo_children():
        wid.destroy()
    
    boton = tk.Button(frame, text="Planilla del curso")
    boton.pack(pady=20)
  
    lbl1 = tk.Label(frame, text="Profesor Titular", bg="#1488CC")
    lbl1.place(x=120, y=50, width=100, height=30)
  
    txt1 = tk.Entry(frame, bg="#1488CC")
    txt1.place(x=240, y=50, width=100, height=30)
  
    lbl2 = tk.Label(frame, text="Profesor Adjunto", bg="#1488CC")
    lbl2.place(x=120, y=90, width=100, height=30)
    
    txt2 = tk.Entry(frame, bg="#1488CC")
    txt2.place(x=240, y=90, width=100, height=30)
    
    lbl3 = tk.Label(frame, text="Tema del Día", bg="#1488CC")
    lbl3.place(x=120, y=130, width=100, height=30)
    
    txt3 = tk.Entry(frame, bg="#1488CC")
    txt3.place(x=240, y=130, width=100, height=30)
    
    lbl4 = tk.Label(frame, text="Trabajo Practicos", bg="#1488CC")
    lbl4.place(x=120, y=170, width=100, height=30)
    
    txt4 = tk.Entry(frame, bg="#1488CC")
    txt4.place(x=240, y=170, width=100, height=30)
    
    lbl5 = tk.Label(frame, text="Examenes", bg="#1488CC")
    lbl5.place(x=120, y=170, width=100, height=30)
    
    txt5 = tk.Entry(frame, bg="#1488CC")
    txt5.place(x=240, y=170, width=100, height=30)
    
    
def modificar_a_planilla_del_alumno(frame):

    for wid in frame.winfo_children():
        wid.destroy()
    
    boton = tk.Button(frame, text="Planilla del Alumno")
    boton.pack(pady=20)
  
    lbl1 = tk.Label(frame, text="Nombre y Apellido", bg="#1488CC")
    lbl1.place(x=120, y=50, width=100, height=30)
    
    txt1 = tk.Entry(frame, bg="#1488CC")
    txt1.place(x=240, y=50, width=100, height=30)
    
    lbl2 = tk.Label(frame, text="Asistencias", bg="#1488CC")
    lbl2.place(x=120, y=90, width=100, height=30)
    
    txt2 = tk.Entry(frame, bg="#1488CC")
    txt2.place(x=240, y=90, width=100, height=30)
    
    lbl3 = tk.Label(frame, text="Notas TP", bg="#1488CC")
    lbl2.place(x=120, y=90, width=100, height=30)
