import pygame
import random,time,math
from Settings import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

from Utilities import *
from Entities import *

clock = pygame.time.Clock()

score = 0

data = loadScene("Game-1")
score = data["PlayerScore"]
while True:
	screen.fill((255,255,255))
	clock.tick(FPS)
	write(screen,"SCORE : "+str(score))
	DataDict["PlayerScore"] = score
	# score = data["PlayerScore"]
	mx,my = pygame.mouse.get_pos()


	for particle in particles:
		particle[0][0] += particle[1][0]
		particle[0][1] += particle[1][1]
		particle[2] -= 0.15
		particle[1][1] += 0.01
		clr = (0,0,0)
		pygame.draw.circle(screen,clr,(int(particle[0][0]),int(particle[0][1])),(int(particle[2])))
		if particle[2] <= 0:
			particles.remove(particle)


	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == ord("s"):
				DataDict["ScreenBG"] = (255,255,255)
				DataDict["PlayerID"] = "Manav"
				SaveScene(screen,"Game-2",DataDict,"GAME.png")


		elif event.type == pygame.MOUSEMOTION:
			mx,my = pygame.mouse.get_pos()


		if event.type == pygame.MOUSEBUTTONDOWN:
			score += 1
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			particles.append([[mx,my],[random.randint(-3,3),random.randint(-3,3)],10])
			

	pygame.mouse.set_visible(False)
	screen.blit(pygame.transform.rotate(Cursor,angle-5),(mx-48,my-34))

	#Handle Rotation


	angle += 0.5
	if angle > 359:
		angle = 0



	# x=float(x)
	# y = float(y)
	# x+=cx
	# y += cy
	#DataDict["PlayerPos"][0] = x
	#DataDict["PlayerPos"][1] = y
	#DataDict["PlayerScore"] = score
	pygame.display.update()