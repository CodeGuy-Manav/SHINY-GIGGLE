import pygame
import os

pygame.init()

def write(surf,tst):
	fnt = pygame.font.SysFont(None,50)
	txt = fnt.render(tst,True,(0,0,0))
	surf.blit(txt,(0,0))

def Debug(txt):
	print(txt)


def SaveScene(scene,id,DataDict,filename):
	path = f"SceneData/SavedGames/{id}"
	try:
		pygame.image.save(scene,path+f"/{filename}.png")
		with open(path+"/Data.py","w") as file:
			file.write(str(DataDict))
	except:
		os.mkdir(path)

def loadScene(id):
	try:
		with open(f"SceneData/SavedGames/{id}/Data.py","r") as file:
			return eval(file.read())
	except:
		print("Scene Not Found\n")
		print("Please Save scene and then try again...\n")