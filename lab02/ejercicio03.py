def punto():
    print("a")
    temperaturas = [1,2,3,4,5,6,7,8,9,10]
    conversion = list(map(lambda x:(x * 1.8) + 32, temperaturas))
    print(conversion)

def main():
    punto()
main()