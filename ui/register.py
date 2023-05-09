import tkinter as tk
from tkinter import messagebox
from db.database import base_datos as sql
from .application import Application
from tkinter.font import BOLD
import util.generic as utl
import customtkinter as ctk
from .partials.base import Base
from util.helpers import encryptPassword
# from ui.form import Form

class Register(Base):
    def __init__(self):
        super().__init__("registro de personal","1000x500")
        self.icon()

        utl.centrar_venta(self.window,1000,500)
        #frame logo
        logo = utl.leer_image("./image/logo.jpeg",(300,500))
        frame_logo = ctk.CTkFrame(self.window, border_width=0,width=300)
        frame_logo.pack(ipadx=10,ipady=1,side="right",expand=tk.NO,fill=tk.BOTH)
        #frame logo
        #frame form
        label1 = ctk.CTkLabel(frame_logo,image=logo,text="")
        label1.place(x=0,y=0,relwidth=1,relheight=1)
        frame_form = ctk.CTkFrame(self.window,border_width=0)
        frame_form.pack(side="left",expand=tk.YES,fill=tk.BOTH)
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

        #content

        label2 = ctk.CTkLabel(frame_form_fill,text="nombres",height=10)
        label3 = ctk.CTkLabel(frame_form_fill,text="apellidos",height=10)
        label4 = ctk.CTkLabel(frame_form_fill,text="contraseña",height=10)
        label5 = ctk.CTkLabel(frame_form_fill,text="confirmar contraseña",height=10)
        label6 = ctk.CTkLabel(frame_form_fill,text="correo electronico",height=10)
        label7 = ctk.CTkLabel(frame_form_fill,text="fecha de nacimiento",height=10)
        label8 = ctk.CTkLabel(frame_form_fill,text="cedula de identidad",height=10)
        label9 = ctk.CTkLabel(frame_form_fill,text="edad")

        self.input1 = ctk.CTkEntry(frame_form_fill)
        self.input2 = ctk.CTkEntry(frame_form_fill)
        self.input3 = ctk.CTkEntry(frame_form_fill)
        self.input3.configure(show="*")
        self.input4 = ctk.CTkEntry(frame_form_fill)
        self.input4.configure(show="*")
        self.input5 = ctk.CTkEntry(frame_form_fill)
        self.input6 = ctk.CTkEntry(frame_form_fill)
        self.input7 = ctk.CTkEntry(frame_form_fill)
        self.input8 = ctk.CTkEntry(frame_form_fill)


        label2.grid(row=0,column=0,pady=10,padx=10)
        self.input1.grid(row=1,column=0,ipady=5,ipadx=15,pady=10,padx=10)

        label3.grid(row=2,column=0)
        self.input2.grid(row=3,column=0,ipady=5,ipadx=15,pady=5,padx=10)

        label4.grid(row=4,column=0)
        self.input3.grid(row=5,column=0,ipady=5,ipadx=15,pady=10,padx=10)

        label5.grid(row=6,column=0)
        self.input4.grid(row=7,column=0,ipady=5,ipadx=15,pady=10,padx=10)

        label6.grid(row=0,column=1)
        self.input5.grid(row=1,column=1,ipady=5,ipadx=15,pady=10,padx=10)

        label7.grid(row=2,column=1)
        self.input6.grid(row=3,column=1,ipady=5,ipadx=15,pady=10,padx=10)

        label8.grid(row=4,column=1)
        self.input7.grid(row=5,column=1,ipady=5,ipadx=15,pady=10,padx=10)

        label9.grid(row=6,column=1)
        self.input8.grid(row=7,column=1,ipady=5,ipadx=15,pady=10,padx=10)

        btn = ctk.CTkButton(frame_form_fill,text="registrarse",command=self.getData)
        btn.grid(row=7,column=2)

        self.window.mainloop()



    def getData(self):
        nombres = self.input1.get()
        apellidos = self.input2.get()
        clave = self.input3.get()
        confirm = self.input4.get()
        correo = self.input5.get()
        f_nacimiento = self.input6.get()
        cedula = self.input7.get()
        edad = self.input8.get()
        edad = int(edad)
        if not nombres or not apellidos or not clave or not confirm or not correo or not f_nacimiento or not cedula or not edad:
            return messagebox.showerror("faltan campos","por favor rellene todos los campos")
        elif clave != confirm:
            return messagebox.showerror("claves no coinciden","las claves ingresadas no son iguales")

        newPassword = encryptPassword(clave)
        sql.CRUD(f'''
        INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad)
        VALUES ("{nombres}","{apellidos}","{newPassword}","{correo}","{f_nacimiento}","{cedula}",{edad})
        ''')

        self.window.destroy()
        Application()




    def show(self):
        if self.input3.cget("show") == "*" or self.input4.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")