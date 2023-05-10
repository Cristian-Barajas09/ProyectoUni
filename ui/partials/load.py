from .base import Base
from ui.application import Application
from ui.form import Form
from ui.inscripcion import Inscripciones
from ui.register import Register
from ui.control import Control

class Load(Base):
    def __init__(self):
        super().__init__("cargando...","800x800")
        self.window.mainloop()
    def destination(self,modulo):
        match(modulo):
            case "principal":
                self.window.destroy()
                Application()
            case "ingresar":
                self.window.destroy()
                Form()
            case "inscripcion":
                self.window.destroy()
                Inscripciones()
            case "registro":
                self.window.destroy()
                Register()
            case "Control":
                self.window.destroy()
                Control()
