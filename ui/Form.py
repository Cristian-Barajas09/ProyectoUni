import tkinter
from partials.base import BaseView
from tkcalendar import DateEntry
from controller.main import Controller
from .main import App
class Form(BaseView):
    def __init__(self):
        super().__init__(title="Ingresar",geometry="500x500",controller=Controller)
        self.resizable(0,0)

        self.main()

        self.window.mainloop()

    def main(self):


        notebook = self.ttk.Notebook(self.window,width=500,height=500)

        frame1 = self.ttk.Frame(self.window,width=500,height=500)
        frame1.place(relx=0,rely=0)

        self.frame2 = self.ttk.Frame(self.window,width=500,height=500)
        self.frame2.place(relx=0,rely=0,relwidth=1,relheight=1)

        notebook.add(frame1,text="iniciar sesion")
        notebook.add(self.frame2,text="registrarse")



        notebook.bind("<<NotebookTabChanged>>",lambda evt: self.cambiar_nombre_pestanha(notebook,evt))

        # frame3 = self.ttk.Frame(frame1)
        # frame3.pack(side="left")
        # frame4 = self.ttk.Frame(frame1)
        # frame4.pack(side="right")

        labelFrame1 = self.ttk.LabelFrame(frame1,text="Correo")
        labelFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.09)
        labelFrame2 = self.ttk.LabelFrame(frame1,text="Contraseña")
        labelFrame2.place(relx=0.25,rely=0.2,relwidth=0.5,relheight=0.1)


        self.input1 = self.ttk.Entry(labelFrame1)
        self.input2 = self.ttk.Entry(labelFrame2,show="*")
        btnShow = self.ttk.Checkbutton(labelFrame2,text="mostrar contraseña",command=lambda:self.show(self.input2))


        btn = self.tk.Button(frame1,text="iniciar sesion",command=self.verificarUsuario)
        self.input1.place(relwidth=1,relheight=0.80)
        self.input2.place(relwidth=1,relheight=0.80)
        btnShow.pack()
        btn.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.10)

        # registro

        self.registrar()


        notebook.pack(expand=True)

    def show(self,input):
        if input.cget("show") == "*":
            input.configure(show="")
        else:
            input.configure(show="*")


    def registrarUsuario(self):
        dicc = {
            "nombres": self.input3.get(),
            "apellidos": self.inputApellidos.get(),
            "correo":self.input4.get(),
            "f_nacimiento":self.inputCalendar.get_date(),
            "cedula":self.input5.get(),
            "sexo":self.input6.get(),
            "clave":self.input7.get(),
            "confirm":self.input8.get()
        }
        result = self._controller.registerData(**dicc)


        if result:
            self.window.destroy()
            self.main()

    def verificarUsuario(self):
        user = self.input1.get()
        password = self.input2.get()
        result = self._controller.getData(user=user,password=password)
        if result:
            self.window.destroy()
            App()

    def cambiar_nombre_pestanha(self,notebook ,event):
            if notebook.tab(notebook.select(),'text') == "iniciar sesion":
                self.window.wm_title("iniciar sesion")
            else:
                self.window.wm_title("registrarse")
    def registrar(self):
        frame = self.tk.Frame(self.frame2,bg="#041D9B")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        #nombres
        label3 = self.ttk.LabelFrame(frame,text="Nombres",)
        label3.place(relx=0.01,rely=0.10,relwidth=0.5,relheight=0.09)
        #Apellidos
        label4 = self.ttk.LabelFrame(frame,text="Apellidos")
        label4.place(relx=0.52,rely=0.10,relwidth=0.5,relheight=0.09)
        #correo
        label5 = self.ttk.LabelFrame(frame,text="Correo")
        label5.place(relx=0.01,rely=0.25,relwidth=0.5,relheight=0.09)
        #f_nacimiento
        label6 = self.ttk.LabelFrame(frame,text="Fecha de nacimiento")
        label6.place(relx=0.52,rely=0.25,relwidth=0.5,relheight=0.09)
        #cedula
        label7 = self.ttk.LabelFrame(frame,text="Cedula")
        label7.place(relx=0.01,rely=0.40,relwidth=0.5,relheight=0.09)
        #sexo
        label8 = self.ttk.LabelFrame(frame,text="Sexo")
        label8.place(relx=0.52,rely=0.40,relwidth=0.5,relheight=0.09)
        #contraseña
        label9 = self.ttk.LabelFrame(frame,text="Contraseña")
        label9.place(relx=0.01,rely=0.55,relwidth=0.5,relheight=0.15)
        #confirmar
        label10 = self.ttk.LabelFrame(frame,text="Confirmar Contraseña")
        label10.place(relx=0.52,rely=0.55,relwidth=0.5,relheight=0.15)

        self.input3 = self.tk.Entry(
            label3,)
        self.input3.place(relx=0, rely=0, relwidth=1, relheight=1)

        #apellidos
        self.inputApellidos = self.tk.Entry(
            label4
        )
        self.inputApellidos.place(relx=0,rely=0,relheight=1,relwidth=1)
        # correo
        self.input4 = self.tk.Entry(
            label5, )
        self.input4.place(relx=0, rely=0, relwidth=1, relheight=1)
        #fecha de nacimento
        self.inputCalendar = DateEntry(
            label6, textvariable="fecha de nacimiento", background="black", foreground="white", state="readonly")
        self.inputCalendar.place(
            relx=0.1, rely=0, relwidth=0.8, relheight=1)
        # cedula
        self.input5 = self.tk.Entry(
            label7)
        self.input5.place(relx=0, rely=0, relwidth=1, relheight=1)
        # sexo
        self.input6 = self.ttk.Combobox(
            label8,
            values=("M","F"),
            state="readonly")
        self.input6.place(relx=0.1, rely=0, relwidth=0.8, relheight=1)
        # clave
        self.input7 = self.tk.Entry(
            label9, show="*" )
        self.input7.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        btn1 = self.ttk.Checkbutton(label9,text="mostrar contraseña",command=lambda: self.show(self.input7))
        btn1.place(relx=0,rely=0.5)


        #confirmar clave
        self.input8 = self.tk.Entry(
            label10,show="*")
        self.input8.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        btn1 = self.ttk.Checkbutton(label10,text="mostrar contraseña",command=lambda: self.show(self.input8))
        btn1.place(relx=0,rely=0.5)

        btn3 = self.tk.Button(frame, text="Registrarse",command=self.registrarUsuario)
        btn3.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)