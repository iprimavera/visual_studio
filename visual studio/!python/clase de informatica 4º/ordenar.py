import random
a = 0
numeros = []
b = 0
while a < 20:
    numeros.append(random.randint(1,1000))
    a += 1
else:
    a = 0
print(numeros)
numeros.sort()
print(numeros)
print("el mayor numero es", numeros[19])
print("el menor numero es", numeros[0])
while a < 20:
    b = b + numeros[a]
    a += 1
else:
    b = b/20
print("la media de todos los numeros es", b)