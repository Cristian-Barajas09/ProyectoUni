from datetime import date
from enum import Enum
from pydantic import BaseModel


class Representante(BaseModel):
    nombres:str
    apellidos:str
    cedula:str
    nacionalidad:str | None
    profesion:str  | None
    direcciones: dict
    telefonos: dict
    parentesco:str
    vive_con_el:bool


class Sexo(Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'

class Turno(Enum):
    MANANA = 'M'
    TARDE = 'T'

class Grupo(Enum):
    A = 'A'
    B = 'B'
    C = 'C'

class Parto(Enum):
    SENCILLO = "sencillo"
    GEMELO = "Gemelos"
    TRILLIZOS = "trillizos"

class Proceso(Enum):
    NATURAL = 'N'
    CESAREA = 'C'
    FORCEP = 'F'
    TERMINO = 'T'

class Mano(Enum):
    DERECHA='D'
    IZQUIERDA='I'
    AMBAS='A'

class ExtraEstudiante(BaseModel):
    gustos:dict
    juegos:dict
    actividades:dict
    vacunas:dict
    alergias:dict
    enfermedades:dict


class Estudiante(BaseModel):
    nombres:str
    apellidos:str
    cedula_escolar:int
    fecha_nacimiento:date
    edad:int
    edad_meses:int
    sexo:Sexo
    lugar_de_nacimiento:str
    entidad_federal:str
    nacionalidad:str
    turno:Turno
    seccion:str
    grupo:Grupo
    instituto_procedencia:str
    parto: Parto
    proceso_nacimiento: Proceso
    mano:Mano
    peso: float
    talla: float
    talla_camisa: str
    talla_pantalon:str
    zapatos:str
    vive_con: str
    hablo:int
    camino:int
    hermanos: bool
    donde_estudian:str
    habla_bien:bool
    juega_con: str
    anno: int
    extra:ExtraEstudiante


