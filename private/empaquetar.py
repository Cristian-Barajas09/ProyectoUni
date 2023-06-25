from util.rutas import dir
import subprocess
import os
class Installer():
    __ruta_proyecto = dir
    __user = os.getlogin()
    def __init__(self) -> None:
        self.main = os.path.join(self.__ruta_proyecto,"main.py")
        self.deactiveDebug()
        self.generar()

    def deactiveDebug(self):
        print(self.main)
        lines = open(self.main,'r').readlines()
        if "DEBUG: bool = True\n" in lines:
            index = lines.index("DEBUG: bool = True\n")
            lines[index] = "DEBUG: bool = False\n"
            out = open(self.main,'w')
            out.writelines(lines)
            out.close()

    def generar(self):
        print(self.main)
        if os.path.exists(os.path.join(self.__ruta_proyecto,"build")):
            os.rmdir(os.path.join(self.__ruta_proyecto,"build"))
        else:
            os.mkdir(os.path.join(self.__ruta_proyecto,"build"))
        build_path = os.path.join(self.__ruta_proyecto,"build")
        subprocess.Popen(f"pyinstaller {self.main} --specpath {build_path} --onefile",shell=True,stdout=True)
