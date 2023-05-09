import customtkinter as ctk
from   db.database import base_datos as sql
from tkinter.font import BOLD
from util.generic import leer_image
from util.rutas import dir

from .partials.base import Base


class Control(Base):
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Control de Personal")
        self.window.geometry("673x500")
        self.icon()

        self.imageSearch = leer_image('./image/lupa-blanca.png',(36,26))

        # frames
        self.frame1 = ctk.CTkFrame(self.window,width=263,height=500)
        self.frame1.place(x=0,y=0)

        self.frame2 = ctk.CTkFrame(self.window,width=260,height=40)
        self.frame2.place(x=340,y=10)

        self.frame3 = ctk.CTkFrame(self.window,width=378,height=420)
        self.frame3.place(x=283,y=60)
        # frame 1
        valores = ["profesores","estudiantes"]
        comandos = ()
        self.select = ctk.CTkOptionMenu(self.frame1,values=valores,command=comandos)
        self.select.place(x=0,y=10)
        # frame 2
        self.search = ctk.CTkEntry(self.frame2,width=260,height=40,placeholder_text="Buscar",font=('Comic Sans MS',16,BOLD))
        self.search.place(x=0,y=0)
        self.btnSearch = ctk.CTkButton(self.frame2,width=36,height=26,text="",image=self.imageSearch,bg_color="#2A2929",fg_color="#2A2929",hover_color="#222222")
        self.btnSearch.place(x=200,y=3)

        # frame 3
        self.get_user()
        # ciclo
        self.window.mainloop()

    #consulta a la base de datos
    def get_user(self):
        datos = sql.consulta("SELECT nombres,apellidos FROM users")
        datos = datos.fetchall()
        y = 0
        for i in datos:
            self.label1 = ctk.CTkLabel(self.frame3,text=f"{i[0]} {i[1]}")
            self.label1.place(x=10,y=y)
            y += 20