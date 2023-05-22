import pygame
import assets
from tkinter import simpledialog

pygame.init()

# Project Configuration
# Display
displaySize = (1000, 563)
width = 1000
height = 563
display = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Space Marker")

# Assets in general
icon = pygame.image.load("assets/space.png")
pygame.display.set_icon(icon)
background = pygame.image.load('assets/bg.jpg')
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)

fontSize = 25
font = pygame.font.Font(None, fontSize)
circleRadius = 5

# Colors
white = (255, 255, 255)
running = True
star = {}
lines = []

# Functions
def openBox():
    position = pygame.mouse.get_pos()
    item = simpledialog.askstring("Space", "Nome da Estrela:")
    if item == '':
        item = "Desconhecido " + str(position)
    star[item] = position
    print(star)
    if len(star) >= 2:
        keys = list(star.keys())
        lines.append((star[keys[-2]], star[keys[-1]]))
    print(lines) 

def drawCircles():
    for item, position in star.items():
        pygame.draw.circle(display, white, position, circleRadius)
        if item != "Desconhecido":
            textStar = item
        else:
            textStar = f"{item} {position}"
        textSurface = font.render(textStar, True, white)
        textRect = textSurface.get_rect(center=(position[0], position[1] - 15))
        display.blit(textSurface, textRect)

def printFunctions():
    saveText = "Pressione F10 para Salvar os Pontos"
    loadText = "Pressione F11 para Carregar os Pontos"
    deleteText = "Pressione F12 para Deletar os Pontos"
    saveSurface = font.render(saveText, True, white)
    loadSurface = font.render(loadText, True, white)
    deleteSurface = font.render(deleteText, True, white)
    display.blit(saveSurface, (10, 10))
    display.blit(loadSurface, (10, 35))
    display.blit(deleteSurface, (10, 60))

def drawLines():
    for line in lines:
        pygame.draw.line(display, white, line[0], line[1], 2) 

# Running the project
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            openBox()
    
    display.fill(white)
    display.blit(background, (0, 0))
    printFunctions()
    drawCircles()
    drawLines()
	

    pygame.display.update()

	
pygame.quit()
