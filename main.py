from ui.form import Form
from private.admin import Admin

from util.rutas import dir
# desactivar si ya quieres iniciar produccion
DEBUG: bool = True


def run():
    if DEBUG:
        print("estas en modo desarrolador")
        Admin()
    else:
        Form()
        print(dir)

if __name__ == "__main__":
    run()