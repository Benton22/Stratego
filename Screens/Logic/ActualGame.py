import pygame
import sys
import random
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground, globalwider
from Screens.Logic.Buttons import PieceSpawner, ButtonBacker, BasicButton, TrashButton
from Pieces.Pieces import Piece, moveLogic

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255
piecePickedUp = False
pieceSelected = False
pieceChosen = 0
pieceChosenL = 0
pieceOut = [""]
player2Setup = False
player2 = [0]
tempxIndex = 0
tempyIndex = 0


#Grids-------------------------------------------------------------------------Grids
potentialMoves = [[0 for i in range(10)] for j in range(10)]
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
spawnerRed.append(PieceSpawner((10*2) * width/24 - width/22, height - 3 * height/48, 30, "Stratego\\Pieces\\Bomb.png", "B", True))
spawnerRed.append(PieceSpawner((11*2) * width/24 - width/22, height - 3 * height/48, 30, "S", "S", False))
spawnerRed.append(PieceSpawner((12*2) * width/24 - width/22, height - 3 * height/48, 30, "Stratego\\Pieces\\Flag.png", "F", True))

spawns = [1, 1, 2, 3, 4, 4, 4, 5, 8, 6, 1, 1]
spawnReset = [1, 1, 2, 3, 4, 4, 4, 5, 8, 6, 1, 1]

buttonBackers = []
for i in range(0, 13):
    buttonBackers.append("")

finishButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "Finish", 34)
endTurnButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "End Turn", 30)
resetButton = BasicButton(width + (globalwider - width)/10, 2 * height/12 + height/48, 8 * (globalwider - width)/10, height/12, "Clear", 34)
trashButton = TrashButton(width + (globalwider - width)/10, 11 * height/12 - height/48, 8 * (globalwider - width)/10, height/12, "Trash", 34, (80,80,80), (62, 62, 62))
randomButton = BasicButton(width + (globalwider - width)/10, 3 * height/12 + 2 * height/48, 8 * (globalwider - width)/10, height/12, "Random", 34)




def gameLogic(screen, mousePressed, gameState):
    global pieceChosen
    global pieceChosenL
    global pieceSelected
    gameStateLocal = gameState
    xIndex, yIndex = gridIndexer()
    keys = pygame.key.get_pressed()

    #Mouse Pressed Logic--------------------------------------------------------------Mouse Pressed Logic
   
    if mousePressed:
        if gameStateLocal == "Setup":
            global player2Setup
            global piecePickedUp
            if piecePickedUp == False:
                #If a piece is not selected
                if xIndex < 12 and yIndex < 12 and yIndex > 6 and grid [xIndex -1 ][yIndex -1] != 0 and grid[xIndex -1][yIndex -1] != "x":
                    #If clicked in a grid with a piece there
                    pieceChosenL = grid[xIndex-1][yIndex-1]
                    grid[xIndex-1][yIndex-1] = 0
                    if pieceChosenL != "B" and pieceChosenL != "F" and pieceChosenL != "S":
                        pieceChosenL -= 1
                    if keys[pygame.K_LSHIFT] != True:
                        piecePickedUp = True
                    else:
                        chosenUpdate()
                        spawns[pieceChosen] += 1
                else:
                    #Creation of piece with spawner buttons
                    for button in range(len(buttonBackers)-1):
                        if spawnerRed[button].over_button() and spawns[button] > 0:
                            spawns[button] -= 1
                            buttonBackers[button].number = spawns[button]
                            piecePickedUp = True
                            pieceChosenL = button
            #If a piece is already selected
            else:
                if trashButton.over_button():
                    piecePickedUp = False
                    spawns[pieceChosen] += 1
                elif xIndex < 12 and yIndex < 12 and yIndex > 6 and grid [xIndex -1 ][yIndex -1] == 0:
                    grid[xIndex -1][yIndex -1] = pieceOut[0].type
                    if keys[pygame.K_LCTRL] == True and spawns[pieceChosenL] > 0:
                        spawns[pieceChosenL] -= 1
                    else:
                        piecePickedUp = False
            #Finish Button
            if finishButton.over_button():
                if all(value == 0 for value in spawns):
                    if player2Setup == True:
                        gameStateLocal = "Playing"
                    else:
                        player2Setup = True
                        for i in range(len(spawns)):
                            spawns[i] = spawnReset[i]
                    changePlayer()
            #Reset Button
            elif resetButton.over_button():
                piecePickedUp = False
                for i in range(10):
                    for j in range(6,10):
                        grid[i][j] = 0
                for i in range(len(spawns)):
                    spawns[i] = spawnReset[i]
            elif randomButton.over_button() and piecePickedUp == False:
                randomPlacements()
        #If gameState != Setup
        else:
            global tempyIndex
            global tempxIndex
            if pieceSelected == False:
                pieceChosenL = grid[xIndex-1][yIndex-1]
                tempxIndex = xIndex -1
                tempyIndex = yIndex -1
                chosenUpdate()
                if xIndex < 12 and yIndex < 12 and pieceChosen >0 and grid[xIndex -1][yIndex -1] != "x" and grid[xIndex -1][yIndex -1] != "B" and grid[xIndex -1][yIndex -1] != "F":
                        pieceSelected = True
                        moveLogic(pieceChosen, xIndex -1, yIndex -1, potentialMoves, grid)
                return tempxIndex, tempyIndex
            else:
                if potentialMoves[xIndex-1][yIndex - 1] == 1:
                    pieceSelected = False
                    grid[tempxIndex][tempyIndex] = 0
                    grid[xIndex -1][yIndex - 1] = pieceChosenL
                    for i in range (0,10):
                        for j in range (0,10):
                            potentialMoves[i][j] = 0
            
    chosenUpdate()
    
    #UI -----------------------------------------------------------------------------------------------UI

    for i in range(len(grid)):
        for f in range(len(grid)):
            if grid[i][f] != 0 and grid[i][f] != "x":
                Piece(gridPos[i][0], gridPos[f][1], 60, grid[i][f], False).draw(screen)
    
    for i in range(len(buttonBackers)):
        buttonBackers[i] = (ButtonBacker((i*2) * width/24 - width/22 - 3, height - 3* height/48 - 3, 36, 60, str(spawns[i-1])))

    for numBackers in range(len(buttonBackers)):
        buttonBackers[numBackers].draw(screen)

    for numSpawner in range(len(spawnerRed)):
        spawnerRed[numSpawner].draw(screen)

    if gameStateLocal == "Setup":
        finishButton.draw(screen)
        resetButton.draw(screen)
        trashButton.draw(screen)
        randomButton.draw(screen)
    else:
        endTurnButton.draw(screen)

    #Movement Logic and Drawing
    #if pieceSelected == True:
        

    #Piece Drawing
    if piecePickedUp:
        pieceOut[0] = Piece(spawnerRed[pieceChosen].locationX, spawnerRed[pieceChosen].locationY, 60, spawnerRed[pieceChosen].type, True)
        pieceOut[0].draw(screen)
    
        
    return gameStateLocal

