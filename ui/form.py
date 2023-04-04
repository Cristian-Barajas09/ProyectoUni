import tkinter as tk
from tkinter import messagebox
import db.database as sqldb
from .application import Application
from tkinter.font import BOLD
import util.generic as utl
import customtkinter as ctk
import os
#formulario de entrada

base_datos = sqldb.BaseDatos(**sqldb.keys_db)



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
class Form:
    def __init__(self,image):
        carpeta_imagenes = os.path.join(image,"logo.ico")
        print(carpeta_imagenes)
        self.image = image
        self.window = ctk.CTk()
        self.window.title("inicio de sesion")
        self.window.geometry("800x500")
        self.window.resizable(0,0)
        self.window.iconbitmap(carpeta_imagenes)

        utl.centrar_venta(self.window,800,500)
        #frame logo
        logo = utl.leer_image("./image/logo.jpeg",(200,200))
        frame_logo = ctk.CTkFrame(self.window, border_width=0,width=300)
        frame_logo.pack(ipadx=10,ipady=10,side="left",expand=tk.NO,fill=tk.BOTH)
        #frame logo
        #frame form
        label1 = ctk.CTkLabel(frame_logo,image=logo,text="")
        label1.place(x=0,y=0,relwidth=1,relheight=1)
        frame_form = ctk.CTkFrame(self.window,border_width=0)
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame form
        #frame form top
        frame_form_top = ctk.CTkFrame(frame_form,height=50,border_width=0)
        frame_form_top.pack(side="top",fill=tk.X,pady=5,padx=10)
        title = ctk.CTkLabel(frame_form_top,text="inicio de sesion",font=('Comic Sans MS',30))
        title.pack(pady=50,expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame form fill
        frame_form_fill = ctk.CTkFrame(frame_form,height=50)
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH,pady=5,padx=10)

        label1 = ctk.CTkLabel(frame_form_fill,text="usuario",font=('Comic Sans MS',20),anchor="w")
        label1.pack(fill=tk.X,padx=20,pady=5)
        self.input1 = ctk.CTkEntry(frame_form_fill,font=('Comic Sans MS',20),height=40)
        self.input1.pack(fill=tk.X,padx=20,pady=10)
        label2 = ctk.CTkLabel(frame_form_fill,text="Contraseña",font=('Comic Sans MS',20),anchor="w")
        label2.pack(fill=tk.X,padx=20,pady=10)
        self.input2 = ctk.CTkEntry(frame_form_fill,font=('Comic Sans MS',20),height=40)
        self.input2.pack(fill=tk.X,padx=20,pady=10)
        self.input2.configure(show="*")
        self.btnShow = ctk.CTkCheckBox(frame_form_fill,text="mostrar contraseña",command=self.show,font=('Comic Sans MS',15))
        self.btnShow.place(x=280,y=210)
        # #end frame
        btn = ctk.CTkButton(frame_form_fill,height=60,font=('Comic Sans MS',20,BOLD),text="iniciar sesion",command=self.getData)
        btn.pack(fill=tk.X,padx=20,pady=50)
        self.window.mainloop()

    def getData(self):
        user = self.input1.get()
        password = self.input2.get()
        print(user)
        if user == "" or password == "":
            messagebox.showerror(title="faltan campos por rellenar",message="por favor rellene todos los campos")
        else:
            result = base_datos.consulta(f"SELECT * FROM users WHERE email = '{user}'")
            data = result.fetchall()
            print(data)
            if data:
                print(password)
                if password in data[0]:
                    self.window.destroy()
                    Application(self.image)
                else:
                    messagebox.showerror(title="contraseña invalida",message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",message="el usuario no se encuentra registrado")
    def show(self):
        if self.input2.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")

