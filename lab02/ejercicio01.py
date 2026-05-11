def primer_punto():
    #a
    print("a")
    primer_numero = int(input("ingrese un numero: "))
    multiplo_tres = lambda x: x % 3 == 0
    print(multiplo_tres(primer_numero))
    
    #b
    print("b")
    segundo_numero = int(input("ingrese un numero: "))
    cubo = lambda x: x ** 3
    print(cubo(segundo_numero))
    
    #c
    print("c")
    tercer_numero = int(input("ingrese un numero: "))
    cuarto_numero = int(input("ingrese un numero: "))
    producto = lambda x, y: x * y
    print(producto(tercer_numero,cuarto_numero))
    
    #d
    print("d")
    quinto_numero = int(input("ingrese un numero: "))
    sexto_numero = int(input("ingrese un numero: "))
    mayor = lambda x, y: x if x > y else y
    print(mayor(quinto_numero,sexto_numero))

    #e
    print("e")
    primera_palabra = input("ingrese la palabra: ")
    verificar_a = lambda x, letra: x[0].lower() == letra.lower() if x else False
    print(verificar_a(primera_palabra,"A"))

    #f
    print("f")
    temperatura = int(input("ingrese la temperatura en Celsius: "))
    convertidor = lambda x: (x * 1.8) + 32
    print(convertidor(temperatura))

def segundo_punto():
    lista_lambdas = [
        lambda x: x * 2,
        lambda x: x + 10,
        lambda x: x ** 2
    ]
    numero_lista = int(input("ingrese un numero: "))
    for i in lista_lambdas:
        print(i(numero_lista))

def main():
    print("1. Primer punto")
    print("2. Segundo punto")
    print("3. Salir")
    punto = int(input("punto a revisar: "))
    while punto != 3:
        match punto:
            case 1:
                primer_punto()
                punto = int(input("punto a revisar: "))
            case 2:
                segundo_punto()
                punto = int(input("punto a revisar: "))
                
            case _:
                print("numero invalido, elija otro")
                punto = int(input("punto a revisar: "))
main()