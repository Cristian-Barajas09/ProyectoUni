import customtkinter as ctk
from customtkinter import CTkImage
import os
from util.rutas import dir
from model.database import base_datos
from util.generic import leer_image
from util.helpers import matchPassword,encryptPassword

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BaseView:
    """
        plantilla base para generar nuevas ventanas
    """
    def __init__(self,title,geometry):
        self.window = ctk.CTk()
        self.window.title(title)
        self.window.geometry(geometry)

    def resizable(self,width:int,height:int):
        """nos dice si debemos bloquear la ventana
            args:
                width -> espera 1 o 0
                height -> espera 1 o 0
        """
        self.window.resizable(width,height)

    def icon(self) -> None:
        """
            nos genera el icono de la ventana
        """
        carpeta_imagenes = os.path.join(dir,"image")
        icon = os.path.join(carpeta_imagenes,"logo.ico")
        self.window.iconbitmap(icon)

    def add_image(self,path,image) -> CTkImage:
        """
            retorna un objeto del tipo imagen que sirve para ingresar imagenes
            en la vista
        """
        return leer_image(path,image)


class BaseController:
    """
        plantilla base para controlar los datos del usuario
    """
    encrypt = encryptPassword
    match = matchPassword
    sql = base_datos
    def __init__(self):
        pass