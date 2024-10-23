texto = list(input("introduce un texto: "))

for i in range(texto.count(" ")):
    texto.remove(" ")

al_reves = texto[::-1]
print(al_reves, texto)
for i in range(len(texto)):
    if al_reves[i] == texto[i]:
        continue
    else:
        print("el texto no es palindromo")
        break
else:
    print("el texto si es palindromo")
    