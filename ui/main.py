from partials.base import BaseView
from controller.main import Controller
from tkcalendar import DateEntry
from tkinter.font import BOLD
from typing import List
from util.generateWord import Word


class App(BaseView):
    def __init__(self):
        super().__init__(title="nombre_colegio",geometry="700x530",controller=Controller)


        self.main()

        self.window.mainloop()


    def main(self):
        self.notebook = self.ttk.Notebook(self.window)
        self.frame1 = self.tk.Frame(self.notebook)
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.frame2 = self.ttk.Frame(self.notebook)
        self.frame2.place(relx=0,rely=0)



        self.controlPersonas()
        self.inscripcion()

        self.notebook.add(self.frame1,text="Busqueda")
        self.notebook.add(self.frame2,text="Inscripciones")
        # self.notebook2.add(self.frame2,text="1")


        self.notebook.place(relx=0,rely=0,relwidth=1,relheight=1)
        # self.notebook2.place(x=0,y=400,width=120,height=20)

    def validate_search(self, event):
        result = self.get_user()
        if self.search.get() == "":
            self.tree.delete(*self.tree.get_children())
            for item in result:
                if item[1] == "admin" or item[1] == self.session[1]:
                    continue
                self.tree.insert('', self.tk.END, values=(
                    item[0], item[1], item[2]))
            self.frame1.update()

    def inscripcion(self):
        self.notebook2 = self.ttk.Notebook(self.frame2)
        self.frame3 = self.ttk.Frame(self.notebook2)
        self.frame4 = self.ttk.Frame(self.notebook2)
        self.frame5 = self.ttk.Frame(self.notebook2)
        self.frame6 = self.ttk.Frame(self.notebook2)
        self.frame7 = self.ttk.Frame(self.notebook2)
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.notebook2.add(self.frame3,text="1")
        self.notebook2.add(self.frame4,text="2")
        self.notebook2.add(self.frame5,text="3")
        self.notebook2.add(self.frame6,text="4")
        self.notebook2.add(self.frame7, text="5")
        self.notebook2.place(relx=0,rely=0.25,relwidth=1,relheight=0.7)
        membrete = self.tk.Frame(self.frame2,border=3,relief="groove")
        membrete.place(x=205,y=15,width=300,height=100)
        lb1 = self.tk.Label(membrete,text="Republica Bolivariana de Venezuela.")
        lb1.pack()
        lb2 = self.tk.Label(membrete,text="Ministerio del poder Popular para la educacion.")
        lb2.pack()
        lb3 = self.tk.Label(membrete,text="Centro de Educacion Inicial")
        lb3.pack()
        lb4 = self.tk.Label(membrete,text="Josefina Molina Duque")
        lb4.pack()

        datos = self.tk.LabelFrame(self.frame3,border=4, relief="groove", text="Datos del alumno(a)")
        datos.place(x=25,y=15,width=650,height=310)

        nombre = self.tk.Label(datos,text="Nombres:").place(x=4,y=12,width=60)
        nombre2 =self.tk.Entry(datos,border=3,relief="ridge").place(x=65,y=12,width=100)

        apellido = self.tk.Label(datos,text="Apellido:").place(x=170,y=12,width=80)
        apellido2 = self.tk.Entry(datos,border="2",relief="ridge").place(x=235,y=12,width=100)

        fecha_nacimiento = self.tk.Label(datos,text="Fecha de Nacimiento :").place(x=370,y=12,width=115)
        fecha_nacimiento1 =DateEntry(datos,state="readonly").place(x=495,y=12, width=100)

        edad_anos = self.tk.Label(datos,text="Edad (Años): ").place(x=8,y=50,width=70)
        edad_anos2 =self.tk. Entry(datos, border=3, relief="ridge").place(x=80,y=50,width=25)

        meses = self.tk.Label(datos,text="Meses:").place(x=115,y=50,width=70)
        meses2 = self.tk.Entry(datos, border=3, relief="ridge").place(x=175,y=50,width=25)

        sexo = self.tk.Label(datos,text="Sexo").place(x=200,y=50,width=70)
        sexo_combo = self.ttk.Combobox(datos,values=["Masculino","Femenino","Omar"]).place(x=250,y=50,width=80)


        lugar_nacimiento = self.tk.Label(datos,text="Lugar de nacimiento:" ).place(x=0,y=90,width=120)
        lugar_nacimiento2 =self.tk. Entry(datos,border=3, relief="ridge").place(x=120,y=90,width=140)

        entidad_federal = self.tk.Label(datos,text="Entidad Federal:" ).place(x=270,y=90,width=120)
        entidad_federal2 =self.tk. Entry(datos,border=3,relief="ridge").place(x=380,y=90,width=140)

        nacionalidad = self.tk.Label(datos,text="Nacionalidad:").place(x=3,y=120,width=80)
        nacionalidad2 = self.tk.Entry(datos,border=3,relief='ridge').place(x=80,y=120,width=140)

        cdula_escolar = self.tk.Label(datos,text="Cedula Escolar Nº:").place(x=240,y=120,width=100)
        cdula_escolar2 = self.tk.Entry(datos,border=3,relief='ridge').place(x=340,y=120,width=140)

        turno = self.tk.Label(datos, text="Turno:").place(x=5,y=150,width=40)

        manana = self.tk.Checkbutton(datos,text="Mañana").place(x=50,y=150,width=80)

        tarde =self.tk. Checkbutton(datos,text="Tarde").place(x=130,y=150,width=60)


