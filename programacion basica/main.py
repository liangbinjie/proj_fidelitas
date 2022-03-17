from buscador import *
from agregar import *


running = True

while running:
    print("Que desea hacer?\n-Buscar\n-Agregar\n")
    do = input("> ")

    if do.lower() == "buscar":
        print('- - - - - - - - - - - - - - - - - - - -')
        tipo = input("Tipo de busqueda\n-General\n-Codigo\n-Precio\n\n >").lower()
        print('- - - - - - - - - - - - - - - - - - - -')

        if tipo == "general":
            nombre_producto = input("Ingrese nombre de producto o codigo: ").lower()
            print(bgeneral(nombre_producto))


        elif tipo == "codigo":
            codigo = input("Ingrese codigo de producto: ")
            print(bcodigo(codigo))


        elif tipo == "precio":
            precio_i = int(input("Ingrese precio inicial: "))
            precio_f = int(input("Ingrese precio de rango final: "))

            if precio_f < precio_i:
                print("Precio de rango final invalido")

            else:
                print(brango(precio_i, precio_f))




    elif do.lower() == "agregar":
        print('- - - - - - - - - - - - - - - - - - - -')
        nombre_producto = input("Nombre de producto a agregar: ")
        codigo = input("Ingrese codigo de producto: ")
        precio = int(input("Ingrese precio de producto: "))
        stock = int(input("Ingrese cantidad de productos en inventario: "))
        addProduct(nombre_producto.lower(), codigo, precio, stock)

    print('- - - - - - - - - - - - - - - - - - - -')

    if do == "1":
        running = False
