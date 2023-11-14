import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from partials.controller import BaseController
from datetime import date
from tkcalendar import DateEntry


class InformacionEstudiante(tk.Toplevel):
    def __init__(self,data,controller:BaseController,master):
        self.main_window = master
        self._controller = controller
        super().__init__(master=master.window,width=670,height=400)
        self.wm_title('Estudiante: %s' % (data['nombres']))
        

        self.inscripcion()


        # self.btn_open_planilla = tk.Button(self,text="Abrir Planilla")
        # self.btn_open_planilla.pack()
        # btnDelete = tk.Button(self,text="eliminar estudiante",command=lambda: self.deleteEstudiante(data['cedula_escolar']))
        # btnDelete.pack()

    def deleteEstudiante(self,cedula):
        result = self._controller.eliminarEstudiante(cedula)



        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.main_window.controlPersonas()
        self.destroy()


    def inscripcion(self):
        self.notebook2: ttk.Notebook = ttk.Notebook(self)
        self.frame3 = ttk.Frame(self.notebook2)
        self.frame4 = ttk.Frame(self.notebook2)
        self.frame5 = ttk.Frame(self.notebook2)

        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.notebook2.add(self.frame3,text="1")
        self.notebook2.add(self.frame4,text="2")
        self.notebook2.add(self.frame5,text="3")

        self.notebook2.place(relx=0,rely=0,relwidth=1,relheight=1)


        datos = tk.LabelFrame(self.frame3,border=4, relief="groove", text="Datos del alumno(a)")
        datos.place(relx=0,rely=0,width=650,height=310)

        nombre = tk.Label(datos,text="Nombres:").place(x=4,y=12,width=60)
        nombre_es2 =tk.Entry(datos,border=3,relief="ridge")
        nombre_es2.insert(0,"cristian")
        nombre_es2.place(x=65,y=12,width=100)


        apellido = tk.Label(datos,text="Apellido:").place(x=170,y=12,width=80)
        apellido_es = tk.Entry(datos,border="2",relief="ridge")
        apellido_es.insert(0,"barajas")
        apellido_es.place(x=235,y=12,width=100)

        fecha_nacimiento = tk.Label(datos,text="Fecha de Nacimiento :").place(x=370,y=12,width=115)
        fecha_nacimiento1 = DateEntry(datos,state="readonly")
        fecha_nacimiento1.place(x=495,y=12, width=100)

        edad_anos = tk.Label(datos,text="Edad (Años): ").place(x=8,y=50,width=70)
        edad_anos2 =tk. Entry(datos, border=3, relief="ridge")
        edad_anos2.insert(0,"20")
        edad_anos2.place(x=80,y=50,width=25)

        meses = tk.Label(datos,text="Meses:").place(x=115,y=50,width=70)
        meses2 = tk.Entry(datos, border=3, relief="ridge")
        meses2.insert(0,"20")
        meses2.place(x=175,y=50,width=25)

        sexo = tk.Label(datos,text="Sexo").place(x=200,y=50,width=70)
        sexo_combo = ttk.Combobox(datos,values=["Masculino","Femenino"])

        sexo_combo.current(0)

        sexo_combo.place(x=250,y=50,width=80)


        lugar_nacimiento = tk.Label(datos,text="Lugar de nacimiento:" ).place(x=0,y=90,width=120)
        lugar_nacimiento2 = tk.Entry(datos,border=3, relief="ridge")
        lugar_nacimiento2.insert(0,"San cristobal")
        lugar_nacimiento2.place(x=120,y=90,width=140)

        entidad_federal = tk.Label(datos,text="Entidad Federal:" ).place(x=270,y=90,width=120)
        entidad_federal2 =tk. Entry(datos,border=3,relief="ridge")
        entidad_federal2.insert(0,"Tachira")
        entidad_federal2.place(x=380,y=90,width=140)

        nacionalidad = tk.Label(datos,text="Nacionalidad:").place(x=3,y=120,width=80)
        nacionalidad2 = tk.Entry(datos,border=3,relief='ridge')
        nacionalidad2.insert(0,"Venezolano")
        nacionalidad2.place(x=80,y=120,width=140)

        cdula_escolar = tk.Label(datos,text="Cedula Escolar Nº:").place(x=240,y=120,width=100)
        cdula_escolar2 = tk.Entry(datos,border=3,relief='ridge')
        cdula_escolar2.insert(0,"31357876")
        cdula_escolar2.place(x=340,y=120,width=140)


        manana_key=tk.StringVar()
        tarde_key = tk.StringVar()

        turno = tk.Label(datos, text="Turno:")
        turno.place(x=5,y=150,width=40)

        manana = tk.Checkbutton(datos,text="Mañana",variable=manana_key,onvalue="M",offvalue="")

        manana.place(x=50,y=150,width=80)

        tarde =tk. Checkbutton(datos,text="Tarde",variable=tarde_key,onvalue="T",offvalue="")

        tarde.place(x=130,y=150,width=60)

        seccion =tk.Label(datos,text="Seccion:").place(x=200,y=150,width=50)
        seccion2 =tk.Entry(datos,border=3,relief='ridge')
        seccion2.insert(0,"A")
        seccion2.place(x=250,y=150,width=18)
