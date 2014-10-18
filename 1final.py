# -*- coding:utf-8 -*-
import pygame,sys,pygame.mixer
import math
import random
from pygame.locals import*
import os

pygame.init()

sound = pygame.mixer.Sound("C:/Python27/All_for_game/Ment.wav")
fale=pygame.mixer.Sound("C:/Python27/All_for_game/fale.wav")
clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()
screen=pygame.display.set_mode((1100,668))
pygame.display.set_caption("Sun System")

window=pygame.Surface((400,30))
##pygame.display.set_caption("Game Over")

info_string=pygame.Surface((400,30))



bg = pygame.image.load("C:/Python27/All_for_game/61.jpg").convert_alpha()
image=pygame.image.load("C:/Python27/All_for_game/4.png").convert_alpha()#?aeaoa
aster=pygame.image.load("C:/Python27/All_for_game/2.png").convert_alpha()#Anoa?iea aieuoie
salut=pygame.image.load("C:/Python27/All_for_game/GO1.png").convert_alpha()
aster1=pygame.transform.scale(aster,(70,70))
aster2=pygame.transform.scale(aster1,(35,35))

def Intersect(x,asteroids_x,y,asteroids_y):
        if (asteroids_x>x-35) and (asteroids_x<x+35) and (asteroids_y>y-35) and (asteroids_y<y+35):
            return 1
        else:
            return 0
            
asteroids_x = list()
asteroids_y = list()
for i in range(20):
        ast=()
        ast=(random.randint(500,1000))
        asteroids_x.append(ast)

for i in range(20):
        asty=()
        asty=(random.randint(0,660))
        asteroids_y.append(asty)
        



x=0
y=0

    





run=True
speed=1
while run:
    sound.play()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    clock.tick(0.5)

    for i in range(len(asteroids_x)):
        screen.blit(aster,(asteroids_x[i],asteroids_y[i]))
    for i in range(len(asteroids_x)):
        asteroids_x[i]=asteroids_x[i]-10
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                sys.exit()
        elif e.type == pygame.KEYDOWN and e.key==K_DOWN: 
            for i in range(len(asteroids_x)):
                asteroids_y[i] =asteroids_y[i]- 70
        elif e.type == pygame.KEYUP and e.key==K_UP:     
            for i in range(len(asteroids_x)):        
                asteroids_y[i] += 70                 
    #tut dobav cikl for
##    if Intersect(x,asteroids_x,y,asteroids_y)==True:
##        sound.stop()
##        image=salut
##        sound=fale
##        screen.blit(image,(x-50,y))
##        sound.play()
    pygame.display.flip()
    
       


    run=False
