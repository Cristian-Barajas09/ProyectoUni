from partials.controller.BaseController import BaseController
from dao.UsuarioDao import UsuarioDao

class UsuarioController(BaseController):
    def __init__(self):
        super().__init__(UsuarioDao)


    def getUsuarios(self):
        return self.sql.getUsuarios()