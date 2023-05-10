import customtkinter as ctk
import tkinter.messagebox as message
from util.rutas import dir

class App:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("conexion")
        self.window.geometry("300x300")
        self.window.resizable(0,0)
        self.label1 = ctk.CTkLabel(self.window,text="Host: ")
        self.label1.pack()
        self.input1 = ctk.CTkEntry(self.window,placeholder_text="localhost")
        self.input1.pack()
        self.label2 = ctk.CTkLabel(self.window,text="User: ")
        self.label2.pack()
        self.input2 = ctk.CTkEntry(self.window,placeholder_text="root")
        self.input2.pack()
        self.label3 = ctk.CTkLabel(self.window,text="Database: ")
        self.label3.pack()
        self.input3 =ctk.CTkEntry(self.window,placeholder_text="test")
        self.input3.pack()
        self.button = ctk.CTkButton(self.window,text="Ingresar",command=self.getData)
        self.button.pack(pady=10)
        self.window.mainloop()


    def getData(self):
        self.host = self.input1.get()
        self.user = self.input2.get()
        self.data_base = self.input3.get()
        if not self.host  or not self.user or not self.data_base:
            message.showerror(title="faltan campos",message="rellene todos los campos")
        else:
            with open(f"{dir}/.env",'w+') as file:
                file.write("# KEYS FOR DATABASE\n\n")
                file.write(f"USER_DATABASE = {self.user}\n")
                file.write(f"DATABASE = {self.data_base}\n")
                file.write(f"HOST_DATABASE = {self.host}\n")
            self.window.destroy()

