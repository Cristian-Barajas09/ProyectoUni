from util.rutas import dir
import subprocess
import os
class Installer():
    __ruta_proyecto = dir
    def __init__(self) -> None:
        self.main = f"{self.__ruta_proyecto}\\main.py"
        self.generar()
    def generar(self):
        print(directorio_actual = os.path.dirname(os.path.abspath(__file__)))
        # subprocess.Popen(f"pyinstaller {self.main}",shell=True,stdout=True)
