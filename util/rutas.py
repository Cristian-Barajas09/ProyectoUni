import os

separador = os.path.sep
directorio_actual = os.path.dirname(os.path.abspath(__file__))
dir = separador.join(directorio_actual.split(separador)[:-1])
