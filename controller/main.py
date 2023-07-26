from tkinter import messagebox
from partials.BaseController import BaseController
from datetime import datetime
from model.database import BaseDatos
from typing import Any
from util.pdf import generate_planilla
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
            print(data)

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


    def registerChild(self,**kwargs:dict[str,Any]):
        """
        :param **kwargs -> {
            nombres:str
            apellidos:str
            fecha_nacimiento
            edad:int
            sexo:str
            lugar_nacimiento:str
            entidad_federal:str
            nacionalidad:str
            cedula_escolar:int
            turno:str
            instituto_procedencia:str
            parto:str
            proceso_nacimiento:str
            mano_dominante:str
            peso:float
            talla:int
            talla_comisa:int
            talla_pantalon
            zapatos
            con_quien_vive
            cuando_hablo
            cuando_camino
            duerme_con
            tiene_hermanos
            donde_estudian_hermanos
            habla_correctamente
            con_quien_juega
            status
            juegos
            actividades
            alergias
            enfermedades
            vacunas
            gustos
            cedula
            nacionalidad
            profesion
            nombre
            apellidos
            vive_con_el
            n_telefono
            direccion
        }
        """
        print(kwargs)

        nombres:str = kwargs["nombres"]
        apellidos:str = kwargs["apellidos"]
        fecha_nacimiento = kwargs["fecha_nacimiento"]
        edad:int = kwargs["edad"]
        sexo:str = kwargs["sexo"]
        lugar_nacimiento:str = kwargs["lugar_nacimiento"]
        entidad_federal:str = kwargs["entidad_federal"]
        nacionalidad:str = kwargs["nacionalidad"]
        cedula_escolar:int = kwargs["cedula_escolar"]
        turno:str = kwargs["turno"]
        instituto_procedencia:str = kwargs["instituto_procedencia"]
        parto:str = kwargs["parto"]
        proceso_nacimiento:str = kwargs["proceso_nacimiento"]
        mano_dominante:str = kwargs["mano_dominante"]
        peso:float = kwargs["peso"]
        talla:int = kwargs["talla"]
        talla_comisa:int = kwargs["talla_comisa"]
        talla_pantalon:int = kwargs["talla_pantalon"]
        zapatos:int = kwargs["zapatos"]
        con_quien_vive:str = kwargs["con_quien_vive"]
        cuando_hablo:int = kwargs["cuando_hablo"]
        cuando_camino:int = kwargs["cuando_camino"]
        duerme_con:str = kwargs["duerme_con"]
        tiene_hermanos:bool = kwargs["tiene_hermanos"]
        donde_estudian_hermanos:str = kwargs["donde_estudian_hermanos"]
        habla_correctamente:bool = kwargs["habla_correctamente"]
        con_quien_juega:str = kwargs["con_quien_juega"]
        status:bool = True
        juegos:list | str = kwargs["juegos"]
        actividades = kwargs["actividades"]
        alergias=kwargs["alergias"]
        enfermedades =kwargs["enfermedades"]
        vacunas= kwargs["vacunas"]
        gustos =kwargs["gustos"]
        results = self.sql.register_child(
                nombres,
                apellidos,
                fecha_nacimiento,
                edad,
                sexo,
                lugar_nacimiento,
                entidad_federal,
                nacionalidad,
                cedula_escolar,
                turno,
                instituto_procedencia,
                parto,
                proceso_nacimiento,
                mano_dominante,
                peso,
                talla,
                talla_comisa,
                talla_pantalon,
                zapatos,
                con_quien_vive,
                cuando_hablo,
                cuando_camino,
                duerme_con,
                tiene_hermanos,
                donde_estudian_hermanos,
                habla_correctamente,
                con_quien_juega,
                status)

        result =self.get_child(cedula_escolar)

        self.sql.set_juegos(result[0]['id'],juegos)
        self.sql.set_actividades(result[0]['id'],actividades)
        self.sql.set_alergias(result[0]['id'],alergias)
        self.sql.set_enfermedades(result[0]['id'],enfermedades)
        self.sql.set_vacunas(result[0]['id'],vacunas)
        self.sql.set_gustos(result[0]['id'],gustos)


        self.set_representante(**kwargs)




        
        return results



    def set_representante(self,**kwargs):

        cedula = kwargs["cedula"]
        nacionalidad = kwargs["nacionalidad"]
        profesion = kwargs["profesion"]
        nombre = kwargs["nombre"]
        apellidos = kwargs["apellidos"]
        vive_con_el = kwargs["vive_con_el"]
        n_telefono = kwargs["n_telefono"]
        direccion = kwargs["direccion"]



        self.sql.set_representantes(cedula,nacionalidad,profesion,nombre,apellidos,vive_con_el)

        self.sql.set_telefono(cedula,n_telefono)
        self.sql.set_direccion(cedula,direccion)

    def set_planilla(self,**kwargs):


        generate_planilla(       )

    def get_users_tree(self) :
        datos = self.sql.consulta(
            "SELECT nombres,apellidos,cedula FROM users"
        )
        datos = datos.fetchall()

        return datos


    def set_sessions(self,cedula:int):
        self.sql.set_session(cedula)


    def search_user(self,search,param):
        result = self.sql.consulta(
            f'SELECT nombres,apellidos FROM users WHERE {param} LIKE "{search}%"')
        result = result.fetchall()

        return result

    def get_users(self):
        return self.sql.get_usuarios()


    def get_child(self,cedula:int):
        return self.sql.get_child(cedula)