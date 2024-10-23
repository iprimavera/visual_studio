print("* Hola! Bienvenido a la minicalculadora de Iván")
operacion = input("- Indica la operación (suma, resta, multiplicacion o potencia): ")
if operacion == "suma" or operacion == "resta" or operacion == "multiplicacion" or operacion == "potencia":
    primerNumero = input("- indica el primer operando: ")
    segundoNumero = input("- indica el segundo operando: ")
    primerNumero = int(primerNumero)
    segundoNumero = int(segundoNumero)
    if operacion == "suma":
        print("el resultado es: ", primerNumero + segundoNumero)
    elif operacion == "resta":
        print("el resultado es: ", primerNumero - segundoNumero)
    elif operacion == "multiplicacion":
        print("el resultado es: ", primerNumero * segundoNumero)
    else:
        print("el resultado es: ", primerNumero ** segundoNumero)
else: 
    print("ERROR: Esa operación no existe")
        