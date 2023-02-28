def impares(a, b):
    if b > a:
        for numero in range(a,b):
            if numero %2 != 0:
                print(numero, end=" ")
    else:
        print("erro")