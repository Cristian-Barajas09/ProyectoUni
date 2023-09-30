from partials.view.baseView import BaseView
from controller.AppController import Controller
from tkcalendar import DateEntry
from babel.numbers import *
from datetime import date
from tkinter import messagebox,dialog
from tkinter.filedialog import askdirectory
from util.helpers import read_env_value
from .partials.inscripcion import inscripcion
import os

class App(BaseView):
    __table_name = 'estudiantes'
    def __init__(self):
        super().__init__(title="C.E.I Josefina Molina de Duque",geometry="900x530",controller=Controller)
        self.icon()

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
        inscripcion(self)

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
                if item['rol'] == "admin" or item['rol'] == self.session['rol']:
                    continue
                self.tree.insert('', self.tk.END, values=(
                    item['nombres'], item['apellidos'], item['cedula']))
            self.controlPersonas()

    def register_child(self,*,
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
                    nombre_re,
                    apellido_re,
                    parentesco,
                    cedula,
                    telefono,
                    direccion_casa,
                    telefono_hab_re,
                    direccion_trabajo,
                    telefono_t_re,
                    telefono_cer_re,
                    dir_cer_re,
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
        'A': 'A' if not(A)  else '',
        'B':'B' if not(B)  else '',
        'C':'C' if not(C) else '',
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
        'nombre_re':nombre_re,
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
        self.tk.Frame(frame_search,bg="#38B1EE").place(relx=0.24, rely=0.35, width=220, height=2)

        self.search.place(relx=0.24, rely=0.2, width=220, height=25)
        self.search.bind("<FocusOut>", self.validate_search)


        self.select = self.ttk.Combobox(frame_search, values=(
            "nombres", "apellidos", "cedula"), state="readonly")
        self.select.current(0)
        self.select.place(relx=0.557, rely=0.2, width=70,height=25)

        self.select.bind("<<ComboboxSelected>>",lambda event: self.validate_param(self.select.get()))

        btn_search = self.tk.Button(frame_search,bg="#041d9b",border=0,fg="#fff", text="Buscar", command=lambda: self.buscar(
            self.search, self.select),cursor="hand2")
        btn_search.place(relx=0.66, rely=0.2, width=70, height=25)
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


        result = self._controller.search(search.get(), param.get(),self.__table_name)

        if result == ():
            self.carga.destroy()
            messagebox.showerror("hubo un problema",f"no hay nadie con ese {param.get()}")
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

        self.person = self.Toplevel()
        self.person.wm_title(f"usuario: {result['nombres']}")


        btnDelete = self.tk.Button(self.person,text="eliminar estudiante",command=lambda: self.deleteEstudiante(result['cedula_escolar']))
        btnDelete.pack()


    def item_selected_representante(self,event):
        values = []
        for selected_item in self.tree3.selection():
            item = self.tree3.item(selected_item)
            values = item['values']

        result = self._controller.obtenerRepresentante(values[2])

        self.person2 = self.Toplevel()
        self.person2.wm_title(f"usuario: {result['nombres']}")


        btnDelete = self.tk.Button(self.person2,text="eliminar representante",command=lambda: self.deleteRepresentante(result['cedula']))
        btnDelete.pack()

    def item_selected_usuarios(self,event):
        values = []
        for selected_item in self.tree2.selection():
            item = self.tree2.item(selected_item)
            values = item['values']

        result = self._controller.obtenerUsuario(values[2])

        self.person3 = self.Toplevel()
        self.person3.wm_title(f"usuario: {result['nombres']}")


        btnDelete = self.tk.Button(self.person3,text="eliminar representante",command=lambda: self.deleteRepresentante(result['cedula']))
        btnDelete.pack()

    def deleteEstudiante(self,cedula):
        result = self._controller.eliminarEstudiante(cedula)

        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.controlPersonas()
        self.person.destroy()

    def deleteRepresentante(self,cedula):
        result = self._controller.eliminarRepresentante(cedula)

        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.controlPersonas()
        self.person.destroy()


    def deleteUsuario(self,cedula):
        result = self._controller.eliminarUsuario(cedula)

        if not(isinstance(result,int)):
            return messagebox.showerror("No se pudo eliminar el usuario")


        self.controlPersonas()
        self.person.destroy()

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
        
        if param == "cedula":
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