# def mostrar_valor_check():
#     etiqueta = Label(datos,text=control.get())
#     etiqueta = Label(datos,text=control2.get())



        seccion =self.tk. Label(datos,text="Seccion:").place(x=200,y=150,width=50)
        seccion2 =self.tk. Entry(datos,border=3,relief='ridge').place(x=250,y=150,width=18)

##grupo
        grupo = self.tk.Label(datos,text="Grupo a cursar:").place(x=280,y=150,width=100)

# cont = IntVar
# cont2 = IntVar
# cont3 = IntVar

#recicla la funcion

        A = self.tk.Checkbutton(datos,text="A").place(x=380,y=150,width=40)
        B = self.tk.Checkbutton(datos,text="B").place(x=420,y=150,width=40)
        C = self.tk.Checkbutton(datos,text="C").place(x=460,y=150,width=40)


        institucion = self.tk.Label(datos,text="Institucion de procedencia:").place(x=1,y=180,width=155)

        institucion2 = self.tk.Entry(datos,border=3,relief="ridge").place(x=150,y=180,width=150)

        del_hogar = self.tk. Label(datos, text="del Hogar:").place(x=300,y=180,width=60)
        del_hogar2 = self.tk.Entry(datos,border=3, relief="ridge").place(x=360,y=180,width=150)

        parto =self.tk. Label(datos,text="Parto sencillo").place(x=4,y=210,width=80)
        parto2 = self.tk.Entry(datos,border=3,relief="ridge").place(x=80,y=210,width=30)

##gemelo
# gemelocontrol = IntVar
# gemelocontrol2 = IntVar

        gemelotext =self.tk. Label(datos,text="Gemelos:").place(x=120,y=210,width=80)
        gemelo = self.tk.Checkbutton(datos,text="1ero").place(x=200,y=210,width=40)
        gemelo2 =self.tk. Checkbutton(datos,text="2do").place(x=240,y=210,width=60)
##


##trillizos
# trillizoscontrol = IntVar
# trillizoscontrol2 = IntVar
# trillizoscontrol3 = IntVar

        trillizostext = self.tk.Label(datos,text="Trillizos:").place(x=300,y=210,width=60)
        trillizos = self.tk.Checkbutton(datos,text="1ero").place(x=360,y=210,width=40)
        trillizos2 = self.tk.Checkbutton(datos,text="2do").place(x=410,y=210,width=40)
        trillizos3=self.tk. Checkbutton(datos,text="3ero").place(x=460,y=210,width=40)

##
        proceso_nacimiento =self.tk.Label(datos,text="Proceso de Nacimiento:").place(x=4,y=240,width=130)

# nacimientocontrol = IntVar
# nacimientocontrol2 = IntVar
# nacimientocontrol3 = IntVar
# nacimientocontrol4 = IntVar

        normal = self.tk.Checkbutton(datos,text="Normal").place(x=135,y=240,width=80)
        cesarea = self.tk.Checkbutton(datos,text="Cesarea").place(x=220,y=240,width=80)
        con_forceps= self.tk.Checkbutton(datos,text="Con Forceps").place(x=300,y=240,width=100)
        a_termino= self.tk.Checkbutton(datos,text="A termino").place(x=400,y=240,width=100)

