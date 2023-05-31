from Conexion import Conectar


class Producto():
    ID_Producto =0,
    Nombre_Producto = "",
    Stock =0,
    Precio = 0,
    Unidad_de_medida = "",
    ID_Receta = 0

    def __init__(self,iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta):
        self.ID_Producto = iD_Producto
        self.Nombre_Producto =nombre_Producto
        self.Stock = stock
        self.Precio = precio
        self.Unidad_de_medida=unidad_de_medida
        self.ID_Receta =iD_Receta
    

