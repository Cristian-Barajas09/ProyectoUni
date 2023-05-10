import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import util.generic as utl
import customtkinter as ctk
from .partials.base import Base
from util.helpers import matchPassword
from util.helpers import encryptPassword
from tkcalendar import DateEntry
#   formulario de entrada


class Form(Base):
    def __init__(self):
        super().__init__("inicio de sesion", "800x500")
        self.resizable(0, 0)
        self.icon()

        utl.centrar_venta(self.window, 800, 500)

        # frame logo
        logo = utl.leer_image("./image/logo.jpeg", (300, 500))
        frame_logo = ctk.CTkFrame(self.window, border_width=0, width=300)
        frame_logo.pack(ipadx=10, ipady=10, side="left",
                        expand=tk.NO, fill=tk.BOTH)
        # endframe logo

        # frame form
        label1 = ctk.CTkLabel(frame_logo, image=logo, text="")
        label1.place(x=0, y=0, relwidth=1, relheight=1)
        frame_form = ctk.CTkFrame(self.window, border_width=0)
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # endframe form
        # frame form top
        frame_form_top = ctk.CTkFrame(frame_form, height=50, border_width=0)
        frame_form_top.pack(side="top", fill=tk.X, pady=5, padx=10)
        title = ctk.CTkLabel(
            frame_form_top, text="Inicio de sesion", font=('Comic Sans MS', 30))
        title.pack(pady=50, expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame form fill
        frame_form_fill = ctk.CTkFrame(frame_form, height=50)
        frame_form_fill.pack(side="bottom", expand=tk.YES,
                             fill=tk.BOTH, pady=5, padx=10)

        label1 = ctk.CTkLabel(frame_form_fill, text="Usuario", font=(
            'Comic Sans MS', 20), anchor="w")
        label1.pack(fill=tk.X, padx=20, pady=5)
        self.input1 = ctk.CTkEntry(frame_form_fill, font=(
            'Comic Sans MS', 20), height=40, placeholder_text="ejemplo@domain.com")
        self.input1.pack(fill=tk.X, padx=20, pady=10)
        label2 = ctk.CTkLabel(frame_form_fill, text="Contraseña", font=(
            'Comic Sans MS', 20), anchor="w")
        label2.pack(fill=tk.X, padx=20, pady=10)
        self.input2 = ctk.CTkEntry(
            frame_form_fill, font=('Comic Sans MS', 20), height=40)
        self.input2.pack(fill=tk.X, padx=20, pady=10)
        self.input2.configure(show="*")
        self.btnShow = ctk.CTkCheckBox(
            frame_form_fill, text="mostrar contraseña", command=self.show, font=('Comic Sans MS', 15))
        self.btnShow.place(x=280, y=210)
        self.registerBtn = ctk.CTkButton(frame_form_fill, text="registrarse", command=self.registro, font=(
            'Comic Sans MS', 20), height=5, bg_color="transparent")
        self.registerBtn.place(x=10, y=210)

        # end frame form fill

        btn = ctk.CTkButton(frame_form_fill, height=70, font=(
            'Comic Sans MS', 20, BOLD), text="iniciar sesion", command=self.getData)
        btn.pack(fill=tk.X, padx=20, pady=50)
        self.window.mainloop()

    def registro(self):
        self.window.destroy()
        Register()

    # revisamos los datos ingresados

    def getData(self):
        user = self.input1.get()
        password = self.input2.get()

        if user == "" or password == "":
            messagebox.showerror(title="faltan campos por rellenar",
                                 message="por favor rellene todos los campos")
        else:
            result = self.sql.consulta(
                f"SELECT * FROM users WHERE email = '{user.lower()}'")
            data = result.fetchall()
            if data:
                savedPassword = data[0][3]
                result = matchPassword(password, savedPassword)
                if result:
                    self.window.destroy()
                    Application()
                else:
                    messagebox.showerror(
                        title="contraseña invalida", message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",
                                     message="el usuario no se encuentra registrado")

    # mostramos contraseña
    def show(self):
        if self.input2.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")


class Register(Base):
    def __init__(self):
        super().__init__("registro de personal", "1000x500")
        self.icon()

        utl.centrar_venta(self.window, 1000, 500)
        # frame logo
        logo = self.add_image("./image/logo.jpeg", (300, 500))
        frame_logo = ctk.CTkFrame(self.window, border_width=0, width=300)
        frame_logo.pack(ipadx=10, ipady=1, side="right",
                        expand=tk.NO, fill=tk.BOTH)
        # frame logo
        # frame form
        label1 = ctk.CTkLabel(frame_logo, image=logo, text="")
        label1.place(x=0, y=0, relwidth=1, relheight=1)
        frame_form = ctk.CTkFrame(self.window, border_width=0)
        frame_form.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        # frame form
        # frame form top
        frame_form_top = ctk.CTkFrame(frame_form, height=50, border_width=0)
        frame_form_top.pack(side="top", fill=tk.X, pady=5, padx=10)
        title = ctk.CTkLabel(
            frame_form_top, text="Inicio de sesion", font=('Comic Sans MS', 30))
        title.pack(pady=50, expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame form fill
        frame_form_fill = ctk.CTkFrame(frame_form, height=50)
        frame_form_fill.pack(side="bottom", expand=tk.YES,
                             fill=tk.BOTH, pady=5, padx=10)

        # content

        label2 = ctk.CTkLabel(frame_form_fill, text="nombres", height=10)
        label3 = ctk.CTkLabel(frame_form_fill, text="apellidos", height=10)
        label4 = ctk.CTkLabel(frame_form_fill, text="contraseña", height=10)
        label5 = ctk.CTkLabel(
            frame_form_fill, text="confirmar contraseña", height=10)
        label6 = ctk.CTkLabel(
            frame_form_fill, text="correo electronico", height=10)
        label7 = ctk.CTkLabel(
            frame_form_fill, text="fecha de nacimiento", height=10)
        label8 = ctk.CTkLabel(
            frame_form_fill, text="cedula de identidad", height=10)
        label9 = ctk.CTkLabel(frame_form_fill, text="edad")

        self.input1 = ctk.CTkEntry(frame_form_fill)
        self.input2 = ctk.CTkEntry(frame_form_fill)
        self.input3 = ctk.CTkEntry(frame_form_fill)
        self.input3.configure(show="*")
        self.input4 = ctk.CTkEntry(frame_form_fill)
        self.input4.configure(show="*")
        self.input5 = ctk.CTkEntry(frame_form_fill)
        self.input6 = DateEntry(frame_form_fill, width=16, background="black",
                                foreground="white", bd=2, state="readonly",)
        self.input7 = ctk.CTkEntry(frame_form_fill)
        self.input8 = ctk.CTkEntry(frame_form_fill)

        label2.grid(row=0, column=0, pady=10, padx=10)
        self.input1.grid(row=1, column=0, ipady=5, ipadx=15, pady=10, padx=10)

        label3.grid(row=2, column=0)
        self.input2.grid(row=3, column=0, ipady=5, ipadx=15, pady=5, padx=10)

        label4.grid(row=4, column=0)
        self.input3.grid(row=5, column=0, ipady=5, ipadx=15, pady=10, padx=10)

        label5.grid(row=6, column=0)
        self.input4.grid(row=7, column=0, ipady=5, ipadx=15, pady=10, padx=10)

        label6.grid(row=0, column=1)
        self.input5.grid(row=1, column=1, ipady=5, ipadx=15, pady=10, padx=10)

        label7.grid(row=2, column=1)
        self.input6.grid(row=3, column=1, ipady=5, ipadx=15, pady=10, padx=10)

        label8.grid(row=4, column=1)
        self.input7.grid(row=5, column=1, ipady=5, ipadx=15, pady=10, padx=10)

        label9.grid(row=6, column=1)
        self.input8.grid(row=7, column=1, ipady=5, ipadx=15, pady=10, padx=10)

        btn = ctk.CTkButton(
            frame_form_fill, text="registrarse", command=self.getData)
        btn.grid(row=7, column=2)

        btnBack = ctk.CTkButton(frame_form_fill,text="volver",command=self.volver)
        btnBack.grid(row=7,column=3)

        self.window.mainloop()

    def getData(self):
        nombres = self.input1.get()
        apellidos = self.input2.get()
        clave = self.input3.get()
        confirm = self.input4.get()
        correo = self.input5.get()
        f_nacimiento = self.input6.get_date()
        cedula = self.input7.get()
        edad = self.input8.get()

        if not nombres or not apellidos or not clave or not confirm or not correo or not f_nacimiento or not cedula or not edad:
            return messagebox.showerror("faltan campos", "por favor rellene todos los campos")
        elif clave != confirm:
            return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")
        elif not edad.isdigit():
            return messagebox.showerror("error", "edad debe ser un numero")


        edad = int(edad)
        newPassword = encryptPassword(clave)
        self.sql.CRUD(f'''
        INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad)
        VALUES ("{nombres}","{apellidos}","{newPassword}","{correo.lower()}","{f_nacimiento}","{cedula}",{edad})
        ''')

        self.window.destroy()
        Application()

    def volver(self):
        self.window.destroy()
        Form()

    def show(self):
        if self.input3.cget("show") == "*" or self.input4.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")

# FRANK AND JHONDEIVI
class Inscripciones(Base):
    def __init__(self) -> None:
        super().__init__("inscripciones","800x800")
        self.icon()
        btnBack = ctk.CTkButton(self.window,text="volver",command=self.volver)
        btnBack.pack()
        self.window.mainloop()
    def volver(self):
        self.window.destroy()
        Application()


###         OMAR           ###
class Control(Base):
    def __init__(self):
        super().__init__("Control de Personal","673x500")
        self.icon()

        self.imageSearch = utl.leer_image('./image/lupa-blanca.png',(36,26))

        # frames
        self.frame1 = ctk.CTkFrame(self.window,width=263,height=500)
        self.frame1.place(x=0,y=0)

        self.frame2 = ctk.CTkFrame(self.window,width=260,height=40)
        self.frame2.place(x=340,y=10)

        self.frame3 = ctk.CTkFrame(self.window,width=378,height=420)
        self.frame3.place(x=283,y=60)
        # frame 1
        valores = ["profesores","estudiantes"]
        comandos = ()
        self.select = ctk.CTkOptionMenu(self.frame1,values=valores,command=comandos)
        self.select.place(x=0,y=10)
        btnBack = ctk.CTkButton(self.frame1,text="volver",command=self.volver)
        btnBack.place(x=0,y=450)
        # frame 2
        self.search = ctk.CTkEntry(self.frame2,width=260,height=40,placeholder_text="Buscar",font=('Comic Sans MS',16,BOLD))
        self.search.place(x=0,y=0)
        self.btnSearch = ctk.CTkButton(self.frame2,width=36,height=26,text="",image=self.imageSearch,bg_color="#2A2929",fg_color="#2A2929",hover_color="#222222",command=self.search_user)
        self.btnSearch.place(x=200,y=3)

        # frame 3
        self.get_user()
        # ciclo
        self.window.mainloop()

    #consulta a la base de datos
    def get_user(self):
        datos = self.sql.consulta("SELECT nombres,apellidos FROM users")
        datos = datos.fetchall()
        y = 0
        for i in datos:
            self.label1 = ctk.CTkLabel(self.frame3,text=f"{i[0]} {i[1]}")
            self.label1.place(x=10,y=y)
            y += 20
    def search_user(self):

        search = self.search.get()
        print(search,type(search))
        datos = self.sql.consulta("SELECT nombres,apellidos FROM users")
        datos = datos.fetchall()
        print(datos)


    def volver(self):
        self.window.destroy()
        Application()


class Application(Base):
    def __init__(self):
        super().__init__("C.E.I Josefina Molina de Duque","600x300")
        self.icon()

        frame_1 = ctk.CTkFrame(self.window,width=200,height=300)
        frame_1.pack(side="left")
        label_1 = ctk.CTkLabel(frame_1,text="Inicio")
        label_1.place(x=20,y=20)
        btn_1 = ctk.CTkButton(master=frame_1,text="incripciones",command=self.inscripciones)
        btn_1.place(x=20,y=50)
        btn_2 = ctk.CTkButton(master=frame_1,text="Control de personal",command=self.personal)
        btn_2.place(x=20,y=100)

        self.window.mainloop()
    def inscripciones(self):
        self.window.destroy()
        Inscripciones()

    def personal(self):
        self.window.destroy()
        Control()

