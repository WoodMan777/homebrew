from copy import deepcopy as dpc
from random import randint as rnd

class Game:
    def __init__(self, arr = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], score = 0):
        self.arr = arr
        self.score = score
    
    def moveLeft(self, randomOn = True):
        prevState = dpc(self.arr)
        for y in range(4):
            tmp = []
            for x in range(4):
                tmp.append(self.arr[y][x])
            
            tmp = self.processRow(tmp)
            for x in range(4):
                self.arr[y][x] = tmp[x]
        
        if prevState != self.arr and randomOn:
            self.addRandomElement()

        return prevState != self.arr
        

    def moveRight(self, randomOn = True):
        prevState = dpc(self.arr)
        for y in range(4):
            tmp = []
            for x in range(4):
                tmp.append(self.arr[y][x])
            
            tmp = self.processRow(tmp[::-1])
            tmp = tmp[::-1]
            for x in range(4):
                self.arr[y][x] = tmp[x]
        
        if prevState != self.arr and randomOn:
            self.addRandomElement()

        return prevState != self.arr


    def moveUp(self, randomOn = True):
        prevState = dpc(self.arr)
        for x in range(4):
            tmp = []
            for y in range(4):
                tmp.append(self.arr[y][x])
            
            tmp = self.processRow(tmp)
            for y in range(4):
                self.arr[y][x] = tmp[y]
        
        if prevState != self.arr and randomOn:
            self.addRandomElement()

        return prevState != self.arr
    

    def moveDown(self, randomOn = True):
        prevState = dpc(self.arr)
        for x in range(4):
            tmp = []
            for y in range(4):
                tmp.append(self.arr[y][x])
            
            tmp = self.processRow(tmp[::-1])
            tmp = tmp[::-1]
            for y in range(4):
                self.arr[y][x] = tmp[y]
        
        if prevState != self.arr and randomOn:
            self.addRandomElement()

        return prevState != self.arr


    def processRow(self, row):
        i = 0
        lastZeroFlag = False
        while i!=3:
            if row[i] == 0:
                lastZeroFlag = True
                del row[i]
                row.append(0)
                if self.areAllTrailingZeros(row, i):
                    break
            
            else:
                if lastZeroFlag:
                    i -= 1
                    lastZeroFlag = False
                if row[i] == row[i+1]:
                    row[i] = row[i] * 2
                    self.score += row[i]
                    row[i+1] = 0
                    i += 1
                    continue
                else:
                    i+=1
                    continue
        return row
        

    def areAllTrailingZeros(self, row, i):
        check = 0
        for j in range(i, 4):
            check += row[j]
        return check == 0
    

    def addRandomElement(self):
        elem = 2
        if (rnd(1,10) == 5):
            elem = 4

        while True:
            x = rnd(0,3)
            y = rnd(0,3)
            
            if self.arr[y][x] == 0:
                self.arr[y][x] = elem
                break
    

    def placeElem(self, x, y, elem = 2):
        self.arr[y][x] = elem
    

    def show(self):
        for y in range(4):
            print(', '.join(map(str, self.arr[y])))
        print(f"Score: {self.score}")


    def getSelfDeepCopy(self):
        return Game(dpc(self.arr), self.score)
    

    def getAllPossibleGameStatesAfterMove(self):
        states = []
        tmpGame = self.getSelfDeepCopy()
        
        if tmpGame.isMoveLegal('L'):
            tmpGame.moveLeft(randomOn = False)
            for y in range(4):
                for x in range(4):
                    if tmpGame.arr[y][x] == 0:
                        tmpGame.placeElem(x,y,2)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,4)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,0)
        
        tmpGame = self.getSelfDeepCopy()

        if tmpGame.isMoveLegal('R'):
            tmpGame.moveRight(randomOn = False)
            for y in range(4):
                for x in range(4):
                    if tmpGame.arr[y][x] == 0:
                        tmpGame.placeElem(x,y,2)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,4)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,0)
        
        tmpGame = self.getSelfDeepCopy()
        
        if tmpGame.isMoveLegal('U'):
            tmpGame.moveUp(randomOn = False)
            for y in range(4):
                for x in range(4):
                    if tmpGame.arr[y][x] == 0:
                        tmpGame.placeElem(x,y,2)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,4)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,0)
        
        tmpGame = self.getSelfDeepCopy()
        if tmpGame.isMoveLegal('D'):
            tmpGame.moveDown(randomOn = False)
            for y in range(4):
                for x in range(4):
                    if tmpGame.arr[y][x] == 0:
                        tmpGame.placeElem(x,y,2)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,4)
                        states.append(tmpGame.getSelfDeepCopy())
                        tmpGame.placeElem(x,y,0)

        return states
    
    
    def isMoveLegal(self, move):
        if move == 'U':
            tmp = self.getSelfDeepCopy()
            return tmp.moveUp()
        elif move == 'D':
            tmp = self.getSelfDeepCopy()
            return tmp.moveDown()
        elif move == 'R':
            tmp = self.getSelfDeepCopy()
            return tmp.moveRight()
        elif move == 'L':
            tmp =self.getSelfDeepCopy()
            return tmp.moveLeft()
    

        