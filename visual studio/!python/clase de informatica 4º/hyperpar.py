numero = input("introduce un numero: ")
numero = list(numero)
a = 0
while a < len(numero):
    if int(numero[a]) % 2 == 0:
        a += 1
    else:
        print("el numero no es hyperpar")
        break
if a == len(numero):
    print("el numero si es hyperpar")