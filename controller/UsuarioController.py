from partials.controller.BaseController import BaseController
from dao.UsuarioDao import UsuarioDao

class UsuarioController(BaseController):
    def __init__(self):
        super().__init__(UsuarioDao)


    def getUsuarios(self):
        return self.sql.getUsuarios()


    def eliminar_usuario(self,cedula):
        return self.sql.eliminar(cedula)


    def obtenerUsuario(self,cedula):
        return self.sql.select(f"SELECT nombres,apellidos,cedula FROM USERS WHERE cedula={cedula}")