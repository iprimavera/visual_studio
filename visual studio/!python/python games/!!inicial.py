import pygame as p
from pygame.locals import *

p.init()
ventana = p.display.set_mode((2560, 1440), FULLSCREEN)
p.display.set_caption("hola mundoo")



while True:
    for event in p.event.get():
        if event.type == QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
            p.quit()
            quit()
    
    
     
    p.display.update()