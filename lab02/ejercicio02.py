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
    

def main():
    punto()
main()