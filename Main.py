import Conexion as Conector

print("Para conectarse a la Base de Datos presione 1")
print("Para cerrar la Base de Datos presione 2")
variableAuxiliar= int(input())
if(variableAuxiliar == 1):
    conn = Conector.Conectar()
else: 
    print("Gracias por cerrar la Base de Datos.")



