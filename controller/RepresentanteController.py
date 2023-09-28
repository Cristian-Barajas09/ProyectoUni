from partials.controller.BaseController import BaseController
from models.Representante.Repesentante import Representante
from dao.RepresentanteDao import RepresentanteDao
class RepresentanteController(BaseController):

    def __init__(self):
        super().__init__(RepresentanteDao)

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
                self.sql.guardarDireccion(cedula=padre.cedula,direccion=v,de=k)

            for k,v in padre.telefonos.items():
                self.sql.guardarTelefono(cedula=padre.cedula,telefono=v)
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
                self.sql.guardarDireccion(cedula=madre.cedula,direccion=v,de=k)

            for k,v in madre.telefonos.items():
                self.sql.guardarTelefono(cedula=madre.cedula,telefono=v)
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
                self.sql.guardarDireccion(cedula=representante.cedula,direccion=v,de=k)

            for k,v in representante.telefonos.items():
                self.sql.guardarTelefono(cedula=representante.cedula,telefono=v)


    def get_representante(self):
        return self.sql.select("SELECT nombres,apellidos,cedula FROM representantes WHERE status != 'inactivo'")

    def eliminar_representante(self,cedula):
        return self.sql.eliminar(cedula)

    def obtenerRepresentante(self,cedula):
        return self.sql.select(f"SELECT * FROM representantes WHERE CEDULA={cedula}",'one')

    def actualizar_datos_padre(self,nom_pa,ape_pa,ced_pa,nac_pa,pro_pa,hab_pa,tel_pa,trabajo_pa,tel_pa_tra,vi_si,vi_no,nombre_ma,ape_ma,ced_ma):
        papa = set_representante(
            nom_pa,ape_pa,ced_pa,nac_pa,pro_pa,hab_pa,tel_pa,trabajo_pa,tel_pa_tra,vi_si,vi_no,nombre_ma,ape_ma,ced_ma
        )
    def actualizar_datos_mama(self,nac_ma,pro_ma,hab_ma,tel_hab_ma,tra_ma,tel_trab_m,vive_con_el_si,vive_con_el_no):
        mama = set_representantes(
            nac_ma,pro_ma,hab_ma,tel_hab_ma,tra_ma,tel_trab_m,vive_con_el_si,vive_con_el_no
        )
    
    def actualizar_datos_representante(self,nombre_re,apellido_re,parentesco,cedula,telefono,direccion_casa,telefono_hab_re,direccion_trabajo,telefono_t_re,telefono_cer_re,dir_cer_re):
        representante = set_representante(
            nombre_re,apellido_re,parentesco,cedula,telefono,direccion_casa,telefono_hab_re,direccion_trabajo,telefono_t_re,telefono_cer_re,dir_cer_re
        )
