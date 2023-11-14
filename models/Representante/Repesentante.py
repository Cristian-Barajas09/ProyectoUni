
class Representante:
    nombres:str
    apellidos:str
    cedula:str
    nacionalidad:str | None
    profesion:str  | None
    direcciones: dict
    telefonos: dict
    parentesco:str
    vive_con_el:bool


    def __init__(self,*,nombres:str,
    apellidos:str,
    cedula:str,
    nacionalidad:str | None,
    profesion:str  | None,
    direcciones: dict,
    telefonos: dict,
    parentesco:str,
    vive_con_el:bool):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.nacionalidad = nacionalidad
        self.profesion = profesion
        self.direcciones = direcciones
        self.telefonos  = telefonos
        self.parentesco = parentesco
        self.vive_con_el = vive_con_el
