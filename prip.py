"""
Здравствуйте Алмас!
Код индийский,Извините за это) делала из того, что знаю.
Вот ссылки откуда я все это брала (делала только по туториалам):
https://www.youtube.com/watch?v=VReH9L84pTA
https://www.youtube.com/watch?v=mEX0R1NOk7Q
Надеюсь не запутаетесь)
"""

from graphics import*
import pygame,sys,pygame.mixer
import math
import random
from pygame.locals import*

pygame.init()

sound = pygame.mixer.Sound("C:/Python27/All_for_game/Ment.wav")
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1100,638))

pygame.display.set_caption("CosmoRocket")

bg = pygame.image.load("C:/Python27/All_for_game/6.jpg").convert_alpha()
image=pygame.image.load("C:/Python27/All_for_game/4.png").convert_alpha()#Rocket
aster=pygame.image.load("C:/Python27/All_for_game/2.png").convert_alpha()
aster1=pygame.image.load("C:/Python27/All_for_game/2.png").convert_alpha()
salut=pygame.image.load("C:/Python27/All_for_game/salut.gif").convert_alpha()
aster1=pygame.transform.scale(aster1,(70,70))
aster2=pygame.transform.scale(aster1,(35,35))


x=0
y=0




a=150
b=326
c=485
d=680
f=753
g=900
h=1100
i=1390
j=1510
k=1600
l=1770
m=1700
n=1950
o=2000
p=2160
r=2250
s=2370
t=2480
def asteroid():
        screen.blit(bg,(0,0))
        screen.blit(image,(x,y))
   
        screen.blit(aster1,(a,70))
        screen.blit(aster,(b,230))
        screen.blit(aster1,(c,370))
        screen.blit(aster,(d,300))
        screen.blit(aster1,(f,70))
        screen.blit(aster,(g,250))
        screen.blit(aster1,(h,160))
        screen.blit(aster,(i,445))
        screen.blit(aster1,(j,600))
        screen.blit(aster,(k,70))
        
        screen.blit(aster1,(l,210))
        screen.blit(aster,(m,350))
        screen.blit(aster1,(n,490))
        screen.blit(aster,(o,660))
        screen.blit(aster1,(p,70))
        screen.blit(aster,(r,210))
        screen.blit(aster1,(s,350))


run=True
pos=(5,10)
##clock=pygame.time.Clock()
speed=1
while run:
    asteroid()
    sound.play()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                sys.exit()
        elif e.type == pygame.KEYDOWN and e.key==K_DOWN:
                y=y+70
        elif e.type == pygame.KEYUP and e.key==K_UP:
                y=y-70
        if a == 70:
            image = salut
        asterrect = aster.get_rect()
 
##    screen.fill((r,0,0))

    clock.tick(380)
    
    pygame.display.flip()
##    y=y+0.2
    a=a-0.5
    b=b-0.5
    c=c-0.5
    d=d-0.5
    f=f-0.5
    g=g-0.5
    h=h-0.5
    i=i-0.5
    j=j-0.5
    k=k-0.5
    l=l-0.5
    m=m-0.5
    n=n-0.5
    o=o-0.5
    p=p-0.5
    r=r-0.5
    s=s-0.5



    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                sys.exit()
        elif e.type == pygame.KEYDOWN and e.key==K_DOWN:
                y=y+70
        elif e.type == pygame.KEYUP and e.key==K_UP:
                y=y-70
        
        
        
    if (a-70)<x and (a+70)>x and y>(q-70) and y<(q+70):
                sound.stop()
                image=salut
                sound=fale
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (b-70)<x and (b+70)>x and y>(ab-70) and y<(ab+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (c-70)<x and (c+70)>x and y>(ac-70) and y<(ac+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (d-70)<x and (d+70)>x and y>(ad-70) and y<(ad+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (f-70)<x and (f+70)>x and y>(af-70) and y<(af+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (g-70)<x and (g+70)>x and y>(ag-70) and y<(ag+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (h-70)<x and (h+70)>x and y>(ah-70) and y<(ah+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (i-70)<x and (i+70)>x and y>(ai-70) and y<(ai+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (j-70)<x and (j+70)>x and y>(aj-70) and y<(aj+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (k-70)<x and (k+70)>x and y>(ak-70) and y<(ak+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (l-70)<x and (l+70)>x and y>(al-70) and y<(al+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break 
    elif (m-70)<x and (m+70)>x and y>(am-70) and y<(am+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (n-70)<x and (n+70)>x and y>(an-70) and y<(an+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (o-70)<x and (o+70)>x and y>(ao-70) and y<(ao+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                break
    elif (p-70)<x and (p+70)>x and y>(ap-70) and y<(ap+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
               
    elif (r-70)<x and (r+70)>x and y>(ar-70) and y<(ar+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
               
    elif (s-70)<x and (s+70)>x and y>(bs-70) and y<(bs+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                
    elif (t-70)<x and (t+70)>x and y>(bt-70) and y<(bt+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
                


    run=False


##pygame.quit()
