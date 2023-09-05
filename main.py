from ui import Signin
from private.admin import Admin
from testApp import TestEstudiante,TestRepresentante

import argparse
# desactivar si ya quieres iniciar produccion

parser = argparse.ArgumentParser(description="app by Cristian :)")

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
    if args.params[0] == 'test':
        tests()
    elif args.params[0] == 'run':
        run()
