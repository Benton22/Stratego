import pygame
import sys
import random
from Screens.Logic.Variables.Globals import globalheight, globalwidth, globalsize, globalbackground, globalwider
from Screens.Logic.Buttons import PieceSpawner, ButtonBacker, BasicButton, TrashButton
from Pieces.Pieces import Piece, moveLogic, drawPotential, combatPositions, combat

height = globalheight
width = globalwidth
size = globalsize
black = 0, 0, 0
background = globalbackground
white = 255, 255, 255
piecePickedUp = False
pieceSelected = False
pieceChosen = 0
pieceOut = [""]
player2Turn = False
tempxIndex = [0, 0]
tempyIndex = [0, 0]
fightingPieces = []
turnstate = [0, 0]
previous_combat = [0]


#Grids-------------------------------------------------------------------------Grids
potentialMoves = [[[0, 0] for i in range(10)] for j in range(10)]
#making the grid
grid = [[0 for i in range(10)] for j in range(10)]

for i in range(2,4):
    for j in range(4,6):
        grid[i][j] = 13
for i in range(6,8):
    for j in range(4,6):
        grid[i][j] = 13

#Position values for Grid
        
gridPos = [(0, 0) for i in range(10)]
for i in range(len(grid)):
    gridPos[i] = (i * height/12) + 15, ((i * height/12) + height/12 + 12)


#ButtonCreation---------------------------------------------------------------------ButtonCreation

spawnerRed = []
for i in range(1, 13):
    spawnerRed.append(PieceSpawner((i*2) * width/24 - width/22, height - 3 * height/48, 30, str(i), i, False))
spawnerRed.append(PieceSpawner((10*2) * width/24 - width/22, height - 3 * height/48, 30, "Stratego\\Pieces\\Bomb.png", 10, True))
spawnerRed.append(PieceSpawner((11*2) * width/24 - width/22, height - 3 * height/48, 30, "S", 11, False))
spawnerRed.append(PieceSpawner((12*2) * width/24 - width/22, height - 3 * height/48, 30, "Stratego\\Pieces\\Flag.png", 12, True))

spawns = [1, 1, 2, 3, 4, 4, 4, 5, 8, 6, 1, 1]
spawnReset = [1, 1, 2, 3, 4, 4, 4, 5, 8, 6, 1, 1]

buttonBackers = []
for i in range(0, 12):
    buttonBackers.append("")

finishButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "Finish", 34)
opponentTurnButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "Done", 30)
resetButton = BasicButton(width + (globalwider - width)/10, 2 * height/12 + height/48, 8 * (globalwider - width)/10, height/12, "Clear", 34)
trashButton = TrashButton(width + (globalwider - width)/10, 11 * height/12 - height/48, 8 * (globalwider - width)/10, height/12, "Trash", 34, (80,80,80), (62, 62, 62))
randomButton = BasicButton(width + (globalwider - width)/10, 3 * height/12 + 2 * height/48, 8 * (globalwider - width)/10, height/12, "Random", 34)
confirmButton = BasicButton(width + (globalwider - width)/10, height/12, 8 * (globalwider - width)/10, height/12, "Confirm", 30)
undoButton = BasicButton(width + (globalwider - width)/10, 2 * height/12 + height/48, 8 * (globalwider - width)/10, height/12, "Undo", 34)




