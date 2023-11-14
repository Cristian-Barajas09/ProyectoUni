class ExtraEstudiante:
    gustos:list
    juegos:list
    actividades:list
    vacunas:list
    alergias:list
    enfermedades:list

    def __init__(self,*,
                gustos:list,
                juegos:list,
                actividades:list,
                vacunas:list,
                alergias:list,
                enfermedades:list):
        self.gustos = gustos
        self.juegos = juegos
        self.actividades = actividades
        self.vacunas = vacunas
        self.alergias = alergias
        self.enfermedades = enfermedades