#grupo
        grupo = tk.Label(datos,text="Grupo a cursar:").place(x=280,y=150,width=100)



        cont =tk.StringVar()
        cont2 = tk.StringVar()
        cont3 = tk.StringVar()

#recicla la funcion

        A = tk.Checkbutton(datos,text="A",variable=cont,onvalue="A",offvalue="")

        A.place(x=380,y=150,width=40)

        B = tk.Checkbutton(datos,text="B",variable=cont2,onvalue="B",offvalue="")
        B.place(x=420,y=150,width=40)

        C = tk.Checkbutton(datos,text="C",variable=cont3,onvalue="C",offvalue="")
        C.place(x=460,y=150,width=40)


        institucion = tk.Label(datos,text="Institucion de procedencia:").place(x=1,y=180,width=155)

        self.institucion2 = tk.Entry(datos,border=3,relief="ridge")
        self.institucion2.insert(0,"IUT")
        self.institucion2.bind("<KeyRelease>",lambda e:  validated(e,self.institucion2,self.del_hogar2))
        self.institucion2.place(x=150,y=180,width=150)

        del_hogar = tk.Label(datos, text="del Hogar:").place(x=300,y=180,width=60)
        self.del_hogar2 = tk.Entry(datos,border=3, relief="ridge")
        self.del_hogar2.place(x=360,y=180,width=150)

        parto_sencillo = tk.StringVar()

        parto = tk.Label(datos,text="Parto sencillo").place(x=4,y=210,width=80)
        self.parto2 = tk.Checkbutton(datos,border=3,variable=parto_sencillo,onvalue="sencillo",offvalue="")
        self.parto2.place(x=80,y=210,width=30)

##gemelo
        gemelocontrol =tk. StringVar()
        gemelocontrol2 = tk. StringVar()

        gemelotext =tk. Label(datos,text="Gemelos:").place(x=120,y=210,width=80)
        gemelo = tk.Checkbutton(datos,text="1ero",variable=gemelocontrol,onvalue="Gemelos",offvalue="")

        gemelo.place(x=200,y=210,width=40)
        gemelo2 =tk. Checkbutton(datos,text="2do",variable=gemelocontrol2,onvalue="Si",offvalue="")

        gemelo2.place(x=240,y=210,width=60)
##


##trillizos
        trillizoscontrol = tk.StringVar()
        trillizoscontrol2 = tk.StringVar()
        trillizoscontrol3 = tk.StringVar()

        trillizostext = tk.Label(datos,text="Trillizos:").place(x=300,y=210,width=60)
        trillizos = tk.Checkbutton(datos,text="1ero",variable=trillizoscontrol,onvalue="trillizos",offvalue="")

        trillizos.place(x=360,y=210,width=40)

        trillizos2 = tk.Checkbutton(datos,text="2do",variable=trillizoscontrol2,onvalue="Si",offvalue="")

        trillizos2.place(x=410,y=210,width=40)

        trillizos3=tk. Checkbutton(datos,text="3ero",variable=trillizoscontrol3,onvalue="Si",offvalue="")

        trillizos3.place(x=460,y=210,width=40)

