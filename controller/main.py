from tkinter import messagebox
from partials.BaseController import BaseController
from datetime import datetime,date
from model.database import BaseDatos
from typing import Any
from util.pdf import generate_planilla
from model.models import Representante,Estudiante
class  Controller(BaseController):
    def __init__(self):
        super().__init__(BaseDatos)

    """
        valida los datos para poder ingresar al sistema
    """



    def getData(self,user:str,password:str) -> bool:
        """
            recibe datos de la vista y los valida para permitir el acceso

            args:
                user:str -> usuario
                password:str -> clave

            return:
                bool -> True si hay acceso, False si no hay acceso
        """
        if user == "" or password == "":
            messagebox.showerror(title="faltan campos por rellenar",
                                message="por favor rellene todos los campos")
        else:
            data = self.sql.getUsuario(email=user)
            print(data)

            if data:
                savedPassword = data[0]["password"]
                result = self.match(password, savedPassword)
                if result:
                    messagebox.showinfo(
                        "bienvenido", f"bienvenido {data[0]['nombres']}",
                    )
                    return True
                else:
                    messagebox.showerror(
                        title="contraseña invalida", message="la contraseña proporsionada es invalida")
            else:
                messagebox.showerror(title="usuario o contraseña invalido",
                                    message="el usuario no se encuentra registrado")
        return False
    """
        crear nuevos usuarios
    """
    def registerData(self,**kwargs) -> bool:
        """
            obtener los datos para poder generar un nuevo usuario
            args:
                **kwargs -> espera los campos pasados por la vista para poder crear nuevo usuario
        """
        edad:int

        if (
            kwargs["nombres"] == "" or
            kwargs["apellidos"] == "" or
            kwargs["clave"] == "" or
            kwargs["confirm"] == "" or
            kwargs["correo"] == "" or
            kwargs["f_nacimiento"] == "" or
            kwargs["cedula"] == "" or
            kwargs["sexo"] == ""
        ):
            return messagebox.showerror("faltan campos", "por favor rellene todos los campos")
        else:
            fecha = datetime.now()
            f_nacimiento:str = str(kwargs["f_nacimiento"])
            sep:str = f_nacimiento.split("-")
            year_nac = int(sep[0])
            edad =  fecha.year - year_nac

            nombres = kwargs["nombres"]
            apellidos = kwargs["apellidos"]
            correo = kwargs["correo"]
            cedula = kwargs["cedula"]
            sexo = kwargs["sexo"]
            clave = kwargs["clave"]




            if kwargs["clave"] != kwargs["confirm"]:
                return messagebox.showerror("claves no coinciden", "las claves ingresadas no son iguales")




            newPassword = self.encrypt(clave)
            result = self.sql.registrarUsuario(
                nombres,apellidos,newPassword,correo,fecha,cedula,edad,sexo
            )
            return result


    def registerChild(self,**kwargs:dict[str,Any]):

        estudiante:Estudiante

        anno_cursar = kwargs["anno_cursar"]
        nombre = kwargs['nombre']
        apellido = kwargs["apellido"]
        f_di = kwargs['f_di']
        f_m = kwargs['f_m']
        f_an = kwargs['f_an']
        e_a = kwargs['e_a']
        e_m = kwargs['e_m']
        sex = kwargs['sex']
        l_n = kwargs['l_n']
        en_fed = kwargs['en_fed']
        nacionalidad = kwargs['nacionalidad']
        ced_escolar = kwargs['ced_escolar']
        man =kwargs['man']
        tar = kwargs['tar']
        secc = kwargs['secc']
        A =  'A' if not(kwargs['A'])  else ''
        B = 'B' if not(kwargs['B'])  else ''
        C  ='C' if not(kwargs['C']) else ''
        instituto_pro = kwargs['instituto_pro']
        del_hogar = kwargs['del_hogar']
        senci = kwargs['senci']
        gem =kwargs['gem']
        g_1 =kwargs['g_1']
        g_2 =kwargs['g_2']
        trill = kwargs['trill']
        t_1 =kwargs['t_1']
        t_2 =kwargs['t_2']
        t_3 =kwargs['t_3']
        nor =kwargs['nor']
        ces =kwargs['ces']
        forcep = kwargs['forcep']
        term = kwargs['term']
        saram = kwargs['saram']
        ru = kwargs['ru']
        lec =kwargs['lec']
        osf =kwargs['osf']
        me = kwargs['me']
        he = kwargs['he']
        pa = kwargs['pa']
        otras = kwargs['otras']
        cuales = kwargs['cuales']
        BCG = kwargs['BCG']
        anti = kwargs['anti']
        rube = kwargs['rube']
        tripe = kwargs['tripe']
        f_a = kwargs['f_a']
        pol = kwargs['pol']
        otras_2 = kwargs['otras_2']
        der = kwargs['der']
        izq = kwargs['izq']
        Amb = kwargs['amb']
        peso = kwargs['peso']
        altura = kwargs['altura']
        talla = kwargs['talla']
        pantalon = kwargs['pantalon']
        zap = kwargs['zap']
        padre = kwargs['padre']
        madre = kwargs['madre']
        abuelos = kwargs['abuelos']
        otro_fami = kwargs['otro_fami']
        empezo_hab = kwargs['empezo_hab']
        quien_duer = kwargs['quien_duer']
        si_her = kwargs['si_her']
        no_her = kwargs['no_her']
        gra_her = kwargs['gra_her']
        hab_correc = kwargs['hab_correc']
        canta = kwargs['canta']
        baila = kwargs['baila']
        historias = kwargs['historias']
        si_dep = kwargs['si_dep']
        cual_dep = kwargs['cual_dep']
        juega_con = kwargs['juega_con']
        juegos_casa = kwargs['juegos_casa']

        fecha_nacimiento = date(f_an,f_m,f_di)
        turno:str
        grupo:str

        procedencia = instituto_pro if instituto_pro != "" else del_hogar
        parto:str
        proceso:str

        if tar != '':
            turno = tar
        else:
            turno = man

        if A != "":
            grupo = "A"
        elif B != "":
            grupo = "B"
        else:
            grupo =  "C"

        if senci != "":
            parto = 1
        elif gem != "":
            parto = 2
        elif trill != "":
            parto = 3



        estudiante = Estudiante(
            anno=anno_cursar,nombres=nombre,apellidos=apellido,cedula_escolar=ced_escolar,
            fecha_nacimiento=fecha_nacimiento,edad=e_a,edad_meses=e_m,sexo=sex,
            lugar_de_nacimiento=l_n,entidad_federal=en_fed,nacionalidad=nacionalidad,
            turno=turno,seccion=secc,grupo=grupo,instituto_procedencia=procedencia,
            parto=parto,proceso_nacimiento=proceso
        )

        self.set_representante(**kwargs)

        self.sql.register_child(nombres=estudiante.nombres)

        self.set_planilla(**kwargs)



    def set_representante(self,**kwargs):
        nom_pa = kwargs['nom_pa']
        ape_pa = kwargs['ape_pa']
        ced_pa = kwargs['ced_pa']
        nac_pa = kwargs['nac_pa']
        pro_pa = kwargs['pro_pa']
        hab_pa = kwargs['hab_pa']
        tel_pa = kwargs['tel_pa']
        trabajo_pa = kwargs['trabajo_pa']
        tel_pa_tra = kwargs['tel_pa_tra']
        vi_si = kwargs['vi_si']
        vi_no = kwargs['vi_no']
        nombre_ma = kwargs['nombre_ma']
        ape_ma = kwargs['ape_ma']
        ced_ma = kwargs['ced_ma']
        nac_ma = kwargs['nac_ma']
        pro_ma = kwargs['pro_ma']
        hab_ma = kwargs['hab_ma']
        tel_hab_ma = kwargs['tel_ma']
        tra_ma = kwargs['tra_ma']
        tel_trab_m = kwargs['tel_ma_trab']
        vive_con_el_si = kwargs['vive_con_el_si']
        vive_con_el_no = kwargs['vive_con_el_no']
        nombre_re = kwargs['nombre_re']
        apellido_re = kwargs['apellido_re']
        parentesco = kwargs['parentesco']
        cedula = kwargs['cedula']
        telefono = kwargs['telefono']
        direccion_casa = kwargs['direccion_casa']
        telefono_hab_re = kwargs['telefono_hab_re']
        direccion_trabajo = kwargs['direccion_trabajo']
        telefono_t_re = kwargs['telefono_t_re']
        telefono_cer_re = kwargs['telefono_cer_re']
        dir_cer_re = kwargs['dir_cer_re']
        if nom_pa != '':
            padre = Representante(
                nombres=nom_pa,
                apellidos=ape_pa,
                cedula=ced_pa,
                nacionalidad=nac_pa,
                profesion=pro_pa,
                direcciones={'habitacion':hab_pa,'trabajo':trabajo_pa},
                telefonos={'habitacion':tel_pa,'trabajo':tel_pa_tra},
                parentesco="padre",
                vive_con_el= vi_si if vi_si else vi_no
            )

            self.sql.set_representantes(representante=padre)
            for k,v in padre.direcciones.items():
                self.sql.set_direccion(cedula=padre.cedula,direccion=v,de=k)

            for k,v in padre.telefonos.items():
                self.sql.set_telefono(cedula=padre.cedula,telefono=v)
        elif nombre_ma != '':
            madre = Representante(
                nombres=nombre_ma,
                apellidos=ape_ma,
                cedula=ced_ma,
                nacionalidad=nac_ma,
                profesion=pro_ma,
                direcciones={'habitacion':hab_ma,'trabajo':tra_ma},
                telefonos={'habitacion':tel_hab_ma,'trabajo':tel_trab_m},
                parentesco="madre",
                vive_con_el= vive_con_el_si if vive_con_el_si else vive_con_el_no
            )

            self.sql.set_representantes(representante=madre)
            for k,v in madre.direcciones.items():
                self.sql.set_direccion(cedula=madre.cedula,direccion=v,de=k)

            for k,v in madre.telefonos.items():
                self.sql.set_telefono(cedula=madre.cedula,telefono=v)
        elif nombre_re != '':
            representante = Representante(
                nombres=nombre_re,
                apellidos=apellido_re,
                cedula=cedula,
                direcciones={'habitacion':direccion_casa,'trabajo':direccion_trabajo,'familiar':dir_cer_re},
                telefonos={'propio':telefono,'habitacion':telefono_hab_re,'trabajo':telefono_t_re,'familiar':telefono_cer_re}
            )

            self.sql.set_representantes(representante=representante)
            for k,v in representante.direcciones.items():
                self.sql.set_direccion(cedula=representante.cedula,direccion=v,de=k)

            for k,v in representante.telefonos.items():
                self.sql.set_telefono(cedula=representante.cedula,telefono=v)

    def set_planilla(self,**kwargs):


        generate_planilla(  **kwargs   )

    def get_users_tree(self) :

        datos = self.sql.get_childs()
        if datos != ():
            datos[0]["rol"] = "estudiante"
        rep = self.sql.get_representantes()
        if rep != ():
            rep[0]["rol"] = "representante"
        usuarios = self.sql.get_usuarios()

        print(usuarios)

        return datos,usuarios,rep


    def set_sessions(self,cedula:int):
        self.sql.set_session(cedula)


    def search_user(self,search,param):
        result = self.sql.consulta(
            f'SELECT nombres,apellidos,cedula FROM users WHERE {param} LIKE "{search}%"')
        result = result.fetchall()

        return result

