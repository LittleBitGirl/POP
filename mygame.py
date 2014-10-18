import pygame
import math
pygame.init()
screen=pygame.display.set_mode((500,200))
run=True
pos=(100,100)
clock=pygame.time.Clock()
speed=2
move_map={pygame.K_LEFT:(-1,0),pygame.K_RIGHT:(1,0),pygame.K_DOWN:(0,1),pygame.K_UP:(0,-1)}

while run:
    screen.fill(black)
    pygame.draw.circle(screen,(255,0,0),map(int,pos),10)
    pygame.display.flip()
    pressed=pygame.key.get_pressed()
    imgrec=imgrec.move(speed)
    movevector=(0,0)
    for i in(move_map[key]for key in move_map if pressed[key]):
        movevector=map(sum,zip(movevector,i))
    if sum(map(abs,movevector))==2:
        movevector=[p/1.4142 for p in movevector]
    movevector=[speed*p for p in movevector]
    pos=map(sum,zip(pos,movevector))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run=False
            
    clock.tick(60)

    
    
    
            