##
        proceso_nacimiento =tk.Label(datos,text="Proceso de Nacimiento:").place(x=4,y=240,width=130)

        nacimientocontrol = tk.StringVar()
        nacimientocontrol2 = tk.StringVar()
        nacimientocontrol3 = tk.StringVar()
        nacimientocontrol4 = tk.StringVar()

        normal = tk.Checkbutton(datos,text="Normal",variable=nacimientocontrol,onvalue="N",offvalue="")
        normal.place(x=135,y=240,width=80)

        cesarea = tk.Checkbutton(datos,text="Cesarea",variable=nacimientocontrol2,onvalue="C",offvalue="")
        cesarea.place(x=220,y=240,width=80)

        con_forceps= tk.Checkbutton(datos,text="Con Forceps",variable=nacimientocontrol3,onvalue="F",offvalue="")
        con_forceps.place(x=300,y=240,width=100)

        a_termino= tk.Checkbutton(datos,text="A termino",variable=nacimientocontrol4,onvalue="T",offvalue="")
        a_termino.place(x=400,y=240,width=100)

##
#Frame4

        datos2 = tk.LabelFrame(self.frame4,border=4, relief="groove", text="Datos del alumno(a)")
        datos2.place(relx=0,rely=0,width=650,height=310)

        enfermedades = tk.Label(datos2,text="Enfermedades padecidas :").place(x=4,y=10,width=135)
        

        #####Keys

        enfermedadcontrol = tk.StringVar()
        enfermedadcontrol2= tk.StringVar()
        enfermedadcontrol3 = tk.StringVar()
        enfermedadcontrol4= tk.StringVar()

        enfermedadcontrol5 = tk.StringVar()
        enfermedadcontrol6= tk.StringVar()
        enfermedadcontrol7 = tk.StringVar()
        enfermedadcontrol8 = tk.StringVar()

        sarampion =tk. Checkbutton(datos2,text="Sarampion",variable=enfermedadcontrol,onvalue="Si",offvalue="")
        sarampion.deselect()
        sarampion.place(x=147,y=10,width=80)

        rubeola = tk.Checkbutton(datos2,text="Rubeola",variable=enfermedadcontrol2,onvalue="Si",offvalue="")
        sarampion.deselect()
        rubeola.place(x=225,y=10,width=80)

        lechina = tk.Checkbutton(datos2,text="Lechina",variable=enfermedadcontrol3,onvalue="Si",offvalue="")
        lechina.deselect()
        lechina.place(x=300,y=10,width=80)

        tosferina = tk.Checkbutton(datos2,text="Tosferina",variable=enfermedadcontrol4,onvalue="Si",offvalue="")
        tosferina.deselect()
        tosferina.place(x=370,y=10,width=80)

        meningitis =tk.Checkbutton(datos2,text="Meningitis",variable=enfermedadcontrol5,onvalue="Si",offvalue="")
        meningitis.deselect()
        meningitis.place(x=450,y=10,width=80)

        hepatitis = tk.Checkbutton(datos2,text="Hepatitis",variable=enfermedadcontrol6,onvalue="Si",offvalue="")
        hepatitis.deselect()
        hepatitis.place(x=535,y=10,width=85)

        parotiditis = tk.Checkbutton(datos2,text="Parotiditis",variable=enfermedadcontrol7,onvalue="Si",offvalue="")
        parotiditis.deselect()
        parotiditis.place(x=4,y=45,width=80)

        otras = tk.Checkbutton(datos2,text="Otras",variable=enfermedadcontrol8,onvalue="Si",offvalue="",command=lambda : otras_function(self.cuales2))
        otras.deselect()
        otras.place(x=90,y=45,width=60)

        cuales= tk.Label(datos2,text="Cuales:")
        cuales.place(x=155,y=45,width=60)
        self.cuales2 = tk. Entry(datos2,border=3,relief="ridge",state="disabled")
        self.cuales2.place(x=210,y=45,width=100)
        # ######

        vacunascontrol = tk.StringVar()
        vacunascontrol2= tk.StringVar()
        vacunascontrol3 = tk.StringVar()
        vacunascontrol4= tk.StringVar()

        vacunascontrol5 = tk.StringVar()
        vacunascontrol6= tk.StringVar()
        vacunascontrol7 = tk.StringVar()

        vacunas =tk.Label(datos2,text="Vacunas recibidas:").place(x=330,y=45,width=100)

        bcg = tk.Checkbutton(datos2,text="BCG",variable=vacunascontrol,onvalue="Si",offvalue="")
        bcg.deselect()
        bcg.place(x=435,y=45,width=45)

        antitetanica = tk.Checkbutton(datos2,text="Antitetanica",variable=vacunascontrol2,onvalue="Si",offvalue="")
        antitetanica.deselect()
        antitetanica.place(x=480,y=45,width=90)

        rubeola = tk.Checkbutton(datos2,text="Rubeola",variable=vacunascontrol3)
        rubeola.deselect()
        rubeola.place(x=4,y=80,width=80)

        triple = tk.Checkbutton(datos2,text="Triple",variable=vacunascontrol4,onvalue="Si",offvalue="")
        triple.deselect()
        triple.place(x=90,y=80,width=60)

        fiebre_amarilla = tk. Checkbutton(datos2,text="Fiebre Amarilla",variable=vacunascontrol5,onvalue="Si",offvalue="")
        fiebre_amarilla.deselect()
        fiebre_amarilla.place(x=150,y=80,width=120)

        polio = tk.Checkbutton(datos2,text="Polio",variable=vacunascontrol6,onvalue="Si",offvalue="")
        polio.deselect()
        polio.place(x=260,y=80,width=60)

        otras = tk.Checkbutton(datos2,text="Otras",variable=vacunascontrol7,onvalue="Si",offvalue="")
        otras.deselect()


        otras.place(x=320,y=80,width=60)

        alergia = tk.Label(datos2,text="Alergico(a):").place(x=380,y=80,width=80)
        self.alergia2 = tk.Entry(datos2,border=3,relief="ridge")
        self.alergia2.insert(0,"la soledad")
        self.alergia2.place(x=460,y=80,width=120)

