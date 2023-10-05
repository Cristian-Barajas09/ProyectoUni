from partials.controller.BaseController import BaseController
from datetime import date
from tkinter import messagebox
from dao.UsuarioDao import UsuarioDao
from models.Usuario.Usuario import Usuario
from models.extra.models import Sexo
from models.extra.niveles import Rol


class FormController(BaseController):

    def __init__(self):
        super().__init__(UsuarioDao)

    def getData(self,user:str,password:str) -> bool:
        """
            recibe datos de la vista y los valida para permitir el acceso

            args:
                user:str -> usuario
                password:str -> clave

            return:
                bool -> True si hay acceso, False si no hay acceso
        """
        if user == "" or password == "":
            messagebox.showerror(title="faltan campos por rellenar",
                                message="por favor rellene todos los campos")
        else:
            data = self.sql.getUsuario(email=user)
            print(data)
            if data:
                savedPassword = data["password"]
                result = self.match(password, savedPassword)
                if result:
                    messagebox.showinfo(
                        "bienvenido", f"bienvenido {data['email']}",
                    )
                    return True
                else:
                    messagebox.showerror(
                        title="contraseña invalida", message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",
                                    message="el usuario no se encuentra registrado")
        return False
    """
        crear nuevos usuarios
    """
    def registerData(self,**kwargs) -> bool:
        """
            obtener los datos para poder generar un nuevo usuario
            args:
                **kwargs -> espera los campos pasados por la vista para poder crear nuevo usuario
        """
        edad:int

        if (
            kwargs["nombres"] == "" or
            kwargs["apellidos"] == "" or
            kwargs["clave"] == "" or
            kwargs["confirm"] == "" or
            kwargs["correo"] == "" or
            kwargs["f_nacimiento"] == "" or
            kwargs["cedula"] == "" or
            kwargs["sexo"] == ""
        ):
            messagebox.showerror("faltan campos", "por favor rellene todos los campos")
            return False
        else:
            fecha = date.today()
            f_nacimiento:str = str(kwargs["f_nacimiento"])
            sep:str = f_nacimiento.split("-")
            year_nac = int(sep[0])
            edad =  fecha.year - year_nac

            nombres = kwargs["nombres"]
            apellidos = kwargs["apellidos"]
            correo = kwargs["correo"]
            cedula = kwargs["cedula"]
            sexo = kwargs["sexo"]
            clave = kwargs["clave"]
            telefono = kwargs["telefono"]

            if sexo == 'Masculino':
                sexo = Sexo.MASCULINO.value
            elif sexo == 'Femenino':
                sexo = Sexo.FEMENINO.value



            if kwargs["clave"] != kwargs["confirm"]:
                return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")




            newPassword = self.encrypt(clave)

            newUsuario = Usuario(
                nombres=nombres,apellidos=apellidos,
                password=newPassword,email=correo,fecha_nacimiento=fecha,
                cedula=cedula,edad=edad,sexo=sexo,rol=Rol.PROFESOR.value,
                n_telefono=telefono
            )

            result: str | int = self.sql.registrarUsuario(
                newUsuario
            )

            return result