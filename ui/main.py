from partials.base import BaseView
from controller.main import Controller
from tkcalendar import DateEntry
from tkinter.font import BOLD
from typing import List
from util.generateWord import Word


class App(BaseView):
    def __init__(self):
        super().__init__(title="nombre_colegio",geometry="700x500",controller=Controller)


        self.main()

        self.window.mainloop()


    def main(self):
        self.notebook = self.ttk.Notebook(self.window)
        self.frame1 = self.tk.Frame(self.notebook,bg="#000")
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.frame2 = self.ttk.Frame(self.notebook)
        self.frame2.place(relx=0,rely=0)


        self.controlPersonas()
        self.inscripcion()

        self.notebook.add(self.frame1,text="Busqueda")
        self.notebook.add(self.frame2,text="Inscripciones")

        self.notebook.place(relx=0,rely=0,relwidth=1,relheight=1)

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
        pass


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