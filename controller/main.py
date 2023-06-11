from tkinter import messagebox
from ui.partials.base import BaseController,BaseView
from datetime import datetime


class FormController(BaseController):
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
            result = self.sql.consulta(
                f"SELECT * FROM users WHERE email = '{user.lower()}'"
            )
            data = result.fetchall()
            if data:
                savedPassword = data[0]["password"]
                result = self.match(password, savedPassword)
                if result:
                    messagebox.showinfo(
                        "bienvenido", f"bienveido {data[0]['primer_nombre']}")
                    return True
                else:
                    messagebox.showerror(
                        title="contraseña invalida", message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",
                                    message="el usuario no se encuentra registrado")
        return False


class RegisterController(BaseController):
    """
        crear nuevos usuarios
    """
    def getData(self,**kwargs) -> None:
        """
            obtener los datos para poder generar un nuevo usuario
            args:
                **kwargs -> espera los campos pasados por la vista para poder crear nuevo usuario
        """
        edad:int
        if (
            not kwargs["nombre_completo"] or
            not kwargs["clave"] or
            not kwargs["confirm"] or
            not kwargs["correo"] or
            not kwargs["f_nacimiento"] or
            not kwargs["cedula"] or
            not kwargs["sexo"]
        ):
            return messagebox.showerror("faltan campos", "por favor rellene todos los campos")
        else:
            fecha = datetime.now()
            f_nacimiento:str = str(kwargs["f_nacimiento"])
            sep:str = f_nacimiento.split("-")
            year_nac = int(sep[0])
            edad =  fecha.year - year_nac

        if kwargs["clave"] != kwargs["confirm"]:
            return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")

        self.separarNombre(kwargs["nombre_completo"])

        # newPassword = self.encryptPassword(kwargs["clave"])
            # self.sql.CRUD(f'''
            # INSERT INTO users(
            #     primer_nombre,
            #     segundo_nombre,
            #     primer_apellido,
            #     segundo_apellido,
            #     password,
            #     email,
            #     fecha_nacimiento,
            #     cedula,
            #     edad,
            #     n_telefono
            # ) VALUES (
            #     "{primer_nombre}",
            #     "{segundo_nombre}",
            #     "{primer_apellido}",
            #     "{segundo_apellido}",
            #     "{newPassword}",
            #     "{correo}",
            #     "{f_nacimiento}",
            #     "{cedula}",
            #     {edad},
            #     "{n_telefono}"
            #     );
            # ''')

            # self.window.destroy()
            # Application()
    def separarNombre(self,nombre_completo:str):
        lista = nombre_completo.split()

        for i in lista:
            print(i)