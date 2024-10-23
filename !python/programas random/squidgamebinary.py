import random

# que me de x puertas de 0 o 1 y las transforme en decimal para memorizarlas, después volver a decirlas

nagrupamietos = 5
npuertas = 100

posicion = ""
nposicion = 0
nrelativposicion = nagrupamietos-1
repetitiva = 0
finalnumber = []


for i in range (npuertas):
    posicion += str(random.randint(0, 1))
print(posicion)

for i in range(int(len(posicion)/nagrupamietos)):
    
    for i in range (nagrupamietos):
        
        if posicion[nposicion] == "1":
            repetitiva += 2**nrelativposicion
        
        nrelativposicion -= 1
        nposicion += 1
    nrelativposicion = nagrupamietos-1
    finalnumber.append(repetitiva)
    repetitiva = 0
print (finalnumber)
    