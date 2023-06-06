import mysql.connector

from Producto import Producto
class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Quebracho00',
                db='bd_ejemplo_tst'
            )
            if self.conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")

        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


def Insertar_Producto(self,producto):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "INSERT INTO productos values(null,%s,%s,%s,%s,null)"
            data = (producto.getiD_Producto(),
                    producto.getnombre_Producto(),
                    producto.getstock(),
                    producto.getprecio(),
                    producto.getunidad_de_medida(),
                    producto.getiD_Receta()
                    )
            
            cursor.execute(sentenciaSQL,data)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto insertado correctamente")

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

    
def Listado_De_Productos(self):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * FROM Productos"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            cursor.Conexion.close()
            return resultados
            
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)
    







        




        
        