##
#Frame4

        datos2 = self.tk.LabelFrame(self.frame4,border=4, relief="groove", text="Datos del alumno(a)")
        datos2.place(x=25,y=15,width=650,height=310)

        enfermedades = self.tk.Label(datos2,text="Enfermedades padecidas :").place(x=4,y=10,width=135)

        # enfermedadcontrol = IntVar
        # enfermedadcontrol2=IntVar
        # enfermedadcontrol3 = IntVar
        # enfermedadcontrol4=IntVar

        sarampion =self.tk. Checkbutton(datos2,text="Sarampion").place(x=147,y=10,width=80)
        rubeola = self.tk.Checkbutton(datos2,text="Rubeola").place(x=225,y=10,width=80)
        lechina = self.tk.Checkbutton(datos2,text="Lechina").place(x=300,y=10,width=80)
        tosferina = self.tk.Checkbutton(datos2,text="Tosferina").place(x=370,y=10,width=80)
        meningitis =self.tk.Checkbutton(datos2,text="Meningitis").place(x=450,y=10,width=80)
        hepatitis = self.tk.Checkbutton(datos2,text="Hepatitis").place(x=535,y=10,width=85)
        parotiditis = self.tk.Checkbutton(datos2,text="Parotiditis").place(x=4,y=45,width=80)
        otras = self.tk.Checkbutton(datos2,text="Otras").place(x=90,y=45,width=60)
        cuales= self.tk.Label(datos2,text="Cuales:").place(x=155,y=45,width=60)
        cuales2 =self.tk. Entry(datos2,border=3,relief="ridge").place(x=210,y=45,width=100)
        # ##

        vacunas = self.tk.Label(datos2,text="Vacunas recibidas:").place(x=330,y=45,width=100)
        bcg = self.tk.Checkbutton(datos2,text="BCG").place(x=435,y=45,width=45)
        antitetanica = self.tk.Checkbutton(datos2,text="Antitetanica").place(x=480,y=45,width=90)
        rubeola = self.tk.Checkbutton(datos2,text="Rubeola").place(x=4,y=80,width=80)
        triple =self.tk.Checkbutton(datos2,text="Triple").place(x=90,y=80,width=60)
        fiebre_amarilla =self.tk. Checkbutton(datos2,text="Fiebre Amarilla").place(x=150,y=80,width=120)
        polio = self.tk.Checkbutton(datos2,text="Polio").place(x=260,y=80,width=60)
        otras = self.tk.Checkbutton(datos2,text="Otras").place(x=320,y=80,width=60)

        alergia = self.tk.Label(datos2,text="Alergico(a):").place(x=380,y=80,width=80)
        alergia2 = self.tk.Entry(datos2,border=3,relief="ridge").place(x=460,y=80,width=120)

        mano = self.tk.Label(datos2,text="Que mano usa frecuentemente:").place(x=0,y=115,width=185)
        derecha = self.tk.Checkbutton(datos2,text="Derecha").place(x=180,y=115,width=60)
        izquierda =self.tk. Checkbutton(datos2,text="Izquierda").place(x=254,y=115,width=80)
        ambas = self.tk.Checkbutton(datos2,text="Ambas").place(x=330,y=115,width=80)


        el_nino =self.tk. Label(datos2,text="El niño(a). Pesa:").place(x=420,y=115,width=100)
        pesa = self.tk.Entry(datos2,border=3,relief="ridge").place(x=520,y=115,width=40)

        el_nino_mide = self.tk.Label(datos2,text="El niño mide:").place(x=4,y=150,width=80)
        mide = self.tk.Entry(datos2,border=3,relief="ridge").place(x=80,y=150,width=30)

        talla_camisa = self.tk.Label(datos2,text="Talla camisa:").place(x=120,y=150,width=80)
        talla = self.tk.Entry(datos2,border=3,relief="ridge").place(x=200,y=150,width=30)

        talla_pantalon =self.tk. Label(datos2,text="Talla Pantalon:").place(x=250,y=150,width=80)
        talla2 = self.tk.Entry(datos2,border=3,relief="ridge").place(x=330,y=150,width=30)

        talla_zapatos = self.tk.Label(datos2,text="Talla zapatos:").place(x=370,y=150,width=80)
        talla3 =self.tk. Entry(datos2,border=2,relief="ridge").place(x=450,y=150,width=30)


        nino_vive = self.tk.Label(datos2,text="El niño vive con:").place(x=4,y=180,width=85)
        padre = self.tk.Checkbutton(datos2,text="Padre").place(x=90,y=185,width=70)
        madre= self.tk.Checkbutton(datos2,text="Madre").place(x=150,y=185,width=70)
        abuelos = self.tk.Checkbutton(datos2,text="Abuelos").place(x=220,y=185,width=62)
        otro = self.tk.Checkbutton (datos2,text="Otro :").place(x=300,y=185,width=60)
        otro2 = self.tk.Entry(datos2,border=2,relief="ridge").place(x=370,y=185,width=100)

        edad_hablar = self.tk.Label(datos2,text="Edad cuando empezo hablar :").place(x=260,y=220,width=160)
        edad_hablar2 = self.tk.Entry(datos2,border=2,relief="ridge").place(x=420,y=220,width=60)

        edad_caminar = self.tk.Label(datos2,text="Edad cuando empezo caminar:").place(x=4,y=220,width=160)
        edad_caminar2 = self.tk.Entry(datos2,border=2,relief="ridge").place(x=165,y=220,width=80)
