import os
from tools import Game


def clearScreen():
    os.system('cls')

clearScreen()
game = Game()
game.placeElem(0,0,2)
game.placeElem(3,0,2)

game.show()

a = "..."
illegalMove = 0

while a != "/exit":
    
    a = input()

    if a == 'L':
        illegalMove = game.moveLeft()
        clearScreen()
        game.show()

    elif a == 'R':
        illegalMove = game.moveRight()
        clearScreen()
        game.show()
    
    elif a == 'U':
        illegalMove = game.moveUp()
        clearScreen()
        game.show()
    
    elif a == 'D':
        illegalMove = game.moveDown()
        clearScreen()
        game.show()
    
    elif a == "/exit":
        break
    
    else:
        print("Unknown move")
    
    if not illegalMove:
        print("Illegal move. No changes to board")
