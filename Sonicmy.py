from json import load
import pygame
from pygame.locals import *
from sys import exit 

pygame.init()


tela = pygame.display.set_mode((1000, 500))
bg_img = pygame.image.load('fundo2.png')
bg = pygame.transform.scale(bg_img, (1100, 500))

width = 1000
i = 0
BRANCO = (255,255,255)

class Sonic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sonic/sonic-1.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-2.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-3.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-4.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-5.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-6.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-7.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-1.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-2.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-3.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-4.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-5.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-6.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-7.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-1.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-2.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-3.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-4.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-5.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-6.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-7.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-1.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-2.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-3.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-4.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-5.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-6.png'))
        self.sprites.append(pygame.image.load('sonic/sonic-7.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128, 64))

        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 100

        
        self.animar = False

    def atacar(self):   
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.15
            if self.atual >= len(self.sprites):
                self.atual= 0
                self.animar = True
            self.image = self.sprites[int(self.atual)]    
            self.image = pygame.transform.scale(self.image, (128, 64))

todas_as_sprites = pygame.sprite.Group()
sonic = Sonic()
todas_as_sprites.add(sonic)

relogio = pygame.time.Clock()


while True:
    
    relogio.tick()
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:    
            sonic.atacar()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()            
    pygame.display.flip()

    