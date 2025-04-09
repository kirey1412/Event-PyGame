import pygame, time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
title=pygame.display.set_caption("Event")

guppi_x,guppi_y=300,0
bg=pygame.image.load("background.png")
guppi=pygame.image.load("guppi.png")

while guppi_y < 500:
    screen.blit(bg, (0,0))
    screen.blit(guppi, (guppi_x, guppi_y))
    pygame.display.flip()
    for i in pygame.event.get():
        print (i)
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            print(i.key)
            if i.key==K_UP:
                guppi_y-=10
            elif i.key==K_DOWN:
                guppi_y+=10
            elif i.key==K_LEFT:
                guppi_x-=10
            elif i.key==K_RIGHT:
                guppi_x+=10
    guppi_y+=1
    time.sleep(0.05)