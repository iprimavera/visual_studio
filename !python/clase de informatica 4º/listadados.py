import random
dados=[]
i = 0
orden = []
a = 0
b = 0
c = []
while len(dados) < 30:
    numero = random.randint(1,6)
    dados.append(numero)
while i < 6:
    i += 1
    print("el numero", i, "ha salido", dados.count(i), "veces")
    orden.append(dados.count(i))
while a < 6:
    if orden[a] >= orden[b]:
        b += 1
        if b == 6:
            c.append(a+1)
            b = 0
            while b < 6:
                if orden[a] == orden[b] and b != a:
                    c.append(b+1)
                    b += 1
                else:
                    b += 1
            if len(c) == 1:
                print("el dado que mas ha salido es el", c[0])
            else:
                print("los dados que mas han salido son:")
                d = 0
                while d < len(c):
                    print(c[d])
                    d += 1
            break
    else:
        a += 1
        b = 0
        