# import customtkinter as tk
import tkinter as tk
from tkinter import ttk
from .empaquetar import Installer
from ui.Form import Form
from ui.main import App
from util.pdf import Word


class Admin:
    """
        ventana para mantener un control a la hora del desarrollo
        debe ser eliminada en produccion
    """
    def __init__(self):
        texto = """esta ventana es exclusiva de los desarroladores
no esta en produccion.
si sale esta pestaña
en produccion resale a diosito,
o en lo creas ¯\_(ツ)_/¯
        """

        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("panel de administrador")
        self.window.configure(background="#000")
        frame1 = tk.Frame(self.window,width=200,height=480,background="#000")
        frame1.place(x=0,y=10)
        self.btn2 = tk.Button(frame1,text="iniciar aplicacion",command=self.form,border=0,background="#041d9b",foreground="#fff")
        self.btn2.place(x=30,y=120,relwidth=0.7,relheight=0.10)
        self.btn4 = tk.Button(frame1,text="generar instalador",command=self.install,border=0,background="#041d9b",foreground="#fff")
        self.btn4.place(x=30,y=240,relwidth=0.7,relheight=0.10)
        self.btn5 = tk.Button(frame1,text="Aplicacion principal",command=self.app,border=0,background="#041d9b",foreground="#fff")
        self.btn5.place(x=30,y=300,relwidth=0.7,relheight=0.10)
        label = tk.Label(self.window,text=texto,background="#000",foreground="#fff")
        label.place(x=220,y=200)
        self.window.mainloop()



    def form(self):
        self.window.destroy()
        Form()

    def app(self):
        self.window.destroy()
        App()
    # def control(self):
    #     self.window.destroy()
    #     Control()

    def install(self):
        self.window.destroy()
        Installer()

