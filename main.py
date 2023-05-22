import pygame, assets
from functions import openBox, drawCircles, printFunctions, drawLines, saveFile, loadFile, deleteFile

pygame.init()

# Project Configuration
# Display
displaySize = (1000, 563)
display = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Space Marker")
black = (0, 0, 0)

# Assets in general
icon = pygame.image.load("assets/space.png")
pygame.display.set_icon(icon)
background = pygame.image.load('assets/bg.jpg')
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
running = True

# Running the project
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveFile()
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            saveFile()
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            openBox()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            saveFile()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            loadFile()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            deleteFile()
    
    display.fill(black)
    display.blit(background, (0, 0))
    printFunctions()
    drawCircles()
    drawLines()
	

    pygame.display.update()

	
pygame.quit()