###
        derechacontrol= tk.StringVar()
        izquierdacontrol = tk.StringVar()
        ambascontrol= tk.StringVar()

        mano = tk.Label(datos2,text="Que mano usa frecuentemente:").place(x=0,y=115,width=185)
        derecha = tk.Checkbutton(datos2,text="Derecha",variable=derechacontrol,onvalue="derecha",offvalue="")
        derecha.deselect()
        derecha.place(x=180,y=115,width=60)

        izquierda = tk. Checkbutton(datos2,text="Izquierda",variable=izquierdacontrol,onvalue="izquierda",offvalue="")
        izquierda.deselect()
        izquierda.place(x=254,y=115,width=80)

        ambas = tk.Checkbutton(datos2,text="Ambas",variable=ambascontrol,onvalue="ambos",offvalue="")
        ambas.deselect()
        ambas.place(x=330,y=115,width=80)


        el_nino = tk. Label(datos2,text="El niño(a). Pesa:").place(x=420,y=115,width=100)
        pesa = tk.Entry(datos2,border=3,relief="ridge")
        pesa.insert(0,"65")
        pesa.place(x=520,y=115,width=40)

        el_nino_mide = tk.Label(datos2,text="El niño mide:").place(x=4,y=150,width=80)
        mide = tk.Entry(datos2,border=3,relief="ridge")
        mide.insert(0,"1.73")
        mide.place(x=80,y=150,width=30)

        talla_camisa = tk.Label(datos2,text="Talla camisa:").place(x=120,y=150,width=80)
        talla = tk.Entry(datos2,border=3,relief="ridge")
        talla.insert(0,"S")
        talla.place(x=200,y=150,width=30)

        talla_pantalon =tk. Label(datos2,text="Talla Pantalon:").place(x=250,y=150,width=80)
        talla2 = tk.Entry(datos2,border=3,relief="ridge")
        talla2.insert(0,"32")
        talla2.place(x=330,y=150,width=30)

        talla_zapatos = tk.Label(datos2,text="Talla zapatos:").place(x=370,y=150,width=80)
        talla3 =tk. Entry(datos2,border=2,relief="ridge")
        talla3.insert(0,"43")
        talla3.place(x=450,y=150,width=30)



