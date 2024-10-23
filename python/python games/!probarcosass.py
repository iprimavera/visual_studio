import pygame
pygame.init()
from pygame.locals import *
 # Cargar imagen original
imagen_original = pygame.image.load("imagenes/mario.png")
 # Obtener dimensiones originales de la imagen
ancho_original = imagen_original.get_width()
alto_original = imagen_original.get_height()
 # Definir el factor de escala (quintuple)
factor_escala = 5
 # Calcular nuevas dimensiones escaladas
ancho_escala = ancho_original * factor_escala
alto_escala = alto_original * factor_escala
 # Escalar la imagen
imagen_escalada = pygame.transform.scale(imagen_original, (ancho_escala, alto_escala))
 # Crear ventana del juego
ventana = pygame.display.set_mode((2560, 1440), FULLSCREEN)
pygame.display.set_caption("Imágenes escaladas")
 # Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
     # Dibujar imagen escalada en la ventana
    ventana.blit(imagen_escalada, (0, 0))
    pygame.display.update()