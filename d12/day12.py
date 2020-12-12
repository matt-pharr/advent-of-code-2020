# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import math

day = '12'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here

def readin(puzzle_input):
    return puzzle_input.splitlines()

def moveship(dir,state):
    if dir[0] == 'N':
        newstate = (state[0],(state[1][0], state[1][1] + int(dir[1:])))

    elif dir[0] == 'S':
        newstate = (state[0],(state[1][0], state[1][1] - int(dir[1:])))
    
    elif dir[0] == 'E':
        newstate = (state[0],(state[1][0] + int(dir[1:]), state[1][1]))
    
    elif dir[0] == 'W':
        newstate = (state[0],(state[1][0] - int(dir[1:]), state[1][1]))
    else:
        print("ERROR")

    return newstate

def rotate(dir,current,angle):
    aint = angle/90
    inverserotatedict = {}
    rotatedict = {}
    rotatedict[0] = 'E'
    rotatedict[1] = 'N'
    rotatedict[2] = 'W'
    rotatedict[3] = 'S'

    inverserotatedict['E'] = 0
    inverserotatedict['N'] = 1
    inverserotatedict['W'] = 2
    inverserotatedict['S'] = 3

    if dir == 'R':
        rint = inverserotatedict[current]
        newint = (rint - aint)%4
        return rotatedict[newint]
    
    elif dir == 'L':
        rint = inverserotatedict[current]
        newint = (rint + aint)%4
        return rotatedict[newint]

    else:
        print("Error1")

def rotatewaypoint(dir,loc,angle):
    dirdict = {}
    dirdict['R'] = -1
    dirdict['L'] = 1
    a1 = angle*math.pi/180*dirdict[dir]

    # Here is where the quantum mechanics kicks in. 
    # Yes I have the spin/rotation matricies memorized, why do you ask.............

    return (loc[0]*int(math.cos(a1)) - loc[1]*int(math.sin(a1)),loc[0]*int(math.sin(a1)) + loc[1]*int(math.cos(a1)))

def instruct(dirs):
    state = ('E',(0,0))
    for dir in dirs:
        if re.match('[N,S,E,W]',dir) is not None:
            # print(dir,state)
            state = moveship(dir,state)
            # print(state)
        elif dir[0] == 'F':
            # print(dir,state)
            state = moveship((state[0] + dir[1:]),state)
            # print(state)
        elif re.match('[L,R]',dir) is not None:
            # print(dir,state)
            state = (rotate(dir[0],state[0],int(dir[1:])), (state[1][0],state[1][1]))
    # print(state)
    return abs(state[1][0]) + abs(state[1][1])

def instructtowp(dirs):
    wp = (10,1)
    boatpos = (0,0)
    direcdict = {}
    direcdict['N'] = (0,1)
    direcdict['S'] = (0,-1)
    direcdict['E'] = (1,0)
    direcdict['W'] = (-1,0)
    for dir in dirs:
        num = int(dir[1:])
        d = dir[0]
        if re.match('[N,S,E,W]',dir) is not None:
            wp = (wp[0] + num*(direcdict[d][0]), wp[1] + num*(direcdict[d][1]))
            # print(dir,'wp', wp)
        elif d == 'F':
            diff = (wp[0], wp[1]) # initially thought we had to move the boat by the difference in waypoint and boat pos...
            #                       yeah that got me final pos 816588420908787809396632331870392006638228294295640960234766184567808231635960609029868229783209298670938
            #                       and yes, I tried putting that into the submission box...
            boatpos = (boatpos[0] + diff[0]*num, boatpos[1] + diff[1]*num)
            # print(dir,'bp',boatpos)
        elif re.match('[L,R]',dir) is not None:
            wp = rotatewaypoint(d,wp,num)
            # print(dir,'wp',wp)
    return abs(boatpos[0]) + abs(boatpos[1])
        

def solve(puzzle_input):
    dirs = readin(puzzle_input)
    s1 = instruct(dirs)
    s2 = instructtowp(dirs)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)