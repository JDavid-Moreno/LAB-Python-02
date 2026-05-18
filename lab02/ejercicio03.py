import math

def punto():
    print("a")
    temperaturas = [1,2,3,4,5,6,7,8,9,10]
    conversion = list(map(lambda x:(x * 1.8) + 32, temperaturas))
    print(conversion)

    print("b")
    listaUno = [1,2,3,4]
    listaDos = [5,6,7,8]
    sumaListas = list(map(lambda x,y: x + y, listaUno, listaDos))
    print(sumaListas)

    print("c")
    radios = [1,2,3,4,5,6,7,8,9,10]
    areas = list(map(lambda x: (x * x) * math.pi, radios))
    print(areas)

    print("d")
    productos = {"pan": 1000, "leche": 2500, "café": 5000}
    listaTuplas = list(map(lambda x: (x[0], x[1] + (x[1] * 0.1)), productos.items()))
    print(listaTuplas)

    print("e")
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    multiplicacion = list(map(lambda fila: list(map(lambda x: x * 10, fila)), matriz))
    print(multiplicacion)

def main():
    punto()
main()