from jinja2 import Environment,FileSystemLoader
from .rutas import dir
import os
from datetime import date
import shutil
from .helpers import generate_env_value
planilla = {
        'anno_cursar':2,
        'nombre':"cristian",
        'apellido':'Barajas',
        'f_di':30,
        'f_m':8,
        'f_an':2004,
        'e_a':18,
        'e_m':216,
        'sex':'M',
        'l_n':'San Cristobal',
        'en_fed':'Tachira',
        'nacionalidad':'Venezolana',
        'cedula':'31357876',
        'man':'X',
        'tar':'_',
        'secc':'_',
        'A':'X',
        'B':'_',
        'C':'_',
        'instituto_pro':'IUT',
        'del_hogar':'NO',
        'senci':'X',
        'gem':'_',
        'g_1':'_',
        'g_2':'_',
        'trill':'_',
        't_1':'_',
        't_2':'_',
        't_3':'_',
        'nor':'X',
        'ces':'_',
        'forcep':'_',
        'term':'',
        'saram':'_',
        'ru':'',
        'lec':'X',
        'osf':'_',
        'me':'_',
        'he':'_',
        'pa':'_',
        'otras':'_',
        'cuales':'Cancer de pito',
        'BCG':'_',
        'anti':'_',
        'rube':'_',
        'tripe':'_',
        'f_a':'_',
        'pol':'_',
        'otras_2':'_',
        'der':'X',
        'izq':'_',
        'Amb':'_',
        'peso':'60',
        'altura':'1.73',
        'talla':'L',
        'pantalon':'32',
        'zap':'43',
        'padre':'_',
        'madre':'X',
        'abuelos':'_',
        'otro_fami':'_',
        'empezo_hab':'2',
        'quien_duer':'_',
        'si_her':'_',
        'no_her':'_',
        'gra_her':'_',
        'hab_correc':'_',
        'canta':'_',
        'baila':'_',
        'historias':'_',
        'si_dep':'_',
        'cual_dep':'_',
        'juega_con':'_',
        'juegos_casa':'_',
        'nom_pa':'_',
        'ape_pa':'_',
        'ced_pa':'_',
        'nac_pa':'_',
        'pro_pa':'_',
        'tel_pa':'_',
        'trabajo_pa':'_',
        'tel_pa_tra':'_',
        'vi_si':'_',
        'vi_no':'_',
        'nombre_ma':'_',
        'ape_ma':'_',
        'ced_ma':'_',
        'nac_ma':'_',
        'pro_ma':'_',
        'hab_ma':'_',
        'tel_hab_ma':'_',
        'tra_ma':'_',
        'tel_ma_trab':'_',
        'vive_con_el_si':'_',
        'vive_con_el_no':'_',
        'nombre_re':'_',
        'apellido_re':'_',
        'parentesco':'_',
        'cedula':'_',
        'telefono':'_',
        'direccion_casa':'_',
        'telefono_hab_re':'_',
        'direccion_trabajo':'_',
        'telefono_t_re':'_',
        'telefono_cer_re':'_',
        'dir_cer_re':'_',


    }


public = os.path.join(dir,"public")
dir_template = os.path.join(dir,"templates")

env = Environment(loader=FileSystemLoader("templates",encoding="utf-8"),comment_start_string="{*",comment_end_string="*}")



def generate_planilla(**kwargs):
    template = env.get_template("template.html")
    html = template.render(kwargs)
    cedula = kwargs["cedula"]
    ruta = os.path.join(public,f"{cedula}.html")
    f = open(ruta,'w',encoding="utf-8")
    f.write(html)
    f.close()


def generate_report(usuarios,ruta):
    # try:
        template = env.get_template("Plantilla impresión Proyecto 2/index.html")

        html = template.render({'users':usuarios})


        carpeta = os.path.join(ruta,"reporte")
        carpeta_imagenes = os.path.join(carpeta,"imagenes")

        logo = os.path.join(dir_template,"Plantilla impresión Proyecto 2","imagenes","logozona.png")
        fondo = os.path.join(dir_template,"Plantilla impresión Proyecto 2","imagenes","fondoniños2.jpg")


        os.mkdir(carpeta)
        os.mkdir(carpeta_imagenes)

        archivo_1 = os.path.join(carpeta_imagenes,"logozona.png")
        archivo_2 = os.path.join(carpeta_imagenes,"fondoniños2.jpg")

        shutil.copyfile(logo,archivo_1)
        shutil.copyfile(fondo,archivo_2)

        generate_env_value("RUTA_REPORTE",ruta)

        ruta = os.path.join(carpeta,f"reporte{date.today()}.html")
        f = open(ruta,'w',encoding="utf-8")
        f.write(html)
        f.close()

    #     return True
    # except:
    #     return False

    

if __name__ == '__main__':

    user_ex = {
        "nombres":"Cristian",
        "apellidos":"Barajas",
        'cedula':31357876,
        'grupo':'A',
        'seccion':'A',
        'docente':'Andi'
    }

    generate_report(**user_ex)