from ui import Signin
from private.admin import Admin
from private.create_models import CreateTables
from testApp import TestEstudiante,TestRepresentante
from util.rutas import dir
import os
import argparse


# desactivar si ya quieres iniciar produccion

parser = argparse.ArgumentParser(description="app by CFJO")

parser.add_argument("params", help="ingresar el nombre del comando", type=str, nargs='+')


args = parser.parse_args()


DEBUG: bool = True

def tests():
    # test = TestRepresentante()
    # test.crear()
    testEstudiante = TestEstudiante()
    testEstudiante.crear_estudiante()



def run():
    if DEBUG:
        print("estas en modo desarrolador")
        Admin()
    else:
        Signin()

if __name__ == "__main__":
    if DEBUG:
        if args.params[0] == 'test':
            tests()
        elif args.params[0] == 'run':
            run()
        elif args.params[0] == 'create':
            sql_file = os.path.join(dir,'db','proyecto_1.sql')
            create = CreateTables(sql_file)

    else:
        run()
