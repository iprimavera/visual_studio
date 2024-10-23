# word = str(input("Please Enter The Word:"))
# wordlist=[]
# j=1
# for i in range(len(word)):
#     wordlist.insert(i,word[i:j])
#     j=j+1
# print("Character Count: " + str(len(word) - wordlist.count(" ")))
# print("Word Count: " + str(wordlist.count(" ")+1))
#! el codigo de arriba es de un ingeniero informatico, que tiene errores, y yo he hecho uno mejor abajo B)
antes, a, palabras, letras = 0, 0, 0, 0
frase = input("escribe una frase:")
for i in frase:
    if i != " ":
        if antes == " " or antes == 0:
            palabras += 1
        letras += 1
    antes = str(i)
    a += 1
print(f"contador de palabras: {palabras}")
print(f"contador de caracteres: {letras}")