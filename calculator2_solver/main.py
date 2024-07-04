import copy
import time

class Actions:
    
    def __init__(self, config):
        self.config = config
    
    def multiplyA(self, num):
        return num * self.config[0]
    
    def multiplyB(self, num):
        return num * self.config[1]
    
    def addA(self, num):
        return num + self.config[2]
    
    def addB(self, num):
        return num + self.config[3]
    
    def addC(self, num):
        return num + self.config[4]
    
    def shiftleft(self, num):
        return num//10
    
    def shiftright(self, num):
        return num%(10**(len(str(num))-1)) # haven't been tested yet
    

#preconfigure your numbers
#___________________
MulA = 0
MulB = 0
AddA = 2
AddB = -3
AddC = -1
#____________________
#end of config

actions = Actions([MulA, MulB, AddA, AddB, AddC]) #initialize action set with values


def numToActionExectutor(x, num):
    if x==0:
        return actions.multiplyA(num)
    elif x==1:
        return actions.multiplyB(num)
    elif x==2:
        return actions.addA(num)
    elif x==3:
        return actions.addB(num)
    elif x==4:
        return actions.addC(num)
    elif x==5:
        return actions.shiftleft(num)
    elif x==6:
        return actions.shiftright(num)

def script_incrementer(array, base, max_depth):
    array[max_depth-1]+=1
    if array[max_depth-1] == base:
        for i in range(max_depth-1, 0, -1):
            if array[i] == base:
                array[i] = 0
                array[i-1] += 1
    return array



goals = []
start_number = -1
max_depth = 4
base = 7
exclude_moves = [] #not working yet
include_moves = [2,3,5]

allowed_moves = []

if exclude_moves == []:
    allowed_moves = include_moves
else:
    allowed_moves = []

print("Enter goal(s) (divide numbers with space)")
goals = list(map(int, input().split()))

print("Enter start_number")
start_number = int(input())

print("Enter maximum moves")
max_depth = int(input())

#mainloop:
mainflag = False
current_script = [0]*max_depth

for i in range(base**max_depth):
    tmp_num = start_number
    tmp_goals = copy.deepcopy(goals)

    #print(current_script)

    for j in current_script:
        print(tmp_num, end=" ")
        tmp_num = numToActionExectutor(j, tmp_num)
        if tmp_num in tmp_goals:
            del tmp_goals[tmp_goals.index(tmp_num)]
    print(tmp_num)
    
    #print(goals)
    
    if len(tmp_goals) == 0:
        flag = False
        
        for k in current_script:
            if k not in allowed_moves:
                flag = True
        
        if flag:
            continue

        print(current_script)
        mainflag = True
    
    current_script = script_incrementer(current_script, base, max_depth)
    #time.sleep(0.01)

if not mainflag:
    print("No results were found")




