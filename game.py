import pygame
import random
import time

clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("first game")
coll = False
collision = 0
x1 = 50
y1 = 0
width = 40
x2 =random.randint(0, 800 - width)
y2 = 0
vel_obj = 5
count=0
temp=0
# coordinates are on top left of origin as well as object


# coll

shoot=False
height = 60
vel = 20
x = 400
y = 800-height

run = True

#bullet
xb=int(x+width/2)
yb=y
vb=15
hits=0



# bnana bounce' nahi na ho raha'
# are 2 blck tch hua to ek block ake pstion ko dur krnah bs karke bata b


while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #print("count=",count)

    #print("velocity=",vel_obj)


    if y1 <= 800 and x1 <= 800:

        y1 += vel_obj
        x1 += vel_obj / 2


    else:
        y1 = y1 - vel_obj

        # x1 = random.randint(0, 800 - width)
        # count
    if y1 >= 799 or y2 >= 799:
        count += 1
    if count >= 20:
        vel_obj += 1
        count = 0

    if y2 <= 800:
        y2 += vel_obj

    else:
        y2 = 0
        x2 = random.randint(0, 800 - width)

    if y1 <= 800 and x1 <= 800:
        y1 += vel_obj
        x1 += vel_obj / 2
    else:
        y1 = random.randint(0,400)
        x1 = 0#random.randint(0, 800 - width)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vel:  # left right move
        x -= vel
        xb = int(x + width / 2)


    if keys[pygame.K_d] and x < 800 - width - 10:
        x += vel
        xb = int(x + width / 2)


    if keys[pygame.K_SPACE]:
        temp=xb
        shoot =True

    if shoot:
        #yb=int(800-height)
        yb=yb-vb
        xb=temp
        if yb<0:
            yb=y
            xb=int(x+width/2)
            shoot=False








    #collision


    if x1 >= x and x1 <= x + width and y1 >= y and y1 <= y + height:
        collision+=1
        print("collsion=",collision)

    elif  x2 >= x and x2 <= x + width and y2 >= y and y2 <= y + height:
        collision+=1
        y2=0
        print("collsion=",collision)

    #bullet colli
    if yb>y1 and yb<y1+height and xb>=x1 and xb<=x1+width:
        hits=hits+1
        y1=random.randint(0,400)
        x1=random.randint(0,800)
        print("hits=",hits)
    if yb > y2 and yb < y2 + height and xb >= x2 and xb <= x2 + width:
        hits=hits+1
        y2=0
        x2=random.randint(0,800)
        print("hits=", hits)










    if collision == 7:
        print("End")

        run = False
        #collision = 0







    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 255, 255), (x, y, width, height))  # player

    pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))  # slant

    pygame.draw.rect(win, (255, 255, 0), (x2, y2, width, height))  # str yello

    pygame.draw.circle(win,(0,0,0),(xb,yb),10)   #bullet

    pygame.display.update()

    # pygame.draw.rect(win, (255, 0, 0), (x / 2, y / 2, width / 2, height / 2))
# stop ni hua? i?are 20 collsionms k baad hua na an, bounce ni ha karte hai wakata


pygame.quit()
