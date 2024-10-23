import random
numero = random.randint(1, 100)
print("ADIVINA UN NUMERO DEL 1 AL 100")
intento = 1
while intento <= 8:
    print("- Indica un numero ( Intento ", intento, "): ")
    tuNumero = input()
    tuNumero = int(tuNumero)
    if tuNumero != numero and not intento == 8:
        if tuNumero < 1 or tuNumero > 100:
            print("ese numero no está entre 1 y 100")
            continue
        elif tuNumero < numero:
            print("- El número secreto es mayor")
        elif tuNumero > numero:
            print("- El numero secreto es menor")
    elif tuNumero == numero:
        print("correcto!!! ese era el numero secreto, lo has acertado al intento numero ", intento)
        break
    else:
        print("Has perdido! :(")
        print("El número secreto era ", numero)
    intento += 1
