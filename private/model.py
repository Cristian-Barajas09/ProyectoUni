import customtkinter as ctk
from db.database import base_datos

class MysqlWindow:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("gestion de la base de datos")
        self.window.geometry("500x500")
        self.window.mainloop()
    def database(self):
        self.result = base_datos.mostrar_bd()
        for result in self.result:
            self.label = ctk.CTkLabel(self.window,text=f"{result[0]}")
            self.label.pack()
