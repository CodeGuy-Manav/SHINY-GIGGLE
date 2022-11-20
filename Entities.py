import pygame

pygame.init()

Cursor = pygame.image.load("Images/Cursor.png").convert_alpha()
Cursor = pygame.transform.scale(Cursor,(75,75))
#Player = pygame.image.load("PlayerSprite.png")
#BG = pygame.image.load("BG.png")

SCREEN_W = 950
SCREEN_H = 600


def ColliderCheck():
	try:
		if screen.get_at((int(x),int(y))) == COLLIDECOLOUR:
			if mx < x:
				x = x+2
				cx = 0

		if screen.get_at((int(x+40),int(y))) == COLLIDECOLOUR:
			if mx > x:
				x = x-2
				cx = 0

		if screen.get_at((int(x),int(y))) == COLLIDECOLOUR:
			if my < y:
				y = y+2
				cy = 0

		if screen.get_at((int(x),int(y+50))) == COLLIDECOLOUR:
			if my > y:
				y = y-2
				cy = 0
	except:
		pass

