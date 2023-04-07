import mysql.connector
import os
import subprocess
from mysql.connector import Error
from .keys import keys_db
# conexion a la base de datos

# --> Rutas

#obtenemo la raiza de la carpeta del proyecto
carpeta_principal = os.path.dirname(__file__)
carpeta_respaldo = os.path.join(carpeta_principal,"respaldo")
class BaseDatos:
    def __init__(self, **kwargs):
        try:
            self.connector = mysql.connector.connect(**kwargs)
            self.cursor = self.connector.cursor()
        except Error as error:
            print("algo salio mal: \n",error)
            exit()
    #decorador para el reporte de base de datos en el servidor
    def reporte_bd(funcion_parametro):
        def interno(self,nombre_bd):
            funcion_parametro(self,nombre_bd)
            print("estas son las bases de datos que tiene el servidor:")
            BaseDatos.mostrar_bd(self)
        return interno
    # consultas a la base datos
    def consulta(self, sql):
        cursor = self.connector.cursor()
        cursor.execute(sql)
        return cursor
    # mostrar base de datos del servidor

    def mostrar_bd(self) -> list:
        self.cursor.execute("SHOW DATABASES")
        lista = []
        for bd in self.cursor:
            # print(bd)
            lista.append(bd)
        return lista

    # elimina una base de datos
    @reporte_bd
    def eliminar_bd(self, nombre_bd:str) -> None :
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"la base de datos {nombre_bd} a sido eliminada con exito")
        except:
            print(f"la base de datos {nombre_bd} no encontrada")


    # crear base de datos
    @reporte_bd
    def crear_bd(self, nombre_bd: str) -> None:
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
            print(f"se creo la base de datos {nombre_bd} o ya existia")
        except:
            print(f"ocurrio un error al crear la base de datos {nombre_bd}")
    def copia_bd(self,nombre_bd):
        with open(f'{carpeta_respaldo}/{nombre_bd}.sql','w') as out:
            subprocess.Popen(f'"C:/xampp/mysql/bin/"mysqldump -u root --databases {nombre_bd}', shell=True,stdout=out)
    #create table
    def create_table(self,table_name:str,numero_columnas:int,columna_detail:list) -> str:
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

