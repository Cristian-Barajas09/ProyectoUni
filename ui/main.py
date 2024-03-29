from partials.view.baseView import BaseView
from controller.AppController import Controller
from tkcalendar import DateEntry
from babel.numbers import *
from datetime import date
from tkinter import messagebox,dialog
from tkinter.filedialog import askdirectory
from util.helpers import read_env_value
from .Informacion import  InformacionRepresentante,InformacionEstudiante,InformacionProfesor
# from .partials.inscripcion import inscripcion
from tkinter import ttk
import os

class App(BaseView):
    __table_name = 'estudiantes'
    def __init__(self,session):
        super().__init__(title="C.E.I Josefina Molina de Duque",geometry="900x530",controller=Controller)
        self.icon()
        self.session = session
        self.main()

        self.resizable(0,0)
        self.config()

        self.window.mainloop()


    def main(self):
        # self.menu()
        self.notebook = self.ttk.Notebook(self.window)
        self.frame1 = self.tk.Frame(self.notebook)
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.frame2 = self.tk.Frame(self.notebook,bg="#19E9E2")
        self.frame2.place(relx=0,rely=0)



        self.controlPersonas()
        self.inscripcion()



        self.notebook.add(self.frame1,text="Busqueda")
        self.notebook.add(self.frame2,text="Inscripciones")


        self.notebook.place(relx=0,rely=0,relwidth=1,relheight=1)




    def menu(self):
        self.frame_menu = self.tk.Frame(bg='#333')
        self.frame_menu.place(relwidth=0.09,relheight=1,x=0,y=0)
        print(os.path.join(self.carpeta_imagenes,'register.png'))

        frmimg1 = self.tk.Frame(self.frame_menu,bg="#333")
        frmimg1.place(relwidth=1,relheight=0.8)

        img1 = self.image(os.path.join(self.carpeta_imagenes,'register.png'),(200,500))
        icon = self.tk.Label(frmimg1,image=img1,bg="#333")
        icon.place(relx=0,rely=0.1,relheight=1,relwidth=1)


    def validate_search(self, event):
        result = self.get_users()
        if self.search.get() == "":
            self.tree.delete(*self.tree.get_children())
            for item in result:
                if item['rol'] == "admin":
                    continue
                self.tree.insert('', self.tk.END, values=(
                    item['nombres'], item['apellidos'], item['cedula']))
            self.controlPersonas()

    def register_child(self,
                    anno_cursar:int,
                    nombre:str,
                    apellido:str,
                    f_di:date,
                    f_m:date,
                    f_an:date,
                    e_a:int,
                    e_m:int,
                    sex:str,
                    l_n:str,
                    en_fed:str,
                    nacionalidad:str,
                    ced_escolar:int,
                    man:str,
                    tar:str,
                    secc:str,
                    A:str,
                    B:str,
                    C:str,
                    instituto_pro:str,
                    del_hogar:str,
                    senci:str,
                    gem:str,
                    g_1,
                    g_2,
                    trill,
                    t_1,
                    t_2,
                    t_3,
                    nor,
                    ces,
                    forcep,
                    term,
                    saram,
                    ru,
                    lec,
                    osf,
                    me,
                    he,
                    pa,
                    otras,
                    cuales,
                    BCG,
                    anti,
                    rube,
                    tripe,
                    f_a,
                    pol,
                    otras_2,
                    der,
                    izq,
                    amb,
                    peso,
                    altura,
                    talla,
                    pantalon,
                    zap,
                    padre,
                    madre,
                    abuelos,
                    otro_fami,
                    empezo_hab,
                    emp_camin,
                    quien_duer,
                    si_her,
                    no_her,
                    gra_her,
                    hab_correc,
                    canta,
                    baila,
                    historias,
                    si_dep,
                    cual_dep,
                    juega_con,
                    juegos_casa,
                    nom_pa,
                    ape_pa,
                    ced_pa,
                    nac_pa,
                    pro_pa,
                    hab_pa,
                    tel_pa,
                    trabajo_pa,
                    tel_pa_tra,
                    vi_si,
                    vi_no,
                    nombre_ma,
                    ape_ma,
                    ced_ma,
                    nac_ma,
                    pro_ma,
                    hab_ma,
                    tel_ma,
                    tra_ma,
                    tel_ma_trab,
                    vive_con_el_si,
                    vive_con_el_no,
                    nombre_re = '',
                    apellido_re = '',
                    parentesco = '',
                    cedula = '',
                    telefono = '',
                    direccion_casa = '',
                    telefono_hab_re = '',
                    direccion_trabajo = '',
                    telefono_t_re = '',
                    telefono_cer_re = '',
                    dir_cer_re = '',
                    ):

        datos = {
        'anno_cursar':anno_cursar,
        'nombre':nombre,
        'apellido':apellido,
        'f_di':f_di,
        'f_m':f_m,
        'f_an':f_an,
        'e_a':e_a,
        'e_m':e_m,
        'sex':sex,
        'l_n':l_n,
        'en_fed':en_fed,
        'nacionalidad':nacionalidad,
        'ced_escolar':ced_escolar,
        'man':man,
        'tar':tar,
        'secc':secc,
        'A':A,
        'B':B,
        'C':C,
        'instituto_pro':instituto_pro,
        'del_hogar':del_hogar,
        'senci':senci,
        'gem':gem,
        'g_1':g_1,
        'g_2':g_2,
        'trill':trill,
        't_1':t_1,
        't_2':t_2,
        't_3':t_3,
        'nor':nor,
        'ces':ces,
        'forcep':forcep,
        'term':term,
        'saram':saram,
        'ru':ru,
        'lec':lec,
        'osf':osf,
        'me':me,
        'he':he,
        'pa':pa,
        'otras':otras,
        'cuales':cuales,
        'BCG':BCG,
        'anti':anti,
        'rube':rube,
        'tripe':tripe,
        'f_a':f_a,
        'pol':pol,
        'otras_2':otras_2,
        'der':der,
        'izq':izq,
        'amb':amb,
        'peso':peso,
        'altura':altura,
        'talla':talla,
        'pantalon':pantalon,
        'zap':zap,
        'padre':padre,
        'madre':madre,
        'abuelos':abuelos,
        'otro_fami':otro_fami,
        'empezo_hab':empezo_hab,
        'emp_camin':emp_camin,
        'quien_duer':quien_duer,
        'si_her':si_her,
        'no_her':no_her,
        'gra_her':gra_her,
        'hab_correc':hab_correc,
        'canta':canta,
        'baila':baila,
        'historias':historias,
        'si_dep':si_dep,
        'cual_dep':cual_dep,
        'juega_con':juega_con,
        'juegos_casa':juegos_casa,
        'nom_pa':nom_pa,
        'ape_pa':ape_pa,
        'ced_pa':ced_pa,
        'nac_pa':nac_pa,
        'pro_pa':pro_pa,
        'hab_pa':hab_pa,
        'tel_pa':tel_pa,
        'trabajo_pa':trabajo_pa,
        'tel_pa_tra':tel_pa_tra,
        'vi_si':vi_si,
        'vi_no':vi_no,
        'nombre_ma':nombre_ma,
        'ape_ma':ape_ma,
        'ced_ma':ced_ma,
        'nac_ma':nac_ma,
        'pro_ma':pro_ma,
        'hab_ma':hab_ma,
        'tel_hab_ma':tel_ma,
        'tra_ma':tra_ma,
        'tel_trab_ma':tel_ma_trab,
        'vive_con_el_si':vive_con_el_si,
        'vive_con_el_no':vive_con_el_no,
        'nombre_re':nombre_re if nombre_re else 'False',
        'apellido_re':apellido_re,
        'parentesco':parentesco,
        'cedula':cedula,
        'telefono':telefono,
        'direccion_casa':direccion_casa,
        'telefono_hab_re':telefono_hab_re,
        'direccion_trabajo':direccion_trabajo,
        'telefono_t_re':telefono_t_re,
        'telefono_cer_re':telefono_cer_re,
        'dir_cer_re':dir_cer_re,
        }


        self._controller.registerChild(**datos)






    def controlPersonas(self):
        frame_search = self.tk.Frame(self.frame1,bg="#222")
        frame_search.place(relx=0, rely=0, relwidth=1, relheight=0.3)


        self.notebook_person = self.ttk.Notebook(self.frame1)
        self.frame_estudiantes = self.tk.Frame(self.notebook_person)
        self.frame_users = self.tk.Frame(self.notebook_person)
        self.frame_representantes = self.tk.Frame(self.notebook_person)
        self.notebook_person.add(self.frame_estudiantes,text="estudiantes")
        self.notebook_person.add(self.frame_users,text="profesores")
        self.notebook_person.add(self.frame_representantes,text="representantes")
        self.notebook_person.bind("<<NotebookTabChanged>>",lambda evt: self.cambiar_parametro_de_busqueda(self.notebook_person ,evt))


        # search
        self.search = self.tk.Entry(frame_search, validate="key",validatecommand=(self.frame1.register(self.validate_entry_text), "%S"),bg="#fff")
        self.tk.Frame(frame_search,bg="#38B1EE").place(relx=0.27, rely=0.35, width=220, height=2)

        self.search.place(relx=0.27, rely=0.2, width=220, height=25)
        self.search.bind("<FocusOut>", self.validate_search)


        self.select = self.ttk.Combobox(frame_search, values=(
            "nombres", "apellidos", "cedula"), state="readonly")
        self.select.current(0)
        self.select.place(relx=0.517, rely=0.2, width=70,height=25)

        self.select.bind("<<ComboboxSelected>>",lambda event: self.validate_param(self.select.get()))

        btn_search = self.tk.Button(frame_search,bg="#041d9b",border=0,fg="#fff", text="Buscar", command=lambda: self.buscar(
            self.search, self.select),cursor="hand2")
        btn_search.place(relx=0.595, rely=0.2, width=70, height=25)
        #search

        self.table_estudiantes()
        self.table_users()
        self.table_representantes()


        btn_generar_plantilla = self.tk.Button(self.frame1,bg="#041d9b",border=0,fg="#fff", text="Generar Planilla del Personal",command=self.generarPlanilla)
        btn_generar_plantilla.place(relx=0.38, rely=0.92, width=160, height=35)

        self.notebook_person.place(relx=0,rely=0.3,relwidth=1,relheight=0.6)

    def table_users(self):
        
        columns = ("nombres","apellidos","cedula")
        self.tree2 = self.ttk.Treeview(self.frame_users,columns=columns,show="headings")

        self.tree2.heading("nombres",text="nombres")
        self.tree2.heading("apellidos",text="apellidos")
        self.tree2.heading("cedula",text="cedula")



        for item in self.get_users():
            self.tree2.insert('',self.tk.END,values=(item['nombres'],item['apellidos'],item['cedula']))

        self.tree2.bind('<<TreeviewSelect>>', self.item_selected_usuarios)

        self.tree2.pack()


        scrollbar = self.ttk.Scrollbar(self.frame1, orient=self.tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.98,rely=0.3,relwidth=0.02,relheight=0.6)

    def table_estudiantes(self):

        columns = ("nombres","apellidos","cedula")
        self.tree = self.ttk.Treeview(self.frame_estudiantes,columns=columns,show="headings",)


        self.tree.heading("nombres",text="nombres")
        self.tree.heading("apellidos",text="apellidos")
        self.tree.heading("cedula",text="cedula")



        for item in self.get_estudiantes():
            self.tree.insert('',self.tk.END,values=(item['nombres'],item['apellidos'],item['cedula']))

        self.tree.bind('<<TreeviewSelect>>', self.item_selected_estudiantes)

        self.tree.pack()


        scrollbar = self.ttk.Scrollbar(self.frame1, orient=self.tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.98,rely=0.3,relwidth=0.02,relheight=0.6)



    def table_representantes(self):
        columns = ("nombres","apellidos","cedula")
        self.tree3 = self.ttk.Treeview(self.frame_representantes,columns=columns,show="headings")

        self.tree3.heading("nombres",text="nombres")
        self.tree3.heading("apellidos",text="apellidos")
        self.tree3.heading("cedula",text="cedula")



        for item in self.get_representantes():
            self.tree3.insert('',self.tk.END,values=(item['nombres'],item['apellidos'],item['cedula']))

        self.tree3.bind('<<TreeviewSelect>>', self.item_selected_representante)

        self.tree3.pack()


        scrollbar = self.ttk.Scrollbar(self.frame1, orient=self.tk.VERTICAL, command=self.tree.yview)
        self.tree3.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.98,rely=0.3,relwidth=0.02,relheight=0.6)

    def buscar(self, search, param):
        if search.get() == "":
            return self.window.bell()

        self.carga = self.tk.Toplevel()
        self.carga.wm_geometry("200x30")
        carga = self.ttk.Progressbar(self.carga)

        carga.pack()
        carga.start(30)

        param = param.get()

        if self.__table_name == 'estudiantes' and param == 'cedula':
            param = 'cedula_escolar'



        result = self._controller.search(search.get(), param,self.__table_name)

        if result == ():
            self.carga.destroy()
            messagebox.showerror("hubo un problema",f"no hay nadie con ese {param}")
        else:
            if len(result) > 0:
                self.carga.destroy()
                self.tree.delete(*self.tree.get_children())
                for item in result:
                    self.tree.insert('', self.tk.END, values=(
                        item['nombres'], item['apellidos'], item['cedula']))
                self.frame1.update()



    def get_users(self):
 
        return self._controller.getUsers()


    def get_estudiantes(self):
        return self._controller.getEstudiantes()

    def get_representantes(self):
        return self._controller.getRepresentantes()

    def item_selected_estudiantes(self,event):
        values = []
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            values = item['values']
        result = self._controller.obtenerEstudiante(values[2])

        InformacionEstudiante(result,self._controller,self)




    def item_selected_representante(self,event):
        values = []
        for selected_item in self.tree3.selection():
            item = self.tree3.item(selected_item)
            values = item['values']

        result = self._controller.obtenerRepresentante(values[2])

        InformacionRepresentante(result,self._controller,self)

    def item_selected_usuarios(self,event):
        values = []
        for selected_item in self.tree2.selection():
            item = self.tree2.item(selected_item)
            values = item['values']

        result = self._controller.obtenerUsuario(values[2])

        InformacionProfesor(result,self._controller,self)


    def validate_entry_number(self,text:str):
        if not(text.isdecimal()):
            self.window.bell()
            return False
        return True

    def validate_entry_text(self,text:str):

        for item in text:
            if item.isdigit():
                self.window.bell()


                return False
            return True


    def validate_param(self,param):
        
        if param == "cedula" or param == "cedula_escolar":
            self.search.delete(0,'end')
            self.search["validatecommand"] = (self.frame1.register(self.validate_entry_number), "%S")
        else:
            self.search.delete(0,'end')
            self.search["validatecommand"] = (self.frame1.register(self.validate_entry_text), "%S")


    def generarPlanilla(self):

        env = read_env_value("RUTA_REPORTE")

        ruta = askdirectory(initialdir=env)
        result = self._controller.generarPlanilla(ruta)

        if result:
            return messagebox.showinfo("exito","reporte guardado con exito")
        return messagebox.showerror("error","no se pudo guardar el reporte")


    def cambiar_parametro_de_busqueda(self,notebook ,event):
            name_notebook =  notebook.tab(notebook.select(),'text')
            if name_notebook == "estudiantes":
                self.__table_name = 'estudiantes'
            elif name_notebook == "profesores":
                self.__table_name = 'users'
            elif name_notebook == 'representantes':
                self.__table_name = 'representantes'

    def inscripcion(self):
        self.notebook2:ttk.Notebook = self.ttk.Notebook(self.frame2)
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
        self.notebook2.add(self.frame7, text="5",state="disabled")
        self.notebook2.place(relx=0,rely=0.25,relwidth=1,relheight=0.7)
        membrete = self.tk.Frame(self.frame2,border=3,relief="groove")

        ## TODO : acomodar las keys (Frank)
        membrete.place(x=205,y=10,width=300,height=120)
        lb1 = self.tk.Label(membrete,text="Republica Bolivariana de Venezuela.")
        lb1.pack()
        lb2 = self.tk.Label(membrete,text="Ministerio del poder Popular para la educacion.")
        lb2.pack()
        lb3 = self.tk.Label(membrete,text="Centro de Educacion Inicial")
        lb3.pack()
        lb4 = self.tk.Label(membrete,text="Josefina Molina Duque")
        lb4.pack()

        ano = self.tk.Label(membrete,text="Año Escolar :")
        ano.place(x=20,y=85,width=80)
        ano2 = f"{date.today().year} - {date.today().year + 1}"


        ano2_label = self.tk.Label(membrete,text=ano2)
        ano2_label.place(x=120,y=85,width=90)

        datos = self.tk.LabelFrame(self.frame3,border=4, relief="groove", text="Datos del alumno(a)")
        datos.place(x=25,y=15,width=650,height=310)

        nombre = self.tk.Label(datos,text="Nombres:").place(x=4,y=12,width=60)
        nombre_es2 =self.tk.Entry(datos,border=3,relief="ridge")
        nombre_es2.insert(0,"cristian")
        nombre_es2.place(x=65,y=12,width=100)


        apellido = self.tk.Label(datos,text="Apellido:").place(x=170,y=12,width=80)
        apellido_es = self.tk.Entry(datos,border="2",relief="ridge")
        apellido_es.insert(0,"barajas")
        apellido_es.place(x=235,y=12,width=100)

        fecha_nacimiento = self.tk.Label(datos,text="Fecha de Nacimiento :").place(x=370,y=12,width=115)
        fecha_nacimiento1 =DateEntry(datos,state="readonly")
        fecha_nacimiento1.place(x=495,y=12, width=100)

        edad_anos = self.tk.Label(datos,text="Edad (Años): ").place(x=8,y=50,width=70)
        edad_anos2 =self.tk. Entry(datos, border=3, relief="ridge")
        edad_anos2.insert(0,"20")
        edad_anos2.place(x=80,y=50,width=25)

        meses = self.tk.Label(datos,text="Meses:").place(x=115,y=50,width=70)
        meses2 = self.tk.Entry(datos, border=3, relief="ridge")
        meses2.insert(0,"20")
        meses2.place(x=175,y=50,width=25)

        sexo = self.tk.Label(datos,text="Sexo").place(x=200,y=50,width=70)
        sexo_combo = self.ttk.Combobox(datos,values=["Masculino","Femenino"])

        sexo_combo.current(0)

        sexo_combo.place(x=250,y=50,width=80)


        lugar_nacimiento = self.tk.Label(datos,text="Lugar de nacimiento:" ).place(x=0,y=90,width=120)
        lugar_nacimiento2 = self.tk.Entry(datos,border=3, relief="ridge")
        lugar_nacimiento2.insert(0,"San cristobal")
        lugar_nacimiento2.place(x=120,y=90,width=140)

        entidad_federal = self.tk.Label(datos,text="Entidad Federal:" ).place(x=270,y=90,width=120)
        entidad_federal2 =self.tk. Entry(datos,border=3,relief="ridge")
        entidad_federal2.insert(0,"Tachira")
        entidad_federal2.place(x=380,y=90,width=140)

        nacionalidad = self.tk.Label(datos,text="Nacionalidad:").place(x=3,y=120,width=80)
        nacionalidad2 = self.tk.Entry(datos,border=3,relief='ridge')
        nacionalidad2.insert(0,"Venezolano")
        nacionalidad2.place(x=80,y=120,width=140)

        cdula_escolar = self.tk.Label(datos,text="Cedula Escolar Nº:").place(x=240,y=120,width=100)
        cdula_escolar2 = self.tk.Entry(datos,border=3,relief='ridge')
        cdula_escolar2.insert(0,"31357876")
        cdula_escolar2.place(x=340,y=120,width=140)


        manana_key=self.tk.StringVar()
        tarde_key = self.tk.StringVar()

        turno = self.tk.Label(datos, text="Turno:")
        turno.place(x=5,y=150,width=40)

        manana = self.tk.Checkbutton(datos,text="Mañana",variable=manana_key,onvalue="M",offvalue="")

        manana.place(x=50,y=150,width=80)

        tarde =self.tk. Checkbutton(datos,text="Tarde",variable=tarde_key,onvalue="T",offvalue="")

        tarde.place(x=130,y=150,width=60)


