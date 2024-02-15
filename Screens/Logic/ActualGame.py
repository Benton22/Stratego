import pygame
import sys
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground, globalwider
from Screens.Logic.Buttons import PieceSpawner, ButtonBacker, BasicButton
from Pieces.Pieces import Piece

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255

pieceSelected = False
pieceChosen = 0


#Grids-------------------------------------------------------------------------Grids
#making the grid
grid = [[0 for i in range(10)] for j in range(10)]

for i in range(2,4):
    for j in range(4,6):
        grid[i][j] = "x"
for i in range(6,8):
    for j in range(4,6):
        grid[i][j] = "x"

#Position values for Grid
        
gridPos = [(0, 0) for i in range(10)]
for i in range(len(grid)):
    gridPos[i] = (i * height/12) + 15, ((i * height/12) + height/12 + 12)


print(grid)
#ButtonCreation---------------------------------------------------------------------ButtonCreation

spawnerRed = []
for i in range(1,10):
    spawnerRed.append(PieceSpawner((i*2) * width/24 - width/22, height - 3 * height/48, 30, str(i), i, False))
spawnerRed.append(PieceSpawner((10*2) * width/24 - width/22, height - 3 * height/48, 30, "S", "S", False))
spawnerRed.append(PieceSpawner((11*2) * width/24 - width/22, height - 3 * height/48, 30, "Pieces\\Bomb.png", "B", True))
spawnerRed.append(PieceSpawner((12*2) * width/24 - width/22, height - 3 * height/48, 30, "Pieces\\Flag.png", "F", True))

spawns = [1, 1, 2, 3, 4, 4, 4, 5, 8, 1, 6, 1]
buttonBackers = []
for i in range(0, 13):
    buttonBackers.append("")

finishButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "Finish", 34)
endTurnButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "End Turn", 30)


pieceOut = [""]


def gameLogic(screen, mousePressed, gameState):
    global pieceSelected
    global pieceChosen
    gameStateLocal = gameState

    xIndex, yIndex = gridIndexer()

    #UI -----------------------------------------------------------------------------------------------UI

    for i in range(len(buttonBackers)):
        buttonBackers[i] = (ButtonBacker((i*2) * width/24 - width/22 - 3, height - 3* height/48 - 3, 36, 60, str(spawns[i-1])))

    for numBackers in range(len(buttonBackers)):
        buttonBackers[numBackers].draw(screen)

    for numSpawner in range(len(spawnerRed)):
        spawnerRed[numSpawner].draw(screen)

    if pieceSelected:
        pieceOut[0] = Piece(spawnerRed[pieceChosen].locationX, spawnerRed[pieceChosen].locationY, 60, spawnerRed[pieceChosen].type, True)
        pieceOut[0].draw(screen)


    for i in range(len(grid)):
        for f in range(len(grid)):
            if grid[i][f] != 0 and grid[i][f] != "x":
                Piece(gridPos[i][0], gridPos[f][1], 60, grid[i][f], False).draw(screen)

    if gameStateLocal == "Setup":
        finishButton.draw(screen)
    else:
        endTurnButton.draw(screen)
                
        

    #Mouse Pressed Logic--------------------------------------------------------------Mouse Pressed Logic
    if mousePressed:
        if gameStateLocal == "Setup":
            if pieceSelected == False:
                for button in range(len(buttonBackers)-1):
                    if spawnerRed[button].over_button() and spawns[button] > 0:
                        spawns[button] -= 1
                        buttonBackers[button].number = spawns[button]
                        pieceSelected = True
                        pieceChosen = button
            else:
                if xIndex < 12 and yIndex < 12 and yIndex > 6 and grid [xIndex -1 ][yIndex -1] == 0:
                    grid[xIndex -1][yIndex -1] = pieceOut[0].type
                    pieceSelected = False
        if finishButton.over_button():
            gameStateLocal = "Playing"
    
    return gameStateLocal




#Pulling mouse location in Grid-form
def gridIndexer():
    xIndex = 0
    yIndex = 0
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX < width/10:
        xIndex = 1
    elif mouseX < 2 * width/10 + 3:
        xIndex = 2
    elif mouseX < 3 * width/10 + 3:
        xIndex = 3
    elif mouseX < 4 * width/10 + 3:
        xIndex = 4
    elif mouseX < 5 * width/10 + 3:
        xIndex = 5
    elif mouseX < 6 * width/10 + 3:
        xIndex = 6
    elif mouseX < 7 * width/10 + 3:
        xIndex = 7
    elif mouseX < 8 * width/10 + 3:
        xIndex = 8
    elif mouseX < 9 * width/10 + 3:
        xIndex = 9
    elif mouseX < 10 * width/10 + 3:
        xIndex = 10
    else:
        xIndex = 20

    if mouseY > width/10:
        if mouseY < 2 * width/10 + 3:
            yIndex = 1
        elif mouseY < 3 * width/10 + 3:
            yIndex = 2
        elif mouseY < 4 * width/10 + 3:
            yIndex = 3
        elif mouseY < 5 * width/10 + 3:
            yIndex = 4
        elif mouseY < 6 * width/10 + 3:
            yIndex = 5
        elif mouseY < 7 * width/10 + 3:
            yIndex = 6
        elif mouseY < 8 * width/10 + 3:
            yIndex = 7
        elif mouseY < 9 * width/10 + 3:
            yIndex = 8
        elif mouseY < 10 * width/10 + 3:
            yIndex = 9
        elif mouseY < 11 * width/10 + 3:
            yIndex = 10
        else:
            yIndex = 20
    else: 
        yIndex = 20
    return(xIndex, yIndex)
