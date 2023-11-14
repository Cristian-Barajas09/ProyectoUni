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



        frameImage = self.tk.Frame(self.window,bg="#757575")
        frameImage.place(relx=0,rely=0,relwidth=0.5,relheight=1)


        img = self.image(os.path.join(self.carpeta_imagenes,'Logo_Josefina_Redondo.png'),(300,500))

        labelImage = self.tk.Label(frameImage,image=img,bg="#333")

        labelImage.place(relx=0,rely=0,relwidth=1,relheight=1)

        frameForm = self.tk.Frame(self.window,bg="#222")
        frameForm.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)




        # label signin
        labelSignin = self.tk.Label(frameForm,text='Iniciar sesion',bg="#222",fg="#fff",font=get_font(15))
        labelSignin.place(x=100,y=50,width=130)

        #Email
        labelEmail = self.tk.Label(frameForm,text='Ingrese su email',fg="#fff",bg="#222")
        labelEmail.place(x=50,y=120,width=130)

        inputEmail = self.tk.Entry(frameForm,bg="#222",fg="#fff",border=0)
        inputEmail.place(x=50,y=150,width=250,height=25)
        self.tk.Frame(frameForm,bg="#fff").place(x=50,y=175,width=250,height=2)

        # Password
        labelPassword = self.tk.Label(frameForm,text='Ingrese su contraseña',fg="#fff",bg="#222")
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


        self.window.mainloop()


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
            App(result)

    def signup(self):
        self.window.destroy()
        Form()


class Form(BaseView):
    def __init__(self):
        super().__init__(title="Registrarse",geometry="700x450",controller=FormController)
        # self.resizable(0,0)
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






    def registrar(self):
        # frames

        frameImage = self.tk.Frame(self.window,bg="#757575")
        frameImage.place(x=400,y=0,width=300,height=450)

        img = self.image(os.path.join(self.carpeta_imagenes,'Logo_Josefina_Redondo.png'),(300,500))

        labelImage = self.tk.Label(frameImage,image=img,bg="#333")
        labelImage.place(x=0,y=0,width=300,height=450)

        frameContent = self.tk.Frame(self.window,bg="#222")
        frameContent.place(x=0,y=0,width=400,height=450)

        # titulo de frameContent
        titulo = self.tk.Label(frameContent,text="Registrarse",bg="#222",fg="#fff",font=get_font(15))
        titulo.place(x=130,y=50,width=130)

        # datos del usuario


        labelName = self.tk.Label(frameContent,text="Nombres",bg="#222",fg="#fff")
        labelName.place(x=20,y=100,width=150)

        inputName = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0)
        inputName.place(x=20,y=120,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=20,y=145,width=150,height=2)


        labelLastname = self.tk.Label(frameContent,text="Apellidos",bg="#222",fg="#fff")
        labelLastname.place(x=220,y=100,width=150)

        inputLastname = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0)
        inputLastname.place(x=220,y=120,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=220,y=145,width=150,height=2)

        labelEmail = self.tk.Label(frameContent,text="Correo",bg="#222",fg="#fff")
        labelEmail.place(x=20,y=160,width=150)
        inputEmail = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0)
        inputEmail.place(x=20,y=180,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=20,y=205,width=150,height=2)

        labelDate = self.tk.Label(frameContent,text="Fecha de nacimiento",bg="#222",fg="#fff")
        labelDate.place(x=220,y=160,width=150)
        inputDate = DateEntry(frameContent,bg="#222",fg="#fff",border=0)
        inputDate.place(x=220,y=180,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=220,y=205,width=150,height=2)

        labelCedula = self.tk.Label(frameContent,text="Cedula",bg="#222",fg="#fff")
        labelCedula.place(x=20,y=220,width=150)
        inputCedula = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0)
        inputCedula.place(x=20,y=240,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=20,y=265,width=150,height=2)

        labelSexo = self.tk.Label(frameContent,text="Sexo",bg="#222",fg="#fff")
        labelSexo.place(x=220,y=220,width=150)
        inputSexo = self.ttk.Combobox(frameContent,values=["Masculino","Femenino"],state="readonly")
        inputSexo.current(0)
        inputSexo.place(x=220,y=240,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=220,y=265,width=150,height=2)


        labelClave = self.tk.Label(frameContent,text="Contraseña",bg="#222",fg="#fff")
        labelClave.place(x=20,y=280,width=150)

        inputClave = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0,show="*")
        inputClave.place(x=20,y=300,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=20,y=325,width=150,height=2)

        labelConfirm = self.tk.Label(frameContent,text="Confirmar contraseña",bg="#222",fg="#fff")
        labelConfirm.place(x=220,y=280,width=150)

        inputConfirm = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0,show="*")
        inputConfirm.place(x=220,y=300,width=150,height=25)

        self.tk.Frame(bg="#fff").place(x=220,y=325,width=150,height=2)

        labelTelefono = self.tk.Label(frameContent,text="Telefono",bg="#222",fg="#fff")
        labelTelefono.place(x=20,y=340,width=150)

        inputTelefono = self.tk.Entry(frameContent,bg="#222",fg="#fff",border=0)
        inputTelefono.place(x=20,y=360,width=150,height=25)
        self.tk.Frame(bg="#fff").place(x=20,y=385,width=150,height=2)

        # button
        btnSigup = self.tk.Button(frameContent,text='Registrarse',cursor="hand2",border=0,background="#38B1EE",fg="#fff",command=lambda: self.registrarUsuario(inputName,inputLastname,inputEmail,inputDate,inputCedula,inputSexo,inputClave,inputConfirm,inputTelefono))
        btnSigup.place(x=200,y=400,width=150,height=40)

        btnSignin = self.tk.Button(frameContent,text='Iniciar sesion',cursor="hand2",border=0,background="#38B1EE",fg="#fff",command=self.signin)
        btnSignin.place(x=40,y=400,width=150,height=40)




    def signin(self):
        self.window.destroy()
        Signin()


    def registrarUsuario(self,nombres,apellidos,correo,f_nacimiento,cedula,sexo,clave,confirm,telefono):
        dicc = {
            "nombres": nombres.get(),
            "apellidos": apellidos.get(),
            "correo":correo.get(),
            "f_nacimiento":f_nacimiento.get_date(),
            "cedula":cedula.get(),
            "sexo":sexo.get(),
            "clave":clave.get(),
            "confirm":confirm.get(),
            'telefono':telefono.get()
        }
        result = self._controller.registerData(**dicc)

        if result:
            self.window.destroy()
            App(result)




