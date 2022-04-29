from os import system
from random import choice


words_list = open('words.txt', 'r')
lista = []
for word in words_list:
    lista.append(word)

def nombre_ganador(nombre, palabra):
    bitacora = open('bitacora.txt', 'a')
    bitacora.write(f"Nombre ganador: {nombre}\n")
    bitacora.write(f"Palabra adivinada: {palabra}\n")
    bitacora.write("-"*60+"\n")


def juego():

    palabra = choice(lista)[:-1]
    print(palabra)
    adivinada = []
    for ch in range(len(palabra)):
        adivinada.append("_")


    palabra_adivinada = ""

    print("\n[PISTA] La palabra comienza con", palabra[0] + "\n")
    input("Enter para seguir")


    intentos = 10
    while intentos != 0:
        system('cls')
        print("Cantidad de intentos disponibles", intentos)
        print("\nAdivine la palabra:\n")

        for i in adivinada:
            print(i, end=" ")
        
        letra = input("\n> ")
        
        if letra == None or letra == "":
            pass
        
        else:
            encontrado = len(palabra)

            for ch in range(len(palabra)):
                if letra in palabra[ch]:
                    adivinada[ch] = letra
                    palabra_adivinada += letra
                
                elif letra not in palabra[ch]:
                    encontrado -= 1
                
            if encontrado == 0:
                print("Incorrecto")
                intentos -= 1
                input()


            if palabra_adivinada == palabra:
                for i in adivinada:
                    print(i, end=" ")
                print("\n\nGANASTE!!")
                nombre = input("Ingrese tu nombre nuevamente: ")
                nombre_ganador(nombre, palabra_adivinada)
                menu()
            

    if intentos == 0:
        print("\n")
        print("*"*40)
        print("\nGAME OVER PERDISTE\n")
        print("La palabra es", palabra, "\n")
        print("*"*40)
        input()
        menu()
            

def menu():
    system('cls')
    on = True
    print("-"*30)
    print("\nQue desea hacer?\n[1]Volver a Jugar\n[2]Ver Bitacora\n[3]Salir\n")
    print("-"*30)
    respuesta = int(input("> "))

    while on:
        if respuesta == 1:
            juego()

        if respuesta == 2:
            bitacora = open('bitacora.txt', 'r')
            print("\n\n")
            print(bitacora.read())
            input("Enter para seguir")
            menu()

        if respuesta == 3:
            quit()


def main():
    on = True

    nombre_jugador = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    print("Bienvenido", nombre_jugador)
    print("*"*60)
    while on:
        menu()


main()
