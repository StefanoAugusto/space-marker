import pygame, assets
from functions import openBox, drawCircles, printFunctions, drawLines, saveFile, loadFile, deleteFile, printTitle

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
pygame.mixer.music.load("assets/soundtrack.mp3")
title = pygame.image.load('assets/title.png')
titleRect = title.get_rect(center=(display.get_width() // 2, 150))
pygame.mixer.music.play(-1)
language = None
backgroundLoaded = False
running = True

# Running the project
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveFile(language)
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            saveFile(language)
            running = False 
        elif backgroundLoaded:
            if event.type == pygame.MOUSEBUTTONUP:
                openBox(language)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
                saveFile(language)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                loadFile(language)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
                deleteFile(language)

    display.fill(black)
    display.blit(title, titleRect)
    printTitle()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
        language = "pt_BR"
        backgroundLoaded = True
    elif keys[pygame.K_F2]:
        language = "en_US"
        backgroundLoaded = True
   
    if backgroundLoaded:
        display.blit(background, (0, 0))
        printFunctions(language)
        drawCircles()
        drawLines()

    pygame.display.update()

	
pygame.quit()
