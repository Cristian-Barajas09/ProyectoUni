from datetime import date
from models.extra.models import Turno,Sexo,Grupo,Parto,Proceso,Mano,Seccion
from .ExtraEstudiante import ExtraEstudiante

class Estudiante:
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

    def __init__(self,*,
                    nombres:str,
                    apellidos:str,
                    cedula_escolar:int,
                    fecha_nacimiento:date,
                    edad:int,
                    edad_meses:int,
                    sexo:Sexo,
                    lugar_de_nacimiento:str,
                    entidad_federal:str,
                    nacionalidad:str,
                    turno:Turno,
                    seccion:str,
                    grupo:Grupo,
                    instituto_procedencia:str,
                    parto: Parto,
                    proceso_nacimiento: Proceso,
                    mano:Mano,
                    peso: float,
                    estatura: float,
                    talla_camisa: str,
                    talla_pantalon:str,
                    talla_zapatos:str,
                    con_quien_vive: str,
                    a_que_edad_hablo:int,
                    a_que_edad_camino:int,
                    duerme_con:str,
                    tiene_hermanos: bool,
                    donde_estudian_hermanos:str,
                    habla_bien:bool,
                    juega_con: str,
                    anno: int,
                    extra:ExtraEstudiante
                ):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula_escolar = cedula_escolar
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.edad_meses = edad_meses
        self.sexo = sexo
        self.lugar_de_nacimiento = lugar_de_nacimiento
        self.entidad_federal = entidad_federal
        self.nacionalidad = nacionalidad
        self.turno = turno
        self.seccion = seccion
        self.grupo = grupo
        self.instituto_procedencia = instituto_procedencia
        self.parto = parto
        self.proceso_nacimiento = proceso_nacimiento
        self.mano = mano
        self.peso = peso
        self.estatura = estatura
        self.talla_camisa = talla_camisa
        self.talla_pantalon = talla_pantalon
        self.talla_zapatos = talla_zapatos
        self.con_quien_vive = con_quien_vive
        self.a_que_edad_hablo = a_que_edad_hablo
        self.a_que_edad_camino = a_que_edad_camino
        self.duerme_con = duerme_con
        self.tiene_hermanos = tiene_hermanos
        self.donde_estudian_hermanos = donde_estudian_hermanos
        self.habla_bien = habla_bien
        self.juega_con = juega_con
        self.anno = anno
        self.extra = extra
