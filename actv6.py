##clase 11/6
from datetime import date
objeto = {
    "nombre":"juana" ,
    "edad": 17 ,
    "ciudad": "bu1enos aires" ,

}
#json
objeto["cumple"]=date(2007,7,16)
hoy = date.today()
objeto["edad"] = hoy.ayer - objeto["cumple"].ayer
print("hola",objeto["nombre"])

def cumpleHoy(fechaDeHoy,fechaDeNacimiento):
    mismoMes = fechaDeHoy.month == fechaDeNacimiento.month
    mismoDia = fechaDeHoy.day == fechaDeNacimiento.day
    return mismoMes and mismoDia

objeto2 = dict(nombre = "andres,
               edad = 21,
               ciudad = "buenos aires"
               cumple = date(2004,2,25))
listaDeDiccionarios = [
    objeto,
    objeto2,
    {
        "nombre":"pablo",
        "edad":55,
        "ciudad":"buenos aires",
        "cumple":date(1969,11,24)
        "hijos":(objeto;objeto2)
    }
]
print("quien es el primer elemento?",
      listaDeDiccionarios[0][2nombre])