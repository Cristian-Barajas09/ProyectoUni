from controller.FormController import FormController
from partials.view.baseView import BaseView
from .main import App
from util.generic import get_font
from tkcalendar import DateEntry
import os

class Signin(BaseView):
    def __init__(self):
        super().__init__('ingresar',"700x500",FormController)

        self.icon()
        self.resizable(0,0)

        self.window.configure(background="#fff")

        img = self.image(os.path.join(self.carpeta_imagenes,'logo.jpeg'),(400,500))

        labelImage = self.tk.Label(self.window,image=img,bg="#333")
        labelImage.place(relx=0,rely=0,relwidth=0.5,relheight=1)

        frameForm = self.tk.Frame(self.window,bg="#222")
        frameForm.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)

        frameImage = self.tk.Frame(self.window,bg="#757575")
        frameImage.place(relx=0,rely=0,relwidth=0.5,relheight=1)

        img = self.tk.PhotoImage(file="/ui/assets/logo.png")
        insert = self.tk.Label(frameImage,image=img)
        insert.place(x=0,y=0)

        # label signin
        labelSignin = self.tk.Label(frameForm,text='Iniciar sesion',bg="#222",fg="#fff",font=get_font(15))
        labelSignin.place(x=100,y=50,width=130)

        #Email
        labelEmail = self.tk.Label(frameForm,text='ingrese su email',fg="#fff",bg="#222")
        labelEmail.place(x=50,y=120,width=130)

        inputEmail = self.tk.Entry(frameForm,bg="#222",fg="#fff",border=0)
        inputEmail.place(x=50,y=150,width=250,height=25)
        self.tk.Frame(frameForm,bg="#fff").place(x=50,y=175,width=250,height=2)

        # Password
        labelPassword = self.tk.Label(frameForm,text='ingrese su contraseña',fg="#fff",bg="#222")
        labelPassword.place(x=50,y=190,width=130)


        inputPassword = self.tk.Entry(frameForm,show="*",bg="#222",border=0,fg="#fff")
        inputPassword.place(x=50,y=220,width=250,height=25)
        self.tk.Frame(frameForm,bg="#fff").place(x=50,y=245,width=250,height=2)

        #btn show password

        btnShow = self.tk.Button(
            frameForm,text='Mostrar contraseña',command=lambda: self.show(inputPassword),cursor="hand2",border=0,background="#38B1EE",fg="#fff")
        btnShow.place(x=50,y=250,width=120,height=20)

        # button

        btnSignin = self.tk.Button(frameForm,text='Iniciar sesion',cursor="hand2",border=0,background="#38B1EE",fg="#fff",command=lambda: self.verificarUsuario(inputEmail,inputPassword))
        btnSignin.place(x=40,y=300,width=260,height=40)

        btnSignup = self.tk.Button(frameForm,text='Registrarse',cursor='hand2',border=0,background="#38B1EE",fg="#fff",command=self.signup)
        btnSignup.place(x=200,y=450,width=100,height=30)









    def show(self,input):
        if input.cget("show") == "*":
            input.configure(show="")
        else:
            input.configure(show="*")


    def verificarUsuario(self,email,password):
        user = email.get()
        password = password.get()
        result = self._controller.getData(user=user,password=password)
        if result:
            self.window.destroy()
            App()

    def signup(self):
        self.window.destroy()
        Form()


class Form(BaseView):
    def __init__(self):
        super().__init__(title="Registrarse",geometry="700x500",controller=FormController)
        self.resizable(0,0)
        self.window.configure(bg="#333")

        self.icon()
        self.main()

        self.window.mainloop()

    def main(self):



        # registro

        self.registrar()



    def show(self,input):
        if input.cget("show") == "*":
            input.configure(show="")
        else:
            input.configure(show="*")


    def registrarUsuario(self,nombres,apellidos,correo,f_nacimiento,cedula,sexo,clave,confirm):
        dicc = {
            "nombres": nombres.get(),
            "apellidos": apellidos.get(),
            "correo":correo.get(),
            "f_nacimiento":f_nacimiento.get_date(),
            "cedula":cedula.get(),
            "sexo":sexo.get(),
            "clave":clave.get(),
            "confirm":confirm.get()
        }
        result = self._controller.registerData(**dicc)


        if result:
            self.window.destroy()
            App()


    def registrar(self):

        # title
        frameTitle = self.tk.Frame(self.window,bg="#222")
        frameTitle.place(relx=0.25,rely=0.01,relwidth=0.5,relheight=0.1)

        labelTitle = self.tk.Label(frameTitle,bg="#222",fg="#fff",text='Registrar usuario',font=get_font(20))
        labelTitle.pack()



        frame = self.tk.Frame(self.window,bg="#222")
        frame.place(relx=0.2,rely=0.15,relwidth=0.6,relheight=0.7)

        labelNames = self.tk.Label(frame,text="Nombres").place(relx=0.01,rely=0.01)
        inputNames = self.tk.Entry(frame)
        inputNames.place(relx=0.01,rely=0.1)

        labelLastname = self.tk.Label(frame,text="Apellidos").place(relx=0.5,rely=0.01)
        inputLastName = self.tk.Entry(frame)
        inputLastName.pack()

        labelEmail = self.tk.Label(frame,text="Correo").pack()
        inputEmail = self.tk.Entry(frame)
        inputEmail.pack()

        labelDate = self.tk.Label(frame,text="Fecha de nacimiento").pack()
        inputDate = DateEntry(frame)
        inputDate.pack()


        labelId = self.tk.Label(frame,text="Cedula de identidad").pack()
        inputId = self.tk.Entry(frame)
        inputId.pack()


        labelGender = self.tk.Label(frame,text="Genero").pack()
        inputGender = self.ttk.Combobox(frame,values=('M','F'),state="readonly")
        inputGender.current(0)
        inputGender.pack()

        labelPassword = self.tk.Label(frame,text="Contraseña").pack()
        inputPassword = self.tk.Entry(frame)
        inputPassword.pack()

        labelConfirmPassword = self.tk.Label(frame,text="Confirmar Contraseña").pack()

        inputConfirmPassword = self.tk.Entry(frame)
        inputConfirmPassword.pack()

        btnSignup = self.tk.Button(frame)
        btnSignup.pack()

        btnSignin = self.tk.Button(self.window,text="iniciar sesion",command=self.signin)
        btnSignin.place(relx=0.8,rely=0.7,relwidth=0.1,relheight=0.01)


    def signin(self):
        self.window.destroy()
        Signin()





