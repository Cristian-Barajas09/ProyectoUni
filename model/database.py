import os
import subprocess
from tkinter import messagebox
from .keys import keys_db
import pymysql.cursors
from pymysql.cursors import Cursor
from pymysql.err import OperationalError
# conexion a la base de datos

# --> Rutas

#obtenemo la raiza de la carpeta del proyecto
carpeta_principal = os.path.dirname(__file__)
carpeta_respaldo = os.path.join(carpeta_principal,"respaldo")

class BaseDatos:
    def __init__(self, **kwargs):
        """
            iniciar la conexion con la base de datos y
            generar un cursor para permitir movernos dentro de esta

            self.connector: pymysql.connect() -> generar conexion
            self.cursor: generar cursor

            args:
                **kwargs -> espera una lista con las llaves de la base de datos
        """
        try:
            self.connector = pymysql.connect(**kwargs)
            self.cursor = self.connector.cursor()
        except OperationalError as error:
            """
                agarrar el error de conexion
            """
            messagebox.showerror("error",error)
            exit()
        finally:
            self.connector.close()
    #decorador para el reporte de base de datos en el servidor
    def reporte_bd(funcion_parametro):
        def interno(self,nombre_bd:str):
            """
                generar un reporte de las bases de datos existentes

                args:
                    funcion_parametro -> espera una funcion como parametro
                    nombre_bd -> espera un string

            """
            funcion_parametro(self,nombre_bd)
            print("estas son las bases de datos que tiene el servidor:")
            BaseDatos.mostrar_bd(self)
        return interno


    # consultas a la base datos
    def consulta(self, sql:str) -> Cursor:
        """
            metodo solo para consultas que nos permite solo realizar consultas a
            la base de datos
            args:
                sql:str -> espera una consulta
        """
        cursor = self.connector.cursor()
        cursor.execute(sql)
        return cursor
    # mostrar base de datos del servidor

    #ejecutar consultas
    def CRUD(self,sql):
        """
            metodo que nos permite realizar los metodos basicos de un crud
            CREATE, READ,UPDATE,DELETE

            args:
                sql:str -> espera la operacion a ejecutar

        """
        self.cursor.execute(sql)
        self.connector.commit()
        self.connector.close()

    def mostrar_bd(self) -> list:
        """
            metodo que nos muestra  las bases de datos existentes
            args:
                nombre_bd:str -> espera el nombre de la base de datos
        """
        self.cursor.execute("SHOW DATABASES")
        lista = []
        for bd in self.cursor:
            # print(bd)
            lista.append(bd)
        return lista

    # elimina una base de datos
    @reporte_bd
    def eliminar_bd(self, nombre_bd:str) -> None :
        """
            metodo que nos permite eliminar una base de datos

            args:
                nombre_bd:str -> espera el nombre de la base de datos
        """
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"la base de datos {nombre_bd} a sido eliminada con exito")
        except:
            print(f"la base de datos {nombre_bd} no encontrada")


    # crear base de datos
    @reporte_bd
    def crear_bd(self, nombre_bd: str) -> None:
        """
            metodo que nos permite crear una base de datos

            args:
                nombre_bd:str -> espera el nombre de la base de datos
        """
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
            print(f"se creo la base de datos {nombre_bd} o ya existia")
        except:
            print(f"ocurrio un error al crear la base de datos {nombre_bd}")

    def copia_bd(self,nombre_bd):
        """
            metodo que nos permite crear una copia de seguridad de una base de datos

            args:
                nombre_db:str -> espera el nombre de la base de datos
        """
        with open(f'{carpeta_respaldo}/{nombre_bd}.sql','w') as out:
            subprocess.Popen(f'"C:/xampp/mysql/bin/"mysqldump -u root --databases {nombre_bd}', shell=True,stdout=out)
        return messagebox.showinfo("exito","copia de seguridad de la base de datos generada con exito")
    #create table
    def create_table(self,table_name:str,numero_columnas:int,columna_detail:list) -> str:
        """
            crea una tabla en la base de datos seleccionada

            args:
                table_name:str -> espera el nombre que le asignaremos a la base de datos
                numero_columnas:str -> espera el numero de columnas que llevara la tabla
                columna_detail:list -> espera los campos que le daremos a la tabla
        """
        try:
            quest = []
            # columnas = int(input("cuantas columnas? \n"))
            # table_name = input("nombre de la tabla: ")
            query = f"CREATE TABLE {table_name}(\n"
            for column in range(numero_columnas):
                quest[column] = columna_detail[column]
                if column == numero_columnas:
                    query += f"{quest}"
                else:
                    query += f"{quest}\n"
                    query += ");"
            self.cursor.execute(query)
            return self.cursor
        except:
            print(f"no se pudo crear la tabla {table_name}")
# execute() es para ejecutar sentencias sql
# commit para mandarlas a mysql
# fetchall obtiene todos los datos de la sentencia

base_datos = BaseDatos(**keys_db)

