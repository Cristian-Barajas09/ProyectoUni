from util.rutas import dir
import subprocess
from subprocess import SubprocessError
import os
import shutil
from tkinter import filedialog
class Installer():
    __ruta_proyecto = dir
    __user = os.getlogin()
    def __init__(self) -> None:
        self.main = os.path.join(self.__ruta_proyecto,"main.py")
        self.deactiveDebug()
        # self.validate_folder()
        self.generar()


    def deactiveDebug(self):
        lines = open(self.main,'r').readlines()
        if "DEBUG: bool = True\n" in lines:
            index = lines.index("DEBUG: bool = True\n")
            admin = lines.index("from private.admin import Admin\n")
            admin2 = lines.index("        Admin()\n")
            lines[index] = "DEBUG: bool = False\n"
            lines[admin] = "#from private.admin import Admin\n"
            lines[admin2] = "#        Admin()\n"
            out = open(self.main,'w')
            out.writelines(lines)
            out.close()

    def moveFiles(self):
        with open(f'{os.path.join(self.main,"dist",".env")}','w+') as file :
            env_debug = open(f'{os.path.join(self.__ruta_proyecto,".env")}','r')
            file.writelines(env_debug)
            file.close()

    # def validate_folder(self):
    #     if os.path.exists(os.path.join(self.path,"production_uni")):
    #         os.rmdir(os.path.join(self.main,"production_un"))
    #     else:
    #         os.mkdir(os.path.join(self.path,"production_uni"))

    def generar(self):
        try:
            subprocess.Popen(".\\venv\\Scripts\\activate",shell=True,stdout=True)
            subprocess.Popen(f"pyinstaller {self.main}",shell=True,stdout=True)
        except SubprocessError as error:
            print(error)
        finally:
            exit()



if __name__ == "__main__":
    install = Installer()