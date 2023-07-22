from ui.Form import Form
from private.admin import Admin

# desactivar si ya quieres iniciar produccion
DEBUG: bool = True


def run():
    if DEBUG:
        print("estas en modo desarrolador")
        Admin()
    else:
        Form()

if __name__ == "__main__":
    run()