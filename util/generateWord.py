import aspose.words as aw
from util.rutas import dir
import os

class Word:
    nombre = "test.docx"
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.pathDir = self.__path(self.nombre)
        self.doc = aw.Document()
        self.builder = aw.DocumentBuilder(self.doc)


    def __path(self,nombre,path=os.path.join(dir,"public","{}")):
        path = path.format(nombre)
        return path

    def write(self,texto):
        self.builder.write(texto)

    def save(self):
        self.doc.save(self.pathDir)
