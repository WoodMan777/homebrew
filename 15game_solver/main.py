import tools
from copy import deepcopy
from time import time

global total_positions

initial_state = "1 4 8 14 5 6 9 12 2 0 10 15 3 7 11 13" #column-by-column
initial_state = "0 4 8 12 1 5 9 13 2 6 10 14 3 7 11 15"

depth = 17



arr = tools.strTo2dArray(initial_state)
game = tools.Board(initial_state)
print(game.getAllPossibleMoves())

all_boards = []
perfect_solutions = []

#LRUD

def recursive_exploration(game :tools.Board, current_depth, max_depth, previous_move):
    possible_moves = game.getAllPossibleMoves()
    if game.position not in all_boards:
        all_boards.append(game.position)
        perfect_solutions.append(current_depth)
    else:
        solution = all_boards.index(game.position)
        if perfect_solutions[solution] > current_depth:
            perfect_solutions[solution] = current_depth

    
    if current_depth == max_depth:
        return

    if (possible_moves & 8) and previous_move != 4:
        tmp = tools.Board(game)
        tmp.makeMoveLeft()
        recursive_exploration(tmp,current_depth+1, max_depth, 8)
    
    if (possible_moves & 4) and previous_move != 8:
        tmp = tools.Board(game)
        tmp.makeMoveRight()
        recursive_exploration(tmp,current_depth+1, max_depth, 4)
    
    if (possible_moves & 2) and previous_move != 1:
        tmp = tools.Board(game)
        tmp.makeMoveUp()
        recursive_exploration(tmp,current_depth+1, max_depth, 2)
    
    if (possible_moves & 1) and previous_move != 2:
        tmp = tools.Board(game)
        tmp.makeMoveDown()
        recursive_exploration(tmp,current_depth+1, max_depth, 1)

#for depth in range(1,12):
#    recursive_exploration(game,0,depth)
#    print(f"Positions found to depth {depth}: {len(all_boards)}")


"""
recursive_exploration(game, 0, depth, 0)

file_out = open("prefect_solutions.txt", "w+")

for i in range(len(all_boards)):
    file_out.write(f"{tools.TwoDArrayToStr(all_boards[i])} : {perfect_solutions[i]}\n")"""


# print(game.isSolved())
# print(str(game))

#current_iter_array = [(game,0)]
#explored_positions = [(game,0)]
#next_iter_array = []

current_iter_array = [game]
explored_positions = {str(game): 0}
next_iter_array = []



def check_if_in_array(array, game):
    for i in array:
        if game == i[0]:
            return True
    return False

st = time()

depth = 1
max_depth = 19
for depth in range(1,max_depth+1):
    print(f"Now at depth {depth}/{max_depth}. {len(current_iter_array)} total elements to check. Elapsed time: {round(time() - st,2)} sec")
    for element in current_iter_array:
        possible_moves = element.getAllPossibleMoves()

        #LRUD

        if possible_moves & 8:
            tmp = tools.Board(element)
            tmp.makeMoveLeft()
            if not str(tmp) in explored_positions.keys():
                explored_positions[str(tmp)] = depth
                next_iter_array.append(tmp)
        
        if possible_moves & 4:
            tmp = tools.Board(element)
            tmp.makeMoveRight()
            if not str(tmp) in explored_positions.keys():
                explored_positions[str(tmp)] = depth
                next_iter_array.append(tmp)
        
        if possible_moves & 2:
            tmp = tools.Board(element)
            tmp.makeMoveUp()
            if not str(tmp) in explored_positions.keys():
                explored_positions[str(tmp)] = depth
                next_iter_array.append(tmp)
        
        if possible_moves & 1:
            tmp = tools.Board(element)
            tmp.makeMoveDown()
            if not str(tmp) in explored_positions.keys():
                explored_positions[str(tmp)] = depth
                next_iter_array.append(tmp)
        
    current_iter_array = deepcopy(next_iter_array)
    next_iter_array = []

print(f"Search completed in {time() - st} seconds, yielded {len(explored_positions)} positions total.")

file_out = open("perfect_solutions.txt", "w+")

for position in list(explored_positions.keys()):
    file_out.write(f"{position} : {explored_positions[position]}\n")