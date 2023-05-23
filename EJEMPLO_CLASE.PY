class Persona():
    
    Nombre = ""
    Telefono = 0
    DNI = 0

    def __init__(self, nombre, telefono,dNI):
        self.Nombre = nombre
        self.Telefono = telefono
        self.DNI= dNI

    def MostrarDatos(self):
        print('La persona se llama: '+self.Nombre+'Cuyo DNI es: '+str(self.DNI)+ 'Y su telefono es: '+str(self.Telefono))


Nombre= 'Kevin Arce Kessler'
Telefono= 15664488
DNI= 22554488

Kevin = Persona(Nombre, Telefono, DNI)

Kevin.MostrarDatos()



    













