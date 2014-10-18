# -*- coding:utf-8 -*-
import pygame,sys,pygame.mixer
import math
import random
from pygame.locals import*

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



bg = pygame.image.load("C:/Python27/All_for_game/6.jpg").convert_alpha()
image=pygame.image.load("C:/Python27/All_for_game/4.png").convert_alpha()#Ðàêåòà
aster=pygame.image.load("C:/Python27/All_for_game/2.png").convert_alpha()#Àñòåðîèä áîëüøîé
salut=pygame.image.load("C:/Python27/All_for_game/GO1.png").convert_alpha()
aster1=pygame.transform.scale(aster,(70,70))
aster2=pygame.transform.scale(aster1,(35,35))

asteroids_x = list()
asteroids_y = list()
for i in range(10):
        ast=()
        ast=(random.randint(0,1100))
        asteroids_x.append(ast)

for i in range(10):
        asty=()
        asty=(random.randint(0,668))
        asteroids_y.append(asty)
        



x=0
y=0


    run=True
def Intersect(x,asteroids_x,y,asteroids_y):
        if (asteroids_x>x-35) and (asteroids_x<x+35) and (asteroids_y>y-35) and (asteroids_y<y+35):
              return 1
        else:
              return 0






speed=1
while run:
    sound.play()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    for i in range(len(asteroids_x)):                         # len() - возвращает длину списка.
        screen.blit(aster,(asteroids_x[i],asteroids_y[i]))    # в квадратных скобках указываются номера координат.

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                sys.exit()
        elif e.type == pygame.KEYDOWN and e.key==K_DOWN:
                y=y+70
        elif e.type == pygame.KEYUP and e.key==K_UP:
                y=y-70
    if Intersect(x,asteroids_x,y,asteroids_y)==True:
        sound.stop()
        image=salut
        sound=fale
        screen.blit(image,(x-50,y))
        sound.play()
    pygame.display.flip()
        
        
    




    run=False


pygame.quit()