def changePlayer():
    tempGrid = [[0 for i in range(10)] for j in range(10)]
    for i in range(0, 10):
        for j in range(0,10):
            flipped_i = 9 - i
            flipped_j = 9 - j
            tempGrid[flipped_i][flipped_j] = grid[i][j]
            if tempGrid[flipped_i][flipped_j] == "B":
                tempGrid[flipped_i][flipped_j] = 10
            elif tempGrid[flipped_i][flipped_j] == "S":
                tempGrid[flipped_i][flipped_j] = 11
            elif tempGrid[flipped_i][flipped_j] == "F":
                tempGrid[flipped_i][flipped_j] = 12
    for i in range(0,10):
        for j in range(0,10):
            if tempGrid[i][j] != "x":
                grid[i][j] = -1 * tempGrid[i][j]
                if grid[i][j] == 10:
                    grid[i][j] = "B"
                elif grid[i][j] == 11:
                    grid[i][j] = "S"
                elif grid[i][j] == 12:
                    grid[i][j] = "F"
    if player2[0] == 0:
        player2[0] = 1
    else:
        player2[0] = 0

def chosenUpdate():
    global pieceChosen
    global pieceChosenL
    if pieceChosenL == "B":
        pieceChosen = 9
    elif pieceChosenL == "S":
        pieceChosen = 10
    elif pieceChosenL == "F":
        pieceChosen = 11
    else:
        pieceChosen = pieceChosenL

def chosenLUpdate():
    global pieceChosen
    global pieceChosenL
    if pieceChosen == 10:
        pieceChosenL = "B"
    elif pieceChosen == 11:
        pieceChosenL = "S"
    elif pieceChosen == 12:
        pieceChosenL = "F"
    else:
        pieceChosenL = pieceChosen

def randomPlacements():
    global pieceChosen
    global pieceChosenL
    for i in range (0,10):
        for j in range (6,10):
            if grid[i][j] == 0:
                sVals = []
                sVals.append(random.randint(0, 11))
                while spawns[sVals[0]] == 0:
                    sVals[0] = random.randint(0, 11)
                pieceChosen = sVals [0] + 1
                chosenLUpdate()
                grid[i][j] = pieceChosenL
                spawns[sVals[0]] -=1
    return grid

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
