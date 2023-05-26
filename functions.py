import pygame, os
from tkinter import simpledialog, messagebox
from languages import messages

pygame.init()
displaySize = (1000, 563)
display = pygame.display.set_mode(displaySize)
font = pygame.font.Font(None, 25)
smallFont = pygame.font.Font(None, 20)
circleRadius = 5
white = (255, 255, 255)
gray = (200, 200, 200)
star = {}
lines = []

# Functions
def openBox(language):
    try:
        position = pygame.mouse.get_pos()
        message = messages.get(language, messages["pt_BR"])["openStar"]
        item = simpledialog.askstring("Space", message)
        if item is None:
            return
        if item == '' and language == "pt_BR":
            item = "Desconhecido " + str(position)
        elif item == '' and language == "en_US":
            item = "Unknown " + str(position)
        if item in star:
            messagebox.showerror("Space", messages.get(language, messages["pt_BR"])["starExistsError"])
            return
        star[item] = position
        #print(star)
        if len(star) >= 2:
            keys = list(star.keys())
            lines.append((star[keys[-2]], star[keys[-1]]))
        #print(lines) 
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

def printFunctions(language):
    saveText = messages.get(language, messages["pt_BR"])["savePoints"]
    loadText = messages.get(language, messages["pt_BR"])["loadPoints"]
    deleteText = messages.get(language, messages["pt_BR"])["deletePoints"]
    developedBy = messages.get(language, messages["pt_BR"])["developedBy"]
    courseInfo = messages.get(language, messages["pt_BR"])["courseInfo"]
    developedBySurface = smallFont.render(developedBy, True, white)
    courseInfoSurface = smallFont.render(courseInfo, True, white)

    display.blit(developedBySurface, (10, 520))
    display.blit(courseInfoSurface, (10, 540))

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

def saveFile(language):
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
              messagebox.showinfo("Space", messages.get(language, messages["pt_BR"])["saveSuccess"])
    except Exception as error:
        messagebox.showerror("Space", messages.get(language, messages["pt_BR"])["errorSave"].format(error=error))

def loadFile(language):
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
            messagebox.showinfo("Space", messages.get(language, messages["pt_BR"])["loadSuccess"])
        else:
            raise error
    except Exception as error:
        messagebox.showerror("Space", str(messages.get(language, messages["pt_BR"])["errorLoad"]))


def deleteFile(language):
    try:
        confirmation = messagebox.askquestion("Space", messages.get(language, messages["pt_BR"])["deleteConfirm"])
        if confirmation == "yes":
            dataFolder = "data"
            filePath = os.path.join(dataFolder, "data.txt")
            if os.path.exists(filePath):
                star.clear()
                lines.clear() 
                os.remove(filePath)
                messagebox.showinfo("Space", messages.get(language, messages["pt_BR"])["deleteSuccess"])            
            elif star:   
                star.clear()
                lines.clear() 
                messagebox.showinfo("Space", messages.get(language, messages["pt_BR"])["deleteSuccess"])                                       
            else:
                messagebox.showinfo("Space", messages.get(language, messages["pt_BR"])["deleteNoFile"])
            if os.path.exists(dataFolder):
                os.rmdir(dataFolder)
    except Exception as error:
       messagebox.showerror("Space", messages.get(language, messages["pt_BR"])["errorDelete"])

def printTitle():
    portuguesePress = "Pressione F1 para usar o aplicativo em Português"
    englishPress = "Press F2 to use the application in English"
    developedByPortuguese = "Desenvolvido por Stefano Augusto Mossi"
    courseInfoPortuguese = "Ciências da Computação - Atitus - 2023/1"
    developedByEnglish = "Developed by Stefano Augusto Mossi"
    courseInfoEnglish =  "Computer Science - Atitus - 2023/1"

    portuguesePressSurface = font.render(portuguesePress, True, white)
    englishPressSurface = font.render(englishPress, True, white)
    developedByPortugueseSurface = smallFont.render(developedByPortuguese, True, white)
    developedByEnglishSurface = smallFont.render(developedByEnglish, True, white)
    courseInfoPortugueseSurface = smallFont.render(courseInfoPortuguese, True, white)
    courseInfoEnglishSurface = smallFont.render(courseInfoEnglish, True, white)

    portuguesePressRect = portuguesePressSurface.get_rect(center=(display.get_width() // 2, 335))
    englishPressRect = englishPressSurface.get_rect(center=(display.get_width() // 2, 360))

    display.blit(portuguesePressSurface, portuguesePressRect)
    display.blit(englishPressSurface, englishPressRect)
    display.blit(developedByPortugueseSurface, (10, 480))
    display.blit(courseInfoPortugueseSurface, (10, 500))
    display.blit(developedByEnglishSurface, (10, 520))
    display.blit(courseInfoEnglishSurface, (10, 540))
