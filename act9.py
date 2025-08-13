## 13/8/2025

from typing import Self


class padre:
    apellido= ''
    def__init__(self,nombre):
       Self.nombre=nombre 
      
class hijo(padre):
    def __init__(self,nombre,lenguajeDeProgramacion):
        super().__init__(nombre)
        self.lenguajeDeProgramacion=lenguajeDeProgramacion 
padre = padre('nombre del padre') 
padre.apellido='apellido del padre'
hijo = hijo('nombre del hijo','python')
print(hijo,nombre,hijo,apellido)
    