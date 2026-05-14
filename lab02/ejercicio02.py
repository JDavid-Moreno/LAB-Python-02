def punto():
    print("a")
    tuplas = [(n,n ** 2) for n in range(1,10)]
    print(tuplas)

    print("b")
    cubos = [x ** 3 for x in range(11,20)]
    print(cubos)

    print("c")
    pares = [x * 2 for x in range(1,10)]
    print(pares)

    print("d")
    lista = [1,2,3,4,5]
    valor = [f"valor:{x}" for x in range(1,10)]
    print(valor)

    print("e")
    fahr = [(x * 1.8) + 32 for x in range(1,10)]
    print(fahr)

    print("f")
    lista_palabras = ["ayuda","industrial","iapp","moreno"]
    for i in lista_palabras:
        if len(i) > 5:
            print(i)
    
    print("g")
    for i in lista_palabras:
        print(i[0])
    
    print("h")
    #usando la lista del punto d
    for i in lista:
        if i % 2 == 0:
            print("es par")
        else:
            print("es impar")
    
    print("i")
    matriz =  [[1,2,3], [4,5,6], [7,8,9]]
    listaAplanada = []
    for i in matriz:
        for j in i:
            listaAplanada.append(j)
    print(listaAplanada)

def main():
    punto()
main()