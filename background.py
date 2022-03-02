from turtle import width
import pygame 

pygame.init()
win = pygame.display.set_mode((1000, 500))
bg_img = pygame.image.load('fundo2.png')
bg = pygame.transform.scale(bg_img, (1100, 500))

width = 1000
i = 0

run = True
while run:


    for event in pygame.event.get():...
    
    win.fill((0,0,0))
    win.blit(bg, (i, 0))
    win.blit(bg, (width+i, 0 ))
    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0
    i -= 1
    pygame.display.update()    