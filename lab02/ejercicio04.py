def punto():
    print("a")
    palabras = ["ayuda", "IAPP", "conocimiento", "Python","reconocer"]
    filtroPalabras = list(filter(lambda x: len(x) > 4, palabras))
    print(filtroPalabras)

    print("b")
    elementos = [1,"cosa",10.2,None,True,False]
    filtroElementos = list(filter(lambda x: x is not None, elementos))
    print(filtroElementos)

    print("c")
    #usando la misma lista del A
    filtroVocal = list(filter(lambda x: x[0].lower() == "a" or x[0].lower() == "e" or x[0].lower() == "i" or x[0].lower() == "o", palabras))
    print(filtroVocal)

    print("d")
    #usando la misma lista del A
    palidromes = list(filter(lambda x: x == x[::-1], palabras))
    print(palidromes)

    print("e")
    listaNumeros = [1,2,3,4,5,6,7,8,9,10,15,20,25]
    filtroNumeros = list(filter(lambda num: num % 10 == 5, listaNumeros))
    print(filtroNumeros)

    print("f")
    productos = [
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Mouse", "precio": 40},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Webcam", "precio": 150}
]
    filtroProductos = list(filter(lambda producto: producto["precio"] > 100, productos))
    print(filtroProductos)

def main():
    punto()
main()