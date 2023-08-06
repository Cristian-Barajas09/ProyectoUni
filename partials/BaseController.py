from util.helpers import matchPassword,encryptPassword
from model.database import BaseDatos
class BaseController:
    """
        plantilla base para controlar los datos del usuario
    """
    encrypt = None
    match = None
    sql:BaseDatos
    def __init__(self,model):

        self.sql = model()
        self.encrypt = encryptPassword
        self.match = matchPassword


