"""
Modulo donde se va a realizar un proceso que controle el ingreso de los reclamos que los clientes hacen
Las funciones presentaran lo siguiente
- Solicitud de datos del cliente
- Anotar y guardar el reclamo para su posterior consulta
- Mostrar la cantidad de reclamos que se han ingresado
"""
from os import system


reclamos_path = "txt/reclamos.txt"


# Funcion para agregar un nuevo reclamo 
def agregar_reclamo():
    # Se presentan las variables donde se le piden los datos al clientes
    reclamo = input("Ingrese su reclamo: ")
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    numero = input("Ingrese su numero telefonico: ")

    # abrimos el archivo plano de los reclamos con funcion de agregar una nueva linea
    with open(reclamos_path, 'a') as reclamos:
        reclamos.write(f"{reclamo}|{nombre}|{email}|{numero}\n") # agregar el reclamo

    print("Reclamo agregado a nuestro sistema")
    # print("Hay un total de", cantReclamos(), "reclamos.")



# Funcion para mostrar la cantidad de reclamos que se han ingresado
def cantReclamos():
    with open(reclamos_path) as reclamos: # abrimos el archivo plano donde contiene los reclamos
        cantReclamos = 0 # Variable que se usara para contar la cantidad de reclamos
        for linea in reclamos: # Por cada linea que hay en el archivo de reclamos
            cantReclamos += 1 # sumamos uno a uno los reclamos
    return cantReclamos # retornamos la cantidad de reclamos



def verReclamos():
    cantReclamos = cantReclamos()
    print(f"Hay {cantReclamos} reclamos")
    reclamos = open('txt/reclamos.txt', 'r')
    for linea in reclamos:
        datos = linea.split('|')
        input()
        system('cls')
        print(f"{datos[1]}: {datos[0]}\n{datos[2]} - {datos[3]}")
# Autor: Binjie Liang