# def mostrar_valor_check():
#     etiqueta = Label(datos,text=control.get())
#     etiqueta = Label(datos,text=control2.get())



        seccion =self.tk.Label(datos,text="Seccion:").place(x=200,y=150,width=50)
        seccion2 =self.tk.Entry(datos,border=3,relief='ridge')
        seccion2.insert(0,"A")
        seccion2.place(x=250,y=150,width=18)
#grupo
        grupo = self.tk.Label(datos,text="Grupo a cursar:").place(x=280,y=150,width=100)



        cont =self.tk.StringVar()
        cont2 = self.tk.StringVar()
        cont3 = self.tk.StringVar()

#recicla la funcion

        A = self.tk.Checkbutton(datos,text="A",variable=cont,onvalue="A",offvalue="")

        A.place(x=380,y=150,width=40)

        B = self.tk.Checkbutton(datos,text="B",variable=cont2,onvalue="B",offvalue="")
        B.place(x=420,y=150,width=40)

        C = self.tk.Checkbutton(datos,text="C",variable=cont3,onvalue="C",offvalue="")
        C.place(x=460,y=150,width=40)


        institucion = self.tk.Label(datos,text="Institucion de procedencia:").place(x=1,y=180,width=155)

        self.institucion2 = self.tk.Entry(datos,border=3,relief="ridge")
        self.institucion2.insert(0,"IUT")
        self.institucion2.bind("<KeyRelease>",lambda e:  validated(e,self.institucion2,self.del_hogar2))
        self.institucion2.place(x=150,y=180,width=150)

        del_hogar = self.tk. Label(datos, text="del Hogar:").place(x=300,y=180,width=60)
        self.del_hogar2 = self.tk.Entry(datos,border=3, relief="ridge")
        self.del_hogar2.place(x=360,y=180,width=150)

        parto_sencillo =self.tk.StringVar()

        parto =self.tk.Label(datos,text="Parto sencillo").place(x=4,y=210,width=80)
        self.parto2 = self.tk.Checkbutton(datos,border=3,variable=parto_sencillo,onvalue="sencillo",offvalue="")
        self.parto2.place(x=80,y=210,width=30)

