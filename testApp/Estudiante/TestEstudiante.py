from dao.EstudianteDao import EstudianteDao
from models.Estudiante.Estudiante import Estudiante
from models.Estudiante.ExtraEstudiante import ExtraEstudiante
from datetime import date
from models.extra.models import Sexo,Turno,Seccion,Grupo,Parto,Proceso,Mano


class TestEstudiante:

    def crear_estudiante(self):
        dao = EstudianteDao()
        fecha_nacimiento = date(2004,8,30)

        extra = ExtraEstudiante(
            gustos=['comer'],
            juegos=['telefono'],
            actividades=['programar'],
            vacunas=['todas :D'],
            alergias=['ninguna'],
            enfermedades=['lechina']
        )


        estudiante = Estudiante(
            nombres="cristian",
            apellidos="Barajas",
            cedula_escolar="16229383",
            fecha_nacimiento=fecha_nacimiento,
            edad=18,
            edad_meses=216,
            sexo=Sexo.MASCULINO,
            lugar_de_nacimiento="San Cristobal",
            entidad_federal="Tachira",
            nacionalidad="venezolana",
            turno=Turno.MANANA,
            seccion=Seccion.A,
            grupo=Grupo.A,
            instituto_procedencia="IMA",
            parto=Parto.SENCILLO,
            proceso_nacimiento=Proceso.NATURAL,
            mano=Mano.DERECHA,
            peso=60,
            estatura=1.73,
            talla_camisa='L',
            talla_pantalon='32',
            talla_zapatos='42',
            con_quien_vive='mamá',
            a_que_edad_hablo=1,
            a_que_edad_camino=2,
            duerme_con="solo :(",
            tiene_hermanos=True,
            donde_estudian_hermanos="Colombia",
            habla_bien=True,
            juega_con="solo :(",
            anno=1,
            extra=extra
        )



        result = dao.guardar(estudiante)

        print(result)

        dao.guardarActividades(estudiante.cedula_escolar,estudiante.extra.actividades[0])

        dao.guardarEnfermedades(estudiante.cedula_escolar,estudiante.extra.enfermedades[0])

        dao.guardarAlergias(estudiante.cedula_escolar,estudiante.extra.alergias[0])

        dao.guardarGustos(estudiante.cedula_escolar,estudiante.extra.gustos[0])

        dao.guardarJuegos(estudiante.cedula_escolar,estudiante.extra.juegos[0])

        dao.guardarVacunas(estudiante.cedula_escolar,estudiante.extra.vacunas[0])

