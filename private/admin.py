# import customtkinter as tk
import tkinter as tk
from tkinter import ttk
from .empaquetar import Installer
from ui.Form import Form
from ui.main import App
from util.generateWord import Word


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
        frame1 = ttk.Frame(self.window,width=200,height=480,)
        frame1.place(x=0,y=10)
        self.btn2 = ttk.Button(frame1,text="iniciar aplicacion",command=self.form)
        self.btn2.place(x=20,y=80)
        self.btn3 = ttk.Button(frame1,text="Word",command=self.generateWord)
        self.btn3.place(x=20,y=120)
        self.btn4 = ttk.Button(frame1,text="generar instalador",command=self.install)
        self.btn4.place(x=20,y=160)
        self.btn5 = ttk.Button(frame1,text="Aplicacion principal",command=self.app)
        self.btn5.place(x=20,y=180)
        label = ttk.Label(self.window,text=texto)
        label.place(x=200,y=10)
        self.window.mainloop()



    def form(self):
        self.window.destroy()
        Form()


    def generateWord(self):
        archivo = Word("test.docx")

        file = archivo.read_template()
        archivo.copy()
        archivo.save()

    def app(self):
        self.window.destroy()
        App()
    # def control(self):
    #     self.window.destroy()
    #     Control()

    def install(self):
        self.window.destroy()
        Installer()

