# import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as message
from tkinter import ttk
from util.rutas import dir

class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("conexion")
        self.window.geometry("300x300")
        self.window.resizable(0,0)
        self.label1 = ttk.Label(self.window,text="Host: ")
        self.label1.pack()
        self.input1 = ttk.Entry(self.window,)
        self.input1.pack()
        self.label2 = ttk.Label(self.window,text="User: ")
        self.label2.pack()
        self.input2 = ttk.Entry(self.window,)
        self.input2.pack()
        self.label3 = ttk.Label(self.window,text="Database: ")
        self.label3.pack()
        self.input3 =ttk.Entry(self.window,)
        self.input3.pack()
        self.label4 = ttk.Label(self.window,text="Password")
        self.label4.pack()
        self.input4 =ttk.Entry(self.window,)
        self.input4.pack()
        self.button = ttk.Button(self.window,text="Ingresar",command=self.getData)
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
                if self.input4.get() != "":
                    file.write(f"PASSWORD_DATABASE = {self.input4.get()}\n")

            self.window.destroy()

