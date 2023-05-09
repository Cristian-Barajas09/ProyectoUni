import tkinter as tk
from tkinter import messagebox
from db.database import base_datos
from .application import Application
from tkinter.font import BOLD
import util.generic as utl
import customtkinter as ctk
from .partials.base import Base
from ui.register import Register
from util.helpers import matchPassword
import bcrypt
#   formulario de entrada



class Form(Base):
    def __init__(self):
        super().__init__("inicio de sesion","800x500")
        self.resizable(0,0)
        self.icon()

        utl.centrar_venta(self.window,800,500)
        #frame logo
        logo = utl.leer_image("./image/logo.jpeg",(300,500))
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
        title = ctk.CTkLabel(frame_form_top,text="Inicio de sesion",font=('Comic Sans MS',30))
        title.pack(pady=50,expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame form fill
        frame_form_fill = ctk.CTkFrame(frame_form,height=50)
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH,pady=5,padx=10)

        label1 = ctk.CTkLabel(frame_form_fill,text="Usuario",font=('Comic Sans MS',20),anchor="w")
        label1.pack(fill=tk.X,padx=20,pady=5)
        self.input1 = ctk.CTkEntry(frame_form_fill,font=('Comic Sans MS',20),height=40,placeholder_text="ejemplo@domain.com")
        self.input1.pack(fill=tk.X,padx=20,pady=10)
        label2 = ctk.CTkLabel(frame_form_fill,text="Contraseña",font=('Comic Sans MS',20),anchor="w")
        label2.pack(fill=tk.X,padx=20,pady=10)
        self.input2 = ctk.CTkEntry(frame_form_fill,font=('Comic Sans MS',20),height=40)
        self.input2.pack(fill=tk.X,padx=20,pady=10)
        self.input2.configure(show="*")
        self.btnShow = ctk.CTkCheckBox(frame_form_fill,text="mostrar contraseña",command=self.show,font=('Comic Sans MS',15))
        self.btnShow.place(x=280,y=210)
        self.registerBtn = ctk.CTkButton(frame_form_fill,text="registrarse",command=self.registro,font=('Comic Sans MS',20),height=5 ,bg_color="transparent")
        self.registerBtn.place(x=10,y=210)
        # #end frame
        btn = ctk.CTkButton(frame_form_fill,height=70,font=('Comic Sans MS',20,BOLD),text="iniciar sesion",command=self.getData)
        btn.pack(fill=tk.X,padx=20,pady=50)
        self.window.mainloop()

    def registro(self):
        self.window.destroy()
        Register()

    def getData(self):
        user = self.input1.get()
        password = self.input2.get()
        if user == "" or password == "":
            messagebox.showerror(title="faltan campos por rellenar",message="por favor rellene todos los campos")
        else:
            result = base_datos.consulta(f"SELECT * FROM users WHERE email = '{user.lower()}'")
            data = result.fetchall()
            if data:
                savedPassword = data[0][3]
                print(type(savedPassword))
                # result = matchPassword(password,savedPassword)
                # print(result)
                # if password in data[0]:
                #     self.window.destroy()
                #     Application()
                # else:
                #     messagebox.showerror(title="contraseña invalida",message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",message="el usuario no se encuentra registrado")
    def show(self):
        if self.input2.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")

