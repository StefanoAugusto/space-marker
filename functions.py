import pygame, os
from tkinter import simpledialog, messagebox
pygame.init()
displaySize = (1000, 563)
display = pygame.display.set_mode(displaySize)
fontSize = 25
font = pygame.font.Font(None, fontSize)
circleRadius = 5
white = (255, 255, 255)
gray = (200, 200, 200)
star = {}
lines = []

# Functions
def openBox():
    try:
        position = pygame.mouse.get_pos()
        item = simpledialog.askstring("Space", "Nome da Estrela:")
        if item is None:
            return
        if item == '':
            item = "Desconhecido " + str(position)
        star[item] = position
        print(star)
        if len(star) >= 2:
            keys = list(star.keys())
            lines.append((star[keys[-2]], star[keys[-1]]))
        print(lines) 
    except:
        pass

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
        sumX = line[0][0] + line[1][0]
        sumY = line[0][1] + line[1][1]
        sumText = f"({sumX}, {sumY})"
        sumSurface = font.render(sumText, True, gray)
        textX = (line[0][0] + line[1][0]) // 2
        textY = (line[0][1] + line[1][1]) // 2
        textRect = sumSurface.get_rect(center=(textX, textY))
        display.blit(sumSurface, textRect)

def saveFile():
    try:
        dataFolder = "data"
        if not os.path.exists(dataFolder):
            os.makedirs(dataFolder)
        filePath = os.path.join(dataFolder, "data.txt")
        with open(filePath, "w") as file:
            for item, position in star.items():
                file.write(f"{item}: {position[0]}, {position[1]}\n")
            for line in lines:
                file.write(f"{line[0][0]}, {line[0][1]} - {line[1][0]}, {line[1][1]}\n")
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:        
              messagebox.showinfo("Space", "Pontos salvos com sucesso!")
    except Exception as error:
        messagebox.showerror("Space", f"Erro ao salvar pontos: {str(error)}")

def loadFile():
    try:
        dataFolder = "data"
        filePath = os.path.join(dataFolder, "data.txt")
        if os.path.exists(filePath):
            with open(filePath, "r") as file:
                star.clear()
                lines.clear()
                for line in file:
                    line = line.strip()
                    if line:
                        if ":" in line:
                            item, position = line.split(":")
                            item = item.strip()
                            position = position.strip().split(",")
                            x = int(position[0].strip())
                            y = int(position[1].strip())
                            star[item] = (x, y)
                        if "-" in line:
                            coords = line.split("-")
                            start = coords[0].strip().split(",")
                            end = coords[1].strip().split(",")
                            x1 = int(start[0].strip())
                            y1 = int(start[1].strip())
                            x2 = int(end[0].strip())
                            y2 = int(end[1].strip())
                            lines.append(((x1, y1), (x2, y2)))
            messagebox.showinfo("Space", "Pontos carregados com sucesso!")
    except Exception as error:
        messagebox.showerror("Space", f"Erro ao carregar pontos: {str(error)}")

def deleteFile():
    try:
        confirmation = messagebox.askquestion("Space", "Tem certeza de que deseja deletar os pontos?")
        if confirmation == "yes":
            dataFolder = "data"
            filePath = os.path.join(dataFolder, "data.txt")
            if os.path.exists(filePath):
                star.clear()
                lines.clear() 
                os.remove(filePath)
                messagebox.showinfo("Space", "Arquivo e pontos deletados com sucesso!")            
            elif star:   
                star.clear()
                lines.clear() 
                messagebox.showinfo("Space", "Pontos deletados com sucesso!")                                       
            else:
                messagebox.showinfo("Space", "Não foram encontrados arquivos ou pontos para serem apagados")
            if os.path.exists(dataFolder):
                os.rmdir(dataFolder)
    except Exception as error:
        messagebox.showerror("Space", f"Erro ao deletar arquivo e pontos: {str(error)}")
