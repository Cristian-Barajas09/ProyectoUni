from partials.db.BaseModel import BaseModel
from models.Estudiante.Estudiante import Estudiante
class EstudianteDao(BaseModel):
    def __init__(self):
        super().__init__(**self.keys_db)




    def guardar(self,estudiante:Estudiante):


        return self.insert(f"INSERT INTO estudiantes (nombres,apellidos,fecha_nacimiento,edad,sexo,lugar_nacimiento,entidad_federal,nacionalidad,cedula_escolar,turno, instituto_procedencia,parto,proceso_nacimiento,mano_dominante,peso,talla,talla_comisa,talla_pantalon,zapatos,con_quien_vive,cuando_hablo,cuando_camino,duerme_con,tiene_hermanos,donde_estudian_hermanos,habla_correctamente,con_quien_juega,id_anno,status) VALUES ('{estudiante.nombres}','{estudiante.apellidos}','{estudiante.fecha_nacimiento}',{estudiante.edad},'{estudiante.sexo.value}','{estudiante.lugar_de_nacimiento}','{estudiante.entidad_federal}','{estudiante.nacionalidad}','{estudiante.cedula_escolar}','{estudiante.turno.value}','{estudiante.instituto_procedencia}','{estudiante.parto.value}','{estudiante.proceso_nacimiento.value}','{estudiante.mano.value}',{estudiante.peso},{estudiante.estatura},'{estudiante.talla_camisa}','{estudiante.talla_pantalon}','{estudiante.talla_zapatos}','{estudiante.con_quien_vive}',{estudiante.a_que_edad_hablo},{estudiante.a_que_edad_camino},'{estudiante.duerme_con}',{estudiante.tiene_hermanos},'{estudiante.donde_estudian_hermanos}',{estudiante.habla_bien},'{estudiante.juega_con}',{estudiante.anno},'activo')")




    def actualizar(self,estudiante: Estudiante):
        return self.update(
            f""" UPDATE estudiantes
                    SET '{estudiante.nombres}',
                        apellidos = '{estudiante.apellidos}',
                        fecha_nacimiento = '{estudiante.fecha_nacimiento}',
                        edad = {estudiante.edad},
                        sexo = '{estudiante.sexo.value}',
                        lugar_nacimiento = '{estudiante.lugar_de_nacimiento}',
                        entidad_federal ='{estudiante.entidad_federal}',
                        nacionalidad ='{estudiante.nacionalidad}',
                        cedula_escolar ={estudiante.cedula_escolar},
                        turno ='{estudiante.turno}',
                        instituto_procedencia ='{estudiante.instituto_procedencia}',
                        parto ='{estudiante.parto}',
                        proceso_nacimiento ='{estudiante.proceso_nacimiento}',
                        mano_dominante ='{estudiante.mano}',
                        peso ={estudiante.peso},
                        talla ={estudiante.estatura},
                        talla_comisa ={estudiante.talla_camisa},
                        talla_pantalon ={estudiante.talla_pantalon},
                        zapatos ={estudiante.talla_zapatos},
                        con_quien_vive ='{estudiante.con_quien_vive}',
                        cuando_hablo ={estudiante.a_que_edad_hablo},
                        cuando_camino ={estudiante.a_que_edad_camino},
                        duerme_con = '{estudiante.duerme_con}',
                        tiene_hermanos ={estudiante.tiene_hermanos},
                        donde_estudian_hermanos ='{estudiante.donde_estudian_hermanos}',
                        habla_correctamente = {estudiante.habla_bien},
                        con_quien_juega = '{estudiante.juega_con}'
                        WHERE id = {estudiante.id}"""
        )




    def eliminar(self,cedula:str):
        query = "UPDATE estudiantes SET status='{0}' WHERE cedula_escolar='{1}'".format('inactivo',cedula)
        print(query)
        return self.update(
            query
        )


    def getEstudiantes(self):
        return self.select("SELECT cedula_escolar as cedula,nombres,apellidos FROM estudiantes where status = 'activo' ")

    def guardarEnfermedades(self,cedula,enfermedad):
        self.insert(f"INSERT INTO enfermedades (cedula_estudiante,enfermedad) VALUES ('{cedula}','{enfermedad}')")



    def guardarGustos(self,cedula,gusto):
        self.insert(f"INSERT INTO gustos (cedula_estudiante,gusto) VALUES ('{cedula}','{gusto}')")




    def guardarJuegos(self,cedula,juegos):
        self.insert(f"INSERT INTO juegos (cedula_estudiante,juego) VALUES ('{cedula}','{juegos}')")




    def guardarActividades(self,cedula,actividad):
        self.insert(f"INSERT INTO actividades (cedula_estudiante,actividad) VALUES ('{cedula}','{actividad}')")




    def guardarVacunas(self,cedula,vacuna):
        self.insert(f"INSERT INTO vacunas (cedula_estudiante,vacuna) VALUES ('{cedula}','{vacuna}')")




    def guardarAlergias(self,cedula,alergia):
        self.insert(f"INSERT INTO alergias (cedula_estudiante,alergias) VALUES ('{cedula}','{alergia}')")


    def generateReport(self):
        return self.select("""select estudiantes.nombres,estudiantes.apellidos,estudiantes.cedula_escolar,annos.anno as grupo,annos.seccion,users.nombres as docente from estudiantes
inner join annos on annos.anno = estudiantes.id_anno AND estudiantes.status ='activo'
inner join users on users.cedula = annos.id_profesor AND users.status='activo'""")

    def obtenerEstudiante(self,cedula):
        return self.select(f"select * from estudiantes where cedula_escolar={cedula}",'one')

# solo porque no me deja subir unos cambios