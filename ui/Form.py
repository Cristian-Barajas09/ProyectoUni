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

        print(os.path.join(self.carpeta_imagenes,'Logo_Josefina_Redondo.png'))
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
            App()

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
        frame.place(x=50,y=80,width=600,height=300)

        labelName = self.tk.Label(frame,text="Nombres",font=get_font(11),bg="#222",fg="#fff").place(x=110,y=15,width=60)
        inputName = self.tk.Entry(frame,bg="#222",fg="#fff",border=0)
        inputName.place(x=50,y=45,width=200)
        self.tk.Frame(frame,bg="#fff").place(x=50,y=64,width=200,height=2)

        labelLastName = self.tk.Label(frame,text="Apellidos",font=get_font(11),bg="#222",fg="#fff").place(x=420,y=15,width=60)
        inputLastName = self.tk.Entry(frame,bg="#222",fg="#fff",border=0)
        inputLastName.place(x=350,y=45,width=200)
        self.tk.Frame(frame,bg="#fff").place(x=350,y=64,width=200,height=2)


        labelEmail = self.tk.Label(frame,text="Correo",bg="#222",fg="#fff",font=get_font(11)).place(x=80,y=100,width=60)
        inputEmail = self.tk.Entry(frame,bg="#222",fg="#fff",border=0)
        inputEmail.place(x=40,y=125,width=140)
        self.tk.Frame(frame,bg="#fff").place(x=40,y=140,width=140,height=2)


        labelDate = self.tk.Label(frame,text="Fecha de nacimiento",bg="#222",fg="#fff",font=get_font(11)).place(x=230,y=100,width=140)
        inputDate = DateEntry(frame)
        inputDate.place(x=250,y=125)

        labelId = self.tk.Label(frame,text="Cedula",bg="#222",fg="#fff",font=get_font(11)).place(x=445,y=100,width=60)
        inputId = self.tk.Entry(frame,bg="#222",fg="#fff",border=0)
        inputId.place(x=440,y=125,width=80)
        self.tk.Frame(frame,bg="#fff").place(x=420,y=140,width=120,height=2)


        labelGender = self.tk.Label(frame,text="Genero",bg="#222",fg="#fff",font=get_font(11)).place(x=70,y=170,width=60)
        inputGender = self.ttk.Combobox(frame,values=('Masculino','Femenino',"Pentasexual",".!."),state="readonly")
        inputGender.current(0)
        inputGender.place(x=70,y=200,width=80)

        labelPassword = self.tk.Label(frame,text="Contraseña",bg="#222",fg="#fff",font=get_font(11)).place(x=220,y=170,width=80)
        inputPassword = self.tk.Entry(frame,fg="#fff",border=0,bg="#222")
        inputPassword.place(x=205,y=190,width=120)
        self.tk.Frame(frame,bg="#fff").place(x=205,y=210,width=120,height=2)



        labelConfirmPassword = self.tk.Label(frame,text="Confirmar Contraseña",bg="#222",fg="#fff",font=get_font(11)).place(x=380,y=170,width=160)
        inputConfirmPassword = self.tk.Entry(frame,bg="#222",fg="#fff",border=0)
        inputConfirmPassword.place(x=390,y=190,width=140)
        self.tk.Frame(frame,bg="#fff").place(x=390,y=210,width=140,height=2)

        btnSignup = self.tk.Button(self.window,
                                   text="registrarse",
                                   command=lambda : self.registrarUsuario(
                                       inputName,inputLastName,inputEmail,inputDate,inputId,inputGender,inputPassword,
                                       inputConfirmPassword
                                   ))
        btnSignup.place(x=0,y=0)

        btnSignin = self.tk.Button(self.window,text="Iniciar sesion",command=self.signin,background="#38B1EE",fg="#fff",border=0)
        btnSignin.pack(side="bottom")

    def signin(self):
        self.window.destroy()
        Signin()





