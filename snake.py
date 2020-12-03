import pygame
import random
#import snakepath
pygame.init()

screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption("Snake (space for pause)")
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((125,125,125))
FONT=pygame.font.SysFont("Chiller",25)
kg=True
clock=pygame.time.Clock()
count = 0
l =[]
for i in range(490,451,-10):
    l.append((0,i))
    pygame.draw.rect(background,(255,0,0),((1,i+1),(8,8)))
print(l)
def food():
    
    x = random.randint(0,800-10)
    x = x//10
    x = x*10
    y = random.randint(0,500-10)
    y = y//10
    y = y*10
    pygame.draw.circle(background,(0,255,0),(x+5,y+5),5)
    return (x,y)
def check():
    
    if l[-1] in l[:-1]:
        return 1
    elif l[-1][0]==800 or l[-1][1]==500 :
        return 1
    elif l[-1][0]<0 or l[-1][1]<0 :
        return 1
    else:
        return 0
        
    
def body(d,pd,pt):
 
    global count
    x,y = l[-1]
    if d == 'd' and pd !='a':
        x +=10
    elif d =='s' and pd !='w':
        y += 10
    elif d =='a' and pd!='d':
        x -=10
    elif d == 'w' and pd!='s':
        y-=10
    l.append((x,y))
    #l.insert(0,(x,y))
    pygame.draw.rect(background,(255,0,0),((x+1,y+1),(8,8)))
    if pt != (x,y):
        pygame.draw.rect(background,(125,125,125),(l[0],(10,10)))
        l.pop(0) 
        return 0
    else:
        count +=1
        return 1
    
def pause():
    flag = True
    c = 0
    while flag:
        for even in pygame.event.get():
            if even.type==pygame.QUIT:
                return False
            elif even.type == pygame.KEYDOWN:
                if even.key == pygame.K_SPACE:
                    flag = False                
        ptext=FONT.render("Game Paused",0,(255,0,0))
        screen.blit(ptext,(850,200))
        pygame.display.flip()
    return True

d = 'w'
pd = 'w'
flag = 1
#l[-1] = (790,0)
while kg:
    clock.tick(20)
    if flag:
        pt = food()
    

    
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            kg=False
        elif even.type == pygame.KEYDOWN:
            pd = d
            if even.key == pygame.K_d and pd !='a':
                d = 'd'
            elif even.key == pygame.K_s and pd!='w':
                d = 's'
            elif even.key == pygame.K_a and pd!='d':
                d = 'a'
            elif even.key == pygame.K_w and pd !='s':
                d = 'w'
            elif even.key == pygame.K_SPACE:
                kg =pause()
    """
    pd =d
    d = snakepath.path(l[-1],d)
    if l[-1] == (790,490):
       print(d)
    """ 
    flag = body(d,pd,pt)
    if check():
        kg = False
    pygame.draw.rect(background,(255,255,255),((800,0),(200,500)))
    stext=FONT.render("SCORE : ",0,(255,0,0))
    ctext=FONT.render(str(count),0,(255,0,0))
    screen.blit(background,(0,0))
    screen.blit(stext,(850,100))
    screen.blit(ctext,(850,130))
    pygame.display.flip()

pygame.quit()
