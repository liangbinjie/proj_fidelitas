from buscador import *
from modificador import *


running = True

while running:
    print("Que desea hacer?\n[1]Buscar\n[2]Agregar\n[3]Eliminar\n[4]Modificar\n[0]Salir")
    do = input("> ").lower()

    if do == "buscar" or do == "1":
        print('- - - - - - - - - - - - - - - - - - - -')
        tipo = input("Tipo de busqueda\n[1]General\n[2]Precio\n\n > ").lower()
        print('- - - - - - - - - - - - - - - - - - - -')

        if tipo == "general" or tipo == "1":
            nombre_producto = input("Ingrese nombre de producto o codigo: ").lower()
            print(bgeneral(nombre_producto))


        # elif tipo == "codigo" or tipo == "2":
        #     codigo = input("Ingrese codigo de producto: ")
        #     print(bcodigo(codigo))


        elif tipo == "precio" or tipo == "2":
            rango_i = int(input("Ingrese precio inicial: "))
            rango_f = int(input("Ingrese precio de rango final: "))

            if rango_f < rango_i:
                print("\nPrecio de rango final invalido\nIntente denuevo")

            else:
                print(brango(rango_i, rango_f))




    elif do == "agregar" or do == "2":
        print('- - - - - - - - - - - - - - - - - - - -')
        nombre_producto = input("Nombre de producto a agregar: ")
        codigo = input("Ingrese codigo de producto: ")
        precio = int(input("Ingrese precio de producto: "))
        stock = int(input("Ingrese cantidad de productos en inventario: "))
        agregar(nombre_producto.lower(), codigo, precio, stock)

    
    elif do == "modificar" or do == "4":
        print('- - - - - - - - - - - - - - - - - - - -')
        producto = input("Nombre o codigo del producto: ")
        dato = input("Tipo de dato: ")
        nuevo = input("Dato nuevo: ")
        modificar(producto, dato, nuevo)



    elif do == "eliminar" or do == "3":
        print('- - - - - - - - - - - - - - - - - - - -')
        producto = input("Ingrese nombre o codigo de producto: ")
        eliminar(producto)




    print('- - - - - - - - - - - - - - - - - - - -')

    if do.lower() == "salir" or do == "0":
        running = False
