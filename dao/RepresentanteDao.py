from partials.db.BaseModel import BaseModel
from models.Representante.Repesentante import Representante

class RepresentanteDao(BaseModel):


    def __init__(self):
        super().__init__(**self.keys_db)


    def guardar(self,representante:Representante):
        return self.insert(
            "INSERT INTO representantes (cedula,nacionalidad,profesion,nombres,apellidos,vive_con_el,parentesco)" +
            f"VALUES ('{representante.cedula}','{representante.nacionalidad}','{representante.profesion}','{representante.nombres}','{representante.apellidos}',{representante.vive_con_el},'{representante.parentesco}')"
        )
    
    def actualizar(self,representante: Representante):
        return self.update(
            f"UPDATE representantes SET nacionalidad='{representante.nacionalidad}',profesion='{representante.profesion}',nombres='{representante.nombres}',apellidos='{representante.apellidos}',vive_con_el='{representante.vive_con_el}',parentesco='{representante.parentesco}' WHERE cedula={representante.cedula}"
        )
    
    def eliminar(self,cedula:str):
        return self.update(
            "UPDATE representantes SET status='{0}' WHERE cedula='{1}'".format('inactivo',cedula)
        )

    def guardarDireccion(self,cedula:str | int,direccion:str,de:str):
        return self.insert(
            f"INSERT INTO direcciones (cedula,direccion,de) VALUES ('{cedula}','{direccion}','{de}')"
        )
    
    def guardarTelefono(self,cedula:str | int,telefono:str):
        return self.insert(
            f"INSERT INTO telefono (cedula,n_telefono) VALUES ('{cedula}','{telefono}')"
        )