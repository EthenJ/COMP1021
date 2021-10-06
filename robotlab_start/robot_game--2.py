# Done by EthenJ

# The following line imports the game function library and map into
# this main program
from game_lib import *

# This is the only 'memory' of the robot that you can use to store things
#
# You are expected to use it to store only a string, which indicates the
# current 'state' of the robot
stateForTask1 = "Go up"
stateForTask2 = "Go up"
stateForTask3 = "Go up"
stateForTask4 = "Go up"
stateForTask5 = "Go up"


# These functions helps the robot to make the decision about what it needs
# to do in order to get to the exit of the map
# 
# The function should return one of the following:
#     "UP"     which means the robot decides to go up
#     "LEFT"   which means the robot decides to go left
#     "RIGHT"  which means the robot decides to go right
#     "DOWN"   which means the robot decides to go down
#     "NONE"   which means the robot decides to stay in the same place

# Your task is to help the robot to make a decision on what to do next.
#
# A collection of functions that you will find very useful here:
#
#    leftIsWall()   returns True if the robot detects that the left side is blocked, otherwise it returns False
#    rightIsWall()	returns True if the robot detects that the right side is blocked, otherwise it returns False
#    upIsWall()	returns True if the robot detects that the up side is blocked, otherwise it returns False
#    downIsWall()	returns True if the robot detects that the down side is blocked, otherwise it returns False

def execute(stateForTask):
    if stateForTask == "Go up":
        return "UP"
    elif stateForTask == "Go right":
        return "RIGHT"
    elif stateForTask == "Go left":
        return "LEFT"
    elif stateForTask == "Go down":
        return "DOWN"


# This is the function for task 0
def makeDecisionForTask0():
    return "UP"


# This is the function for task 1
def makeDecisionForTask1():
    global stateForTask1
    if not upIsWall():
        stateForTask1 = "Go up"
    else:
        stateForTask1 = "Go right"
    return execute(stateForTask1)


# This is the function for task 2
def makeDecisionForTask2():
    global stateForTask2
    if not upIsWall():
        stateForTask2 = "Go up"
    elif not rightIsWall() and not stateForTask2 == "Go left":
        stateForTask2 = "Go right"
    else:
        stateForTask2 = "Go left"
    return execute(stateForTask2)


# This is the function for task 3
def makeDecisionForTask3():
    global stateForTask3
    if not upIsWall():
        stateForTask3 = "Go up"
    elif not rightIsWall() and not stateForTask3 == "Go left":
        stateForTask3 = "Go right"
    else:
        stateForTask3 = "Go left"
    return execute(stateForTask3)


# This is the function for task 4
forwards = ["Go up", "Go right", "Go down", "Go left"]
lefts = ["Go left", "Go up", "Go right", "Go down"]
rights = ["Go right", "Go down", "Go left", "Go up"]
backwards = ["Go down", "Go left", "Go up", "Go right"]
func_forwards = [upIsWall, rightIsWall, downIsWall, leftIsWall]
func_lefts = [leftIsWall, upIsWall, rightIsWall, downIsWall]
func_rights = [rightIsWall, downIsWall, leftIsWall, upIsWall]
find_the_wall_4 = False


stateForTask4 = "Find a wall first!"
def makeDecisionForTask4():
    global stateForTask4
    if stateForTask4 == "Find a wall first!":
        if leftIsWall():
            stateForTask4 = "Go up"
        else:
            return "LEFT"
    elif stateForTask4 == "Go up":
        if leftIsWall():
            stateForTask4 = "Go right"
        else:
            stateForTask4 = "Go left"
            return "LEFT"
    elif stateForTask4 == "Go down":
        if rightIsWall():
            stateForTask4 = "Go left"
        else:
            stateForTask4 = "Go right"
            return "RIGHT"
    elif stateForTask4 == "Go left":
        if downIsWall():
            stateForTask4 = "Go up"
        else:
            stateForTask4 = "Go down"
            return "DOWN"
    elif stateForTask4 == "Go right":
        if upIsWall():
            stateForTask4 = "Go down"
        else:
            stateForTask4 = "Go up"
            return "UP"
    return "NONE"


# This is the function for task 5
def makeDecisionForTask5():
    global stateForTask5
    for i in range(0, 4):
        if stateForTask5 == forwards[i]:
            if not func_rights[i]():
                stateForTask5 = rights[i]
            elif func_rights[i]():
                if not func_forwards[i]():
                    stateForTask5 = forwards[i]
                elif not func_lefts[i]():
                    stateForTask5 = lefts[i]
                else:
                    stateForTask5 = backwards[i]
            break
        else:
            continue
    return execute(stateForTask5)


# The following line of code chooses the map of the game before it starts
# 
# You can change the map of the game by changing the parameters:
# 
# - Parameter 1 can be either:
#   - "task0", "task1", "task2", "task3", "task4" or "task5"
#     which mean the predefined maps from the task that you want to work on
#
#   - "custom"
#     which means any customized map(s) that you can add in game_map.py
#
# - Parameter 2 is a number representing the map you want to use
chooseGameMap("task4", 0)

#####
#
# !!! You DO NOT need to change anything from this point onwards
#
#####

# Using the makeDecision function to set the Decision function used in each of the tasks
setDecisionFuncForTask0(makeDecisionForTask0)
setDecisionFuncForTask1(makeDecisionForTask1)
setDecisionFuncForTask2(makeDecisionForTask2)
setDecisionFuncForTask3(makeDecisionForTask3)
setDecisionFuncForTask4(makeDecisionForTask4)
setDecisionFuncForTask5(makeDecisionForTask5)

# Start the game
startGame()
