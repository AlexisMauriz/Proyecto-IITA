def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho - aplicacion_ancho) / 2)  # Corrección de la fórmula para calcular x
    y = int((pantall_largo - aplicacion_largo) / 2)  # Corrección de la fórmula para calcular y
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