###

        datos3 = self.tk.LabelFrame(self.frame5,text="Continuacion",border=3,relief="groove")
        datos3.place(x=100,y=50,width=500,height=250)

        duerme_nino = self.tk.Label(datos3,text="Con quien duerme el niño:").place(x=8,y=15,width=140)
        duerme_nino2 =self.tk.Entry(datos3,border=2,relief="ridge").place(x=160,y=15,width=60)

        hermano_nino = self.tk.Label(datos3,text="Tiene hermanos en otro grupo o Primaria:").place(x=2,y=40,width=235)

        hermano_nino2 = self.tk.Checkbutton(datos3,text="Si").place(x=230,y=40,width=40)
        hermano_nino3 = self.tk.Checkbutton(datos3,text="No").place(x=280,y=40,width=40)
        hermano_nino4 = self.tk.Label(datos3,text="Grado(s):").place(x=320,y=40,width=60)
        hermano_nino5 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=380,y=40,width=80)

        habla_correctamente = self.tk.Label(datos3,text="Habla correctamente:").place(x=5,y=70,width=120)
        habla_correctamente2 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=130,y=70,width=40)

        cantar = self.tk.Label(datos3,text="Le gusta cantar:").place(x=170,y=70,width=100)
        cantar2 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=260,y=70,width=40)

        bailar = self.tk.Label(datos3,text="Le gusta bailar:").place(x=300,y=70,width=100)
        bailar2 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=400,y=70,width=40)

        contar_historias = self.tk.Label(datos3,text="Le gusta contar historias:").place(x=2,y=100,width=140)
        contar_historias2 =self.tk. Entry(datos3,border="2",relief="ridge").place(x=140,y=100,width=40)

        actividades_fisicas =self.tk. Label(datos3,text="Participa en actividades deportivas:").place(x=200,y=100,width=190)
        actividades_fisicas2 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=400,y=100,width=40)
        actividades_fisicas3 =self.tk. Label(datos3,text="Cual(s):").place(x=3,y=130,width=40)
        actividades_fisicas4 =self.tk. Entry(datos3,border=2,relief="ridge").place(x=50,y=130,width=80)

        juega = self.tk.Label(datos3,text="Con quien juega generalmente :").place(x=140,y=130,width=170)
        juega2 = self.tk.Entry(datos3,border=2,relief="ridge").place(x=320,y=130,width=100)

        juegos_realiza =self.tk. Label(datos3,text="Que juegos realiza en su hogar:").place(x=2,y=160,width=170)
        juegos_realiza2 =self.tk. Entry(datos3,border=2,relief="ridge").place(x=180,y=160,width=100)

