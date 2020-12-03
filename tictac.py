import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("TicTakToe")
background=pygame.Surface(screen.get_size())
background=background.convert()
red = (255,0,0)
yel = (0,0,255)
background.fill((125,125,125))
count =0
bord=[]
for i in range(3):
    bord.append([0,0,0])

for i in range(1,4):
    pygame.draw.line(background,(255,255,255),(200*i,0),(200*i,600),3)
for i in range(1,4):
    pygame.draw.line(background,(255,255,255),(0,200*i),(600,200*i),3)

def locate(pt,c):
    x = pt[0] //200
    y = pt[1] //200
    i,j = x,y
    x =x*200 +100
    y =y*200 +100
    if(c%2 ==0):
        drawx((x,y))
        bord[j][i] =2
        check((j,i),2)
    else:
        drawc((x,y))
        bord[j][i] =1
        check((j,i),1)
        

    
def drawx(pt):
    pygame.draw.line(background,red,(pt[0]-50,pt[1]-50),(pt[0]+50,pt[1]+50),10)
    pygame.draw.line(background,red,(pt[0]+50,pt[1]-50),(pt[0]-50,pt[1]+50),10)

def drawc(pt):
    pygame.draw.circle(background,yel,pt,50,10)
    
def check(pt,val):
    #print(bord)
    i,j = pt
    tempx =0
    tempy =0
    tempzr =0
    tempzl =0
    for t in range(3):
        if bord[i][t] == val:
            tempx +=1
        if bord[t][j] ==val:
            tempy +=1
        if bord[t][t] == val:
            tempzr +=1
        if bord[t][2-t] == val:
            tempzl +=1
    #print(tempx,tempy,tempzr,tempzl)
    if tempx ==3:
        pygame.draw.line(background,(255,255,255),(100,(i+1)*200 -100),(500,(i+1)*200-100),10)
    elif tempy ==3:
        pygame.draw.line(background,(255,255,255),((j+1)*200-100,100),((j+1)*200-100,500),10)
    elif tempzr ==3:
        pygame.draw.line(background,(255,255,255),(100,100),(500,500),10)
    elif tempzl ==3:
        pygame.draw.line(background,(255,255,255),(500,100),(100,500),10)                         
        
    
    

kg = True
while kg:

    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            kg=False
        elif even.type==pygame.MOUSEBUTTONDOWN:
            start=pygame.mouse.get_pos()
            locate(start,count)
            count +=1
            

    screen.blit(background,(0,0))
    pygame.display.flip()
pygame.quit()

