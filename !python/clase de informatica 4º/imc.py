peso=input("escribe tu peso: ")
altura=input("escribe tu altura: ")
peso=int(peso)
altura=float(altura)
imc = peso / (altura**2)
if imc<18.5:
    print("tienes bajo peso")
elif imc<24.9:
    print("tienes un peso ideal")
elif imc<29.9:
    print("tienes sobrepeso")
else:
    print("tienes obesidad")
    