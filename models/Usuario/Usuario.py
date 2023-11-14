from datetime import date
from models.extra.models import Sexo
from models.extra.niveles import Rol
class Usuario:
    cedula:str
    nombres:str
    apellidos:str
    password:str
    email:str
    fecha_nacimiento:date
    edad:int
    n_telefono:str
    sexo:Sexo
    rol:Rol

    def __init__(
            self
            ,*,
            cedula:str,
            nombres:str,
            apellidos:str,
            password:str,
            email:str,
            fecha_nacimiento:date,
            edad:int,
            n_telefono:str,
            sexo:Sexo,
            rol:Rol
            ):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.password = password
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.n_telefono = n_telefono
        self.sexo = sexo
        self.rol = rol