###
        padrecontrol= tk.StringVar()
        madrecontrol = tk.StringVar()
        abueloscontrol= tk.StringVar()
        otrocontrol= tk.StringVar()

        nino_vive = tk.Label(datos2,text="El niño vive con:").place(x=4,y=180,width=85)
        padre = tk.Checkbutton(datos2,text="Padre",variable=padrecontrol,onvalue="Si",offvalue="")
        padre.deselect()
        padre.place(x=90,y=185,width=70)

        madre= tk.Checkbutton(datos2,text="Madre",variable=madrecontrol,onvalue="Si",offvalue="")
        madre.deselect()
        madre.place(x=150,y=185,width=70)

        abuelos = tk.Checkbutton(datos2,text="Abuelos",variable=abueloscontrol,onvalue="Si",offvalue="")
        abuelos.deselect()
        abuelos.place(x=220,y=185,width=62)

        otro = tk.Checkbutton (
                datos2,
                command=lambda : otras_function(otro2),
                text="Otro :",variable=otrocontrol,onvalue="Si",offvalue="")
        otro.deselect()
        otro.place(x=300,y=185,width=60)

        otro2 = tk.Entry(datos2,border=2,relief="ridge",state="disabled")
        otro2.place(x=370,y=185,width=100)

        edad_hablar = tk.Label(datos2,text="Edad cuando empezo hablar :").place(x=260,y=220,width=160)
        edad_hablar2 = tk.Entry(datos2,border=2,relief="ridge")
        edad_hablar2.insert(0,"1")
        edad_hablar2.place(x=420,y=220,width=60)

        edad_caminar = tk.Label(datos2,text="Edad cuando empezo caminar:").place(x=4,y=220,width=160)
        edad_caminar2 = tk.Entry(datos2,border=2,relief="ridge")
        edad_caminar2.insert(0,"2")
        edad_caminar2.place(x=165,y=220,width=80)
###

        datos3 = tk.LabelFrame(self.frame5,text="Continuacion",border=3,relief="groove")
        datos3.place(relx=0,rely=0,width=500,height=250)

        duerme_nino = tk.Label(datos3,text="Con quien duerme el niño:").place(x=8,y=15,width=140)
        duerme_nino2 =tk.Entry(datos3,border=2,relief="ridge")
        duerme_nino2.insert(0,"solo")
        duerme_nino2.place(x=160,y=15,width=60)

        hermano_nino = tk.Label(datos3,text="Tiene hermanos en otro grupo o Primaria:").place(x=2,y=40,width=235)


        hermanocontrol= tk.StringVar()
        hermano2control = tk.StringVar()

        

        hermano_nino2 = tk.Checkbutton(datos3,text="Si",variable=hermanocontrol,onvalue='True',
        offvalue="",command=lambda : otras_function(hermano_nino5))
        hermano_nino2.deselect()
        hermano_nino2.place(x=230,y=40,width=40)

        hermano_nino3 = tk.Checkbutton(datos3,text="No",variable=hermano2control,onvalue='False',offvalue="")
        hermano_nino3.deselect()
        hermano_nino3.place(x=280,y=40,width=40)

        hermano_nino4 = tk.Label(datos3,text="Grado(s):")
        hermano_nino4.place(x=320,y=40,width=60)
        hermano_nino5 = tk.Entry(datos3,border=2,relief="ridge",state="disabled")
        hermano_nino5.place(x=380,y=40,width=80)

        habla_correctamente2 = tk.StringVar()

        habla_correctamente = tk.Label(datos3,text="Habla correctamente:").place(x=5,y=70,width=120)
        habla_correctamente_check = tk.Checkbutton(datos3,border=2,variable=habla_correctamente2,onvalue="si",offvalue="")
        habla_correctamente_check.place(x=130,y=70,width=40)

        cantar2 = tk.StringVar()

        cantar = tk.Label(datos3,text="Le gusta cantar:").place(x=170,y=70,width=100)
        cantar_check = tk.Checkbutton(datos3,border=2,variable=cantar2,onvalue="si",offvalue="")

        cantar_check.place(x=260,y=70,width=40)

        bailar2 = tk.StringVar()

        bailar = tk.Label(datos3,text="Le gusta bailar:").place(x=300,y=70,width=100)
        bailar_check = tk.Checkbutton(datos3,border=2,variable=bailar2,onvalue="si",offvalue="")
        bailar_check.place(x=400,y=70,width=40)

        contar_historias2 = tk.StringVar()

        contar_historias = tk.Label(datos3,text="Le gusta contar historias:").place(x=2,y=100,width=140)
        contar_historias_check =tk.Checkbutton(datos3,border="2",variable=contar_historias2,onvalue="si",offvalue="")
        contar_historias_check.place(x=140,y=100,width=40)

        actividades_fisicas2 = tk.StringVar()

        actividades_fisicas =tk. Label(datos3,text="Participa en actividades deportivas:").place(x=200,y=100,width=190)
        actividades_fisicas_check = tk.Checkbutton(datos3,border=2,variable=actividades_fisicas2,onvalue="si",offvalue="",command=lambda : otras_function(self.actividades_fisicas4))
        actividades_fisicas_check.place(x=400,y=100,width=40)
        actividades_fisicas3 = tk. Label(datos3,text="Cual(s):").place(x=3,y=130,width=40)
        self.actividades_fisicas4 =tk. Entry(datos3,border=2,relief="ridge",state="disabled")
        self.actividades_fisicas4.place(x=50,y=130,width=80)

        juega = tk.Label(datos3,text="Con quien juega generalmente :").place(x=140,y=130,width=170)
        juega2 = tk.Entry(datos3,border=2,relief="ridge")
        juega2.insert(0,"solo :(")
        juega2.place(x=320,y=130,width=100)

        juegos_realiza = tk.Label(datos3,text="Que juegos realiza en su hogar:").place(x=2,y=160,width=170)
        juegos_realiza2 = tk. Entry(datos3,border=2,relief="ridge")
        juegos_realiza2.insert(0,"mobile legends")
        juegos_realiza2.place(x=180,y=160,width=100)


