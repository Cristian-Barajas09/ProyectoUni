import customtkinter as ctk
from customtkinter import CTkImage
import os
from util.rutas import dir
from db.database import base_datos
from util.generic import leer_image
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Base:
    sql = base_datos
    def __init__(self,title,geometry):
        self.window = ctk.CTk()
        self.window.title(title)
        self.window.geometry(geometry)

    def resizable(self,width,height):
        self.window.resizable(width,height)

    def icon(self) -> None:
        carpeta_imagenes = os.path.join(dir,"image")
        icon = os.path.join(carpeta_imagenes,"logo.ico")
        self.window.iconbitmap(icon)

    def add_image(self,path,image) -> CTkImage:
        return leer_image(path,image)
