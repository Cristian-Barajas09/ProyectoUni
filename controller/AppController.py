from tkinter import messagebox
from partials.controller.BaseController import BaseController
from datetime import datetime,date
from dao.EstudianteDao import EstudianteDao
from typing import Any
from util.pdf import generate_planilla,generate_report
from models.Estudiante.Estudiante import Estudiante
from models.Estudiante.ExtraEstudiante import ExtraEstudiante
from models.extra.models import Mano

from pydantic import ValidationError


from .RepresentanteController import RepresentanteController
from .UsuarioController import UsuarioController


class  Controller(BaseController):
    def __init__(self):

        self.representante = RepresentanteController()
        self.users = UsuarioController()

        super().__init__(EstudianteDao)

    """
        valida los datos para poder ingresar al sistema
    """



    def registerChild(self,**kwargs):
        print(kwargs)
        estudiante:Estudiante

        anno_cursar = kwargs["anno_cursar"]
        nombre = kwargs['nombre']
        apellido = kwargs["apellido"]
        fecha_nacimiento_dia = kwargs['f_di']
        fecha_nacimiento_mes = kwargs['f_m']
        fecha_nacimiento_anos = kwargs['f_an']
        edad_annos = kwargs['e_a']
        edad_meses = kwargs['e_m']
        sexo = kwargs['sex']
        lugar_nacimiento = kwargs['l_n']
        entidad_fedederal = kwargs['en_fed']
        nacionalidad = kwargs['nacionalidad']
        cededula_escolar = kwargs['ced_escolar']
        mannana =kwargs['man']
        tarde = kwargs['tar']
        seccion = kwargs['secc']
        grupo_A = kwargs['A']
        grupo_B = kwargs['B']
        grupo_C  =kwargs['C']
        instituto_de_procedencia = kwargs['instituto_pro']
        estudio_en_el_hogar = kwargs['del_hogar']
        # cuanto hijos tuvo

        sencillo = kwargs['senci']
        gemelos =kwargs['gem']
        gemelo_1 =kwargs['g_1']
        gemelo_2 =kwargs['g_2']
        trillisos = kwargs['trill']
        trillisos_1 =kwargs['t_1']
        trillisos_2 =kwargs['t_2']
        trillisos_3 =kwargs['t_3']

        # proceso de nacimiento
        normal =kwargs['nor']
        cesesarea =kwargs['ces']
        forceps = kwargs['forcep']
        a_termino = kwargs['term']

        #enfermedades
        sarampion = kwargs['saram']
        rubeola = kwargs['ru']
        lecechina =kwargs['lec']
        tosferina =kwargs['osf']
        meningitis = kwargs['me']
        hepatitis = kwargs['he']
        parotiditis = kwargs['pa']
        otras = kwargs['otras']
        cuales = kwargs['cuales']
        # fin enfermedades
        # vacunas
        BCG = kwargs['BCG']
        antitetanica = kwargs['anti']
        vacuna_rubeola = kwargs['rube']
        triple = kwargs['tripe']
        fibre_amarilla = kwargs['f_a']
        polio = kwargs['pol']
        otras_2 = kwargs['otras_2']
        #fin vacunas
        #manos
        derecha = kwargs['der']
        izquierda = kwargs['izq']
        Ambas = kwargs['amb']
        peso = kwargs['peso']
        altura = kwargs['altura']
        talla_camisa = kwargs['talla']
        pantalon = kwargs['pantalon']
        zapatos = kwargs['zap']
        vive_con_padre = kwargs['padre']
        vive_con_madre = kwargs['madre']
        vive_con_abuelos = kwargs['abuelos']
        vive_con_otro_fami = kwargs['otro_fami']
        empezo_hablar = kwargs['empezo_hab']
        con_quien_duerme = kwargs['quien_duer']
        tiene_hermanos_estudiando = kwargs['si_her']
        no_tiene_hermanos_estudiando = kwargs['no_her']
        grado_del_hermano = kwargs['gra_her']
        habla_correctamente = kwargs['hab_correc']
        canta = kwargs['canta']
        baila = kwargs['baila']
        cuenta_historias = kwargs['historias']
        practica_algun_deporte = kwargs['si_dep']
        cual_deporte = kwargs['cual_dep']
        juega_con = kwargs['juega_con']
        que_juegos_realiza_en_casa = kwargs['juegos_casa']
        emp_camin = kwargs['emp_camin']

        fecha_nacimiento = date(fecha_nacimiento_anos,fecha_nacimiento_mes,fecha_nacimiento_dia)

        turno = mannana if mannana else tarde

        print("grupos",grupo_A,grupo_B,grupo_C)

        grupo = grupo_A


        if grupo_B:
            grupo = grupo_B
        elif grupo_C:
            grupo = grupo_C

        print("grupo",grupo)

        procedencia = instituto_de_procedencia if instituto_de_procedencia != "" else estudio_en_el_hogar

        parto = sencillo

        if gemelos:
            parto = 2
        elif trillisos:
            parto = 3

        print("proceso",normal,cesesarea,forceps,a_termino)
        proceso = normal

        if cesesarea:
            proceso = cesesarea
        elif forceps:
            proceso = forceps
        elif a_termino:
            proceso = a_termino

        print(proceso)

        enfermedades = []


        if sarampion:
            enfermedades.append(sarampion)
        elif rubeola:
            enfermedades.append(rubeola)
        elif lecechina:
            enfermedades.append(tosferina)
        elif meningitis:
            enfermedades.append(meningitis)
        elif hepatitis:
            enfermedades.append(hepatitis)
        elif parotiditis:
            enfermedades.append(parotiditis)
        elif otras:
            enfermedades.append(cuales)

        vacunas = []

        if BCG:
            vacunas.append(BCG)
        elif antitetanica:
            vacunas.append(antitetanica)
        elif vacuna_rubeola:
            vacunas.append(vacuna_rubeola)
        elif triple:
            vacunas.append(triple)
        elif fibre_amarilla:
            vacunas.append(fibre_amarilla)
        elif polio:
            vacunas.append(polio)

        print("manos",derecha,izquierda,Ambas)
        mano_que_usa = Mano.DERECHA.value

        if izquierda == "izquierda":
            mano_que_usa = Mano.IZQUIERDA.value
        elif Ambas == "ambas":
            mano_que_usa = Mano.AMBAS.value

        print("mano",mano_que_usa)

        familiar = vive_con_padre

        if vive_con_madre:
            familiar = vive_con_madre
        elif vive_con_abuelos:
            familiar = vive_con_abuelos
        elif vive_con_otro_fami:
            familiar = vive_con_otro_fami

        hermanos = True
        grados = grado_del_hermano

        if hermanos == 'False':
            hermanos = False
            grados = None

        act_deport = False
        deport = None

        if practica_algun_deporte:
            act_deport = True
            deport = cual_deporte

        if sexo == "Masculino":
            sexo = "M"
        else:
            sexo = "F"

        if habla_correctamente == "si":
            habla_correctamente = True
        else:
            habla_correctamente = False


        extra = ExtraEstudiante(
            vacunas=vacunas,
            enfermedades=enfermedades,
            gustos=[canta,baila,cuenta_historias],
            juegos=[juega_con,que_juegos_realiza_en_casa],
            actividades=[deport],
            alergias=[otras_2]
        )
        print(turno)
        print(grupo)

        print(nacionalidad)

        try:
            estudiante = Estudiante(
                anno=anno_cursar,nombres=nombre,apellidos=apellido,cedula_escolar=cededula_escolar,
                fecha_nacimiento=fecha_nacimiento,edad=edad_annos,edad_meses=edad_meses,sexo=sexo,
                lugar_de_nacimiento=lugar_nacimiento,entidad_federal=entidad_fedederal,nacionalidad=nacionalidad,
                turno=turno,seccion=seccion,grupo=grupo,instituto_procedencia=procedencia,
                parto=parto,proceso_nacimiento=proceso,
                mano=mano_que_usa,peso=peso,estatura=altura,
                talla_camisa=talla_camisa,talla_pantalon=pantalon,
                talla_zapatos=zapatos,con_quien_vive=familiar,a_que_edad_camino=emp_camin,a_que_edad_hablo=int(empezo_hablar),
                duerme_con=con_quien_duerme,tiene_hermanos=hermanos,donde_estudian_hermanos=grados,
                habla_bien=habla_correctamente,juega_con=juega_con,extra=extra
            )
        except ValidationError as e:
            messagebox.showerror("Error",e)
            return



        id = self.sql.guardar(estudiante)
        self.representante.set_representante(**kwargs)

        self.guardarEnfermedades(estudiante.cedula_escolar,estudiante.extra.enfermedades)

        self.guardarGustos(estudiante.cedula_escolar,estudiante.extra.gustos)
        self.guardarJuegos(estudiante.cedula_escolar,estudiante.extra.juegos)
        self.guardarActividades(estudiante.cedula_escolar,estudiante.extra.actividades)
        self.guardarVacunas(estudiante.cedula_escolar,estudiante.extra.vacunas)
        self.guardarAlergias(estudiante.cedula_escolar,estudiante.extra.alergias)

        self.set_planilla(**kwargs)

        return messagebox.showinfo("Exito","Estudiante registrado con exito")

    def set_planilla(self,**kwargs):
        generate_planilla(**kwargs)

    def guardarActividades(self,cedula:int | str,actividades:list):
        for actividad in actividades:
            self.sql.guardarActividades(cedula=cedula,actividad=actividad)

    def guardarVacunas(self,cedula:int | str,vacunas:list):
        for vacuna in vacunas:
            self.sql.guardarVacunas(cedula=cedula,vacuna=vacuna)

    def guardarJuegos(self,cedula:int | str,juegos:list):
        for juego in juegos:
            self.sql.guardarJuegos(cedula=cedula,juegos=juego)

    def guardarAlergias(self,cedula:int | str,alergias:list):
        for alergia in alergias:
            self.sql.guardarAlergias(cedula=cedula,alergia=alergia)

    def guardarGustos(self,cedula:int | str,gustos:list):
        for gusto in gustos:
            self.sql.guardarGustos(cedula=cedula,gusto=gusto)

    def guardarEnfermedades(self,cedula:int | str,enfermedades:list):
        for enfermedad in enfermedades:
            self.sql.guardarEnfermedades(cedula=cedula,enfermedad=enfermedad)


    def getEstudiantes(self):

        return self.sql.getEstudiantes()

    def getRepresentantes(self):
        return self.representante.get_representante()

    def getUsers(self):
        return self.users.getUsuarios()


    def set_sessions(self,cedula:int):
        self.sql.set_session(cedula)


    def search(self,search,param,table):

        query = ""

        if table == 'users':
            query = 'SELECT nombres,apellidos,{cedula} FROM {table} WHERE {param} LIKE "{search}%" AND status = "activo"'.format(cedula='cedula',table=table,param=param,search=search)
        elif table == 'estudiantes':
            query = 'SELECT nombres,apellidos,{cedula} FROM {table} WHERE {param} LIKE "{search}%" AND status = "activo"'.format(cedula='cedula_escolar as cedula',table=table,param=param,search=search)
        elif table == "representantes":
            query = 'SELECT nombres,apellidos,{cedula} FROM {table} WHERE {param} LIKE "{search}%" AND status = "activo"'.format(cedula='cedula',table=table,param=param,search=search)

        print(query)

        result = self.sql.select(
            query
        )
        print(result)
        return result


    def obtenerUsuario(self,cedula):
        return self.users.obtenerUsuario(cedula)

    def obtenerEstudiante(self,cedula):
        return self.sql.obtenerEstudiante(cedula)

    def obtenerRepresentante(self,cedula):
        return self.representante.obtenerRepresentante(cedula)

    def generarPlanilla(self,ruta):
        result = self.sql.generateReport()

        return generate_report(result,ruta)

    def eliminarRepresentante(self,cedula):
        result = self.representante.eliminar_representante(cedula)
        return result

    def eliminarEstudiante(self,cedula):
        result = self.sql.eliminar(cedula)
        return result

    def eliminarUsuario(self,cedula):
        result = self.users.eliminar_usuario(cedula)
        return result

    def modificarRepresentante(self,cedula):
        result = self.representante.modificar_representante(cedula)
        return result

    def modificarEstudiante(self,anno,nombres,apellidos,cedula_escolar,fecha_nacimiento,edad,edad_meses,sexo,lugar_de_nacimiento,entidad_federal,nacionalidad,turno,seccion,grupo,instituto_procedencia,parto,proceso_nacimiento,enfermedades,vacunas,mano_que_usa,peso,altura,talla,pantalon,talla_zapatos_estudiante,familiar,empezo_hab,quien_duer,hermanos,gra_her,hab_correc,canta,baila,historias,si_dep,cual_dep,juega_con,juegos_casa):

        estudiante = Estudiante(
            anno=anno,nombres=nombres,apellidos=apellidos,cedula_escolar=cedula_escolar,
            fecha_nacimiento=fecha_nacimiento,edad=edad,edad_meses=edad_meses,sexo=sexo,
            lugar_de_nacimiento=lugar_de_nacimiento,entidad_federal=entidad_federal,nacionalidad=nacionalidad,
            turno=turno,seccion=seccion,grupo=grupo,instituto_procedencia=instituto_procedencia,
            parto=parto,proceso_nacimiento=proceso_nacimiento,enfermedades=enfermedades,vacunas=vacunas,
            mano_que_usa=mano_que_usa,peso=peso,altura=altura,
            talla=talla,pantalon=pantalon,
            talla_zapatos_estudiante=talla_zapatos_estudiante,familiar=familiar,empezo_hab=empezo_hab,
            quien_duer=quien_duer,hermanos=hermanos,gra_her=gra_her,hab_correc=hab_correc,
            canta=canta,baila=baila,historias=historias,si_dep=si_dep,
            cual_dep=cual_dep,juega_con=juega_con,juegos_casa=juegos_casa
        )

        return self.sql.actualizar(estudiante)

# solo porque no me deja subir unos cambios