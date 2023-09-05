from models import Representante
from dao.RepresentanteDao import RepresentanteDao
class TestRepresentante:
    def crear(self):
        padre = Representante(
            nombres="Juan Carlos",
            apellidos="Barajas Gambo",
            cedula="15503301",
            nacionalidad="Venezolana",
            profesion="",
            direcciones={'':''},
            telefonos={},
            parentesco="Padre",
            vive_con_el=False
        )

        representanteDao = RepresentanteDao()

        representanteDao.guardar(padre)
        for k,v in padre.direcciones.items():
            representanteDao.guardarDireccion(cedula=padre.cedula,direccion=v,de=k)

        for k,v in padre.telefonos.items():
            representanteDao.guardarTelefono(cedula=padre.cedula,telefono=v)

