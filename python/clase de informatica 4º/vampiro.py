numero = int(input("escribe un numero: "))
numero_lista = list(str(numero))
segundo_numero = int

def ElNumeroEstaEnLista(numero0, numero1, numero2):
    """te devuelve true si los dos numeros seleccionados componen al numero inicial"""
    
    numero1_str = str(numero1)
    numero2_str = str(numero2)
    numero_lista = list(str(numero0))
    
    for digito in numero1_str:
        if digito not in numero_lista:
            return False
        numero_lista.remove(digito)
    for digito in numero2_str:
        if digito not in numero_lista:
            return False
        numero_lista.remove(digito)
    return True

if numero > 10**9:
    print("el numero es demasiado grande")
elif numero < 0:
    print("el numero no puede ser negativo")
elif len(numero_lista) % 2 != 0:
    print("no es un numero vampiro")
else:
    for i in range(1, numero // 2):
        segundo_numero = numero // i
        if len(str(i)) == len(numero_lista) // 2 and len(str(segundo_numero)) == len(numero_lista) // 2: 
            #los numeros son los dos la mitad de grandes que el elegido
            if i % 10 !=0 or segundo_numero % 10 != 0:
                #los numeros no acaban simultaneamente en 0
                if ElNumeroEstaEnLista(numero, i, segundo_numero): #! uso una funcion porque si no me lio
                    print("el numero si es un numero vampiro")
                    break
                else:
                    continue
            else:
                continue
            
    else:
        print("no es un numero vampiro")