##gemelo
        gemelocontrol =self.tk. StringVar()
        gemelocontrol2 = self.tk. StringVar()

        gemelotext =self.tk. Label(datos,text="Gemelos:").place(x=120,y=210,width=80)
        gemelo = self.tk.Checkbutton(datos,text="1ero",variable=gemelocontrol,onvalue="Gemelos",offvalue="")

        gemelo.place(x=200,y=210,width=40)
        gemelo2 =self.tk. Checkbutton(datos,text="2do",variable=gemelocontrol2,onvalue="Si",offvalue="")

        gemelo2.place(x=240,y=210,width=60)
##


##trillizos
        trillizoscontrol = self.tk.StringVar()
        trillizoscontrol2 = self.tk.StringVar()
        trillizoscontrol3 = self.tk.StringVar()

        trillizostext = self.tk.Label(datos,text="Trillizos:").place(x=300,y=210,width=60)
        trillizos = self.tk.Checkbutton(datos,text="1ero",variable=trillizoscontrol,onvalue="trillizos",offvalue="")

        trillizos.place(x=360,y=210,width=40)

        trillizos2 = self.tk.Checkbutton(datos,text="2do",variable=trillizoscontrol2,onvalue="Si",offvalue="")

        trillizos2.place(x=410,y=210,width=40)

        trillizos3=self.tk. Checkbutton(datos,text="3ero",variable=trillizoscontrol3,onvalue="Si",offvalue="")

        trillizos3.place(x=460,y=210,width=40)

