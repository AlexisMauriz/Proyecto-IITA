def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))  # Corregir la fórmula para calcular x
    y = int((pantall_largo / 2) - (aplicacion_largo / 2))  # Corregir la fórmula para calcular y
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
