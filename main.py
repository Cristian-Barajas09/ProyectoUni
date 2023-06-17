from ui.main import Form
from private.admin import Admin

from util.rutas import dir
# desactivar si ya quieres iniciar produccion
DEBUG: bool = False


def run():
    if DEBUG:
        print("estas en modo desarrolador")
        Admin()
    else:
        Form()

if __name__ == "__main__":
    run()