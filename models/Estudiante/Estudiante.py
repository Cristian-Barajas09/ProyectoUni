from pydantic import BaseModel
from datetime import date
from models.extra.models import Turno,Sexo,Grupo,Parto,Proceso,Mano,Seccion
from .ExtraEstudiante import ExtraEstudiante

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
    seccion:Seccion
    grupo:Grupo
    instituto_procedencia:str
    parto: Parto
    proceso_nacimiento: Proceso
    mano:Mano
    peso: float
    estatura: float
    talla_camisa: str
    talla_pantalon:str
    talla_zapatos:str
    con_quien_vive: str
    a_que_edad_hablo:int
    a_que_edad_camino:int
    duerme_con:str
    tiene_hermanos: bool
    donde_estudian_hermanos:str
    habla_bien:bool
    juega_con: str
    anno: int
    extra:ExtraEstudiante
