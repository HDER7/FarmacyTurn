def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por sumar")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print(f"No es un numero")
        else:
            print(f"Ingresate el numero {numero}")
            break

pedir_numero()
try:
    suma()
except TypeError:
    print("No se puede concatenar tipos distintos")
except ValueError:
    print("Eso no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")

def suma2(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")

suma2(1,"d")

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ValueError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

cociente(1,'d')

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo('mfmfkjf')