### Datos representante ====================================================================================


class InformacionRepresentante(tk.Toplevel):
    def __init__(self,data,controller:BaseController,master):
        self.main_window = master
        self.controller = controller
        self.data = data

        super().__init__(master=master.window,width=400,height=500)
        self.wm_title('Representante: %s' % (self.data['nombres']))

        self.direcciones = self.controller.representante.getDireccionesRepresentante(self.data['cedula'])
        self.telefonos = self.controller.representante.getTelefonosRepresentante(self.data['cedula'])

        print(self.direcciones)
        

        match self.data['parentesco']:
            case 'padre':
                self.actualizarDatosPadre()
            case 'madre':
                self.actualizarDatosMadre()
            case 'representante':
                self.actualizarDatosRepresentante()

        # self.btn_open_planilla = tk.Button(self,text="Abrir Planilla")
        # self.btn_open_planilla.pack()
        # btnDelete = tk.Button(self,text="eliminar estudiante",command=lambda: self.deleteEstudiante(data['cedula_escolar']))
        # btnDelete.pack()

    def actualizarDatosPadre(self):
        padre = tk.LabelFrame(self,text="Datos del Padre",border=3,relief="groove")
        padre.place(relx=0.2,rely=0.1,width=300,height=300)

        nombre = tk.Label(padre,text="Nombres :")
        nombre.place(x=0,y=3,width=80)
        nombre_pa2 = tk.Entry(padre,border=2,relief="groove")
        nombre_pa2.insert(0,self.data['nombres'])
        nombre_pa2.place(x=85,y=3,width=140)
        apellido = tk.Label(padre,text="Apellidos:")
        apellido.place(x=0,y=28,width=60)
        apellido_pa = tk.Entry(padre,border=2,relief="groove")
        apellido_pa.insert(0,self.data['apellidos'])
        apellido_pa.place(x=70,y=30,width=140)

        ci = tk.Label(padre,text="C.I").place(x=0,y=60,width=20)
        ci_pa = tk.Entry(padre,border=2,relief="groove")
        ci_pa.insert(0,self.data['cedula'])
        ci_pa.place(x=30,y=60,width=60)

        nacionalidad = tk.Label(padre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad_pa = tk.Entry(padre,border=2,relief="groove")
        nacionalidad_pa.insert(0,self.data['nacionalidad'])
        nacionalidad_pa.place(x=200,y=60,width=90)

        profesion = tk.Label(padre,text="Profesion:").place(x=0,y=95,width=70)
        profesion_pa = tk.Entry(padre,border=2,relief="groove")
        profesion_pa.insert(0,self.data['profesion'])
        profesion_pa.place(x=70,y=95,width=100)


        habitacion = tk.Label(padre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion_pa = tk. Entry(padre,border="2",relief="groove")
        habitacion_pa.insert(0,'')
        habitacion_pa.place(x=140,y=130,width=140)

        telefonoh =  tk. Label(padre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh_pa = tk.Entry(padre,border=2,relief="groove")
        telefonoh_pa.insert(0,"11223349871")
        telefonoh_pa.place(x=40,y=160,width=80)

        trabajo = tk.Label(padre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo_pa = tk.Entry(padre,border=2,relief="groove")
        trabajo_pa.insert(0,"Bogota")
        trabajo_pa.place(x=140,y=190,width=140)

        telefonot = tk.Label(padre,text="Telf :").place(x=0,y=220,width=30)
        telefonot_pa = tk.Entry(padre,border=2,relief="groove")
        telefonot_pa.insert(0,"11223349871")
        telefonot_pa.place(x=50,y=220,width=80)



        viveninocontrol= tk.StringVar()
        vivenino2control = tk.StringVar()

        
        vive = tk.Label(padre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si = tk.Checkbutton(padre,text="Si",variable=viveninocontrol,onvalue="si",offvalue="")
        si.deselect()
        si.place(x=120,y=250,width=40,)

        no = tk.Checkbutton(padre,text="No",variable=vivenino2control,onvalue="no",offvalue="")
        no.deselect()
        no.place(x=170,y=250,width=40)

        


    def actualizarDatosMadre(self):
        madre = tk.LabelFrame(self,text="Datos de la Madre",border=3,relief="groove")
        madre.place(relx=0.2,rely=0.1,width=300,height=300)

        nombre_madre = tk.Label(madre,text="Nombres :")
        nombre_madre.place(x=0,y=3,width=120)
        nombre_madre2 = tk.Entry(madre,border=2,relief="groove")
        nombre_madre2.insert(0,"Naiby")
        nombre_madre2.place(x=140,y=3,width=140)

        apellido_madre = tk.Label(madre,text="Apellidos:")
        apellido_madre.place(x=0,y=28,width=60)
        apellido_madre2 = tk.Entry(madre,border=2,relief="groove")
        apellido_madre2.insert(0,"Bolivar")
        apellido_madre2.place(x=70,y=30,width=140)


        ci = tk.Label(madre,text="C.I").place(x=0,y=60,width=20)
        ci_ma = tk.Entry(madre,border=2,relief="groove")
        ci_ma.insert(0,"16229382")
        ci_ma.place(x=30,y=60,width=60)

        nacionalidad = tk.Label(madre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad_ma = tk.Entry(madre,border=2,relief="groove")
        nacionalidad_ma.insert(0,"venezolana")
        nacionalidad_ma.place(x=200,y=60,width=90)

        profesion = tk.Label(madre,text="Profesion:").place(x=0,y=95,width=70)
        profesion_ma = tk. Entry(madre,border=2,relief="groove")
        profesion_ma.insert(0,"escritora")
        profesion_ma.place(x=70,y=95,width=100)

        habitacion = tk. Label(madre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion_ma = tk.Entry(madre,border="2",relief="groove")
        habitacion_ma.insert(0,"Santa Teresa")
        habitacion_ma.place(x=140,y=130,width=140)

        telefonoh = tk. Label(madre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh_ma =tk. Entry(madre,border=2,relief="groove")
        telefonoh_ma.insert(0,"11223349871")
        telefonoh_ma.place(x=40,y=160,width=80)

        trabajo = tk.Label(madre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo_ma =tk.Entry(madre,border=2,relief="groove")
        trabajo_ma.insert(0,"Santa Teresa")
        trabajo_ma.place(x=140,y=190,width=140)

        telefonot = tk.Label(madre,text="Telf :").place(x=0,y=220,width=30)
        telefonot_ma = tk.Entry(madre,border=2,relief="groove")
        telefonot_ma.insert(0,"11223349871")
        telefonot_ma.place(x=50,y=220,width=80)

        vive_con_control_ma= tk.StringVar()
        vive_con_contro2_ma = tk.StringVar()

        vive = tk.Label(madre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si2 = tk.Checkbutton(madre,text="Si",variable=vive_con_control_ma,onvalue="si",offvalue="")
        si2.deselect()
        si2.place(x=120,y=250,width=40)

        no2 = tk.Checkbutton(madre,text="No",variable=vive_con_contro2_ma,onvalue="no",offvalue="")
        no2.deselect()
        no2.place(x=170,y=250,width=40)

    def actualizarDatosRepresentante(self):

        representante = tk.LabelFrame(self,border=2,relief="groove",text="Datos Representantes")
        representante.place(relx=0.2,rely=0.1,width=500,height=250)

        nombre = tk.Label(representante,text="Nombre:").place(x=0,y=5,width=60)
        nombre_re2 =tk.Entry(representante,border=2,relief="groove")
        nombre_re2.place(x=60,y=5,width=180)

        apellido_representante = tk.Label(representante,text="Apellido").place(x=240,y=5,width=60)
        apellido_re2 =tk. Entry(representante,border=2,relief="groove")
        apellido_re2.place(x=300,y=5,width=180)

        parentesco = tk.Label(representante,text="Parentesco").place(x=5, y=40, width=60)
        parentesco_re1 =tk. Entry(representante,border=2,relief="groove")
        parentesco_re1.place(x=70,y=40,width=155)

        ci = tk.Label(representante,text="C.I:").place(x=230,y=40,width=20)
        ci_re =tk. Entry(representante,border=2,relief="groove")
        ci_re.place(x=260,y=40,width=80)

        phone_re = tk.Label(representante,text="Telf:").place(x=350,y=40,width=20)
        phone_re1 =tk. Entry(representante,border=2,relief="groove")
        phone_re1.place(x=380,y=40,width=100)

        direccion1_hab =tk. Label(representante,text="Direccion de Habitación").place(x=5,y=70,width=130)
        direccion_hab = tk.Entry(representante,border=2,relief="groove")
        direccion_hab.place(x=140,y=70,width=200)

        phone_re =tk.Label(representante,text="Telf:").place(x=350,y=70,width=20)
        phone_re2 =tk.Entry(representante,border=2,relief="groove")
        phone_re2.place(x=380,y=70,width=100)

        direccion_tra =tk. Label(representante,text="Direccion de Trabajo").place(x=5.5,y=105,width=109)
        direccion_tra2 = tk.Entry(representante,border=2,relief="groove")
        direccion_tra2.place(x=120,y=105,width=220)

        phone_re =tk.Label(representante,text="Telf:").place(x=350,y=105,width=20)
        phone_re3 =tk.Entry(representante,border=2,relief="groove")
        phone_re3.place(x=380,y=105,width=100)

        direccion_f_Cer =tk.Label(representante,text="Direccion de Familiar Cercano:").place(x=4,y=140,width=170)
        direccion_f_Cer2 =tk.Entry(representante,border=2,relief="groove")
        direccion_f_Cer2.place(x=175,y=140,width=305)

        telefonot =  tk.Label(representante,text="Telf de Familiar Cercano:").place(x=5,y=180,width=140)
        telefonot_re2 =tk. Entry(representante,border=2,relief="groove")
        telefonot_re2.place(x=150,y=180,width=170)

    def deleteRepresentante(self,cedula):
        result = self._controller.eliminarRepresentante(cedula)

        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.main_window.controlPersonas()
        self.destroy()


class InformacionProfesor(tk.Toplevel):
    def __init__(self,data,controller: BaseController,master):
        self._controller = controller
        self.main_window = master
        super().__init__(master=master.window)
        self.wm_title('Profesor: %s' % (data['nombres']))

        # self.btn_open_planilla = tk.Button(self,text="Abrir Planilla")
        # self.btn_open_planilla.pack()

        # btnDelete = tk.Button(self,text="eliminar estudiante",command=lambda: self.deleteEstudiante(data['cedula_escolar']))
        # btnDelete.pack()




    def deleteUsuario(self,cedula):
        result = self._controller.eliminarUsuario(cedula)

        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.main_window.controlPersonas()
        self.destroy()


def validated(event,input1,input2,):

        if input1.get() != "":
                input2.configure(state="disabled")
        else:
                input2.configure(state="normal")

def otras_function(input):
        if input["state"] == "disabled":
                input.configure(state="normal")
        else:
                input.configure(state="disabled")

def otro_representante_function(self,notebook: ttk.Notebook):
        if notebook.tab(4)['state'] == "disabled":
                notebook.tab(4,state="normal")
                self.button_sin_representante.configure(state="disabled")
        else :
                notebook.tab(4,state="disabled")
                self.button_sin_representante.configure(state="normal")