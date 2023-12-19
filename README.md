# proyecto-iita.py

# Interfaz Gráfica con Tkinter - README

Este proyecto muestra una interfaz gráfica simple utilizando la biblioteca Tkinter en Python. La interfaz consta de una ventana principal que contiene barras laterales y superior, además de un área central de visualización con una imagen y botones de menú.

## Contenido del Proyecto

- **`main.py`**: Contiene la clase `FormularioMaestroDesign` que define la ventana principal y sus funcionalidades.
- **`config.py`**: Almacena las variables de colores utilizadas en la interfaz.
- **`util/`**: Directorio con funciones de utilidad para manejar ventanas y cargar imágenes.

## Estructura y Funcionalidades

### Clase `FormularioMaestroDesign` en `main.py`

Esta clase crea y controla la ventana principal de la interfaz gráfica. A continuación se detallan sus métodos principales:

- **`__init__()`**: Inicializa la ventana principal y carga las imágenes utilizadas en la interfaz.
- **`config_window()`**: Configura el título, el ícono y el tamaño de la ventana.
- **`paneles()`**: Crea las secciones de la interfaz: barra superior, lateral y cuerpo principal.
- **`controles_barra_superior()`** y **`controles_menu_lateral()`**: Añaden elementos (etiquetas, botones) a las barras laterales y superior respectivamente.
- **`controles_cuerpo()`**: Muestra una imagen en el cuerpo principal.
- **`configurar_boton_menu()`**: Configura los botones del menú lateral.
- **`bind_hover_events()`, `on_enter()`, `on_leave()`**: Manejan los eventos de interacción con los botones.
- **`toggle_panel()`**: Alterna la visibilidad del menú lateral al hacer clic en un botón de la barra superior.

### Archivos de Configuración

- **`config.py`**: Contiene las variables de colores utilizadas en la interfaz.

### Utilidades

- **`util/`**: Contiene funciones auxiliares para cargar imágenes y centrar la ventana.

## Uso

1. Asegúrate de tener instaladas las bibliotecas `tkinter` y `PIL` (Python Imaging Library).
2. Modifica las rutas de las imágenes en `./imagenes/` que deseas cargar en la interfaz.
3. Importa la clase `FormularioMaestroDesign` desde tu archivo principal.
4. Crea una instancia con `FormularioMaestroDesign()` y ejecuta la aplicación con `app.mainloop()`.

## Consideraciones

- **Personalización**: Puedes modificar los colores, tamaños y añadir más elementos según tus necesidades.
- **Manejo de Eventos**: Añade más funcionalidades manejando eventos de interacción con los botones o agregando más acciones a los botones del menú.

Claro, aquí tienes un README básico para el código proporcionado:

---

# README - Uso de FormularioMaestroDesign

Este código utiliza la clase `FormularioMaestroDesign` para crear una interfaz gráfica básica utilizando la biblioteca Tkinter en Python.

## Uso

1. **Importación de la clase `FormularioMaestroDesign`**

   Asegúrate de tener la estructura de carpetas adecuada para la importación. Por ejemplo, si la clase `FormularioMaestroDesign` está definida en el archivo `form_maestro_desing.py` dentro de un directorio llamado `formularios`, la importación se verá como:

   ```python
   from formularios.form_maestro_desing import FormularioMaestroDesign
   ```

2. **Instanciación y Ejecución de la Interfaz**

   Crea una instancia de `FormularioMaestroDesign`:

   ```python
   app = FormularioMaestroDesign()
   ```

3. **Ejecuta la Aplicación**

   Utiliza el método `mainloop()` para iniciar la aplicación y mostrar la interfaz gráfica:

   ```python
   app.mainloop()
   ```

## Consideraciones

- **Estructura del Proyecto**: Asegúrate de tener la estructura de archivos correcta para la importación.
- **Personalización**: Puedes modificar y ampliar la clase `FormularioMaestroDesign` para agregar más elementos, funcionalidades y mejorar la interfaz según tus necesidades.
  Claro, aquí tienes un documento README explicando el código proporcionado:

---

# README - Función para Centrar una Ventana

La función `centrar_ventana()` se encarga de posicionar una ventana en el centro de la pantalla. Aquí se detalla su funcionamiento:

## Detalles de la Función

### Parámetros

- **`ventana`**: Representa la ventana a posicionar.
- **`aplicacion_ancho`**: Anchura deseada para la ventana.
- **`aplicacion_largo`**: Altura deseada para la ventana.

### Descripción

1. **Obtención de las Dimensiones de la Pantalla**

   - `pantall_ancho = ventana.winfo_screenwidth()`: Obtiene el ancho de la pantalla en píxeles.
   - `pantall_largo = ventana.winfo_screenheight()`: Obtiene la altura de la pantalla en píxeles.

2. **Cálculo de las Coordenadas para Centrar la Ventana**

   - `x = int((pantall_ancho - aplicacion_ancho) / 2)`: Calcula la coordenada x para posicionar la ventana en el centro horizontal de la pantalla.
   - `y = int((pantall_largo - aplicacion_largo) / 2)`: Calcula la coordenada y para posicionar la ventana en el centro vertical de la pantalla.

3. **Establecimiento de la Geometría de la Ventana**

   - `ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")`: Asigna la geometría a la ventana con el ancho y alto especificados, y las coordenadas x e y para posicionarla en el centro de la pantalla.

## Uso

Para utilizar esta función, proporciona la ventana que deseas centrar, junto con el ancho y alto deseados. Llama a la función `centrar_ventana()` con estos parámetros para posicionar la ventana en el centro de la pantalla.

```python
centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo)
```

## Consideraciones

- Esta función puede ser utilizada al inicio de la creación de una ventana para asegurarse de que aparezca centrada en la pantalla.
- Es útil cuando se desea una apariencia más estética y consistente al mostrar ventanas.

Claro, aquí tienes un documento README explicando el código proporcionado:

---

# README - Carga de una Imagen con Dimensiones Específicas

El fragmento de código proporcionado se enfoca en cargar una imagen con dimensiones específicas utilizando una función `load_image()`.

## Detalles del Código

### Variables

- **`ruta_imagen`**: Ruta del archivo de imagen que se desea cargar.
- **`dimensiones`**: Tupla que contiene el tamaño deseado de la imagen en píxeles (ancho x alto).
- **`imagen_cargada`**: Variable que almacenará la imagen cargada con las dimensiones especificadas.

### Descripción

1. **Ruta de la Imagen**

   - `ruta_imagen = "./ruta/a/la/imagen.jpg"`: Especifica la ruta donde se encuentra el archivo de imagen que se desea cargar.

2. **Dimensiones Deseadas**

   - `dimensiones = (200, 200)`: Define las dimensiones deseadas para la imagen. En este caso, se indica un tamaño de 200 píxeles de ancho y 200 píxeles de alto.

3. **Carga de la Imagen**

   - `imagen_cargada = load_image(ruta_imagen, dimensiones)`: Llama a la función `load_image()` para cargar la imagen ubicada en la ruta especificada con las dimensiones deseadas.

## Uso

Para utilizar este código, asegúrate de tener una función `load_image()` definida en tu proyecto que sea capaz de cargar una imagen desde una ruta con las dimensiones específicas proporcionadas. Luego, utiliza las variables `ruta_imagen` y `dimensiones` para cargar la imagen deseada.

## Consideraciones

- La función `load_image()` debe estar definida correctamente y ajustada para cargar una imagen desde la ruta especificada con las dimensiones proporcionadas.
- Asegúrate de que la ruta proporcionada sea válida y apunte a la ubicación correcta del archivo de imagen.
# Proyecto-IITA
