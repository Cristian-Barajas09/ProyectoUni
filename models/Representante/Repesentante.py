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
