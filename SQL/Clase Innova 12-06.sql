/*use bd_ejemplo_tst;*/

/*
C: create /insert
R: read/select
U: update 
D: delete 
*/

select * from Productos;
UPDATE Productos set Precio = 500 WHERE Id_Producto = 1;

DELETE from Productos WHERE Nombre_Producto LIKE 'Harina%';
select * from Productos WHERE Nombre_Producto LIKE 'Harina%';
CREATE TABLE Receta(
ID_Receta int not null auto_increment Primary key,
Nombre_Receta varchar(40)
);

INSERT INTO Receta (Nombre_Receta) Values("Pan casero");
INSERT INTO Receta (Nombre_Receta) Values("Biscochuelo");
INSERT INTO Receta (Nombre_Receta) Values("MEdialunas");
INSERT INTO Receta (Nombre_Receta) Values("Bizcocho");
INSERT INTO Receta (Nombre_Receta) Values("Facturas");





