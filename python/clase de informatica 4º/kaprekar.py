numero = list(input("escribe un numero de menos de 5 digitos: "))
mayor = None
menor = None
x = 0
if len(numero) > 4:
    print("el numero es demasiado grande")
else:
    if len(numero) < 4:
        for i in range(4-len(numero)):
            numero.append("0")
    if numero[2] == numero[1] and numero[0] == numero[3] and numero[1] == numero[3]:
        print("el numero es un repdigit, por lo tanto no puede iterarse hasta llegar al numero 6174")
    elif numero == ["6","1" ,"7" ,"4"]:
        print("el numero es la propia constante de Kaprekar por lo tanto necesita 0 iteraciones")
    else:
        while numero != "6174":
            if x >= 1:
                numero = list(numero)
            if len(numero) < 4:
                for i in range(4-len(numero)):
                    numero.append("0")
            numero.sort(reverse=True)
            mayor = int(numero[0]+numero[1]+numero[2]+numero[3])
            numero. sort()
            menor = int(numero[0]+numero[1]+numero[2]+numero[3])
            numero = str(mayor - menor)
            x += 1
        else:
            print(f"ha necesitado {x} iteraciones")
        