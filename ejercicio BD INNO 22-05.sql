CREATE DATABASE BD_EJEMPLO_TST;
use bd_ejemplo_tst;

insert INTO bd_ejemplo_tst.persona(DNI,Nombre,Telefono)
VALUES(30222555,'Debora',15505050);/*INSERTA UN REGISTRO EN LA TABLA*/

SELECT * from bd_ejemplo_tst.persona; /*TRAE TODOS LOS REGISTROS DE LA TABLA PERSONA*/

DELETE from bd_ejemplo_tst.persona WHERE Nombre = 'Jose'; /*ESTO ELIMINA DONDE LOS REGISTROS COINCIDAN CON EL NOMBRE DE JOSE*/

DELETE from bd_ejemplo_tst.persona; /*ESTO ELIMINA TODA LA TABLA ENTERA*/


/*UPDATE DELETE SELECT */
/*
hola
esto
es un
comentario
*/