import os
import subprocess
import pymysql.cursors
from pymysql.err import OperationalError,Error
from ..utils.keys import keys_db
from tkinter import messagebox
import pymysql.cursors


class BaseModel :

    keys_db = keys_db


    carpeta_principal = os.path.dirname(__file__)
    carpeta_respaldo = os.path.join(carpeta_principal,"respaldo")
    def __init__(self, **kwargs):
        """
            iniciar la conexion con la base de datos y
            generar un cursor para permitir movernos dentro de esta

            self.connector: pymysql.connect() -> generar conexion
            self.cursor: generar cursor

            args:
                **kwargs -> espera una lista con las llaves de la base de datos
        """
        self.kwargs = kwargs

    def connect(self) :
        try:
            connector = pymysql.connect(**self.kwargs)
            cursor = connector.cursor()
            return connector,cursor
        except OperationalError as error:
            """
                agarrar el error de conexion
            """
            print(error)
            messagebox.showerror("error",error)
            exit()




    def insert(self,query:str):
        con,cur = self.connect()
        try:

            cur.execute(query)
            con.commit()
        except Error as error:
            con.rollback()
            raise RuntimeError("no se pudo guardar el objeto")
        else:
            return con.insert_id()
        finally:
            con.close()
            cur.close()


    def update(self,query:str):
        con,cur = self.connect()

        try:
            cur.execute(query)
            con.commit()
        except Error as error:
            con.rollback()
            raise RuntimeError("no se pudo actualizar el objeto")
        else:
            return cur.rowcount
        finally:
            con.close()
            cur.close()

    def delete(self,query:str,):
        con,cur = self.connect()

        try:
            cur.execute(query)
            con.commit()
        except Error as error:
            con.rollback()
            raise RuntimeError("no se pudo eliminar el objeto")
        else:
            return cur.rowcount
        finally:
            con.close()
            cur.close()


    def select(self,query):
        con,cur = self.connect()

        try:
            cur.execute(query)
        except Error as error:
            raise RuntimeError("no se pudo encontrar el objeto")
        else:
            return cur.fetchall()
        finally:
            con.close()
            cur.close()

    def selectOne(self,query):
        con,cur = self.connect()

        try:
            cur.execute(query)
        except Error as error:
            raise RuntimeError("no se pudo encontrar el objeto")
        else:
            return cur.fetchone()
        finally:
            con.close()
            cur.close()




    def copia_bd(self,nombre_bd):
        """
            metodo que nos permite crear una copia de seguridad de una base de datos

            args:
                nombre_db:str -> espera el nombre de la base de datos
        """
        with open(f'{self.carpeta_respaldo}/{nombre_bd}.sql','w') as out:
            subprocess.Popen(f'"C:/xampp/mysql/bin/"mysqldump -u root --databases {nombre_bd}', shell=True,stdout=out)
        return messagebox.showinfo("exito","copia de seguridad de la base de datos generada con exito")
    #create table
