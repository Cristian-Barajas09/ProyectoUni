from pydantic import BaseModel

class ExtraEstudiante(BaseModel):
    gustos:list
    juegos:list
    actividades:list
    vacunas:list
    alergias:list
    enfermedades:list