##
        proceso_nacimiento =self.tk.Label(datos,text="Proceso de Nacimiento:").place(x=4,y=240,width=130)

        nacimientocontrol = self.tk.StringVar()
        nacimientocontrol2 = self.tk.StringVar()
        nacimientocontrol3 = self.tk.StringVar()
        nacimientocontrol4 = self.tk.StringVar()

        normal = self.tk.Checkbutton(datos,text="Normal",variable=nacimientocontrol,onvalue="N",offvalue="")
        normal.place(x=135,y=240,width=80)

        cesarea = self.tk.Checkbutton(datos,text="Cesarea",variable=nacimientocontrol2,onvalue="C",offvalue="")
        cesarea.place(x=220,y=240,width=80)

        con_forceps= self.tk.Checkbutton(datos,text="Con Forceps",variable=nacimientocontrol3,onvalue="F",offvalue="")
        con_forceps.place(x=300,y=240,width=100)

        a_termino= self.tk.Checkbutton(datos,text="A termino",variable=nacimientocontrol4,onvalue="T",offvalue="")
        a_termino.place(x=400,y=240,width=100)

##
#Frame4

        datos2 = self.tk.LabelFrame(self.frame4,border=4, relief="groove", text="Datos del alumno(a)")
        datos2.place(x=25,y=15,width=650,height=310)

        enfermedades = self.tk.Label(datos2,text="Enfermedades padecidas :").place(x=4,y=10,width=135)
        

        #####Keys

        enfermedadcontrol = self.tk.StringVar()
        enfermedadcontrol2= self.tk.StringVar()
        enfermedadcontrol3 = self.tk.StringVar()
        enfermedadcontrol4= self.tk.StringVar()

        enfermedadcontrol5 = self.tk.StringVar()
        enfermedadcontrol6= self.tk.StringVar()
        enfermedadcontrol7 = self.tk.StringVar()
        enfermedadcontrol8 = self.tk.StringVar()

        sarampion =self.tk. Checkbutton(datos2,text="Sarampion",variable=enfermedadcontrol,onvalue="Si",offvalue="")
        sarampion.deselect()
        sarampion.place(x=147,y=10,width=80)

        rubeola = self.tk.Checkbutton(datos2,text="Rubeola",variable=enfermedadcontrol2,onvalue="Si",offvalue="")
        sarampion.deselect()
        rubeola.place(x=225,y=10,width=80)

        lechina = self.tk.Checkbutton(datos2,text="Lechina",variable=enfermedadcontrol3,onvalue="Si",offvalue="")
        lechina.deselect()
        lechina.place(x=300,y=10,width=80)

        tosferina = self.tk.Checkbutton(datos2,text="Tosferina",variable=enfermedadcontrol4,onvalue="Si",offvalue="")
        tosferina.deselect()
        tosferina.place(x=370,y=10,width=80)

        meningitis =self.tk.Checkbutton(datos2,text="Meningitis",variable=enfermedadcontrol5,onvalue="Si",offvalue="")
        meningitis.deselect()
        meningitis.place(x=450,y=10,width=80)

        hepatitis = self.tk.Checkbutton(datos2,text="Hepatitis",variable=enfermedadcontrol6,onvalue="Si",offvalue="")
        hepatitis.deselect()
        hepatitis.place(x=535,y=10,width=85)

        parotiditis = self.tk.Checkbutton(datos2,text="Parotiditis",variable=enfermedadcontrol7,onvalue="Si",offvalue="")
        parotiditis.deselect()
        parotiditis.place(x=4,y=45,width=80)

        otras = self.tk.Checkbutton(datos2,text="Otras",variable=enfermedadcontrol8,onvalue="Si",offvalue="",command=lambda : otras_function(self.cuales2))
        otras.deselect()
        otras.place(x=90,y=45,width=60)

        cuales= self.tk.Label(datos2,text="Cuales:")
        cuales.place(x=155,y=45,width=60)
        self.cuales2 =self.tk. Entry(datos2,border=3,relief="ridge",state="disabled")
        self.cuales2.place(x=210,y=45,width=100)
        # ######

        vacunascontrol = self.tk.StringVar()
        vacunascontrol2= self.tk.StringVar()
        vacunascontrol3 = self.tk.StringVar()
        vacunascontrol4= self.tk.StringVar()

        vacunascontrol5 = self.tk.StringVar()
        vacunascontrol6= self.tk.StringVar()
        vacunascontrol7 = self.tk.StringVar()

        vacunas = self.tk.Label(datos2,text="Vacunas recibidas:").place(x=330,y=45,width=100)

        bcg = self.tk.Checkbutton(datos2,text="BCG",variable=vacunascontrol,onvalue="Si",offvalue="")
        bcg.deselect()
        bcg.place(x=435,y=45,width=45)

        antitetanica = self.tk.Checkbutton(datos2,text="Antitetanica",variable=vacunascontrol2,onvalue="Si",offvalue="")
        antitetanica.deselect()
        antitetanica.place(x=480,y=45,width=90)

        rubeola = self.tk.Checkbutton(datos2,text="Rubeola",variable=vacunascontrol3)
        rubeola.deselect()
        rubeola.place(x=4,y=80,width=80)

        triple =self.tk.Checkbutton(datos2,text="Triple",variable=vacunascontrol4,onvalue="Si",offvalue="")
        triple.deselect()
        triple.place(x=90,y=80,width=60)

        fiebre_amarilla =self.tk. Checkbutton(datos2,text="Fiebre Amarilla",variable=vacunascontrol5,onvalue="Si",offvalue="")
        fiebre_amarilla.deselect()
        fiebre_amarilla.place(x=150,y=80,width=120)

        polio = self.tk.Checkbutton(datos2,text="Polio",variable=vacunascontrol6,onvalue="Si",offvalue="")
        polio.deselect()
        polio.place(x=260,y=80,width=60)

        otras = self.tk.Checkbutton(datos2,text="Otras",variable=vacunascontrol7,onvalue="Si",offvalue="")
        otras.deselect()


        otras.place(x=320,y=80,width=60)

        alergia = self.tk.Label(datos2,text="Alergico(a):").place(x=380,y=80,width=80)
        self.alergia2 = self.tk.Entry(datos2,border=3,relief="ridge")
        self.alergia2.insert(0,"la soledad")
        self.alergia2.place(x=460,y=80,width=120)

