use bd_ejemplo_tst; 
CREATE TABLE if not exists Receta(ID_Receta int);
CREATE TABLE if not exists Productos (
ID_Producto INT not null PRIMARY KEY AUTO_INCREMENT,
Nombre_Producto varchar(20) not null,
Stock int  not null,
Precio double  not null,
Unidad_de_medida varchar(10)  not null,
ID_Receta int  not null,
ID_Insumo int  not null,
FOREIGN KEY (ID_Receta) REFERENCES Productos(ID_Producto));


