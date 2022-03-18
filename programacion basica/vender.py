from buscador import *
from modificador import *


def vender():
    producto = input("Inserte nombre de producto a vender: ")
    cantidad = int(input("Ingrese cantidad de productos a comprar: "))

    stock = bstock(producto)
    if stock >= cantidad:
        modificar(producto, "stock", stock-cantidad)

    elif stock < cantidad:
        print("No hay suficiente en inventario")
    

vender()
