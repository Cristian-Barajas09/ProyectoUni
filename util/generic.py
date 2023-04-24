from PIL import ImageTk,Image
from customtkinter import CTkImage

def leer_image(path,size) -> CTkImage:
    return CTkImage(
        dark_image=Image.open(path).resize(size,Image.ANTIALIAS),
        size=size,
    )

def centrar_venta(ventana,aplicacion_ancho,aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (pantalla_ancho / 2))
    y = int((pantalla_largo / 2) - (pantalla_largo / 2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")