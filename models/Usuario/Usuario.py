from pydantic import BaseModel
from datetime import date
from models.extra.models import Sexo
from models.extra.niveles import Rol
class Usuario(BaseModel):
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