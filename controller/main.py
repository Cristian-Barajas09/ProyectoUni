from tkinter import messagebox
from partials.BaseController import BaseController
from datetime import datetime
from model.database import BaseDatos
from typing import Any
from util.pdf import generate_planilla
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

        anno_cursar = kwargs["anno_cursar"],
        nombre = kwargs['nombre'],
        apellido = kwargs["apellido"],
        f_di = kwargs['f_di'],
        f_m = kwargs['f_m'],
        f_an = kwargs['f_an'],
        e_a = kwargs['e_a'],
        e_m = kwargs['e_m'],
        sex = kwargs['sex'],
        l_n = kwargs['l_n'],
        en_fed = kwargs['en_fed'],
        nacionalidad = kwargs['nacionalidad'],
        ced_escolar = kwargs['ced_escolar'],
        man =kwargs['man'],
        tar = kwargs['tar'],
        secc = kwargs['secc'],
        A =  'A' if not(kwargs['A'])  else '',
        B = 'B' if not(kwargs['B'])  else '',
        C  ='C' if not(kwargs['C']) else '',
        instituto_pro = kwargs['instituto_pro'],
        del_hogar = kwargs['del_hogar'],
        senci = kwargs['senci'],
        gem =kwargs['gem'],
        g_1 =kwargs['g_1'],
        g_2 =kwargs['g_2'],
        trill = kwargs['trill'],
        t_1 =kwargs['t_1'],
        t_2 =kwargs['t_2'],
        t_3 =kwargs['t_3'],
        nor =kwargs['nor'],
        ces =kwargs['ces'],
        forcep = kwargs['forcep'],
        term = kwargs['term'],
        saram = kwargs['saram'],
        ru = kwargs['ru'],
        lec =kwargs['lec'],
        osf =kwargs['osf'],
        me = kwargs['me'],
        he = kwargs['he'],
        pa = kwargs['pa'],
        otras = kwargs['otras'],
        cuales = kwargs['cuales'],
        BCG = kwargs['BCG'],
        anti = kwargs['anti'],
        rube = kwargs['rube'],
        tripe = kwargs['tripe'],
        f_a = kwargs['f_a'],
        pol = kwargs['pol'],
        otras_2 = kwargs['otras_2'],
        der = kwargs['der'],
        izq = kwargs['izq'],
        Amb = kwargs['amb'],
        peso = kwargs['peso'],
        altura = kwargs['altura'],
        talla = kwargs['talla'],
        pantalon = kwargs['pantalon'],
        zap = kwargs['zap'],
        padre = kwargs['padre'],
        madre = kwargs['madre'],
        abuelos = kwargs['abuelos'],
        otro_fami = kwargs['otro_fami'],
        empezo_hab = kwargs['empezo_hab'],
        quien_duer = kwargs['quien_duer'],
        si_her = kwargs['si_her'],
        no_her = kwargs['no_her'],
        gra_her = kwargs['gra_her'],
        hab_correc = kwargs['hab_correc'],
        canta = kwargs['canta'],
        baila = kwargs['baila'],
        historias = kwargs['historias'],
        si_dep = kwargs['si_dep'],
        cual_dep = kwargs['cual_dep'],
        juega_con = kwargs['juega_con'],
        juegos_casa = kwargs['juegos_casa'],

        self.set_representante(**kwargs)

        self.sql.register_child()

        self.set_planilla(**kwargs)



    def set_representante(self,**kwargs):
        nom_pa = kwargs['nom_pa'],
        ape_pa = kwargs['ape_pa'],
        ced_pa = kwargs['ced_pa'],
        nac_pa = kwargs['nac_pa'],
        pro_pa = kwargs['pro_pa'],
        hab_pa = kwargs['hab_pa'],
        tel_pa = kwargs['tel_pa'],
        trabajo_pa = kwargs['trabajo_pa'],
        tel_pa_tra = kwargs['tel_pa_tra'],
        vi_si = kwargs['vi_si'],
        vi_no = kwargs['vi_no'],
        nombre_ma = kwargs['nombre_ma,']
        ape_ma = kwargs['ape_ma'],
        ced_ma = kwargs['ced_ma'],
        nac_ma = kwargs['nac_ma'],
        pro_ma = kwargs['pro_ma'],
        hab_ma = kwargs['hab_ma'],
        tel_hab_ma = kwargs['tel_ma'],
        tra_ma = kwargs['tra_ma'],
        tel_trab_m = kwargs['tel_ma_trab'],
        vive_con_el_si = kwargs['vive_con_el_si'],
        vive_con_el_no = kwargs['vive_con_el_no'],
        nombre_re = kwargs['nombre_re'],
        apellido_re = kwargs['apellido_re'],
        parentesco = kwargs['parentesco'],
        cedula = kwargs['cedula'],
        telefono = kwargs['telefono'],
        direccion_casa = kwargs['direccion_casa'],
        telefono_hab_re = kwargs['telefono_hab_re'],
        direccion_trabajo = kwargs['direccion_trabajo'],
        telefono_t_re = kwargs['telefono_t_re'],
        telefono_cer_re = kwargs['telefono_cer_re'],
        dir_cer_re = kwargs['dir_cer_re'],
        self.sql.set_representantes()

    def set_planilla(self,**kwargs):


        generate_planilla(  **kwargs   )

    def get_users_tree(self) :
        datos = self.sql.consulta(
            "SELECT nombres,apellidos,cedula FROM users")
        datos = datos.fetchall()

        return datos


    def set_sessions(self,cedula:int):
        self.sql.set_session(cedula)


    def search_user(self,search,param):
        result = self.sql.consulta(
            f'SELECT nombres,apellidos,cedula FROM users WHERE {param} LIKE "{search}%"')
        result = result.fetchall()

        return result

