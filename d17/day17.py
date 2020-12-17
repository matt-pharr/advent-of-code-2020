# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import numpy as np

day = '17'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    d1 = {'#':1,'.':0}
    a = [[x for x in b] for b in puzzle_input.splitlines()]
    n = np.zeros(np.shape(a))
    for i in range(len(n)):
        for j in range(len(n[i])):
            n[i][j] = d1[puzzle_input.splitlines()[i][j]]
    return n

def getsurr(arr,loc):
    directions = ((1,0,0),(-1,0,0),(1,-1,0),(-1,-1,0),(0,-1,0),(1,1,0),(-1,1,0),(0,1,0), \
                    (1,0,-1),(0,0,-1),(-1,0,-1),(1,-1,-1),(-1,-1,-1),(0,-1,-1),(1,1,-1),(-1,1,-1),(0,1,-1),\
                    (1,0,1),(0,0,1),(-1,0,1),(1,-1,1),(-1,-1,1),(0,-1,1),(1,1,1),(-1,1,1),(0,1,1))
    sumofsurron = 0
    for d in directions:
        newloc = tuple([sum(x) for x in zip(d,loc)])
        twonewloc = []
        for i in range(3):
            if newloc[i] == len(arr):
                twonewloc.append(0)
            else:
                twonewloc.append(newloc[i])
    
        sumofsurron += arr[tuple(twonewloc)]
        # print(twonewloc)
        # print(arr[tuple(twonewloc)])
    return sumofsurron
    
def getsurr4(arr,loc):
    directions = ((0,0,0),(1,0,0),(-1,0,0),(1,-1,0),(-1,-1,0),(0,-1,0),(1,1,0),(-1,1,0),(0,1,0), \
                    (1,0,-1),(0,0,-1),(-1,0,-1),(1,-1,-1),(-1,-1,-1),(0,-1,-1),(1,1,-1),(-1,1,-1),(0,1,-1),\
                    (1,0,1),(0,0,1),(-1,0,1),(1,-1,1),(-1,-1,1),(0,-1,1),(1,1,1),(-1,1,1),(0,1,1))
    sumofsurron = 0
    for i in range(-1,2,1):
        for d in directions:
            if i == 0 and d == (0,0,0):
                continue
            else:
                newloc = (d[0] + loc[0], d[1] + loc[1], d[2] + loc[2], i + loc[3])
                twonewloc = []
                for j in range(4):
                    if newloc[j] == len(arr):
                        twonewloc.append(0)
                    else:
                        twonewloc.append(newloc[j])
                sumofsurron += arr[tuple(twonewloc)]
                # print(twonewloc)
                # print(arr[tuple(twonewloc)])
    return sumofsurron

def step(arr,steps=1):
    surr = np.zeros(np.shape(arr))
    arrnew = np.zeros(np.shape(arr))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                surr[i][j][k] = getsurr(arr,(i,j,k))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if 2 <= surr[i][j][k] <=3 and arr[i][j][k] == 1:
                    arrnew[i][j][k] = 1
                elif arr[i][j][k] == 0 and surr[i][j][k] == 3:
                    arrnew[i][j][k] = 1
                else:
                    arrnew[i][j][k] = 0

    # print(steps)
    if steps > 1:
        return step(arrnew,steps-1)
    else:
        return sum(sum(sum(arrnew)))

def step4(arr,steps=1):
    surr = np.zeros(np.shape(arr))
    arrnew = np.zeros(np.shape(arr))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                for l in range(len(arr[i][j][k])):
                    surr[i][j][k][l] = getsurr4(arr,(i,j,k,l))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                for l in range(len(arr[i][j][k])):
                    if 2 <= surr[i][j][k][l] <=3 and arr[i][j][k][l] == 1:
                        arrnew[i][j][k][l] = 1
                    elif arr[i][j][k][l] == 0 and surr[i][j][k][l] == 3:
                        arrnew[i][j][k][l] = 1
                    else:
                        arrnew[i][j][k][l] = 0

    # print(steps)
    if steps > 1:
        return step4(arrnew,steps-1)
    else:
        return sum(sum(sum(sum(arrnew))))

def setupgrid(ogrid):
    scale = 30
    pocketdim = np.zeros((scale,scale,scale))
    mid = (scale - len(ogrid))// 2
    for j in range(len(ogrid)):
        for k in range(len(ogrid[j])):
            pocketdim[scale//2][mid + j][ mid + k] = ogrid[j][k]
    return pocketdim

def setupgrid4(ogrid):
    scale = 16 #chosen because 8 (len of og slice) + 6 (number of steps) = 14, so 14 is the max length it could be at final step time. Add one on each side for buffer
    pocketdim = np.zeros((scale,scale,scale,scale))
    mid = (scale - len(ogrid))// 2
    for j in range(len(ogrid)):
        for k in range(len(ogrid[j])):
            pocketdim[scale//2][scale//2][mid + j][ mid + k] = ogrid[j][k]
    return pocketdim

def solve(puzzle_input):
    ogrid = readin(puzzle_input)
    g0 = setupgrid(ogrid)
    g04 = setupgrid4(ogrid)
    # print(g0[3])
    # print(step(g0))
    s1 = step(g0,6)
    yield s1
    s2 = step4(g04,6)
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)