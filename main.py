import pygame, assets

pygame.init()
#Configuration of the project:
#Display
displaySize = (1000, 563)
width = 1000
height = 563
display = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Space Marker")
#assets in general
icon = pygame.image.load("assets/space.png")
pygame.display.set_icon(icon)
background = pygame.image.load('assets/bg.jpg')
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
font = pygame.font.Font(None, 36)
#Colors:
white = (255, 255, 255)
running = True

#Running the project:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    display.fill(white)
    display.blit(background, (0, 0))

    pygame.display.update()
  
    
pygame.quit()