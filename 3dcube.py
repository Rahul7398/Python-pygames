import pygame
from math import cos,sin
import math
import random
import time
import matmul
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Tree")
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((0,0,0))
kg=True
clock=pygame.time.Clock()
a = 0
p = [
[-100,100,-100],[100,100,-100],[100,-100,-100],[-100,-100,-100],
[-100,100,100],[100,100,100],[100,-100,100],[-100,-100,100],

]

def rotatex(a):
	a = math.radians(a)
	mat = [
	[1,0,0],
	[0,cos(a),-sin(a)],
	[0,sin(a),cos(a)]
	]
	return mat
def rotatey(a):
	a = math.radians(a)
	mat = [
	[cos(a),0,sin(a)],
	[0,1,0],
	[-sin(a),0,cos(a)]
	]
	return mat
def rotatez(a):
	a = math.radians(a)
	mat = [
	[cos(a),-sin(a),0],
	[sin(a),cos(a),0],
	[0,0,1]
	]
	return mat
def translate(m):
	if len(m)==3:
		return int(m[0]+250),int(m[1]+250),int(m[2])
	return int(m[0]+250),int(m[1]+250)
def ortho():
	mat =[
	[1,0,0],
	[0,1,0]
	]
	return mat
def convert(m):
	mat = list(m)
	m.append(1)
	return m

def perpect(d,z):
	s = 1/(d-z)
	return s


def draw(x,y,z):
	global a,p
	background.fill((0,0,0))
	pnew = matmul.tranpose(p)
	j = matmul.multiply(rotatez(az),pnew)
	j = matmul.multiply(rotatey(ax),j)
	j = matmul.multiply(rotatex(ay),j)
	j = matmul.multiply(ortho(),j)
	j2 = matmul.tranpose(j)
	for i in range(len(j2)):
		j2[i] = translate(j2[i])
	for i in j2:
		pygame.draw.circle(background,(255,255,255),i,4,0)
	for i in range(len(j2)//2):
		pygame.draw.aaline(background,(255,255,255),j2[i],j2[i+4],1)
		pygame.draw.aaline(background,(255,255,255),j2[i],j2[(i+1)%4],1)
		pygame.draw.aaline(background,(255,255,255),j2[i+4],j2[(i+1)%4+4],1)



ax,ay,az,s=0,0,0,1
while kg:
	clock.tick(30)
	for even in pygame.event.get():
		if even.type==pygame.QUIT:
			kg=False

	x = pygame.key.get_pressed()
	if x[pygame.K_x]:
		ax += s*1
	elif x[pygame.K_y]:
		ay += s*1
	elif x[pygame.K_z]:
		az += s*1
	elif x[pygame.K_UP]:
		s = 1
	elif x[pygame.K_DOWN]:
		s = -1
	#pygame.draw.line(background,x[0],x[1],x[2],2)
	draw(ax,ay,az)
	#input()
	screen.blit(background,(0,0))
	pygame.display.flip()
pygame.quit()