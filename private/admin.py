import customtkinter as ctk
from .model import MysqlWindow
from .empaquetar import Installer
from ui.main import Form,Control


class Admin:
    def __init__(self):
        texto = """esta ventana es exclusiva de los desarroladores
no esta en produccion.
si sale esta pestaña
en produccion resale a diosito,
o en lo creas ¯\_(ツ)_/¯
        """

        self.window = ctk.CTk()
        self.window.geometry("500x500")
        self.window.title("panel de administrador")
        frame1 = ctk.CTkFrame(self.window,width=200,height=480,fg_color="#343434")
        frame1.place(x=0,y=10)
        self.btn1 = ctk.CTkButton(frame1,text="mysql",command=self.mysqlWindow)
        self.btn1.place(x=20,y=40)
        self.btn2 = ctk.CTkButton(frame1,text="iniciar aplicacion",command=self.form)
        self.btn2.place(x=20,y=80)
        self.btn3 = ctk.CTkButton(frame1,text="control de personal",command=self.control)
        self.btn3.place(x=20,y=120)
        self.btn4 = ctk.CTkButton(frame1,text="generar instalador",command=self.install)
        self.btn4.place(x=20,y=160)
        label = ctk.CTkLabel(self.window,text=texto)
        label.place(x=200,y=10)
        self.window.mainloop()

    def mysqlWindow(self):
        self.window.destroy()
        MysqlWindow()


    def form(self):
        self.window.destroy()
        Form()


    def control(self):
        self.window.destroy()
        Control()

    def install(self):
        self.window.destroy()
        Installer()

