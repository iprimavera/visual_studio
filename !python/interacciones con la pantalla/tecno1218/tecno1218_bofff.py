import pyautogui
import time
import random
import win32api
import win32con
import keyboard

# pregunta 692 187, 1801 232
# 692 236, 1801 285
# 691 288, 1801 336
# 691 341, 1801 389
# 691 392, 1801 442
# 1861 312 402
# 1233 410 255
# 139 216 255
# 877 488
# 958 575
# 253 175 98
# 708 156 155

aleatorio = 0
c = 800
lax = 695
first = False
preguntas = []
ancho = 1110
alto = 45
lista = []
yacreada = False
yagane = False
azul = [139, 216, 255]
naranja = [253, 175, 98]
index = 0
fin = None


def click(xcord, ycord):
    win32api.SetCursorPos((xcord, ycord))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def captura(xcord, ycord, cap):
    coso = cap.crop((xcord, ycord, xcord+ancho, ycord+alto))
    if coincide(877, 488, *naranja):
        if yacreada == False:
            lista[1].append(coso)
        else:
            preguntas[index][1].append(coso)
        return True
    elif coincide(958, 575, *naranja):
        if yacreada == False:
            lista[2].append(coso)
        else:
            if len(preguntas[index][2]) == 0:
                preguntas[index][2].append(coso)
        return True
    else:
        return False


def malalt(xcord, ycord, cap):
    if yacreada:
        coso = cap.crop((xcord, ycord, xcord+ancho, ycord+alto))
        if coso in preguntas[index][1]:
            return True
    return False


def coincide(xcord, ycord, r, g, b):
    if pyautogui.pixelMatchesColor(xcord, ycord, (r, g, b)):
        return True
    else:
        return False


while True:
    while coincide(708, 156, 155, 155, 155):
        yacreada = False
        yagane = False
        foto = pyautogui.screenshot()
        aleatorio = random.randint(1, 4)
        question = foto.crop((692, 187, 1801, 232))
        lista = [question, [], []]
        if keyboard.is_pressed('esc'):
            break
        for i in preguntas:
            if question == i[0]:
                yacreada = True
                index = preguntas.index(i)
                if len(i[2]) > 0:
                    click(c, 700)
                    hola = pyautogui.locateOnScreen(i[2][0])
                    x, y, a, b = hola
                    click(c, y+5)
                    yagane = True
                    break

        while True:
            if keyboard.is_pressed('esc'):
                break
            if yagane == True:
                break
            if aleatorio == 1:
                if not malalt(691, 236, foto):
                    click(c, 261)
                    time.sleep(0.1)
                    if captura(691, 236, foto) and yacreada == False:
                        preguntas.append(lista)
                    break
                else:
                    aleatorio += 1
                    print("cambio1")
            if aleatorio == 2:
                if not malalt(691, 288, foto):
                    click(c, 313)
                    time.sleep(0.1)
                    if captura(691, 288, foto) and yacreada == False:
                        preguntas.append(lista)
                    break
                else:
                    aleatorio += 1
                    print("cambio2")
            if aleatorio == 3:
                if not malalt(691, 341, foto):
                    click(c, 366)
                    time.sleep(0.1)
                    if captura(691, 341, foto) and yacreada == False:
                        preguntas.append(lista)
                    break
                else:
                    aleatorio += 1
                    print("cambio3")
            if aleatorio == 4:
                if not malalt(691, 392, foto):
                    click(c, 417)
                    time.sleep(0.1)
                    if captura(691, 392, foto) and yacreada == False:
                        preguntas.append(lista)
                    break
                else:
                    aleatorio = 1
                    print("cambio4")
        time.sleep(0.05)
        while coincide(lax, 250, *azul) or coincide(lax, 300, *azul) or coincide(lax, 350, *azul) or coincide(lax, 400, *azul):
            time.sleep(0.02)
    if pyautogui.pixelMatchesColor(1233, 410, (255, 0, 0)):
        click(1861, 402)
        print("fallo")
        while not coincide(708, 156, 155, 155, 155):
            click(1861, 312)
    else:
        while True:
            time.sleep(0.02)
            if keyboard.is_pressed('esc'):
                fin = True
                break
            elif keyboard.is_pressed("c"):
                fin = False
                break
        if fin:
            break
        else:
            while not coincide(708, 156, 155, 155, 155):
                click(1861, 312)
