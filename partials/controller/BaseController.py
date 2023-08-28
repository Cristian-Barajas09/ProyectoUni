from util.helpers import matchPassword,encryptPassword
from partials.db.BaseModel import BaseModel
class BaseController:
    """
        plantilla base para controlar los datos del usuario
    """
    encrypt = None
    match = None
    sql:BaseModel
    def __init__(self,model:BaseModel):

        self.sql = model()
        self.encrypt = encryptPassword
        self.match = matchPassword


