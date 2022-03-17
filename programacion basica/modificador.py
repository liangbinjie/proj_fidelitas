"""
Modulo donde se implementan funciones que modifican el inventario
Funciones como agregar productos
Eliminar productos
Cambiar informacion del producto
"""

import os

def agregar(nombre_producto, codigo, precio, stock):
    with open("programacion basica/proyecto/producto.txt", 'a') as productos:
        productos.write(f"{nombre_producto} {codigo} {precio} {stock}\n")
    
    print("Producto:", nombre_producto, "| añadido a la base de datos")


def eliminar(producto):
    with open("programacion basica/proyecto/producto.txt", 'r') as productos:
        with open("programacion basica/proyecto/eliminados.txt", 'w') as eliminado_file:
            for linea in productos:
                datos = linea.split()
                if producto not in datos:
                    eliminado_file.write(linea)
                
                encontrado = 0
                if producto in datos:
                    encontrado = 1
                    print("Eliminando producto:", datos[0], "\nCodigo:", datos[1])


    os.replace('programacion basica/proyecto/eliminados.txt', 'programacion basica/proyecto/producto.txt')
    
    if encontrado == 0:
        print("Producto no encontrado")
    
    else:
        print("\nProducto eliminado")
