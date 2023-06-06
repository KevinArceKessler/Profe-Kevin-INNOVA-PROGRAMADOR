import Conexion as conexionBD
from Producto import Producto

print("*******BIENVENIDO A LA CALCULADORA BIG BRED SA***********")
print("¿Quiere ingresar un producto?")
print("Para ingresar un producto ingrese 1")
print("Para ver el listado de los productos ingrese 2")
ingresaProducto = int(input())
if ingresaProducto == 1:
    con = conexionBD.Conectar()
    nombreProducto = input("Ingrese el nombre del producto:")
    stockProducto = int(input("Ingrese el stock del producto:"))
    precioProducto = int(input("Ingrese el precio del producto:"))
    unidadDeMedidaProducto = input("Ingrese la unidad de medida del producto:")
    producto = Producto(0,nombreProducto,stockProducto,precioProducto,unidadDeMedidaProducto,0)
    conexionBD.Insertar_Producto(producto)
    
elif  ingresaProducto == 2:
    con = conexionBD.Conectar()
    prod=conexionBD.Listado_De_Productos()
    for i in prod:
        print("Nombre:" + i[1] + "Stock:" + i[2] + "Precio" + i[3]+ "Unidad de medida del producto" + i[4])







