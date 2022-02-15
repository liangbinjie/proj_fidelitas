"""Avance numero 1, de la semana 4"""

# Autor del documento: Binjie Liang
# Se procede a realizar el punto 1 del proyecto, que es el Inventario

"""
Inventario: se solicita los siguientes datos de un producto:
- Nombre del producto
- Codigo del producto
- Precio
- Cantidad disponible
"""

nombreProducto = input("Nombre del producto: ")
codigoProducto = input("Ingrese el codigo del producto: ")
precioProducto = int(input("Ingrese el precio del producto: "))
cantDisponible = int(input("Ingrese la cantidad disponible: "))

# Estos datos de entrada se almacenaran en un archivo plano

# En el futuro se añadirán funciones como: agregar, modificar, eliminar y consultar productos

""" 
Por medio de una funcion (que se hara en el futuro) se podra consultar lo siguiente:
i. Por código de producto
ii. General, todos los productos con sus datos relevantes
iii. Por precio, ya sea por rangos, mayores o menores a un valor en particular
iv. Opción para desplegar en pantalla o a un archivo plano la consulta específica.
"""

print("Que busqueda desea realizar?\n-Codigo\nPrecio\nGeneral")
consulta = input("> ")

if consulta == "Codigo":
    # se va a realizar una busqueda por el archivo plano
    print(codigoProducto)

elif consulta == "Precio":
    print(precioProducto)

elif consulta == "General":
    print(nombreProducto, codigoProducto, precioProducto, cantDisponible)

