import os
import customtkinter as ctk
from .inscripcion import Inscripciones
from .control import Control
from util.rutas import dir
class Application:
    def __init__(self):
        self.window = ctk.CTk()
        carpeta_imagenes = os.path.join(dir,"image")
        icon = os.path.join(carpeta_imagenes,"logo.ico")
        self.window.iconbitmap(icon)
        self.window.title("C.E.I Josefina Molina de Duque")
        self.window.geometry("600x300")

        frame_1 = ctk.CTkFrame(self.window,width=200,height=300)
        frame_1.pack(side="left")
        label_1 = ctk.CTkLabel(frame_1,text="Inicio")
        label_1.place(x=20,y=20)
        btn_1 = ctk.CTkButton(master=frame_1,text="incripciones",command=self.inscripciones)
        btn_1.place(x=20,y=50)
        btn_2 = ctk.CTkButton(master=frame_1,text="Control de personal",command=self.personal)
        btn_2.place(x=20,y=100)
        self.window.mainloop()
    def inscripciones(self):
        self.window.destroy()
        Inscripciones()

    def personal(self):
        self.window.destroy()
        Control()

