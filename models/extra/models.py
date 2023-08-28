from enum import Enum

class Sexo(Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'

class Turno(Enum):
    MANANA = 'M'
    TARDE = 'T'

class Grupo(Enum):
    A = 'A'
    B = 'B'
    C = 'C'

class Parto(Enum):
    SENCILLO = "sencillo"
    GEMELO = "Gemelos"
    TRILLIZOS = "trillizos"

class Proceso(Enum):
    NATURAL = 'N'
    CESAREA = 'C'
    FORCEP = 'F'
    TERMINO = 'T'

class Mano(Enum):
    DERECHA='D'
    IZQUIERDA='I'
    AMBAS='A'

class Seccion(Enum):
    A = 'A'
    B = 'B'
    C = 'C'




