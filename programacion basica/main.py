from inventario import inventario
from comprar import *
from os import system
from getpass import getpass
from reclamos import *
from cliente import cliente

system('cls')
basedatos = {"admin": "admin1234", "benji": "1386"}
intentos = 1


running = True

while running:
    system('cls')
    print("Como quieres entrar?\n[1]Cliente\n[2]Administrador\n[3]Salir")
    respuesta = input("> ")

    if respuesta == "1":
        system('cls')
        cliente(respuesta)



    if respuesta == "2":
        usuario = input("Usuario: ")
        contra = getpass("Contraseña: ")


        while usuario not in basedatos or contra != basedatos[usuario]:
            intentos += 1
            print("Invalido, intente otra vez")
            usuario = input("Usuario: ")
            contra = getpass("Contraseña: ")
            if intentos == 3:
                print("Has usado el numero maximo de intentos")
                quit()
        
        else:
            system("cls")
            print("Adonde quieres entrar?\n[1]Inventario\n[2]Reportes\n[3]Ver Reclamos")
            admin = input("> ")

            if admin == "1":
                system("cls")
                print('\n- - - - - - - - - - - - - - - - - - - -')
                print("Has entrado al inventario")
                inventario()
            # Creacion de funcion para Reportes generales

            if admin == "3":
                verReclamos()


    if respuesta == "3":
        running = False
