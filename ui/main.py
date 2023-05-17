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
        logo = self.add_image("./image/logo.jpeg", (300, 500))
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
            print(data)
            if data:
                savedPassword = data["password"]
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
        label_img = ctk.CTkLabel(frame_logo, image=logo, text="")
        label_img.place(x=0, y=0, relwidth=1, relheight=1)
        frame_form = ctk.CTkFrame(self.window, border_width=0)
        frame_form.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        # frame form
        # frame form top
        frame_form_top = ctk.CTkFrame(frame_form, height=50, border_width=0)
        frame_form_top.pack(side="top", fill=tk.X, pady=5, padx=10)
        title = ctk.CTkLabel(
            frame_form_top, text="Registro de personal", font=('Comic Sans MS', 30))
        title.pack(pady=50, expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame form fill
        frame_form_fill = ctk.CTkFrame(frame_form, height=50)
        frame_form_fill.pack(side="bottom", expand=tk.YES,fill=tk.BOTH, pady=5, padx=10)

        # content
        label1 = ctk.CTkLabel(frame_form_fill, text="primer nombre", height=10)
        label2 = ctk.CTkLabel(frame_form_fill, text="segundo nombre", height=10)
        label3 = ctk.CTkLabel(frame_form_fill, text="primer apellido", height=10)
        label4 = ctk.CTkLabel(
            frame_form_fill, text="segundo nombre", height=10)
        label5 = ctk.CTkLabel(
            frame_form_fill, text="clave", height=10)
        label6 = ctk.CTkLabel(
            frame_form_fill, text="confirmar clave", height=10)
        label7 = ctk.CTkLabel(
            frame_form_fill, text="correo electronico", height=10)
        label8 = ctk.CTkLabel(frame_form_fill, text="fecha de nacimiento")
        label9 = ctk.CTkLabel(frame_form_fill, text="cedula de identidad")
        label10 = ctk.CTkLabel(frame_form_fill,text="edad")
        label11 = ctk.CTkLabel(frame_form_fill,text="numero de telefono")
        #nombre 1
        self.input1 = ctk.CTkEntry(frame_form_fill)
        #nombre 2
        self.input2 = ctk.CTkEntry(frame_form_fill)
        # apellido 1
        self.input3 = ctk.CTkEntry(frame_form_fill)
        # apellido 2
        self.input4 = ctk.CTkEntry(frame_form_fill)
        # clave
        self.input5 = ctk.CTkEntry(frame_form_fill)
        # confirmar clave
        self.input6 = ctk.CTkEntry(frame_form_fill)
        # correo
        self.input7 = ctk.CTkEntry(frame_form_fill)
        # fecha de nacimiento
        self.input8 = DateEntry(frame_form_fill, width=16, background="black",
                                foreground="white", bd=2, state="readonly",)
        # cedula
        self.input9 = ctk.CTkEntry(frame_form_fill)
        # edad
        self.input10 = ctk.CTkEntry(frame_form_fill)
        # n_telefono
        self.input11 = ctk.CTkEntry(frame_form_fill)
        # nombre 1
        label1.grid(row=0,column=0,pady=5,padx=5)
        self.input1.grid(row=1,column=0,pady=5,padx=5)
        # nombre 2
        label2.grid(row=2,column=0,pady=5,padx=5)
        self.input2.grid(row=3,column=0,pady=5,padx=5)
        # apellido 1
        label3.grid(row=4,column=0,pady=5,padx=5)
        self.input3.grid(row=5,column=0,pady=5,padx=5)
        # apellido 2
        label4.grid(row=6,column=0,pady=5,padx=5)
        self.input4.grid(row=7,column=0,pady=5,padx=5)
        # clave
        label5.grid(row=0,column=1,pady=5,padx=5)
        self.input5.grid(row=1,column=1,pady=5,padx=5)

        #confirmar clave
        label6.grid(row=2,column=1,pady=5,padx=5)
        self.input6.grid(row=3,column=1,pady=5,padx=5)

        # correo
        label7.grid(row=4,column=1,pady=5,padx=5)
        self.input7.grid(row=5,column=1,pady=5,padx=5)

        # f_nacimiento
        label8.grid(row=6,column=1,pady=5,padx=5)
        self.input8.grid(row=7,column=1,pady=5,padx=5)

        # cedula
        label9.grid(row=0,column=2,pady=5,padx=5)
        self.input9.grid(row=1,column=2,pady=5,padx=5)

        # edad
        label10.grid(row=2,column=2,pady=5,padx=5)
        self.input10.grid(row=3,column=2,pady=5,padx=5)

        #n_telefono
        label11.grid(row=4,column=2,pady=5,padx=5)
        self.input11.grid(row=5,column=2,pady=5,padx=5)

        btn = ctk.CTkButton(
            frame_form_fill, text="registrarse", command=self.getData)
        btn.grid(row=4,column=3,pady=5,padx=5)

        btnBack = ctk.CTkButton(frame_form_fill,text="volver",command=self.volver)
        btnBack.grid(row=5,column=3,pady=5,padx=5)




        self.window.mainloop()

    def getData(self):
        primer_nombre = self.input1.get()
        segundo_nombre = self.input2.get()
        primer_apellido = self.input3.get()
        segundo_apellido = self.input4.get()
        clave = self.input5.get()
        confirm = self.input6.get()
        correo = self.input7.get()
        f_nacimiento = self.input8.get_date()
        cedula = self.input9.get()
        edad = self.input10.get()
        n_telefono = self.input11.get()
        if (
            not primer_nombre or
            not segundo_nombre or
            not primer_apellido or
            not segundo_apellido or
            not clave or
            not confirm or
            not correo or
            not f_nacimiento or
            not cedula or
            not edad or
            not n_telefono
        ):
            return messagebox.showerror("faltan campos", "por favor rellene todos los campos")
        elif clave != confirm:
            return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")
        elif not edad.isdigit():
            return messagebox.showerror("error", "edad debe ser un numero")


        edad = int(edad)
        newPassword = encryptPassword(clave)
        self.sql.CRUD(f'''
        INSERT INTO users(
            primer_nombre,
            segundo_nombre,
            primer_apellido,
            segundo_apellido,
            password,
            email,
            fecha_nacimiento,
            cedula,
            edad,
            n_telefono
        ) VALUES (
            "{primer_nombre}",
            "{segundo_nombre}",
            "{primer_apellido}",
            "{segundo_apellido}",
            "{newPassword}",
            "{correo}",
            "{f_nacimiento}",
            "{cedula}",
            {edad},
            "{n_telefono}"
            );
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
        datos = self.sql.consulta("SELECT primer_nombre,primer_apellido FROM users")
        datos = datos.fetchall()
        y = 0
        for i in datos:
            self.label1 = ctk.CTkLabel(self.frame3,text=f"{i[0]} {i[1]}")
            self.label1.place(x=10,y=y)
            y += 20
    def search_user(self):
        datos = self.sql.consulta("select * from users")
        datos = datos.fetchall()
        print(datos)
        jsonData = []
        for i in datos:
            print(i)


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

