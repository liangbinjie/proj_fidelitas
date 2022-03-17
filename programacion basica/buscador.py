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
def brango(precio_i:int, precio_f:int):
    # precio_i seria precio inicial y precio_f seria precio final, para marcar el rango de los precios
    with open("producto.txt") as productos:
        for linea in productos: # por cada linea que hay en producto.txt
            datos = linea.split()
            if int(datos[2]) >= precio_i and int(datos[2]) <= precio_f:
                print(f"{datos[0]}: {datos[2]}")
                return datos[2]
# ?????
