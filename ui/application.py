import tkinter as tk
import util.generic as utl
from datetime import time
import customtkinter as ctk
class Application:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.iconbitmap("C:\\Users\\CRISTIAN\\Desktop\\proyecto uni\\image\\logo.ico")
        self.window.title("C.E.I Josefina Molina de Duque")
        self.window.geometry("600x300")

        frame1 = ctk.CTkFrame(self.window,width=200,height=300)
        frame1.pack(side="left")
        label1 = ctk.CTkLabel(frame1,text="Inicio")
        self.window.mainloop()
