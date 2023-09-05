from partials.db.BaseModel import BaseModel
from models.Usuario.Usuario import Usuario


class UsuarioDao(BaseModel):

    def __init__(self):
        super().__init__(**self.keys_db)

    def registrarUsuario( self,usuario:Usuario):
        self.insert(
            f"INSERT INTO USERS (cedula,nombres,apellidos,password,email,fecha_nacimiento,edad,n_telefono,sexo) VALUES ({usuario.cedula},'{usuario.nombres}','{usuario.apellidos}','{usuario.password}','{usuario.email}','{usuario.fecha_nacimiento}',{usuario.edad},'{usuario.n_telefono}','{usuario.sexo.value}')"
        )




    def getUsuario(self,email):
        return self.select(f"SELECT email,password FROM USERS WHERE email='{email}'")




    def setSession(self,cedula):
        return self.insert(f"INSERT INTO sessions (user_ced,status) VALUES ('{cedula}',TRUE)")




    def getSession(self):
        return self.select("SELECT user_ced FROM sessions WHERE status<>FALSE")




    def delSession(self,cedula):
        return self.update(f"UPDATE sessions SET status=FALSE WHERE user_ced={cedula}")