##Datos del padre

        padre = self.tk.LabelFrame(self.frame6,text="Datos del Padre",border=3,relief="groove")
        padre.place(x=25,y=10,width=300,height=300)

        nombre = self.tk.Label(padre,text="Nombres :")
        nombre.place(x=0,y=3,width=80)
        nombre2 = self.tk.Entry(padre,border=2,relief="groove").place(x=85,y=3,width=140)
        
        apellido =self.tk.Label(padre,text="Apellidos:")
        apellido.place(x=0,y=28,width=60)
        apellido2 = self.tk.Entry(padre,border=2,relief="groove").place(x=70,y=30,width=140)

        ci =self.tk. Label(padre,text="C.I").place(x=0,y=60,width=20)
        ci2 =self.tk. Entry(padre,border=2,relief="groove").place(x=30,y=60,width=60)

        nacionalidad = self.tk.Label(padre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad2 = self.tk.Entry(padre,border=2,relief="groove").place(x=200,y=60,width=90)

        profesion =self.tk.Label(padre,text="Profesion:").place(x=0,y=95,width=70)
        profesion2 =self.tk. Entry(padre,border=2,relief="groove").place(x=70,y=95,width=100)

        habitacion =self.tk. Label(padre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion2 =self.tk. Entry(padre,border="2",relief="groove").place(x=140,y=130,width=140)

        telefonoh =self.tk. Label(padre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh2 =self.tk. Entry(padre,border=2,relief="groove").place(x=40,y=160,width=80)

        trabajo = self.tk.Label(padre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo2 =self.tk. Entry(padre,border=2,relief="groove").place(x=140,y=190,width=140)

        telefonot = self.tk.Label(padre,text="Telf :").place(x=0,y=220,width=30)
        telefonot2 = self.tk.Entry(padre,border=2,relief="groove").place(x=50,y=220,width=80)

        vive = self.tk.Label(padre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si = self.tk.Checkbutton(padre,text="Si").place(x=120,y=250,width=40)
        no = self.tk.Checkbutton(padre,text="No").place(x=170,y=250,width=40)

###Datos de la madre

        madre = self.tk.LabelFrame(self.frame6,text="Datos de la Madre",border=3,relief="groove")
        madre.place(x=370,y=3,width=300,height=300)

        nombre_madre = self.tk.Label(madre,text="Nombres y apellidos:")
        nombre_madre.place(x=0,y=3,width=120)
        nombre_madre2 = self.tk.Entry(madre,border=2,relief="groove").place(x=125,y=3,width=140)

        apellido_madre =self.tk.Label(madre,text="Apellidos:")
        apellido_madre.place(x=0,y=28,width=60)
        apellido_madre2 = self.tk.Entry(madre,border=2,relief="groove").place(x=70,y=30,width=140)


        ci =self.tk. Label(madre,text="C.I").place(x=0,y=60,width=20)
        ci2 =self.tk. Entry(madre,border=2,relief="groove").place(x=30,y=60,width=60)

        nacionalidad = self.tk.Label(madre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad2 = self.tk.Entry(madre,border=2,relief="groove").place(x=200,y=60,width=90)

        profesion =self.tk.Label(madre,text="Profesion:").place(x=0,y=95,width=70)
        profesion2 =self.tk. Entry(madre,border=2,relief="groove").place(x=70,y=95,width=100)

        habitacion =self.tk. Label(madre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion2 =self.tk. Entry(madre,border="2",relief="groove").place(x=140,y=130,width=140)

        telefonoh =self.tk. Label(madre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh2 =self.tk. Entry(madre,border=2,relief="groove").place(x=40,y=160,width=80)

        trabajo = self.tk.Label(madre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo2 =self.tk. Entry(madre,border=2,relief="groove").place(x=140,y=190,width=140)

        telefonot = self.tk.Label(madre,text="Telf :").place(x=0,y=220,width=30)
        telefonot2 = self.tk.Entry(madre,border=2,relief="groove").place(x=50,y=220,width=80)

        vive = self.tk.Label(madre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si = self.tk.Checkbutton(madre,text="Si").place(x=120,y=250,width=40)
        no = self.tk.Checkbutton(madre,text="No").place(x=170,y=250,width=40)

### Datos representante
        representante =self.tk.LabelFrame(self.frame7,border=2,relief="groove",text="Datos Representantes")
        representante.place(x=120,y=45,width=450,height=260)

        nombre = self.tk. Label(representante,text="Nombre:").place(x=0,y=5,width=60)
        nombre2 =self.tk. Entry(representante,border=2,relief="groove").place(x=100,y=5,width=140)

        apellido_representante = self.tk.Label(representante,text="Apellido").place(x=0,y=40,width=60)
        apellido2 =self.tk. Entry(representante,border=2,relief="groove").place(x=100,y=40,width=140)

        ci = self.tk.Label(representante,text="C.I").place(x=280,y=40,width=20)
        ci2 =self.tk. Entry(representante,border=2,relief="groove").place(x=300,y=40,width=60)

        nacionalidad =self.tk. Label(representante,text="Nacionalidad :").place(x=0,y=70,width=90)
        nacionalidad2 = self.tk.Entry(representante,border=2,relief="groove").place(x=90,y=70,width=90)

        profesion =self.tk.Label(representante,text="Profesion:").place(x=190,y=70,width=60)
        profesion2 =self.tk.Entry(representante,border=2,relief="groove").place(x=250,y=70,width=100)

        habitacion =self.tk.Label(representante,text="Direccion de Habitacion :").place(x=0,y=100,width=140)
        habitacion2 =self.tk.Entry(representante,border="2",relief="groove").place(x=150,y=100,width=140)

        telefonoh =self.tk.Label(representante,text="Telf :").place(x=0,y=140,width=30)
        telefonoh2 =self.tk.Entry(representante,border=2,relief="groove").place(x=30,y=140,width=80)

        trabajo =self.tk.Label(representante,text="Direccion de Trabajo :").place(x=120,y=140,width=120)
        trabajo2 =self.tk.Entry(representante,border=2,relief="groove").place(x=250,y=140,width=140)

        telefonot =self.tk.Label(representante,text="Telf :").place(x=0,y=180,width=30)
        telefonot2 =self.tk. Entry(representante,border=2,relief="groove").place(x=40,y=180,width=80)

        vive =self.tk.Label(representante,text="Vive con el niño(a) :").place(x=120,y=180,width=120)
        si =self.tk. Checkbutton(representante,text="Si").place(x=240,y=180,width=40)
        no = self.tk.Checkbutton(representante,text="No").place(x=290,y=180,width=40)








    def controlPersonas(self):
        frame_search = self.tk.Frame(self.frame1,bg="#000")
        frame_search.place(relx=0, rely=0, relwidth=1, relheight=0.3)
        self.search = self.ttk.Entry(frame_search, justify="right",validate="key",validatecommand=(self.frame1.register(self.validate_entry_number), "%S"))
        self.search.place(relx=0.34, rely=0.2, width=220, height=25)
        self.search.bind("<FocusOut>", self.validate_search)


        self.select = self.ttk.Combobox(frame_search, values=(
            "nombres", "apellidos", "cedula"), state="readonly")
        self.select.current(0)
        self.select.place(relx=0.34, rely=0.21, width=70,)

        self.select.bind("<<ComboboxSelected>>",lambda event: self.validate_param(self.select.get()))

        btn_search = self.tk.Button(frame_search,bg="#041d9b",border=0,fg="#fff", text="Buscar", command=lambda: self.search_user(
            self.search.get(), self.select.get()))
        btn_search.place(relx=0.46, rely=0.6, width=60, height=35)


        columns = ("nombres","apellidos","cedula")
        self.tree = self.ttk.Treeview(self.frame1,columns=columns,show="headings")

        self.tree.heading("nombres",text="nombres")
        self.tree.heading("apellidos",text="apellidos")
        self.tree.heading("cedula",text="cedula")



        # self.get_user()

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.place(relx=0,rely=0.3,relwidth=1,relheight=0.6)


        scrollbar = self.ttk.Scrollbar(self.frame1, orient=self.tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.98,rely=0.3,relwidth=0.02,relheight=0.6)

    # def buscar(self, search, param):
    #     if search.get() == "":
    #         return self.root.bell()

    #     self.carga = tk.Toplevel()
    #     self.carga.wm_geometry("200x30")
    #     carga = ttk.Progressbar(self.carga)

    #     carga.pack()
    #     carga.start(30)

    #     result = self.ctrl.busqueda(search.get(), param.get())

    #     if not (isinstance(result, list)):
    #         messagebox.showerror("Error", result)
    #     else:
    #         if len(result) > 0:
    #             self.carga.destroy()
    #             self.tree.delete(*self.tree.get_children())
    #             for item in result:
    #                 self.tree.insert('', tk.END, values=(
    #                     item[0], item[1], item[2]))
    #             self.frame1.update()


    def search_user(self,search,param):

        result = self._controller.search_user(search.capitalize(),param)
        if result != ():
            return result
        return []


    def get_user(self):
        return self._controller.get_user()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            self.person = self.tk.Toplevel()
            self.person.wm_title("usuario")


    def validate_entry_number(self,text):


        if not(text.isdecimal()):
            self.root.bell()
            return False
        return True

    def validate_entry_text(self,text):


        for item in text:
            if item.isdigit():
                self.root.bell()


                return False
            return True
        

    def validate_param(self,param):
        if param == "cedula":
            self.search.delete(0,'end')
            self.search["validatecommand"] = (self.frame1.register(self.validate_entry_number), "%S")
        else:
            self.search.delete(0,'end')
            self.search["validatecommand"] = (self.frame1.register(self.validate_entry_text), "%S")