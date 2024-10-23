numero = input("escribe un numero: ")
numero = list(numero)
if int(numero[len(numero)-1]) > 0 and int(numero[0]) > 0:
    for i in range(len(numero)):
        if (int(numero[i]) + (int(len(numero)) - i)) % 2 != 0:
            if i == len(numero) - 1:
                print("el numero si es reversible")
                break
        else:
            print("el numero no es reversible")
            break
else:
    print("el numero no es reversible")