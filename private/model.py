import customtkinter as ctk
from model.database import base_datos

class MysqlWindow:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("gestion de la base de datos")
        self.window.geometry("500x500")
        self.btn1 = ctk.CTkButton(self.window,text="mostrar bases de datos",command=self.database)
        self.btn1.pack(pady=10)
        self.btn2 = ctk.CTkButton(self.window,text="crear tabla",command=self.create_table)
        self.btn2.pack(pady=10)
        self.window.mainloop()
    def database(self):
        self.vent1 = ctk.CTkToplevel()
        self.result = base_datos.mostrar_bd()
        # print(self.result[0][0])
        for result in self.result:
            self.label = ctk.CTkLabel(self.vent1,text=f"{result[0]}")
            self.label.pack()


    def create_table(self):
        self.vent2 = ctk.CTkToplevel()
        self.label1 = ctk.CTkLabel(master=self.vent2,text="nombre de la tabla")
        self.label1.pack()
        self.input1 = ctk.CTkEntry(master=self.vent2,placeholder_text="test")
        self.input1.pack()
        # text = self.input1.get()
        # print(text)
        # base_datos.create_table("test",4)
