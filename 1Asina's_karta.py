import pygame,sys,pygame.mixer
import math
import random

from pygame.locals import*

pygame.init()

screen = pygame
screen=pygame.display.set_mode((1200,700))
pygame.display.set_caption("CosmoStars")
sound = pygame.mixer.Sound("C:/Python27/All_for_game/Ment.wav")
clock = pygame.time.Clock()

bg = pygame.image.load("C:/Python27/All_for_game/cosmo2.jpg").convert_alpha()
image=pygame.image.load("C:/Python27/All_for_game/4.png").convert_alpha()
q=pygame.image.load("C:/Python27/All_for_game/q3.png").convert_alpha()
earth=pygame.image.load("C:/Python27/All_for_game/earth3.png").convert_alpha()
earth1=pygame.transform.scale(earth,(150,150))
sun=pygame.image.load("C:/Python27/All_for_game/sun1.png").convert_alpha()
merc=pygame.image.load("C:/Python27/All_for_game/merc1.png").convert_alpha()
jupiter=pygame.image.load("C:/Python27/All_for_game/jup.png").convert_alpha()
##jupiter.push = False
image2=pygame.transform.scale(image,(70,70))
image=pygame.transform.scale(image,(70,70))
hole=pygame.image.load("C:/Python27/All_for_game/cosmo2.jpg").convert_alpha()
clk=pygame.mixer.Sound("C:/Python27/All_for_game/UFO.wav")

jup=pygame.transform.scale(jupiter,(800,800))



mx,my=pygame.mouse.get_pos()
vx,vy=pygame.mouse.get_pos()

win=pygame.display.set_mode((1200,700))

def window(win):
    bg = pygame.image.load("C:/Python27/All_for_game/cosmo2.jpg").convert_alpha()
    win=pygame.display.set.mode((1200,700))
    sound = pygame.mixer.Sound("C:/Python27/All_for_game/Ment.wav")
    pygame.display.set_caption("VENUS")
    venus=pygame.image.load("C:/Python27/All_for_game/hole.png").convert_alpha()
    return

    
##game=pygame.display.set_icon("C:/Python27/All_for_game/image_rocket.py")

run=True
while run:
    
            
    
    sound.play()            
    screen.blit(bg,(0,0))
    screen.blit(earth1,(500,375))
    screen.blit(sun,(-400,50))
    screen.blit(q,(350,150))
    screen.blit(q,(590,70))
    screen.blit(q,(700,300))
    screen.blit(q,(400,300))
    screen.blit(q,(200,390))
    screen.blit(q,(400,500))
    screen.blit(q,(200,650))
    screen.blit(q,(550,720))
    screen.blit(q,(700,500))
    screen.blit(q,(900,150))
    screen.blit(q,(1000,375))
    screen.blit(q,(1100,600))
    screen.blit(q,(200,100))
    screen.blit(image,(mx-35,my-35))
     
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type ==KEYDOWN and e.key==K_ESCAPE:
            sys.exit()
##        if e.type == pygame.MOUSEBUTTONDOWN:
##            print "test"
        elif e.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
##        elif e.type==pygame.MOUSEBUTTONDOWN:
##            if jupiter.push == False:
##                jupiter.x=earth1.x
                
##        elif e.type==pygame.mouse.get_pos()
##            jupiter=pygame.image.load("C:/Python27/All_for_game/jup1.png").convert_alpha()
##            screen.blit(jupiter,(500,375))
            
##            open 
        
    
    pygame.display.flip()

    
