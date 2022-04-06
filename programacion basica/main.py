from comprar import *
from os import system
from reclamos import *
from cliente import cliente
from admin import *

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
        admin()

    if respuesta == "3":
        running = False
