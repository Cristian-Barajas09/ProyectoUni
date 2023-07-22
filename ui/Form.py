import tkinter
from partials.base import BaseView
from tkcalendar import DateEntry
from controller.main import Controller
from .main import App
class Form(BaseView):
    def __init__(self):
        super().__init__(title="",geometry="",controller=Controller)

        self.main()


    def main(self):
        self.window.wm_geometry("500x500")
        self.window.wm_protocol('WM_DELETE_WINDOW',self.window.destroy)
        self.window.wm_attributes('-topmost',1)
        self.window.wm_resizable(0,0)

        notebook = self.ttk.Notebook(self.window,width=500,height=500)

        frame1 = self.ttk.Frame(self.window,width=500,height=500)
        frame1.place(relx=0,rely=0)

        self.frame2 = self.ttk.Frame(self.window,width=500,height=500)
        self.frame2.place(relx=0,rely=0)

        notebook.add(frame1,text="iniciar sesion")
        notebook.add(self.frame2,text="registrarse")



        notebook.bind("<<NotebookTabChanged>>",lambda evt: self.cambiar_nombre_pestanha(notebook,evt))

        # frame3 = self.ttk.Frame(frame1)
        # frame3.pack(side="left")
        # frame4 = self.ttk.Frame(frame1)
        # frame4.pack(side="right")

        labelFrame1 = self.ttk.LabelFrame(frame1,text="Correo")
        labelFrame1.place(relx=0.35,rely=0.2)
        labelFrame2 = self.ttk.LabelFrame(frame1,text="Contraseña")
        labelFrame2.place(relx=0.35,rely=0.3)


        self.input1 = self.ttk.Entry(labelFrame1)
        self.input2 = self.ttk.Entry(labelFrame2,show="*")
        btnShow = self.ttk.Checkbutton(labelFrame2,text="mostrar contraseña",command=lambda:self.show(self.input2))


        btn = self.ttk.Button(frame1,text="iniciar sesion",command=self.verificarUsuario)
        self.input1.pack(expand=True)
        self.input2.pack(expand=True)
        btnShow.pack()
        btn.place(relx=0.35,rely=0.5,relwidth=0.25)

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
        frame = self.ttk.Frame(self.frame2)
        frame.place(relx=0.04, rely=0.2, relwidth=0.92, relheight=1)

        #nombres
        label3 = self.ttk.LabelFrame(frame,text="Nombres")
        label3.place(relx=0.01,rely=0.01,relwidth=0.5,relheight=0.12)
        #Apellidos
        label4 = self.ttk.LabelFrame(frame,text="Apellidos")
        label4.place(relx=0.53,rely=0.01,relwidth=0.5,relheight=0.12)
        #correo
        label5 = self.ttk.LabelFrame(frame,text="Correo")
        label5.place(relx=0.01,rely=0.15,relwidth=0.5,relheight=0.12)
        #f_nacimiento
        label6 = self.ttk.LabelFrame(frame,text="Fecha de nacimiento")
        label6.place(relx=0.53,rely=0.15,relwidth=0.5,relheight=0.12)
        #cedula
        label7 = self.ttk.LabelFrame(frame,text="Cedula")
        label7.place(relx=0.01,rely=0.3,relwidth=0.5,relheight=0.12)
        #sexo
        label8 = self.ttk.LabelFrame(frame,text="Sexo")
        label8.place(relx=0.53,rely=0.3,relwidth=0.5,relheight=0.12)
        #contraseña
        label9 = self.ttk.LabelFrame(frame,text="Contraseña")
        label9.place(relx=0.01,rely=0.45,relwidth=0.5,relheight=0.15)
        #confirmar
        label10 = self.ttk.LabelFrame(frame,text="Confirmar Contraseña")
        label10.place(relx=0.53,rely=0.45,relwidth=0.5,relheight=0.15)

        self.input3 = self.ttk.Entry(
            label3,)
        self.input3.place(relx=0, rely=0, relwidth=1, relheight=1)
        #apellidos
        self.inputApellidos = self.ttk.Entry(
            label4
        )
        self.inputApellidos.place(relx=0,rely=0,relheight=1,relwidth=1)
        # correo
        self.input4 = self.ttk.Entry(
            label5, )
        self.input4.place(relx=0, rely=0, relwidth=1, relheight=1)
        #fecha de nacimento
        self.inputCalendar = DateEntry(
            label6, textvariable="fecha de nacimiento", background="black", foreground="white", state="readonly")
        self.inputCalendar.place(
            relx=0.1, rely=0, relwidth=0.8, relheight=1)
        # cedula
        self.input5 = self.ttk.Entry(
            label7)
        self.input5.place(relx=0, rely=0, relwidth=1, relheight=1)
        # sexo
        self.input6 = self.ttk.Combobox(
            label8,
            values=("M","F"),
            state="readonly")
        self.input6.place(relx=0.1, rely=0, relwidth=0.8, relheight=1)
        # clave
        self.input7 = self.ttk.Entry(
            label9, show="*" )
        self.input7.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        btn1 = self.ttk.Checkbutton(label9,text="mostrar contraseña",command=lambda: self.show(self.input7))
        btn1.place(relx=0,rely=0.5)


        #confirmar clave
        self.input8 = self.ttk.Entry(
            label10,show="*")
        self.input8.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        btn1 = self.ttk.Checkbutton(label10,text="mostrar contraseña",command=lambda: self.show(self.input8))
        btn1.place(relx=0,rely=0.5)

        btn3 = self.ttk.Button(frame, text="Registrarse",command=self.registrarUsuario)
        btn3.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)