###
        derechacontrol= self.tk.StringVar()
        izquierdacontrol = self.tk.StringVar()
        ambascontrol= self.tk.StringVar()

        mano = self.tk.Label(datos2,text="Que mano usa frecuentemente:").place(x=0,y=115,width=185)
        derecha = self.tk.Checkbutton(datos2,text="Derecha",variable=derechacontrol,onvalue="derecha",offvalue="")
        derecha.deselect()
        derecha.place(x=180,y=115,width=60)

        izquierda =self.tk. Checkbutton(datos2,text="Izquierda",variable=izquierdacontrol,onvalue="izquierda",offvalue="")
        izquierda.deselect()
        izquierda.place(x=254,y=115,width=80)

        ambas = self.tk.Checkbutton(datos2,text="Ambas",variable=ambascontrol,onvalue="ambos",offvalue="")
        ambas.deselect()
        ambas.place(x=330,y=115,width=80)


        el_nino =self.tk. Label(datos2,text="El niño(a). Pesa:").place(x=420,y=115,width=100)
        pesa = self.tk.Entry(datos2,border=3,relief="ridge")
        pesa.insert(0,"65")
        pesa.place(x=520,y=115,width=40)

        el_nino_mide = self.tk.Label(datos2,text="El niño mide:").place(x=4,y=150,width=80)
        mide = self.tk.Entry(datos2,border=3,relief="ridge")
        mide.insert(0,"1.73")
        mide.place(x=80,y=150,width=30)

        talla_camisa = self.tk.Label(datos2,text="Talla camisa:").place(x=120,y=150,width=80)
        talla = self.tk.Entry(datos2,border=3,relief="ridge")
        talla.insert(0,"S")
        talla.place(x=200,y=150,width=30)

        talla_pantalon =self.tk. Label(datos2,text="Talla Pantalon:").place(x=250,y=150,width=80)
        talla2 = self.tk.Entry(datos2,border=3,relief="ridge")
        talla2.insert(0,"32")
        talla2.place(x=330,y=150,width=30)

        talla_zapatos = self.tk.Label(datos2,text="Talla zapatos:").place(x=370,y=150,width=80)
        talla3 =self.tk. Entry(datos2,border=2,relief="ridge")
        talla3.insert(0,"43")
        talla3.place(x=450,y=150,width=30)



###
        padrecontrol= self.tk.StringVar()
        madrecontrol = self.tk.StringVar()
        abueloscontrol= self.tk.StringVar()
        otrocontrol= self.tk.StringVar()

        nino_vive = self.tk.Label(datos2,text="El niño vive con:").place(x=4,y=180,width=85)
        padre = self.tk.Checkbutton(datos2,text="Padre",variable=padrecontrol,onvalue="Si",offvalue="")
        padre.deselect()
        padre.place(x=90,y=185,width=70)

        madre= self.tk.Checkbutton(datos2,text="Madre",variable=madrecontrol,onvalue="Si",offvalue="")
        madre.deselect()
        madre.place(x=150,y=185,width=70)

        abuelos = self.tk.Checkbutton(datos2,text="Abuelos",variable=abueloscontrol,onvalue="Si",offvalue="")
        abuelos.deselect()
        abuelos.place(x=220,y=185,width=62)

        otro = self.tk.Checkbutton (
                datos2,
                command=lambda : otras_function(otro2),
                text="Otro :",variable=otrocontrol,onvalue="Si",offvalue="")
        otro.deselect()
        otro.place(x=300,y=185,width=60)

        otro2 = self.tk.Entry(datos2,border=2,relief="ridge",state="disabled")
        otro2.place(x=370,y=185,width=100)

        edad_hablar = self.tk.Label(datos2,text="Edad cuando empezo hablar :").place(x=260,y=220,width=160)
        edad_hablar2 = self.tk.Entry(datos2,border=2,relief="ridge")
        edad_hablar2.insert(0,"1")
        edad_hablar2.place(x=420,y=220,width=60)

        edad_caminar = self.tk.Label(datos2,text="Edad cuando empezo caminar:").place(x=4,y=220,width=160)
        edad_caminar2 = self.tk.Entry(datos2,border=2,relief="ridge")
        edad_caminar2.insert(0,"2")
        edad_caminar2.place(x=165,y=220,width=80)
