def addProduct(nombre_producto, codigo, precio, stock):
    with open("producto.txt", 'a') as productos:
        productos.write(f"{nombre_producto} {codigo} {precio} {stock}\n")
    
    print("Producto:", nombre_producto, "| añadido a la base de datos")
