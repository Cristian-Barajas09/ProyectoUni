from util.helpers import matchPassword,encryptPassword

class BaseController:
    """
        plantilla base para controlar los datos del usuario
    """
    encrypt = None
    match = None
    sql = None
    def __init__(self,model):

        self.sql = model()
        self.encrypt = encryptPassword
        self.match = matchPassword