###

        datos3 = self.tk.LabelFrame(self.frame5,text="Continuacion",border=3,relief="groove")
        datos3.place(x=100,y=50,width=500,height=250)

        duerme_nino = self.tk.Label(datos3,text="Con quien duerme el niño:").place(x=8,y=15,width=140)
        duerme_nino2 =self.tk.Entry(datos3,border=2,relief="ridge")
        duerme_nino2.insert(0,"solo")
        duerme_nino2.place(x=160,y=15,width=60)

        hermano_nino = self.tk.Label(datos3,text="Tiene hermanos en otro grupo o Primaria:").place(x=2,y=40,width=235)


        hermanocontrol= self.tk.StringVar()
        hermano2control = self.tk.StringVar()

        

        hermano_nino2 = self.tk.Checkbutton(datos3,text="Si",variable=hermanocontrol,onvalue='True',
        offvalue="",command=lambda : otras_function(hermano_nino5))
        hermano_nino2.deselect()
        hermano_nino2.place(x=230,y=40,width=40)

        hermano_nino3 = self.tk.Checkbutton(datos3,text="No",variable=hermano2control,onvalue='False',offvalue="")
        hermano_nino3.deselect()
        hermano_nino3.place(x=280,y=40,width=40)

        hermano_nino4 = self.tk.Label(datos3,text="Grado(s):")
        hermano_nino4.place(x=320,y=40,width=60)
        hermano_nino5 = self.tk.Entry(datos3,border=2,relief="ridge",state="disabled")
        hermano_nino5.place(x=380,y=40,width=80)

        habla_correctamente2 = self.tk.StringVar()

        habla_correctamente = self.tk.Label(datos3,text="Habla correctamente:").place(x=5,y=70,width=120)
        habla_correctamente_check = self.tk.Checkbutton(datos3,border=2,variable=habla_correctamente2,onvalue="si",offvalue="")
        habla_correctamente_check.place(x=130,y=70,width=40)

        cantar2 = self.tk.StringVar()

        cantar = self.tk.Label(datos3,text="Le gusta cantar:").place(x=170,y=70,width=100)
        cantar_check = self.tk.Checkbutton(datos3,border=2,variable=cantar2,onvalue="si",offvalue="")

        cantar_check.place(x=260,y=70,width=40)

        bailar2 = self.tk.StringVar()

        bailar = self.tk.Label(datos3,text="Le gusta bailar:").place(x=300,y=70,width=100)
        bailar_check = self.tk.Checkbutton(datos3,border=2,variable=bailar2,onvalue="si",offvalue="")
        bailar_check.place(x=400,y=70,width=40)

        contar_historias2 = self.tk.StringVar()

        contar_historias = self.tk.Label(datos3,text="Le gusta contar historias:").place(x=2,y=100,width=140)
        contar_historias_check =self.tk.Checkbutton(datos3,border="2",variable=contar_historias2,onvalue="si",offvalue="")
        contar_historias_check.place(x=140,y=100,width=40)

        actividades_fisicas2 = self.tk.StringVar()

        actividades_fisicas =self.tk. Label(datos3,text="Participa en actividades deportivas:").place(x=200,y=100,width=190)
        actividades_fisicas_check = self.tk.Checkbutton(datos3,border=2,variable=actividades_fisicas2,onvalue="si",offvalue="",command=lambda : otras_function(self.actividades_fisicas4))
        actividades_fisicas_check.place(x=400,y=100,width=40)
        actividades_fisicas3 =self.tk. Label(datos3,text="Cual(s):").place(x=3,y=130,width=40)
        self.actividades_fisicas4 =self.tk. Entry(datos3,border=2,relief="ridge",state="disabled")
        self.actividades_fisicas4.place(x=50,y=130,width=80)

        juega = self.tk.Label(datos3,text="Con quien juega generalmente :").place(x=140,y=130,width=170)
        juega2 = self.tk.Entry(datos3,border=2,relief="ridge")
        juega2.insert(0,"solo :(")
        juega2.place(x=320,y=130,width=100)

        juegos_realiza =self.tk. Label(datos3,text="Que juegos realiza en su hogar:").place(x=2,y=160,width=170)
        juegos_realiza2 =self.tk. Entry(datos3,border=2,relief="ridge")
        juegos_realiza2.insert(0,"mobile legends")
        juegos_realiza2.place(x=180,y=160,width=100)

        ##Datos del padre ==================================================

        padre = self.tk.LabelFrame(self.frame6,text="Datos del Padre",border=3,relief="groove")
        padre.place(x=25,y=10,width=300,height=300)

        nombre = self.tk.Label(padre,text="Nombres :")
        nombre.place(x=0,y=3,width=80)
        nombre_pa2 = self.tk.Entry(padre,border=2,relief="groove")
        nombre_pa2.insert(0,"Juan")
        nombre_pa2.place(x=85,y=3,width=140)
        
        apellido =self.tk.Label(padre,text="Apellidos:")
        apellido.place(x=0,y=28,width=60)
        apellido_pa = self.tk.Entry(padre,border=2,relief="groove")
        apellido_pa.insert(0,"Barajas")
        apellido_pa.place(x=70,y=30,width=140)

        ci =self.tk. Label(padre,text="C.I").place(x=0,y=60,width=20)
        ci_pa =self.tk. Entry(padre,border=2,relief="groove")
        ci_pa.insert(0,"15503303")
        ci_pa.place(x=30,y=60,width=60)

        nacionalidad = self.tk.Label(padre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad_pa = self.tk.Entry(padre,border=2,relief="groove")
        nacionalidad_pa.insert(0,"Venezolana")
        nacionalidad_pa.place(x=200,y=60,width=90)

        profesion =self.tk.Label(padre,text="Profesion:").place(x=0,y=95,width=70)
        profesion_pa =self.tk. Entry(padre,border=2,relief="groove")
        profesion_pa.insert(0,"Carguero")
        profesion_pa.place(x=70,y=95,width=100)

        habitacion =self.tk. Label(padre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion_pa =self.tk. Entry(padre,border="2",relief="groove")
        habitacion_pa.insert(0,"Bogota")
        habitacion_pa.place(x=140,y=130,width=140)

        telefonoh =self.tk. Label(padre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh_pa =self.tk.Entry(padre,border=2,relief="groove")
        telefonoh_pa.insert(0,"11223349871")
        telefonoh_pa.place(x=40,y=160,width=80)

        trabajo = self.tk.Label(padre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo_pa =self.tk. Entry(padre,border=2,relief="groove")
        trabajo_pa.insert(0,"Bogota")
        trabajo_pa.place(x=140,y=190,width=140)

        telefonot = self.tk.Label(padre,text="Telf :").place(x=0,y=220,width=30)
        telefonot_pa = self.tk.Entry(padre,border=2,relief="groove")
        telefonot_pa.insert(0,"11223349871")
        telefonot_pa.place(x=50,y=220,width=80)



        viveninocontrol= self.tk.StringVar()
        vivenino2control = self.tk.StringVar()

        vive = self.tk.Label(padre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si = self.tk.Checkbutton(padre,text="Si",variable=viveninocontrol,onvalue="si",offvalue="")
        si.deselect()
        si.place(x=120,y=250,width=40,)

        no = self.tk.Checkbutton(padre,text="No",variable=vivenino2control,onvalue="no",offvalue="")
        no.deselect()
        no.place(x=170,y=250,width=40)

        ###Datos de la madre ===================================================

        madre = self.tk.LabelFrame(self.frame6,text="Datos de la Madre",border=3,relief="groove")
        madre.place(x=370,y=3,width=300,height=300)

        nombre_madre = self.tk.Label(madre,text="Nombres :")
        nombre_madre.place(x=0,y=3,width=120)
        nombre_madre2 = self.tk.Entry(madre,border=2,relief="groove")
        nombre_madre2.insert(0,"Naiby")
        nombre_madre2.place(x=140,y=3,width=140)

        apellido_madre =self.tk.Label(madre,text="Apellidos:")
        apellido_madre.place(x=0,y=28,width=60)
        apellido_madre2 = self.tk.Entry(madre,border=2,relief="groove")
        apellido_madre2.insert(0,"Bolivar")
        apellido_madre2.place(x=70,y=30,width=140)


        ci =self.tk. Label(madre,text="C.I").place(x=0,y=60,width=20)
        ci_ma =self.tk. Entry(madre,border=2,relief="groove")
        ci_ma.insert(0,"16229382")
        ci_ma.place(x=30,y=60,width=60)

        nacionalidad = self.tk.Label(madre,text="Nacionalidad :").place(x=110,y=60,width=90)
        nacionalidad_ma = self.tk.Entry(madre,border=2,relief="groove")
        nacionalidad_ma.insert(0,"venezolana")
        nacionalidad_ma.place(x=200,y=60,width=90)

        profesion = self.tk.Label(madre,text="Profesion:").place(x=0,y=95,width=70)
        profesion_ma =self.tk. Entry(madre,border=2,relief="groove")
        profesion_ma.insert(0,"escritora")
        profesion_ma.place(x=70,y=95,width=100)

        habitacion =self.tk. Label(madre,text="Direccion de Habitacion :").place(x=0,y=130,width=140)
        habitacion_ma =self.tk. Entry(madre,border="2",relief="groove")
        habitacion_ma.insert(0,"Santa Teresa")
        habitacion_ma.place(x=140,y=130,width=140)

        telefonoh =self.tk. Label(madre,text="Telf :").place(x=0,y=160,width=30)
        telefonoh_ma =self.tk. Entry(madre,border=2,relief="groove")
        telefonoh_ma.insert(0,"11223349871")
        telefonoh_ma.place(x=40,y=160,width=80)

        trabajo = self.tk.Label(madre,text="Direccion de Trabajo :").place(x=0,y=190,width=120)
        trabajo_ma =self.tk.Entry(madre,border=2,relief="groove")
        trabajo_ma.insert(0,"Santa Teresa")
        trabajo_ma.place(x=140,y=190,width=140)

        telefonot = self.tk.Label(madre,text="Telf :").place(x=0,y=220,width=30)
        telefonot_ma = self.tk.Entry(madre,border=2,relief="groove")
        telefonot_ma.insert(0,"11223349871")
        telefonot_ma.place(x=50,y=220,width=80)

        vive_con_control_ma= self.tk.StringVar()
        vive_con_contro2_ma = self.tk.StringVar()

        vive = self.tk.Label(madre,text="Vive con el niño(a) :").place(x=0,y=250,width=120)
        si2 = self.tk.Checkbutton(madre,text="Si",variable=vive_con_control_ma,onvalue="si",offvalue="")
        si2.deselect()
        si2.place(x=120,y=250,width=40)

        no2 = self.tk.Checkbutton(madre,text="No",variable=vive_con_contro2_ma,onvalue="no",offvalue="")
        no2.deselect()
        no2.place(x=170,y=250,width=40)


        otro_representante = self.tk.Checkbutton(self.frame6,text="Otro Representante",command=lambda : otro_representante_function(self,self.notebook2))
        otro_representante.deselect()
        otro_representante.place(x=720,y=250,width=120)

        self.button_sin_representante = self.tk.Button(self.frame6,text="Guardar",state="normal",command=lambda : self.register_child(
            anno_cursar = date.today().year,nombre=nombre_es2.get(),apellido=apellido_es.get(),f_di=fecha.day,f_m=fecha.month,
            f_an=fecha.year,e_a=edad_anos2.get(),e_m=meses2.get(),sex=sexo_combo.get(),l_n=lugar_nacimiento2.get(),
            en_fed=entidad_federal2.get(),nacionalidad=nacionalidad2.get(),ced_escolar=cdula_escolar2.get(),man=manana_key.get(),
            tar=tarde_key.get(),secc=seccion2.get(),A=cont.get(),B=cont2.get(),C=cont3.get(),instituto_pro=self.institucion2.get(),
            del_hogar=self.del_hogar2.get(),emp_camin=edad_caminar2.get(),senci=parto_sencillo.get(),gem="",g_1=gemelocontrol.get(),g_2=gemelocontrol2.get(),trill="",
            t_1=trillizoscontrol.get(),t_2=trillizoscontrol2.get(),t_3=trillizoscontrol3.get(),nor=nacimientocontrol.get(),
            ces=nacimientocontrol2.get(),forcep=nacimientocontrol3.get(),term=nacimientocontrol4.get(),
            saram=enfermedadcontrol.get(),ru=enfermedadcontrol2.get(),lec=enfermedadcontrol3.get(),osf=enfermedadcontrol4.get(),
            me=enfermedadcontrol5.get(),he=enfermedadcontrol6.get(),pa=enfermedadcontrol7.get(),otras=enfermedadcontrol8.get(),
            cuales=self.cuales2.get(),BCG=vacunascontrol.get(),anti=vacunascontrol2.get(),rube=vacunascontrol3.get(),
            tripe=vacunascontrol4.get(),f_a=vacunascontrol5.get(),pol=vacunascontrol6.get(),otras_2=self.alergia2.get(),
            der=derechacontrol.get(),izq=izquierdacontrol.get(),amb=ambascontrol.get(),peso=pesa.get(),altura=mide.get(),
            talla=talla.get(),pantalon=talla2.get(),zap=talla3.get(),padre=padrecontrol.get(),madre=madrecontrol.get(),
            abuelos=abueloscontrol.get(),otro_fami=otrocontrol.get(),empezo_hab=edad_hablar2.get(),quien_duer=duerme_nino2.get(),
            si_her=hermanocontrol.get(),no_her=hermano2control.get(),gra_her=hermano_nino5.get(),
            hab_correc=habla_correctamente2.get(),canta=cantar2.get(),baila=bailar2.get(),historias=contar_historias2.get(),
            si_dep=actividades_fisicas2.get(),cual_dep=self.actividades_fisicas4.get(),juega_con=juega2.get(),juegos_casa=juegos_realiza2.get(),
            nom_pa=nombre_pa2.get(),ape_pa=apellido_pa.get(),ced_pa=ci_pa.get(),nac_pa=nacionalidad_pa.get(),
            pro_pa=profesion_pa.get(),hab_pa=habitacion_pa.get(),tel_pa=telefonoh_pa.get(),trabajo_pa=trabajo_pa.get(),
            tel_pa_tra=telefonoh_pa.get(),vi_si=viveninocontrol.get(),vi_no=vivenino2control.get(),nombre_ma=nombre_madre2.get(),
            ape_ma=apellido_madre2.get(),ced_ma=ci_ma.get(),nac_ma=nacionalidad_ma.get(),pro_ma=profesion_ma.get(),
            hab_ma=habitacion_ma.get(),tel_ma=telefonoh_ma.get(),tra_ma=trabajo_ma.get(),tel_ma_trab=telefonot_ma.get(),
            vive_con_el_si=vive_con_control_ma.get(),vive_con_el_no=vive_con_contro2_ma.get()
        ))
        self.button_sin_representante.place(x=720,y=300,width=120)

### Datos representante ====================================================================================
        representante =self.tk.LabelFrame(self.frame7,border=2,relief="groove",text="Datos Representantes")
        representante.place(x=105,y=40,width=500,height=250)

        nombre = self.tk.Label(representante,text="Nombre:").place(x=0,y=5,width=60)
        nombre_re2 =self.tk.Entry(representante,border=2,relief="groove")
        nombre_re2.place(x=60,y=5,width=180)

        apellido_representante = self.tk.Label(representante,text="Apellido").place(x=240,y=5,width=60)
        apellido_re2 =self.tk. Entry(representante,border=2,relief="groove")
        apellido_re2.place(x=300,y=5,width=180)

        parentesco = self.tk.Label(representante,text="Parentesco").place(x=5, y=40, width=60)
        parentesco_re1 =self.tk. Entry(representante,border=2,relief="groove")
        parentesco_re1.place(x=70,y=40,width=155)

        ci = self.tk.Label(representante,text="C.I:").place(x=230,y=40,width=20)
        ci_re =self.tk. Entry(representante,border=2,relief="groove")
        ci_re.place(x=260,y=40,width=80)

        phone_re = self.tk.Label(representante,text="Telf:").place(x=350,y=40,width=20)
        phone_re1 =self.tk. Entry(representante,border=2,relief="groove")
        phone_re1.place(x=380,y=40,width=100)

        direccion1_hab =self.tk. Label(representante,text="Direccion de Habitación").place(x=5,y=70,width=130)
        direccion_hab = self.tk.Entry(representante,border=2,relief="groove")
        direccion_hab.place(x=140,y=70,width=200)

        phone_re =self.tk.Label(representante,text="Telf:").place(x=350,y=70,width=20)
        phone_re2 =self.tk.Entry(representante,border=2,relief="groove")
        phone_re2.place(x=380,y=70,width=100)

        direccion_tra =self.tk. Label(representante,text="Direccion de Trabajo").place(x=5.5,y=105,width=109)
        direccion_tra2 = self.tk.Entry(representante,border=2,relief="groove")
        direccion_tra2.place(x=120,y=105,width=220)

        phone_re =self.tk.Label(representante,text="Telf:").place(x=350,y=105,width=20)
        phone_re3 =self.tk.Entry(representante,border=2,relief="groove")
        phone_re3.place(x=380,y=105,width=100)

        direccion_f_Cer =self.tk.Label(representante,text="Direccion de Familiar Cercano:").place(x=4,y=140,width=170)
        direccion_f_Cer2 =self.tk.Entry(representante,border=2,relief="groove")
        direccion_f_Cer2.place(x=175,y=140,width=305)

        telefonot =self.tk.Label(representante,text="Telf de Familiar Cercano:").place(x=5,y=180,width=140)
        telefonot_re2 =self.tk. Entry(representante,border=2,relief="groove")
        telefonot_re2.place(x=150,y=180,width=170)


        fecha:date  = fecha_nacimiento1.get_date()

        btn = self.tk.Button(self.frame7,text="Guardar",command=lambda: self.register_child(
            anno_cursar = date.today().year,nombre=nombre_es2.get(),apellido=apellido_es.get(),f_di=fecha.day,f_m=fecha.month,
            f_an=fecha.year,e_a=edad_anos2.get(),emp_camin=edad_caminar2.get(),e_m=meses2.get(),sex=sexo_combo.get(),l_n=lugar_nacimiento2.get(),
            en_fed=entidad_federal2.get(),nacionalidad=nacionalidad2.get(),ced_escolar=cdula_escolar2.get(),man=manana_key.get(),
            tar=tarde_key.get(),secc=seccion2.get(),A=cont.get(),B=cont2.get(),C=cont3.get(),instituto_pro=self.institucion2.get(),
            del_hogar=self.del_hogar2.get(),senci=parto_sencillo.get(),gem="",g_1=gemelocontrol.get(),g_2=gemelocontrol2.get(),trill="",
            t_1=trillizoscontrol.get(),t_2=trillizoscontrol2.get(),t_3=trillizoscontrol3.get(),nor=nacimientocontrol.get(),
            ces=nacimientocontrol2.get(),forcep=nacimientocontrol3.get(),term=nacimientocontrol4.get(),
            saram=enfermedadcontrol.get(),ru=enfermedadcontrol2.get(),lec=enfermedadcontrol3.get(),osf=enfermedadcontrol4.get(),
            me=enfermedadcontrol5.get(),he=enfermedadcontrol6.get(),pa=enfermedadcontrol7.get(),otras=enfermedadcontrol8.get(),
            cuales=self.cuales2.get(),BCG=vacunascontrol.get(),anti=vacunascontrol2.get(),rube=vacunascontrol3.get(),
            tripe=vacunascontrol4.get(),f_a=vacunascontrol5.get(),pol=vacunascontrol6.get(),otras_2=self.alergia2.get(),
            der=derechacontrol.get(),izq=izquierdacontrol.get(),amb=ambascontrol.get(),peso=pesa.get(),altura=mide.get(),
            talla=talla.get(),pantalon=talla2.get(),zap=talla3.get(),padre=padrecontrol.get(),madre=madrecontrol.get(),
            abuelos=abueloscontrol.get(),otro_fami=otrocontrol.get(),empezo_hab=edad_hablar2.get(),quien_duer=duerme_nino2.get(),
            si_her=hermanocontrol.get(),no_her=hermano2control.get(),gra_her=hermano_nino5.get(),
            hab_correc=habla_correctamente2.get(),canta=cantar2.get(),baila=bailar2.get(),historias=contar_historias2.get(),
            si_dep=actividades_fisicas2.get(),cual_dep=self.actividades_fisicas4.get(),juega_con=juega2.get(),juegos_casa=juegos_realiza2.get(),
            nom_pa=nombre_pa2.get(),ape_pa=apellido_pa.get(),ced_pa=ci_pa.get(),nac_pa=nacionalidad_pa.get(),
            pro_pa=profesion_pa.get(),hab_pa=habitacion_pa.get(),tel_pa=telefonoh_pa.get(),trabajo_pa=trabajo_pa.get(),
            tel_pa_tra=telefonoh_pa.get(),vi_si=viveninocontrol.get(),vi_no=vivenino2control.get(),nombre_ma=nombre_madre2.get(),
            ape_ma=apellido_madre2.get(),ced_ma=ci_ma.get(),nac_ma=nacionalidad_ma.get(),pro_ma=profesion_ma.get(),
            hab_ma=habitacion_ma.get(),tel_ma=telefonoh_ma.get(),tra_ma=trabajo_ma.get(),tel_ma_trab=telefonot_ma.get(),
            vive_con_el_si=vive_con_control_ma.get(),vive_con_el_no=vive_con_contro2_ma.get(),nombre_re=nombre_re2.get(),
            apellido_re=apellido_re2.get(),parentesco=parentesco_re1.get(),cedula=ci_re.get(),telefono=phone_re1.get(),direccion_casa=direccion_hab.get(),
            telefono_hab_re=phone_re2.get(),direccion_trabajo=direccion_tra2.get(),telefono_t_re=phone_re3.get(),
            telefono_cer_re=telefonot_re2.get(),dir_cer_re= direccion_f_Cer2.get()
        ))
        btn.place( relx=0.9,rely=0.8)


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
