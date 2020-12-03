import pygame,math
import random
import time
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Tree")
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))
kg=True
clock=pygame.time.Clock()

def draw(x,y,l,a):
	y1 = y - l * math.sin(math.radians(a))
	x1 = x + l * math.cos(math.radians(a))
	if l>2:
		if l<10:
			col = (0,125,0)
			w = 2
		else:
			col = (210,105,30)
			w = 5
		
		pygame.draw.line(background,col,(x,y),(x1,y1),w)
		'''
		screen.blit(background,(0,0))
		pygame.display.flip()
		'''
		cho1 = [a+30,a+15,]
		cho2 = [a-30,a-15]
		cho = cho1+cho2
		for i in range(random.randint(2,4)):
			draw(x1,y1,l*random.randint(50,90)/100,a+random.randint(-30,30))

		'''
		draw(x1,y1,l*random.randint(50,90)/100,a+30)
		draw(x1,y1,l*random.randint(50,90)/100,a-30)
		'''


draw(250,500,100,90)
c = 0
while kg:
	clock.tick(100)
	for even in pygame.event.get():
		if even.type==pygame.QUIT:
			kg=False
	
	#pygame.draw.line(background,x[0],x[1],x[2],2)
	screen.blit(background,(0,0))
	pygame.display.flip()
pygame.quit()
