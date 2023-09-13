def perfumeria():
    n=0
    while True:
        n += 1
        yield f"Su turno es:\nP-0{n}\nAguarde y será atendido"


def farmacia():
    n=0
    while True:
        n += 1
        yield f"Su turno es:\nF-0{n}\nAguarde y será atendido"


def cosmetica():
    n=0
    while True:
        n += 1
        yield f"Su turno es:\nC-0{n}\nAguarde y será atendido"




