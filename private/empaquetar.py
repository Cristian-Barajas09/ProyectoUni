from util.rutas import dir
import subprocess
import os
class Installer():
    __ruta_proyecto = dir
    def __init__(self) -> None:
        self.main = os.path.join(self.__ruta_proyecto,"main.py")
        self.generar()
    def generar(self):
        print(self.main)
        if os.path.exists(os.path.join(self.__ruta_proyecto,"build")):
            os.rmdir(os.path.join(self.__ruta_proyecto,"build"))
        else:
            os.mkdir(os.path.join(self.__ruta_proyecto,"build"))
        build_path = os.path.join(self.__ruta_proyecto,"build")
        subprocess.Popen(f"pyinstaller {self.main} --specpath {build_path} --onefile",shell=True,stdout=True)
