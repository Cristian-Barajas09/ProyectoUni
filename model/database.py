from partials.BaseModel import BaseModel
from pymysql.cursors import Cursor
from datetime import date


class BaseDatos(BaseModel):


    def __init__(self):
        super().__init__(**self.keys_db)



    def registrarUsuario(self,nombres,apellidos,password,email,f_nacimiento,cedula,edad,sexo):

        return self.CRUD(f'''
                INSERT INTO users(
                    nombres,
                    apellidos,
                    password,
                    email,
                    fecha_nacimiento,
                    cedula,
                    edad,
                    sexo,
                    status
                ) VALUES (
                    "{nombres}",
                    "{apellidos}",
                    "{password}",
                    "{email}",
                    "{f_nacimiento}",
                    "{cedula}",
                    {edad},
                    "{sexo}",
                    TRUE
                );
                ''')



    def getUsuario(self,email):
        result:Cursor = self.consulta(
            sql=f"SELECT * FROM users WHERE email = '{email}'"
        )
        result = result.fetchall()

        return result


    def register_child(self,
                    nombres:str,
                    apellidos:str,
                    fecha_nacimiento:date,
                    edad:int,
                    sexo:str,
                    lugar_nacimiento:str,
                    entidad_federal:str,
                    nacionalidad:str,
                    cedula_escolar:int,
                    turno:str,
                    instituto_procedencia:str,
                    parto:str,
                    proceso_nacimiento:str,
                    mano_dominante:str,
                    peso:float,
                    talla:int,
                    talla_comisa:int,
                    talla_pantalon:int,
                    zapatos:int,
                    con_quien_vive:str,
                    cuando_hablo:int,
                    cuando_camino:int,
                    duerme_con:str,
                    tiene_hermanos:bool,
                    donde_estudian_hermanos:str,
                    habla_correctamente:bool,
                    con_quien_juega:str,
                    status:bool
                    ):
        return self.CRUD(
            sql=f"""
            INSERT INTO estudiantes (
                nombres,
                apellidos,
                fecha_nacimiento,
                edad,
                sexo,
                lugar_nacimiento,
                entidad_federal,
                nacionalidad,
                cedula_escolar,
                turno,
                instituto_procedencia,
                parto,
                proceso_nacimiento,
                mano_dominante,
                peso,
                talla,
                talla_comisa,
                talla_pantalon,
                zapatos,
                con_quien_vive,
                cuando_hablo,
                cuando_camino,
                duerme_con,
                tiene_hermanos,
                donde_estudian_hermanos,
                habla_correctamente,
                con_quien_juega,
                status
            ) VALUES (
                '{nombres}',
                '{apellidos}',
                '{fecha_nacimiento}',
                {edad},
                '{sexo}',
                '{lugar_nacimiento}',
                '{entidad_federal}',
                '{nacionalidad}',
                '{cedula_escolar}',
                '{turno}',
                '{instituto_procedencia}',
                '{parto}',
                '{proceso_nacimiento}',
                '{mano_dominante}',
                {peso},
                {talla},
                {talla_comisa},
                {talla_pantalon},
                {zapatos},
                '{con_quien_vive}',
                '{cuando_hablo}',
                '{cuando_camino}',
                '{duerme_con}',
                {tiene_hermanos},
                '{donde_estudian_hermanos}',
                {habla_correctamente},
                '{con_quien_juega}',
                {status})"""
        )


    def set_anno(self,anno:int,seccion:str,profesor:int):
        return self.CRUD(
            sql=f"INSERT INTO annos (anno,seccion,id_profesor) VALUES ({anno},'{seccion}',{profesor})"
        )

    def set_gustos(self,estudiante:int,gusto:str):
        return self.CRUD(
            sql=f"INSERT INTO gustos (id_estudiante,gusto) VALUES ({estudiante},'{gusto}')"
        )

    def set_juegos(self,id_estudiante:int,juego:str):
        return self.CRUD(
            sql=f"INSERT INTO juegos (id_estudiante,juego) VALUES ({id_estudiante},'{juego}'"
        )

    def set_actividades(self,id_estudiante:int,acti:str):
        return self.CRUD(
            sql=f"INSERT INTO actividades (id_estudiante,actividad) VALUES ({id_estudiante},'{acti}'"
        )

    def set_vacunas(self,id_estudiante:int,vacuna:str):
        return self.CRUD(
            sql=f"INSERT INTO vacunas (id_estudiante,vacuna) VALUES ({id_estudiante},'{vacuna}')"
        )

    def set_alergias(self,id_estudiante:int,alergia:str):
        return  self.CRUD(
            sql=f"INSERT INTO alergias (id_estudiante,alergia) VALUES ({id_estudiante},'{alergia}')"
        )

    def set_enfermedades(self,id_estudiante:int,alergia:str):
        return  self.CRUD(
            sql=f"INSERT INTO alergias (id_estudiante,enfermedades) VALUES ({id_estudiante},'{alergia}')"
        )


    def set_representantes(self,cedula:int,nacionalidad:str,profesion:str,nombres:str,apellidos:str,vive_con_el:bool):
        return self.CRUD (
            sql=f"INSERT INTO representante (cedula,nacionalidad,profesion,nombre,apellidos,vive_con_el,status) VALUES ({cedula},'{nacionalidad}','{profesion}','{nombres}','{apellidos}',{vive_con_el}')"
        )


    def set_direccion(self,cedula: int,direccion:str,de: str):
        """
        :param cedula:int -> cedula del representante
        :param direccion:str -> direccion del representate

        :param de:str -> de donde es la direccion
        ex: trabajo,casa,etc no importa si vives de bajo de un puente
        """
        return self.CRUD(
            sql=f"INSERT INTO direcciones (cedula,direccion,de) VALUES ({cedula},'{direccion}','{de}')"
        )

    def set_telefono(self,cedula: int,telefono: int):
        return self.CRUD(
            sql=f"INSERT INTO (cedula,n_telefeno) VALUES ({cedula},{telefono})"
        )

    def set_session(self,cedula:int | str):
        return self.CRUD(
            sql=f"INSERT INTO sessions (user_ced,status) VALUES ({cedula},TRUE)"
        )

    def get_usuarios(self):
        result:Cursor = self.consulta(
            sql="SELECT * FROM users"
        )

        return result.fetchall()
    
    def get_child(self,cedula:int):
        result:Cursor =  self.consulta(
            sql=f"SELECT * FROM estudiantes WHERE cedula_escolar = {cedula}"
        )

        return result.fetchone()