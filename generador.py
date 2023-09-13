def generador():
    for x in range(1,5):
        yield x * 10

g = generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))


def mi_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


g2 = mi_generador()

print(next(g2))
print(next(g2))
print(next(g2))


def gen():
    n = 0
    while True:
        n += 1
        yield n


generador = gen()

def gen():
    lista=["Te quedan 3 vidas","Te quedan 2 vidas","Te queda 1 vida","Game Over"]
    for i in lista:
        yield i

perder_vida = gen()