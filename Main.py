import Controlador

while True:
    print("\n+-------------------------------------------+")
    print("|         Big Bread SA         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - ALTA / BAJA / MODIFICACION DE INSUMOS")
    print("3 - ALTA / BAJA / MODIFICACION DE PRODUCCIÓN DIARIA")
    print("4 - ALTA / BAJA / MODIFICACION DE RECETAS")
    print("5 - LISTADO DE PRODUCTOS")
    print("6 - LISTADO DE PRODUCCIÓN EN UN INTERVALO")
    print("7 - LISTADO DE INSUMOS DIARIO")
    print("8 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Controlador.InsertarProducto()
    elif opcion == 2:
        None
    elif opcion == 3:
        None
    elif opcion == 4:
        None
    elif opcion == 5:
        Controlador.ListarProductos()
    elif opcion == 6:
        None
    elif opcion == 7:
        None
    elif opcion == 8:
        break
    else:
        print("¡Opción incorrecta!")


