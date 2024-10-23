import sys,pygame as p
from pygame.locals import *

p.init()
ventana = p.display.set_mode((600, 600))
p.display.set_caption("hola mundoo")



color = [249, 100, 6]
maxcolor = False
frames = 0


while True:
    
    
    
    ventana.fill(color)
    if frames == 20:
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
    
    reversecolor = color.copy()
    reversecolor.reverse()
    p.draw.circle(ventana, reversecolor, (300, 300), 20)
    
    for evento in p.event.get():
        if evento.type == QUIT:
            p.quit()
            sys.exit() 
    p.display.update()