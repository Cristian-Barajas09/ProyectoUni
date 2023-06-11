import tkinter as tk
from controller.main import FormController,RegisterController
from tkinter.font import BOLD
import util.generic as utl
import customtkinter as ctk
from .partials.base import BaseView
from tkcalendar import DateEntry
from util.generateWord import Word
#   formulario de entrada


class Form(BaseView):
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
        result = FormController().getData(user,password)
        if result:
            self.window.destroy()
            Application()


    # mostramos contraseña
    def show(self):
        if self.input2.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")


class Register(BaseView):
    def __init__(self):
        super().__init__("registro de personal", "500x500")
        self.icon()

        utl.centrar_venta(self.window, 500, 500)

        frame = ctk.CTkFrame(self.window)
        frame.place(relx=0.04, rely=0.2, relwidth=0.92, relheight=0.6)
        #nombre
        self.input1 = ctk.CTkEntry(
            frame, placeholder_text="Nombre Completo", border_width=0)
        self.input1.place(relx=0.3, rely=0.04, relwidth=0.4, relheight=0.15)
        # correo
        self.input2 = ctk.CTkEntry(
            frame, placeholder_text="Correo Electronico", border_width=0)
        self.input2.place(relx=0.01, rely=0.3, relwidth=0.4, relheight=0.15)
        #fecha de nacimento
        self.inputCalendar = DateEntry(
            frame, textvariable="fecha de nacimiento", background="black", foreground="white", state="readonly")
        self.inputCalendar.place(
            relx=0.55, rely=0.3, relwidth=0.4, relheight=0.15)
        # cedula
        self.input4 = ctk.CTkEntry(
            frame, placeholder_text="C.I", border_width=0)
        self.input4.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.15)
        # sexo
        self.input5 = ctk.CTkEntry(
            frame, placeholder_text="sexo", border_width=0)
        self.input5.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.15)
        # clave
        self.input6 = ctk.CTkEntry(
            frame, placeholder_text="Contraseña", border_width=0)
        self.input6.place(relx=0.01, rely=0.7, relwidth=0.4, relheight=0.15)
        #confirmar clave
        self.input7 = ctk.CTkEntry(
            frame, placeholder_text="Confirmar contraseña", border_width=0)
        self.input7.place(relx=0.55, rely=0.7, relwidth=0.4, relheight=0.15)

        btn = ctk.CTkButton(self.window, text="Registrarse",
                            corner_radius=10, fg_color="gray", text_color='white', hover_color="black",cursor="",command=self.getData)
        btn.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)

        self.window.mainloop()

    def getData(self):
        datos = {}
        datos["nombre_completo"] = self.input1.get()
        datos["correo"] = self.input2.get()
        datos["f_nacimiento"] = self.inputCalendar.get_date()
        datos["cedula"] = self.input4.get()
        datos["sexo"] = self.input5.get()
        datos["clave"] = self.input6.get()
        datos["confirm"] = self.input7.get()
        RegisterController().getData(
            **datos
        )


    def volver(self):
        self.window.destroy()
        Form()

    def show(self):
        if self.input3.cget("show") == "*" or self.input4.cget("show") == "*":
            self.input2.configure(show="")
        else:
            self.input2.configure(show="*")

# FRANK AND JHONDEIVI


class Inscripciones(BaseView):
    def __init__(self) -> None:
        super().__init__("Inscripciones", "800x800")
        self.icon()
        self.generarWord()
        btnBack = ctk.CTkButton(
            self.window, text="volver", command=self.volver)
        btnBack.pack()
        self.window.mainloop()

    def volver(self):
        self.window.destroy()
        Application()

    def generarWord(self):
        elemento = Word("test.docx")
        elemento.write("prueba desde python")
        elemento.save()

###         OMAR           ###


class Control(BaseView):
    def __init__(self):
        super().__init__("Control de Personal", "673x500")
        self.icon()

        self.imageSearch = utl.leer_image('./image/lupa-blanca.png', (36, 26))

        # frames
        self.frame1 = ctk.CTkFrame(self.window, width=263, height=500)
        self.frame1.place(x=0, y=0)

        self.frame2 = ctk.CTkFrame(self.window, width=260, height=40)
        self.frame2.place(x=340, y=10)

        self.frame3 = ctk.CTkFrame(self.window, width=378, height=420)
        self.frame3.place(x=283, y=60)
        # frame 1
        valores = ["profesores", "estudiantes"]
        comandos = ()
        self.select = ctk.CTkOptionMenu(
            self.frame1, values=valores, command=comandos)
        self.select.place(x=0, y=10)
        btnBack = ctk.CTkButton(
            self.frame1, text="volver", command=self.volver)
        btnBack.place(x=0, y=450)
        # frame 2

        self.search = ctk.CTkEntry(self.frame2, width=260, height=40,
                                   placeholder_text="Buscar", font=('Comic Sans MS', 16, BOLD))
        self.search.place(x=0, y=0)
        self.btnSearch = ctk.CTkButton(self.frame2, width=36, height=26, text="", image=self.imageSearch,
                                       bg_color="#2A2929", fg_color="#2A2929", hover_color="#222222", command=self.search_user)
        self.btnSearch.place(x=200, y=3)

        # frame 3
        self.get_user()
        # ciclo
        self.window.mainloop()

    # consulta a la base de datos
    def get_user(self):
        datos = self.sql.consulta(
            "SELECT primer_nombre,primer_apellido FROM users")
        datos = datos.fetchall()
        y = 0
        for elemento in datos:
            self.label1 = ctk.CTkLabel(
                self.frame3, text=f"{elemento['primer_nombre']} {elemento['primer_apellido']}")
            self.label1.place(x=10, y=y)
            y += 20

    def search_user(self):
        search = self.search.get().capitalize()
        result = self.sql.consulta(
            f'SELECT primer_nombre,primer_apellido FROM users WHERE primer_nombre LIKE "{search}%"')
        result = result.fetchall()
        y = 0
        if result != ():
            self.windowDatos = ctk.CTkToplevel()
            self.windowDatos.title = "datos encontrados"
            for elemento in result:
                self.label2 = ctk.CTkLabel(
                    self.windowDatos, text=f"{elemento['primer_nombre']} {elemento['primer_apellido']}")
                self.label2.place(x=10, y=y)
                y += 20
            self.windowDatos.mainloop()

    def volver(self):
        self.window.destroy()
        Application()


class Application(BaseView):
    def __init__(self):
        super().__init__("C.E.I Josefina Molina de Duque", "600x300")
        self.icon()

        frame_1 = ctk.CTkFrame(self.window, width=200, height=300)
        frame_1.pack(side="left")
        label_1 = ctk.CTkLabel(frame_1, text="Inicio")
        label_1.place(x=20, y=20)
        btn_1 = ctk.CTkButton(
            master=frame_1, text="incripciones", command=self.inscripciones)
        btn_1.place(x=20, y=50)
        btn_2 = ctk.CTkButton(
            master=frame_1, text="Control de personal", command=self.personal)
        btn_2.place(x=20, y=100)

        self.window.mainloop()

    def inscripciones(self):
        self.window.destroy()
        Inscripciones()

    def personal(self):
        self.window.destroy()
        Control()
