def cambiarletra(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


opercion = cambiarletra("min")

opercion('palabra')


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

#@decorar_saludo
def mayus(texto):
    print(texto.upper())


def minus(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayus)

mayuscula_decorada('Heider')
