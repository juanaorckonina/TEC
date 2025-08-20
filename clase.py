
##20/8/2025

class persona:
    def __init__(self,nombre):
        self.nombre=nombre
class alumno(persona):
    def __init__(self, nombre):
        super().__init__(nombre)
class profsor(persona):
    def __init__(self, nombre):
        super().__init__(nombre)
class clase:
    def __init__(self,materia,grado,division,profesor):
        self.materia=materia
        self.grado=grado
        self.division=division
        self.alumnos=[]
        self.profesor=profesor
    def agregar_alumno(self,nombre)
        self.alumnos.append(alumno)  
gabriel=profsor("Gabriel")
nombres_de_alumnos=[]
TIC5to1ra = clase("TIC",5,1,gabriel)
        