import sys,pygame as p
from pygame.locals import *
import random
import time

p.init()
ventana = p.display.set_mode((2560, 1440), FULLSCREEN)
p.display.set_caption("hola mundoo")
tiempo = 0
color = [0, 174, 6]
ran1 = random.randint(0, 2480)
ran2 = random.randint(0, 1290)
t=0
frames = 0
maxcolor = False
imagen = p.image.load("imagenes/mario.png")
imagen = p.transform.scale(imagen, (80, 150))
ventana.fill((color))
def mario():
    ventana.blit(imagen, (ran1,ran2))
mario()
while True:
    
    tiempo += 1
    
    for event in p.event.get():
        if event.type == QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
            p.quit()
            sys.exit() 
    if tiempo%50==0:
        ran1 = random.randint(0, 2480)
        ran2 = random.randint(0, 1290)
        tiempo = 0
    
    ventana.fill(color)
    if frames == 7:
        if maxcolor != True:
            if color[2] < 255:
                color[2] = color[2]+1
            else:
                maxcolor = True
        else:
            if color[2] > 0:
                color[2] = color[2]-1
            else:
                maxcolor = False
        frames = 0
    else:
        frames +=1
    
    mario()
                  
    p.display.update()