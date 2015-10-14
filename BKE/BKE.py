__author__ = 'terence'

###
### Imports
###
import random
import TurtleDrawLib
import turtle
#import tkMessageBox

###
### Global Variables
###
global log
log = []
global blokPositions
blokPositions = []
global playerTurnIndicator
playerTurnIndicator = True
#This mutex makes sure that only 1 thread can enter the designated method
global clickMutex
clickMutex = True
#This variable is used for how many times has been clicked on the form. (When 9 reached end of game, unless player wins beforehand
global clickCounter
clickCounter = 0
global endGame
endGame = False


###
### Read-only Variables
###
width = 800
height = 600
#width = 1092
#height = 1080
gameBlokWidth = width/3
gameBlokHeight = (height*0.8)/3
tdl = TurtleDrawLib

def drawLogWindow():
    tdl.drawRectangle(0,height*0.8,width,height*0.2,'white','black')

def main():
    tdl.graphicsInit("Boter Kaas en eieren",'white',width,height)
    #tkMessageBox.showinfo("Introductie", "Welkom bij Boter Kaas en eieren (A.K.A. BKE)")
    writeToLog("Introductie: Welkom bij Boter Kaas en eieren (A.K.A. BKE)")
    createGame()
    writeToLog("Player 1 is about to move.")
    turtle.onscreenclick(onScreenClickEvent)
    tdl.done()

def onScreenClickEvent(x,y):
    global clickMutex
    global endGame
    if clickMutex:
        clickMutex = False
        if endGame:
            endGame = False
            createGame()
            clickMutex = True
            return
        #align offset to left & top
        x = (width/2)+x
        y = (height/2)-y
        global playerTurnIndicator
        for i in range(0,9):
            bPos = blokPositions[i].split(',')
            xx = int(bPos[0])
            yy = int(bPos[1])
            ww = int(bPos[2])
            hh = int(bPos[3])
            if x >= xx and x < (xx+ww) and y >= yy and y < (yy+hh):
                if(len(bPos) == 5):
                    clickMutex = True
                    return
                if playerTurnIndicator:
                    tdl.drawRectangle(xx,yy,ww,hh,'black','grey')
                    tdl.drawCross(xx,yy,ww,hh,'black','red')
                    blokPositions[i] += ",X"
                    writeToLog("Player 2 is about to move.")
                else:
                    tdl.drawRectangle(xx,yy,ww,hh,'black','grey')
                    tdl.drawCircle(xx,yy,ww,hh,'black','blue','grey')
                    blokPositions[i] += ",O"
                    writeToLog("Player 1 is about to move.")
                playerTurnIndicator = not playerTurnIndicator
                checkGame()
                clickMutex = True
                return
        clickMutex = True

def checkGame():
    circles = []
    crosses = []
    global endGame
    #Check if Circle or Cross has won
    for i in range(0,len(blokPositions)):
        bPos = blokPositions[i].split(',')
        if (len(bPos) == 5):
            if(bPos[4] == "O"):
                circles.append((i+1))
            elif(bPos[4] == "X"):
                crosses.append((i+1))
    if checkWin(circles):
        writeToLog("Player 1 has won!")
        writeToLog("Game has ended!")
        endGame = True
    if checkWin(crosses):
        writeToLog("Player 2 has won!")
        writeToLog("Game has ended!")
        endGame = True

def checkWin(list):
    wins = ["123","147","159","258","357","369","456","789"]
    for s in wins:
        checkList = []
        for ss in list:
            checkList.append(int(ss))
        winCounter = 0
        for c in s:
            if int(c) in checkList:
                winCounter += 1
        if winCounter == 3:
            return True
    return False

def createGame():
    #clear list blokPositions
    writeToLog("New game started! ")
    del blokPositions[:]
    #clear list log
    del log[:]
    for i in range(0,3):
        for j in range(0,3):
            #switch i & j for different drawing index
            x = int(j*gameBlokWidth)
            y = int(i*gameBlokHeight)
            w = int(gameBlokWidth)
            h = int(gameBlokHeight)
            tdl.drawRectangle(x,y,w,h,'black','grey')
            blokPositions.append(str(x)+","+str(y)+","+str(w)+","+str(h))
    #print(blokPositions)

def writeToLog(text):
    global log
    drawLogWindow()
    log.insert(0,text)
    if len(log) == 6:
        log.pop()
    indexLine = 20
    for s in log:
        tdl.writeText(s,3,(height*0.8)+indexLine)
        indexLine += 20

main()

