import random
listaNombres = []
while len(listaNombres) < 5:
    print("introduce el nombre ", len(listaNombres) + 1)
    nombre = input()
    listaNombres.append(nombre)
else:
    numero = random.randint(0,4)
    print("la persona elegida es", listaNombres[numero])