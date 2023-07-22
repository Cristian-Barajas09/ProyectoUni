from tkinter import messagebox
from partials.BaseController import BaseController
from datetime import datetime
from model.database import BaseDatos

class  Controller(BaseController):
    def __init__(self):
        super().__init__(BaseDatos)
    """
        valida los datos para poder ingresar al sistema
    """
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

            if data:
                savedPassword = data[0]["password"]
                result = self.match(password, savedPassword)
                if result:
                    messagebox.showinfo(
                        "bienvenido", f"bienvenido {data[0]['nombres']}",
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
            return messagebox.showerror("faltan campos", "por favor rellene todos los campos")
        else:
            fecha = datetime.now()
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




            if kwargs["clave"] != kwargs["confirm"]:
                return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")




            newPassword = self.encrypt(clave)
            result = self.sql.registrarUsuario(
                nombres,apellidos,newPassword,correo,fecha,cedula,edad,sexo
            )
            return result





    def get_users(self) :
        datos = self.sql.consulta(
            "SELECT nombres,apellidos FROM users")
        datos = datos.fetchall()

        return datos


    def search_user(self,search,param):
        result = self.sql.consulta(
            f'SELECT nombres,apellidos FROM users WHERE {param} LIKE "{search}%"')
        result = result.fetchall()

        return result

