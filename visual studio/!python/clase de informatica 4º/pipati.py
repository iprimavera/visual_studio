import random
print("JUEGA AL PIEDRA PAPEL O TIJERA")
marcadorP = 0
marcadorO = 0
while marcadorP < 3 and marcadorO < 3:
    ordenador = random.randint(1, 3)
    tuEleccion = input("- Indica tu eleccion (Piedra [D], Papel [P] o Tijeras [T]): ")
    if ordenador == 1:
        eleccion = "piedra"
    elif ordenador == 2:
        eleccion = "papel"
    else:
        eleccion = "tijeras"
    if tuEleccion == "D":
        if ordenador == 1:
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        elif ordenador == 2:
            marcadorO += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        else:
            marcadorP += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
    elif tuEleccion == "P":
        if ordenador == 1:
            marcadorP += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        elif ordenador == 2:
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        else:
            marcadorO += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
    elif tuEleccion == "T":
        if ordenador == 1:
            marcadorO += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        elif ordenador == 2:
            marcadorP += 1
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
        else:
            print("- el ordenador ha elegido ", eleccion)
            print("- Marcador: ", marcadorP, " - ", marcadorO)
            continue
    else:
        print("- esa no es una eleccion valida")
        continue
if marcadorO == 3:
    print("Has perdido! :(")
else:
    print("Has ganado!!!")
