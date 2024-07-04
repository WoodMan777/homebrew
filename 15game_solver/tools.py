from copy import deepcopy

class Board:
    def __init__(self, input_data):
        
        if type(input_data) != Board:
            input_data = input_data.split()
            self.position = []

            for i in range(4):
                self.position.append(list(map(int,input_data[4*i:4*i+4])))
            
            for x in range(4):
                if not 0 in self.position[x]:
                    continue
                else:
                    self.x_0 = x
                    self.y_0 = self.position[x].index(0)
                    break

        else:
            self.position = deepcopy(input_data.position)
            self.x_0 = deepcopy(input_data.x_0)
            self.y_0 = deepcopy(input_data.y_0)
    
    def getAllPossibleMoves(self):
        moves = 15 #LRUD :=: 1111
        if not self.x_0:
            moves &= 11
        if self.x_0 == 3:
            moves &= 7
        if not self.y_0:
            moves &= 14
        if self.y_0 == 3:
            moves &= 13
        
        return moves
    
    
    def makeMoveLeft(self):
        if not (self.getAllPossibleMoves() & 8):
            return False
        
        self.position[self.x_0][self.y_0], self.position[self.x_0+1][self.y_0] = self.position[self.x_0+1][self.y_0], self.position[self.x_0][self.y_0]
        self.x_0 += 1
    
    def makeMoveRight(self):
        if not (self.getAllPossibleMoves() & 4):
            return False
        
        self.position[self.x_0][self.y_0], self.position[self.x_0-1][self.y_0] = self.position[self.x_0-1][self.y_0], self.position[self.x_0][self.y_0]
        self.x_0 -= 1
    
    def makeMoveUp(self):
        if not (self.getAllPossibleMoves() & 2):
            return False
        
        self.position[self.x_0][self.y_0], self.position[self.x_0][self.y_0+1] = self.position[self.x_0][self.y_0+1], self.position[self.x_0][self.y_0]
        self.y_0 += 1

    def makeMoveDown(self):
        if not (self.getAllPossibleMoves() & 1):
            return False
        
        self.position[self.x_0][self.y_0], self.position[self.x_0][self.y_0-1] = self.position[self.x_0][self.y_0-1], self.position[self.x_0][self.y_0]
        self.y_0 -= 1
    
    def showAll(self):
        for x in range(4):
            for y in range(4):
                print(self.position[y][x], end = " ")
            print()

    def isSolved(self):
        if self.position == [[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15]]:
            return True
        else:
            return False
    
    def __str__(self):
        s = ""
        for i in self.position:
            for j in i:
                s += str(j) + " "
        return s
    
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False
    

"""class SearchTree:
    def __init__(self):
        pass
"""    


        
"""def recursiveSearch(game, depth_to_go):
    if game.isSolved():"""


def strTo2dArray(s):
    s = s.split()
    res = []

    for i in range(4):
        res.append(list(map(int,s[4*i:4*i+4])))
    
    return res

def TwoDArrayToStr(arr):
    s = ""

    for i in arr:
        for j in i:
            s += str(j) + " "
    
    return s

def allPossibleMoves(arr):
    brflag = False

    for x in range(4):
        if not 0 in arr[x]:
            continue
        else:
            x_0 = x
            y_0 = arr[x].index(0)
    
    moves = 15 #LRUD :=: 1111
    if not x_0:
        moves &= 1011
    if x_0 == 3:
        moves &= 111
    if not y_0:
        moves &= 1110
    if y_0 == 3:
        moves &= 1101
    
    return moves



def makeMoveLeft(arr):
    pass

def makeMoveRight(arr):
    pass

def makeMoveUp(arr):
    pass

def makeMoveDown(arr):
    pass


            