def gameLogic(screen, mousePressed, gameState):
    global pieceChosen
    global pieceSelected
    gameStateLocal = gameState
    xIndex, yIndex = gridIndexer()
    keys = pygame.key.get_pressed()
    
    #Mouse Pressed Logic--------------------------------------------------------------Mouse Pressed Logic
   
    if mousePressed:
        if gameStateLocal == "Setup":
            global player2Turn
            global piecePickedUp
            if piecePickedUp == False:
                #If a piece is not selected
                if xIndex < 12 and yIndex < 12 and yIndex > 6 and grid [xIndex -1 ][yIndex -1] != 0 and grid[xIndex -1][yIndex -1] != 13:
                    #If clicked in a grid with a piece there
                    pieceChosen = grid[xIndex-1][yIndex-1]
                    pieceChosen -= 1
                    grid[xIndex-1][yIndex-1] = 0
                    if keys[pygame.K_LSHIFT] != True:
                        piecePickedUp = True
                    else:
                        spawns[pieceChosen] += 1
                else:
                    #Creation of piece with spawner buttons
                    for button in range(len(buttonBackers)):
                        if spawnerRed[button].over_button() and spawns[button] > 0:
                            spawns[button] -= 1
                            buttonBackers[button].number = spawns[button]
                            piecePickedUp = True
                            pieceChosen = button
            #If a piece is already selected
            else:
                if trashButton.over_button():
                    piecePickedUp = False
                    spawns[pieceChosen] += 1
                elif xIndex < 12 and yIndex < 12 and yIndex > 6 and grid [xIndex -1 ][yIndex -1] == 0:
                    grid[xIndex -1][yIndex -1] = pieceOut[0].type
                    if keys[pygame.K_LCTRL] == True and spawns[pieceChosen] > 0:
                        spawns[pieceChosen] -= 1
                    else:
                        piecePickedUp = False
            #Finish Button
            if finishButton.over_button():
                if all(value == 0 for value in spawns):
                    if player2Turn == True:
                        gameStateLocal = "Playing"
                    else:
                        player2Turn = True
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
        #If gameState != Setup ---------------- moving chosen pieces in game
        else:
            #pieces picked up
            if turnstate[0] <= 1:
                if pieceSelected == False and xIndex < 11 and yIndex < 11:
                    if grid[xIndex -1][yIndex - 1] < 19:
                        pieceChosen = grid[xIndex-1][yIndex-1]
                    if pieceChosen != 13 and pieceChosen != 0 and pieceChosen != 10 and pieceChosen != 12 and turnstate[0] == 0:
                        tempxIndex[0] = xIndex -1
                        tempyIndex[0] = yIndex -1
                        if xIndex < 12 and yIndex < 12 and pieceChosen >0:
                                pieceSelected = True
                                moveLogic(pieceChosen, xIndex -1, yIndex -1, potentialMoves, grid)
                    #If you're trying to move the piece back
                    elif xIndex == tempxIndex[1] and yIndex == tempyIndex[1] and turnstate[0] == 1:
                        pieceSelected = True
                        potentialMoves[tempxIndex[0]][tempyIndex[0]][0] = 1
                        potentialMoves[tempxIndex[0]][tempyIndex[0]][1] = "Center"
                        potentialMoves[tempxIndex[1] -1][tempyIndex[1] -1][0] = 1
                        potentialMoves[tempxIndex[1] -1][tempyIndex[1] -1][1] = "Center"
                        return turnstate
                    #placing piece back down
                else:
                    if xIndex < 11 and yIndex < 11 and potentialMoves[xIndex - 1][yIndex - 1][0] == 1:
                        pieceSelected = False
                        if turnstate[0] == 0:
                            tempxIndex[1] = xIndex
                            tempyIndex[1] = yIndex
                            turnstate[0] = 1
                            if potentialMoves[xIndex -1][yIndex -1][1] == "Enemy":
                                fight = combatPositions(tempxIndex[0], tempyIndex[0], pieceChosen, xIndex -1, yIndex - 1, grid, previous_combat)
                                fightingPieces.append(fight[1])
                                fightingPieces.append(fight[2])
                            else:
                                if tempxIndex[0] == xIndex - 1 and tempyIndex[0] == yIndex -1:
                                    turnstate[0] = 0
                                grid[tempxIndex[0]][tempyIndex[0]] = 0
                                grid[xIndex -1][yIndex - 1] = pieceChosen
                        else:
                                if grid[tempxIndex[1] -1][tempyIndex[1] -1] < 19:
                                    grid[tempxIndex[1]-1][tempyIndex[1]-1] = 0
                                else:
                                    grid[tempxIndex[1] -1][tempyIndex[1] -1] = fightingPieces[1]
                                grid[xIndex -1][yIndex - 1] = pieceChosen
                                turnstate[0] = 0
                        for i in range (0,10):
                            for j in range (0,10):
                                potentialMoves[i][j][0] = 0
                                potentialMoves[i][j][1] = 1
                        
            if confirmButton.over_button() and (turnstate[0] <= 1 or turnstate[0] == 3):
                if turnstate[0] == 1:
                    turnstate [0] = 2
                    if grid[tempxIndex[1] -1][tempyIndex[1] -1] >= 20:
                        #Display the enemy fighting piece here
                        turnstate[0] = 3
                elif turnstate[0] == 3:
                    combat(fightingPieces [0], fightingPieces [1], tempxIndex [1], tempyIndex [1], grid)
                    turnstate[0] = 2
                elif turnstate[0] == -1:
                    turnstate [0] = 0
            elif opponentTurnButton.over_button() and turnstate[0] == 2:
                changePlayer()
                if turnstate[0] == 2:
                    turnstate [0] = 0
                else:
                    turnstate[0] = -1
            if undoButton.over_button() and turnstate[0] == 1:
                turnstate [0] = 2

    #UI -----------------------------------------------------------------------------------------------UI
    drawPotential(screen, potentialMoves)

    print ("tempIndex[0] =", tempxIndex[0], tempyIndex[0], "tempIndex[1] =", tempxIndex[1], tempyIndex[1], "Mouse Index = ", xIndex, yIndex, turnstate, previous_combat)
    #Button logic and drawing the pieces when the fight is happening
    for i in range(len(grid)):
        for f in range(len(grid)):
            if grid[i][f] != 0 and grid[i][f] < 13:
                Piece(gridPos[i][0], gridPos[f][1], 60, grid[i][f], False, turnstate).draw(screen)
            elif grid[i][f] > 19:
                #if turnstate[0] <= 2:
                combatPieceMaker(screen, fightingPieces [0], fightingPieces[1], i, f)
                #else:
                    #combatPieceMaker(screen, fightingPieces[0], abs(fightingPieces[1]), i, f)
    for i in range(len(buttonBackers)):
        buttonBackers[i] = (ButtonBacker((i*2) * width/24 + width /22 - 9, height - 3* height/48 - 3, 36, 60, str(spawns[i])))

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
        if turnstate[0] == 1 or turnstate[0] == -1 or turnstate[0] == 3:
            confirmButton.draw(screen)
        elif turnstate[0] == 2:
            opponentTurnButton.draw(screen)
    #Piece Drawing
    if piecePickedUp:
        pieceOut[0] = Piece(spawnerRed[pieceChosen].locationX, spawnerRed[pieceChosen].locationY, 60, spawnerRed[pieceChosen].type, True, turnstate)
        pieceOut[0].draw(screen)
    return gameStateLocal

