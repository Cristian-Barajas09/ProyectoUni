from partials.db.BaseModel import BaseModel
from models.Usuario.Usuario import Usuario


class UsuarioDao(BaseModel):

    def __init__(self):
        super().__init__(**self.keys_db)

    def registrarUsuario( self,usuario:Usuario):
        return self.insert(
            f"INSERT INTO USERS (cedula,nombres,apellidos,password,email,fecha_nacimiento,edad,n_telefono,sexo) VALUES ({usuario.cedula},'{usuario.nombres}','{usuario.apellidos}','{usuario.password}','{usuario.email}','{usuario.fecha_nacimiento}',{usuario.edad},'{usuario.n_telefono}','{usuario.sexo.value}')"
        )

    def eliminar(self,cedula:str):
        return self.update(
            "UPDATE users SET status='{0}' WHERE cedula='{1}'".format('inactivo',cedula)
        )


    def getUsuario(self,email):
        return self.select(f"SELECT email,password FROM USERS WHERE email='{email}' AND status='activo'",'one')


    def getUsuarios(self):
        return self.select(f"SELECT * FROM USERS WHERE status = 'activo'")


    #proximamente
    def setSession(self,cedula):
        return self.insert(f"INSERT INTO sessions (user_ced,status) VALUES ('{cedula}',TRUE)")




    def getSession(self):
        return self.select("SELECT user_ced FROM sessions WHERE status<>FALSE")




    def delSession(self,cedula):
        return self.update(f"UPDATE sessions SET status=FALSE WHERE user_ced={cedula}")