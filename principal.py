from numeros import *


def inicio():
    m = """Elige un turno para?:
    [1] Farmacia
    [2] Cosmetica
    [3] Perfumeria"""
    i = 's'
    while True:
        try:
            print(m)
            entrada = int(input())
        except:
            print("\nEse no es un numero\n")
        else:
            break
    return entrada


c = cosmetica()
f = farmacia()
p = perfumeria()

while True:
    eleccion = inicio()
    if eleccion == 1:
        print(next(f))
        eleccion = input("Otro turno?[s/n]: ")
    elif eleccion == 2:
        print(next(c))
        eleccion = input("Otro turno?[s/n]: ")
    elif eleccion == 3:
        print(next(p))
        eleccion = input("Otro turno?[s/n]: ")
    else:
        break
    if eleccion == 'n':
        break
