from ui.Form import Form
from private.admin import Admin
from testApp.Estudiante.TestEstudiante import TestEstudiante
# import argparse
# desactivar si ya quieres iniciar produccion

# parser = argparse.ArgumentParser(description="framework by Cristian :)")

# parser.add_argument("params", help="ingresar el nombre del comando", type=str, nargs='+')


# args = parser.parse_args()


DEBUG: bool = True

def tests():
    testEstudiante = TestEstudiante()
    testEstudiante.crear_estudiante()



def run():
    if DEBUG:
        print("estas en modo desarrolador")
        Admin()
    else:
        Form()

if __name__ == "__main__":
        run()