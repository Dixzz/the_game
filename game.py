import pygame
import random
import time
clock=pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("first game")
seconds=0
coll=False
collision=0
x1=50
y1=0
width=40
x2=random.randint(0,800-width)
y2=0
vel_obj=5
count=0
x3=random.randint(0,800-width )
y3=0

#coordinates are on top left of origin as well as object

#coll
status=False

height=60
vel=20
run=True
isjump=False
jumpcount=10
x=400-width/2
y=800-height


import time
def timer():
   now = time.localtime(time.time())
   #print(now)
   return now[5]

while run:


    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False



    if y1<=800 and x1<=800:

        y1+=vel_obj
        x1+=vel_obj/2


    '''else:

        y1=y1-vel_obj'''

        #x1 = random.randint(0, 800 - width)
    if count>20:
        vel_obj+=2
        count=0
        #cout ko phrse)0? are humko baar baar increment karna hai na velocitybc
    if y1>800 or y2>800 or y3>800:
        count+=1


    '''if y3<=800 and x3<=800:
        y3+=vel_obj
        x3-=vel_obj/2
    else:
        y3=0
        x3 = random.randint(0, 800 - width)'''


    if y2 <= 800:
        y2 += vel_obj

    else:

        y2 = 0
        x2 = random.randint(0, 800 - width)

    if y1<=800 and x1<=800:
        y1+=vel_obj
        x1+=vel_obj/2
    else:
        y1=0
        x1 = random.randint(0, 800 - width)


    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and x>vel:    #left right move
        x-=vel
    if keys[pygame.K_d] and x<800-width-10:
        x+=vel
    if not(isjump):                         #restrict up down jump while in air

        if keys[pygame.K_w] and y>vel:             #pressed when on land
            y-=vel
        if keys[pygame.K_s] and y<800-height:
            y+=vel
        if keys[pygame.K_SPACE]:
            isjump=True
    else:                                       #in air
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y=y-(jumpcount**2)*0.5*neg
            jumpcount-=1
        else:
            isjump=False
            jumpcount=10
    if x1>=x and x1<=x+width and y1>=y and y1<=y+height or x2>=x and x2<=x+width and y2>=y and y2<=y+height: #or x3>=x and x3<=x+width and y3>=y and y3<=y+height :


        collision=collision+1
        print (collision)
        if collision>=7:
            print("End")

            run=False
            #collision=0

    win.fill((255,255,255))
    pygame.draw.rect(win,(0,0,0),(x,y,width,height))  #player


    pygame.draw.rect(win, (0, 0, 255), (int (x1), int (y1),height,width ))  #slant

    pygame.draw.rect(win, (255,0 ,128), (int (x2), int (y2),height,width))  #str

    #pygame.draw.rect(win,(255,0,0),(int(x3),int(y3),height,width))


#lmao, betterasf
    pygame.display.update()

    #pygame.draw.rect(win, (255, 0, 0), (x / 2, y / 2, width / 2, height / 2))


pygame.quit()
