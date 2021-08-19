def main():
    s=0
    cp = 0
    ci = 0
    print("Promedio de 10 numeros")
    for number in range(10):
        n = int(input("Escribe un numero"))
        if n%2 == 0:
            cp = cp + 1
        else:
            ci= ci + 1 
        s = s + n
    prom = s / 10
    print (f"El promedio es: {prom}, hay {cp} numeros pares y {ci+ numeros impares")
    

if __name__=='__main__':
    main()
