from partials.BaseModel import BaseModel



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
        result = self.consulta(
            sql=f"SELECT * FROM users WHERE email = '{email}'"
        )
        result = result.fetchall()

        return result
