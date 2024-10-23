import random
fin_juego = False
valores_de_juego = (1, 1000)
minimo, maximo = valores_de_juego
turnos = 0
while True:
    iniciar = input(f"""
-piensa un numero del {minimo} al {maximo}
-cuando lo tengas escribe \"c\" para empezar a jugar
-si quieres salir escribe cualquier otra cosa\n
""")
    if iniciar == "c":
        print("\n-voy a intentar adivinar tu numero")
        print("-si tu numero es menor al que diga di \"menor\"\n-si tu numero es mayor al que diga di \"mayor\"\n-si lo he adivinado di \"si\"")
        while fin_juego == False:
            turnos += 1
            numero = random.randint(minimo, maximo)
            print("\n-he pensado en el numero", numero)
            respuesta = input("\n")
            match respuesta:
                case "mayor":
                    if maximo == numero:
                        print("\n-debes de haberme dicho alguna indicacion mal\n-va a haber que terminar la partida")
                        fin_juego = True
                    else:
                        minimo = numero + 1
                case "menor":
                    if minimo == numero:
                        print("\n-debes de haberme dicho alguna indicacion mal\n-va a haber que terminar la partida")
                        fin_juego = True
                    else:
                        maximo = numero - 1
                case "si":
                    print("\n-¡Genial!\n-turnos que he tardado en adivinarlo:", turnos)
                    fin_juego = True
                case _:
                    pass
        continuar = input("\n-quieres jugar de nuevo?\n\n")
        if continuar == "no":
            break
        else:
            fin_juego = False
            turnos = 0
            minimo, maximo = valores_de_juego
    else:
        break
