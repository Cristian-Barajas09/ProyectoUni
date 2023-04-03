import customtkinter as ctk
import db.database as sqldb


base_datos = sqldb.BaseDatos(**sqldb.keys_db)


class MysqlWindow:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("gestion de la base de datos")
        self.database()
        self.window.mainloop()
    def database(self):
        self.result = base_datos.mostrar_bd()
        for result in self.result:
            self.label = ctk.CTkLabel(self.window,text=f"{result[0]}")
            self.label.pack()
