import customtkinter as ctk
import os
from util.rutas import dir
class Base:
    def icon(self) -> None:
        carpeta_imagenes = os.path.join(dir,"image")
        icon = os.path.join(carpeta_imagenes,"logo.ico")
        self.window.iconbitmap(icon)