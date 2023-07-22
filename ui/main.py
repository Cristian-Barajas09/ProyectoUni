from partials.base import BaseView
from controller.main import Controller
from tkcalendar import DateEntry
from tkinter.font import BOLD
from typing import List
from util.generateWord import Word


class App(BaseView):
    def __init__(self):
        super().__init__(title="nombre_colegio",geometry="700x700",controller=Controller)


        self.main()

        self.window.mainloop()


    def main(self):
        self.notebook = self.ttk.Notebook(self.window)
        self.frame1 = self.ttk.Frame(self.notebook)
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.frame2 = self.ttk.Frame(self.notebook)
        self.frame2.place(relx=0,rely=0)


        self.controlPersonas()
        self.inscripcion()

        self.notebook.add(self.frame1,text="Busqueda")
        self.notebook.add(self.frame2,text="Inscripciones")

        self.notebook.place(relx=0,rely=0,relwidth=1,relheight=1)

    def inscripcion(self):
        pass


    def controlPersonas(self):
        self.search = self.ttk.Entry(self.frame1,)
        self.search.place(relx=0.2,rely=0.01,relwidth=0.1)
        self.btnSearch = self.ttk.Button(self.frame1, text="search",command=self.render_user)
        self.btnSearch.place(relx=0.3,rely=0.01)

        columns = ("nombres","apellidos")
        self.tree = self.ttk.Treeview(self.frame1,columns=columns,show="headings")

        self.tree.heading("nombres",text="nombres")
        self.tree.heading("apellidos",text="apellidos")


        self.render_user()

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.place(relx=0,rely=0,relwidth=1,relheight=1)


        scrollbar = self.ttk.Scrollbar(self.frame1, orient=self.tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns',ipadx=10,ipady=10)


    def searchUser(self):
        search = self.search.get()
        result = self._controller.search_user(search.capitalize())
        if result != ():
            return result
        return []

    def render_user(self):
        search = self.searchUser()
        if search != []:
            self.tree.delete(*self.tree.get_children())
            for item in search:
                self.tree.insert('',self.tk.END,values=(item["nombres"],item["apellidos"]))
        else:
            self.tree.delete(*self.tree.get_children())
            data = self.getUser()
            for item in data:
                self.tree.insert('',self.tk.END,values=(item["nombres"],item["apellidos"]))

    def getUser(self):
        return self._controller.get_user()

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            self.person = self.tk.Toplevel()
            self.person.wm_title("usuario")