def changePlayer():
    tempGrid = [[0 for i in range(10)] for j in range(10)]
    for i in range(0, 10):
        for j in range(0,10):
            flipped_i = 9 - i
            flipped_j = 9 - j
            tempGrid[flipped_i][flipped_j] = grid[i][j]
    for i in range(0,10):
        for j in range(0,10):
            if tempGrid[i][j] != 13:
                grid[i][j] = -1 * tempGrid[i][j]
    if turnstate[1] == 0:
        turnstate[1] = 1
    else:
        turnstate[1] = 0

def combatPieceMaker(screen, attacking, defending, i, f):
    if grid[i][f] == 20:
        Piece(gridPos[i][0] + 11, gridPos[f][1] + 31, 40, attacking, False, turnstate).draw(screen)
        Piece(gridPos[i][0] + 11, gridPos[f][1] - 12, 40, defending, False, turnstate).draw(screen)
    elif grid[i][f] == 23:
        Piece(gridPos[i][0] + 11, gridPos[f][1] + 31, 40, defending, False, turnstate).draw(screen)
        Piece(gridPos[i][0] + 11, gridPos[f][1] - 12, 40, attacking, False, turnstate).draw(screen)
    elif grid[i][f] == 21:
        Piece(gridPos[i][0] - 11, gridPos[f][1] +11, 40, defending, False, turnstate).draw(screen)
        Piece(gridPos[i][0] + 31, gridPos[f][1] +11, 40, attacking, False, turnstate).draw(screen)
    if grid[i][f] == 22:
        Piece(gridPos[i][0] - 11, gridPos[f][1] + 11, 40, attacking, False, turnstate).draw(screen)
        Piece(gridPos[i][0] + 31, gridPos[f][1] + 11, 40, defending, False, turnstate).draw(screen)

def randomPlacements():
    global pieceChosen
    for i in range (0,10):
        for j in range (6,10):
            if grid[i][j] == 0:
                sVals = []
                sVals.append(random.randint(0, 11))
                while spawns[sVals[0]] == 0:
                    sVals[0] = random.randint(0, 11)
                pieceChosen = sVals [0] + 1
                grid[i][j] = pieceChosen
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
