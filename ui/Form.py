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

        frame1 = self.tk.Frame(self.window,width=500,height=500,bg="#222")
        frame1.place(relx=0,rely=0)

        self.frame2 = self.tk.Frame(self.window,width=500,height=500)
        self.frame2.place(relx=0,rely=0,relwidth=1,relheight=1)

        notebook.add(frame1,text="iniciar sesion")
        notebook.add(self.frame2,text="registrarse")



        notebook.bind("<<NotebookTabChanged>>",lambda evt: self.cambiar_nombre_pestanha(notebook,evt))

        # frame3 = self.ttk.Frame(frame1)
        # frame3.pack(side="left")
        # frame4 = self.ttk.Frame(frame1)
        # frame4.pack(side="right")

        labelFrame1 = self.tk.LabelFrame(frame1,text="Correo",background="#222",fg="#fff",border=0)
        labelFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.09)
        labelFrame2 = self.tk.LabelFrame(frame1,text="Contraseña",background="#222",fg="#fff",border=0)
        labelFrame2.place(relx=0.25,rely=0.2,relwidth=0.5,relheight=0.15)


        self.input1 = self.tk.Entry(labelFrame1,border=0)
        self.input2 = self.tk.Entry(labelFrame2,show="*",border=0)
        btnShow = self.tk.Checkbutton(labelFrame2,background='#222',fg='#fff',text="mostrar contraseña",command=lambda:self.show(self.input2))


        btn = self.tk.Button(frame1,text="iniciar sesion",command=self.verificarUsuario,border=0,background="#041d9b",foreground="#fff")
        self.input1.place(relwidth=1,relheight=0.80)
        self.input2.place(relwidth=1,relheight=0.50)
        btnShow.place(rely=0.5)
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
        frame = self.tk.Frame(self.frame2,bg="#222")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        

        #nombres
        label3 = self.tk.LabelFrame(frame,text="Nombres",bg="#222",fg="#fff",border=0)
        label3.place(relx=0.01,rely=0.10,relwidth=0.5,relheight=0.09)
        #Apellidos
        label4 = self.tk.LabelFrame(frame,text="Apellidos",bg="#222",fg="#fff",border=0)
        label4.place(relx=0.52,rely=0.10,relwidth=0.5,relheight=0.09)
        #correo
        label5 = self.tk.LabelFrame(frame,text="Correo",bg="#222",fg="#fff",border=0)
        label5.place(relx=0.01,rely=0.25,relwidth=0.5,relheight=0.09)
        #f_nacimiento
        label6 = self.tk.LabelFrame(frame,text="Fecha de nacimiento",bg="#222",fg="#fff",border=0)
        label6.place(relx=0.52,rely=0.25,relwidth=0.5,relheight=0.09)
        #cedula
        label7 = self.tk.LabelFrame(frame,text="Cedula",bg="#222",fg="#fff",border=0)
        label7.place(relx=0.01,rely=0.40,relwidth=0.5,relheight=0.09)
        #sexo
        label8 = self.tk.LabelFrame(frame,text="Sexo",bg="#222",fg="#fff",border=0)
        label8.place(relx=0.52,rely=0.40,relwidth=0.5,relheight=0.09)
        #contraseña
        label9 = self.tk.LabelFrame(frame,text="Contraseña",bg="#222",fg="#fff",border=0)
        label9.place(relx=0.01,rely=0.55,relwidth=0.5,relheight=0.15)
        #confirmar
        label10 = self.tk.LabelFrame(frame,text="Confirmar Contraseña",bg="#222",fg="#fff",border=0)
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
        btn1 = self.tk.Checkbutton(label9,text="mostrar contraseña",command=lambda: self.show(self.input7),bg="#222",fg="#fff")
        btn1.place(relx=0,rely=0.5)


        #confirmar clave
        self.input8 = self.tk.Entry(
            label10,show="*")
        self.input8.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        btn1 = self.tk.Checkbutton(label10,text="mostrar contraseña",command=lambda: self.show(self.input8),bg='#222',fg='#fff')
        btn1.place(relx=0,rely=0.5)

        btn3 = self.tk.Button(frame, text="Registrarse",command=self.registrarUsuario)
        btn3.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)