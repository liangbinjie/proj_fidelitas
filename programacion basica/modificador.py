"""
Modulo donde se implementan funciones que modifican el inventario
Funciones como agregar productos
Eliminar productos
Cambiar informacion del producto
"""

import os
from buscador import *

def agregar(nombre_producto, codigo, precio, stock):
    with open("producto.txt", 'a') as productos:
        productos.write(f"{nombre_producto},{codigo},{precio},{stock}\n")
    
    print("Producto:", nombre_producto, "| añadido a la base de datos")


def eliminar(producto):
    encontrado = 0
    with open("producto.txt", 'r') as productos:
        with open("eliminados.txt", 'w') as eliminado_file:
            for linea in productos:
                datos = linea.split(",")

                if producto not in datos:
                    eliminado_file.write(linea)
                
 
                if producto in datos:
                    encontrado = 1
                    print("Eliminando producto:", datos[0], "\nCodigo:", datos[1])


    os.replace('eliminados.txt', 'producto.txt')
    
    if encontrado == 0:
        print("Producto no encontrado")
    
    else:
        print("\nProducto eliminado")
                    



def modificar(producto, dato, nuevo):
    # Primero buscamos el producto
    with open("producto.txt", 'r') as productos:
        with open("modificado.txt", 'w') as modificado:
            for line in productos:
                datos = line.split(",")

                if producto not in datos:
                        modificado.write(line)

                if producto in datos:

                    if dato == "nombre":
                        modificado.write(f"{nuevo},{datos[1]},{datos[2]},{datos[3]}")
                    
                    if dato == "codigo":
                        modificado.write(f"{datos[0]},{nuevo},{datos[2]},{datos[3]}")

                    if dato == "precio":
                        modificado.write(f"{datos[0]},{datos[1]},{nuevo},{datos[3]}")

                    if dato == "stock":
                        modificado.write(f"{datos[0]},{datos[1]},{datos[2]},{nuevo}\n")

    os.replace('modificado.txt', 'producto.txt')

