from tkinter import messagebox
from partials.controller.BaseController import BaseController
from datetime import datetime,date
from dao.EstudianteDao import EstudianteDao
from typing import Any
from util.pdf import generate_planilla,generate_report
from models.Estudiante.Estudiante import Estudiante
from .RepresentanteController import RepresentanteController


class  Controller(BaseController):
    def __init__(self):

        self.representante = RepresentanteController()

        super().__init__(EstudianteDao)

    """
        valida los datos para poder ingresar al sistema
    """


    def registerChild(self,**kwargs:dict[str,Any]):

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
        grupo_A =  'A' if not(kwargs['A'])  else ''
        grupo_B = 'B' if not(kwargs['B'])  else ''
        grupo_C  ='C' if not(kwargs['C']) else ''
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

        fecha_nacimiento = date(fecha_nacimiento_anos,fecha_nacimiento_mes,fecha_nacimiento_dia)
        turno:str
        grupo:str

        procedencia = instituto_de_procedencia if instituto_de_procedencia != "" else estudio_en_el_hogar
        parto:str
        proceso:str
        enfermedades:str
        vacunas:str
        mano_que_usa:str
        peso_estudiante:str
        altura_estudiante:str
        talla_camisa_estudiante:str
        talla_pantalon_estudiante:str
        talla_zapatos_estudiante:int
        familiar:str
        comenzo_hablar:str
        duerme_con:str
        hermanos:str
        grados:str
        h_c:str
        cant:str
        bai:str
        contar_historias:str
        act_deport:str
        deport:str
        jue_con:str
        juegos_hogar:str

        if tarde != '':
            turno = tarde
        else:
            turno = mannana

        if grupo_A != "":
            grupo = "A"
        elif grupo_B != "":
            grupo = "B"
        else:
            grupo =  "C"

        if sencillo != "":
            parto = 1
        elif gemelos != "":
            parto = 2
        elif trillisos != "":
            parto = 3

        if normal != "":
            proceso = "N"
        elif cesesarea != "":
            proceso = "C"
        elif forceps != "":
            proceso = "F"
        elif a_termino != "":
            proceso = "T"


        if sarampion != "":
            enfermedades = "saram"
        elif rubeola != "":
            enfermedades = "ru"
        elif lecechina != "":
            enfermedades = "lec"
        elif tosferina != "":
            enfermedades = "tosferina"
        elif meningitis != "":
            enfermedades = "me"
        elif hepatitis != "":
            enfermedades = "he"
        elif parotiditis != "":
            enfermedades = "pa"
        else:
            enfermedades = kwargs["otras"]

        if BCG != "":
            vacunas = "BCG"
        elif antitetanica != "":
            vacunas = "anti"
        elif vacuna_rubeola != "":
            vacunas = "rube"
        elif triple != "":
            vacunas = "tripe"
        elif fibre_amarilla != "":
            vacunas = "f-a"
        elif polio != "":
            vacunas = "pol"
        else:
            vacunas = "otras_2"


        if derecha != "":
            mano_que_usa = "der"
        elif izquierda != "":
            mano_que_usa = "izq"
        else:
            mano_que_usa = "Amb"

        if peso != "":
            peso_estudiante = "peso"

        if altura != "":
            altura_estudiante = "altura"
            
        if talla_camisa != "":
            talla_camisa_estudiante = "talla"

        if pantalon != "":
            talla_pantalon_estudiante = "pantalon"
        if zapatos != "":
            talla_zapatos_estudiante

        if vive_con_padre != "":
            familiar = "padre"
        elif vive_con_madre != "":
            familiar = "madre"
        elif vive_con_abuelos != "":
            familiar = "abuelos"
        else:
            familiar = "otro_fami"

        if empezo_hablar != "":
            comenzo_hablar = "empezo_hab"
            
        if con_quien_duerme != "":
            duerme_con = "quien_duer"
        
        if tiene_hermanos_estudiando != "":
            hermanos = "si_her"
        else:
            hermanos = "no_her"
            
        if grado_del_hermano != "":
            grados = "gra_her"
            
        if habla_correctamente != "":
            h_c = "hab_correc"
            
        if canta != "":
            cant = canta
        
        if baila != "":
            bai = "baila"
        
        if cuenta_historias != "":
            contar_historias = "historias"
        
        if practica_algun_deporte != "":
            act_deport = "si_dep"
        
        if cual_deporte != "":
            deport = "cual_dep"
        
        if juega_con != "":
            jue_con = "juega_con"
            
        if que_juegos_realiza_en_casa != "":
            juegos_hogar = "juegos_casa"

        estudiante = Estudiante(
            anno=anno_cursar,nombres=nombre,apellidos=apellido,cedula_escolar=cededula_escolar,
            fecha_nacimiento=fecha_nacimiento,edad=edad_annos,edad_meses=edad_meses,sexo=sexo,
            lugar_de_nacimiento=lugar_nacimiento,entidad_federal=entidad_fedederal,nacionalidad=nacionalidad,
            turno=turno,seccion=seccion,grupo=grupo,instituto_procedencia=procedencia,
            parto=parto,proceso_nacimiento=proceso,enfermedades=enfermedades,vacunas=vacunas,
            mano_que_usa=mano_que_usa,peso=peso_estudiante,altura=altura_estudiante,
            talla=talla_camisa_estudiante,pantalon=talla_pantalon_estudiante,
            talla_zapatos_estudiante=zapatos,familiar=familiar,empezo_hab=comenzo_hablar,
            quien_duer=duerme_con,hermanos=hermanos,gra_her=grados,hab_correc=h_c,
            canta=cant,baila=bai,historias=contar_historias,si_dep=act_deport,
            cual_dep=deport,juega_con=jue_con,juegos_casa=juegos_hogar
        )

        self.representante.set_representante(**kwargs)

        id = self.sql.guardar(estudiante)

        self.sql.guardarEnfermedades(id)

        self.sql.guardarGustos(id)
        self.sql.guardarJuegos(id)
        self.sql.guardarActividades(id)
        self.sql.guardarVacunas(id)
        self.sql.guardarAlergias(id)

        


        self.set_planilla(**kwargs)





    def set_planilla(self,**kwargs):


        generate_planilla(  **kwargs   )

    def getEstudiantes(self):

        return self.sql.getEstudiantes()




    def set_sessions(self,cedula:int):
        self.sql.set_session(cedula)


    def search_user(self,search,param):
        result = self.sql.consulta(
            f'SELECT nombres,apellidos,cedula FROM users WHERE {param} LIKE "{search}%"')
        result = result.fetchall()

        return result


    def generarPlanilla(self):
        result = self.sql.generateReport()
        result[0]["docente"] = 'admin'

        generate_report(result)

