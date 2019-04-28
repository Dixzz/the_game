import pygame
import random

import time

clock = pygame.time.Clock()
pygame.init()
scrw=800
scrh=800
win = pygame.display.set_mode((scrw,scrh))
pygame.display.set_caption("first game")
coll = False
collision = 0
x1 = 50
y1 = 0
width = 40
x2 =random.randint(0, scrw - width)
y2 = 0
vel_obj = 10
count=0
temp=0


shoot=False
height = 60
vel = 20
x = 400
y = scrh-height
temp1=vel

run = True

#bullet
xb=int(x+width/2)
yb=y
vb=15
hits=0

bg = pygame.image.load('bg1.jpg')





while run:

    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #print("count=",count)

    #print("velocity=",vel_obj)

    win.blit(bg, [scrh, scrw])
    if y1 <= scrh and x1 <= scrw:

        y1 += vel_obj
        x1 += vel_obj / 2


    else:
        y1 = y1 - vel_obj

        # x1 = random.randint(0, 800 - width)
        # count
    if y1 >= scrh-2 or y2 >= scrh-2:
        count += 1
    if count >= 20:
        vel_obj += 1
        count = 0

    if y2 <= scrh:
        y2 += vel_obj

    else:
        y2 = 0
        x2 = random.randint(0, scrw - width)

    if y1 <= scrh and x1 <= scrw:
        y1 += vel_obj
        x1 += vel_obj / 2
    else:
        y1 = random.randint(0,400)
        x1 = 0#random.randint(0, 800 - width)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x >=width/2:  # left right move
        x -= vel
        xb = int(x + width / 2)


    if keys[pygame.K_d] and x < scrw - width - 10:
        x += vel
        xb = int(x + width / 2)


    if keys[pygame.K_SPACE] and yb==y:
        temp=xb
        shoot =True

    if keys[pygame.K_LSHIFT]:

        vel=int(vel/2)
    else: vel=temp1


    if shoot:
        #yb=int(800-height)
        yb=yb-vb
        xb=temp
        if yb<=0:
            yb=y
            xb=int(x+width/2)
            shoot=False









    #collision


    if x1 >= x and x1 <= x + width and y1 >= y and y1 <= y + height:
        collision+=1
        y1=0
        print("collsion=",collision)


    if  x2 >= x-width and x2 <= x + width and y2 >= y and y2 <= y + height:
        collision+=1
        y2=0
        print("collsion=",collision)

    #bullet colli
    if yb>y1 and yb<y1+height and xb>=x1 and xb<=x1+width and yb<y:
        hits=hits+1
        yb=0
        y1=random.randint(0,400)
        x1=0#random.randint(0,800-width)
        print("hits=",hits)
        vel_obj+=2
    if yb > y2 and yb < y2 + height and xb >= x2 and xb <= x2 + width and yb<y:
        hits=hits+1
        yb=0
        y2=0
        x2=random.randint(0,scrw-width)
        print("hits=", hits)













    if collision == 7:
        print("End")

        run = False
        #collision = 0







    win.fill((255, 255, 255))
    win.blit(bg, [0, 0])
    pygame.draw.rect(win, (0, 255, 255), (x, y, width, height))  # player
    pygame.draw.rect(win, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), (x1, y1, width, height))  # slant
    #pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))  # slant

    pygame.draw.rect(win, (255, 255, 0), (x2, y2, width, height))  # str yello

    pygame.draw.circle(win,(255,255,255),(xb,yb),10)   #bullet

    pygame.display.update()




pygame.quit()
