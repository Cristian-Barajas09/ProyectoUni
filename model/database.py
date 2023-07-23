from partials.BaseModel import BaseModel
from pymysql.cursors import Cursor


class BaseDatos(BaseModel):


    def __init__(self):
        super().__init__(**self.keys_db)



    def registrarUsuario(self,nombres,apellidos,password,email,f_nacimiento,cedula,edad,sexo):

        self.CRUD(f'''
                INSERT INTO users(
                    nombres,
                    apellidos,
                    password,
                    email,
                    fecha_nacimiento,
                    cedula,
                    edad,
                    sexo
                ) VALUES (
                    "{nombres}",
                    "{apellidos}",
                    "{password}",
                    "{email}",
                    "{f_nacimiento}",
                    "{cedula}",
                    {edad},
                    "{sexo}"
                );
                ''')



    def getUsuario(self,email):
        result:Cursor = self.consulta(
            sql=f"SELECT * FROM users WHERE email = '{email}'"
        )
        result = result.fetchall()

        return result


    def register_child(self):
        self.CRUD(
            sql="INSERT INTO estudiantes () VALUES ()"
        )


    def set_seccion(self,seccion,profesor):
        self.CRUD(
            sql="INSERT INTO secciones (seccion,id_profesor) VALUES ('{}',{})"
        )