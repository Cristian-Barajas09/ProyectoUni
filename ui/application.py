import tkinter as tk
import util.generic as utl
import os
import customtkinter as ctk
class Application:
    def __init__(self,image):
        self.window = ctk.CTk()
        carpeta_imagenes = os.path.join(image,"logo.ico")
        self.window.iconbitmap(carpeta_imagenes)
        self.window.title("C.E.I Josefina Molina de Duque")
        self.window.geometry("600x300")

        frame1 = ctk.CTkFrame(self.window,width=200,height=300)
        frame1.pack(side="left")
        label1 = ctk.CTkLabel(frame1,text="Inicio")
        self.window.mainloop()
