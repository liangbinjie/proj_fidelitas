from buscador import *
from modificador import *
from os import system

divisor = "-"*60
factura_path = 'txt/factura.txt'


def factura(comprado, subtotal):
    print("- "*13)
    print("\nProceso de facturacion\n")
    empleado = input("Ingrese nombre empleado: ")
    cliente = input("Ingrese nombre de cliente: ")
    identificacion = input("Ingrese identificacion: ")
    telefono = input("Ingrese numero de telefono: ")
    direccion = input("Ingrese direccion: ")


    iva = subtotal * 0.13
    total = subtotal * 1.13

    
    factura =  open(factura_path, 'w')
    datos_cliente = f"Cliente: {cliente}\nIdentificacion: {identificacion}\nTelefono: {telefono}\nDireccion: {direccion}"
    fact = f"Empleado: {empleado}\n\nProductos comprados\n{divisor}\n{comprado}\n{divisor}\n{datos_cliente}\n{divisor}\nSubtotal: ${subtotal}\nIVA: {iva}\nTotal: {round(total)}\n{divisor}\nGracias por visitarnos"
    factura.write(fact)
    return fact


def comprar():
    producto = input("Digite producto que quiere comprar: ")
    producto = bproducto(producto) # buscamos el producto en el inventario

    if producto != False: # si el producto esta en el inventario
        stock = bstock(producto) # buscamos cuanto tenemos en stock
        print(f"Tenemos en inventario {stock} {producto}") 
        cantidad = int(input("Cuantos desea comprar?\n> "))
        if cantidad <= stock: # si la cantidad que desea comprar el cliente es menor o igual a nuestro stock
            precio = bprecio(producto) # buscamos el precio del producto
            valor = precio*cantidad # le damos el valor final al/los producto/s
            modificar(producto, "stock", stock-cantidad) # modificamos el stock
            print(f"Este producto tiene un precio de {precio} c/u")
            print(f"Un valor de {valor} por estos productos")
            return int(valor), producto, cantidad # retornamos el valor, el producto y la cantidad comprada

        if cantidad > stock:
            return 0, 0, 0

    elif producto == False: # si no encontramos el producto, regresamos todo en Falso
        return False, False, False


def proceso_compra():

    comprado = ""
    subtotal = 0
    facturar = 0
    valor, producto, cant = comprar()
    
    if valor or producto or cant != False:
        subtotal += valor
        comprado += f"{producto} | {cant} | ${valor}\n" + ""
        facturar = 1
    
    elif valor == False and producto == False and cant == False:
        print("Sin resultados")
    
    elif valor == 0 and producto == 0 and cant == 0:
        print("No tenemos tanto pa")

    continuar = input("Desea continuar comprando? y/n\n> ")

    if continuar == "y":
        continuar = True
        while continuar:
            valor, producto, cant= comprar()
            if valor or producto or cant != False:
                subtotal += valor
                comprado += f"{producto} | {cant} | ${valor}\n" + ""
                facturar = 1
            
            elif valor or producto or cant == False:
                print("Sin resultados")
            continuar = input("Desea continuar comprando? y/n\n> ")
        
            if continuar == "n":
                continuar = False

    

    if facturar == 1:
        fact_impresa = factura(comprado, subtotal)
        print("Factura lista")
        input()
        system('cls')
        print(fact_impresa)
    
    elif facturar == 0:
        pass
    input()
    system('cls')
