# import customtkinter as ctk
import tkinter
from tkinter import ttk
# from customtkinter import CTkImage
import os
from util.rutas import dir

from util.generic import leer_image_tkinter

from PIL.ImageTk import PhotoImage
from typing import Tuple,Any

from partials.controller.BaseController import BaseController





# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")

class BaseView:
    """
        plantilla base para generar nuevas ventanas
    """
    window: tkinter.Tk
    tk = tkinter
    ttk = ttk
    _controller:BaseController
    carpeta_imagenes = os.path.join(dir,"image")

    def __init__(self,title:str,geometry:str,controller:BaseController,):
        self.window = self.tk.Tk()
        self.window.title(title)
        self.window.geometry(geometry)

        self._controller = controller()

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

        icon = os.path.join(self.carpeta_imagenes,"logo.ico")
        self.window.iconbitmap(icon)

    # def add_image(self,path,size) -> CTkImage:
        """
            retorna un objeto del tipo imagen que sirve para ingresar imagenes
            en la vista
        """
        # return leer_image(path,size)

    def add_image(self,path:str,size: Tuple[int,int]) -> PhotoImage:
        """
            retorna un objeto del tipo imagen que sirve para ingresar imagenes
            en la vista
        """
        return leer_image_tkinter(path,size)

    def image(self,path:str,size:tuple):
        return PhotoImage(file=path,size=size)