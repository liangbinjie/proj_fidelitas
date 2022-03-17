# Modulo para hacer busqueda dentro del inventario


# Funcion para hacer una busqueda general
def bgeneral(producto):
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open("producto.txt") as productos:
        for linea in productos: # por cada linea que tiene el archivo plano
            datos = linea.split() # dividiremos los datos que tiene cada linea
            if producto in datos: # si el nombre del producto esta dentro de la linea
                return f"\nNombre de producto: {datos[0]}\nCodigo: {datos[1]}\nPrecio: {datos[2]}\nEn inventario: {datos[3]}"  # regresamos el nombre, codigo y precio del producto



# Funcion para hacer una busqueda por medio de codigo
def bcodigo(codigo):
    # vamos a abrir el archivo plano donde estan almacenados los productos
    with open("producto.txt") as productos:
        for linea in productos: # por cada linea que tiene el archivo plano
            datos = linea.split() # vamos a dividir los datos de cada linea dentro de un arreglo
            if codigo in datos: # si el codigo del producto esta dentro de la linea
                return "Nombre producto: " + datos[0], "Precio: " + datos[2], "Cant Disponible: " + datos[3] # regresamos el nombre y precio del producto



# Funcion de busqueda por rango de precios
def brango(rango_i:int, rango_f:int):
    lista = []
    # rango_i seria precio inicial y rango_f seria precio final, para marcar el rango de los precios
    with open("producto.txt") as productos:
        for linea in productos: # por cada linea que hay en producto.txt
            datos = linea.split() # dividimos los datos de cada linea
            if int(datos[2]) >= rango_i and int(datos[2]) <= rango_f: # si los datos del precio es igual o mayor al rango inicial y menior o igual al rango final

                lista.append(f"{datos[0]}: {datos[2]}") # agregamos el nombre del producto y su precio dentro del arreglo llamado lista
                

    return lista # al final regresamos el arreglo con todos los datos
