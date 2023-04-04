from ui.form import Form
from private.admin import Admin
import os
# desactivar si ya quieres iniciar produccion
DEBUG: bool = False


if DEBUG:
    print("estas en modo desarrolador")
    Admin()
else:
    carpeta_imagenes = os.path.join(os.path.dirname(__file__),"image")
    Form(carpeta_imagenes)

