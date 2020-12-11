# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import numpy as np # boooo you suck

day = '11'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    return [list(a) for a in puzzle_input.splitlines()]

# PLEASE AVERT YOUR EYES OH GOD this is the clunkiest evilest most python-abusive function i have ever written

# def count_seats(seats,loc):
#     a = 0
#     try:
#         if seats[loc[0]+1][loc[1]] == '#':
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]+1][loc[1]-1] == '#' and loc[1] != 0:
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]+1][loc[1]+1] == '#':
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]][loc[1]+1] == '#':
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]][loc[1]-1] == '#' and loc[1] != 0:
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]-1][loc[1]] == '#' and loc[0] != 0:
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]-1][loc[1]+1] == '#' and loc[0] != 0:
#             a += 1
#     except:
#         pass
#     try:
#         if seats[loc[0]-1][loc[1]-1] == '#' and loc[1] != 0 and loc[0] != 0:
#             a += 1
#     except:
#         pass

#     return a


def count_seats(seats,loc,new):
    directions = [(-1,-1), (1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,1), (-1,0)]
    a = 0
    
    for d in directions:
        # print(d)
        x = loc[0] + d[0]
        y = loc[1] + d[1]
        cont = True
        while cont:
            if x < 0 or x == len(seats) or y < 0 or y == len(seats[0]):
                cont = False
                break
            else:
                if seats[x][y] == '#':
                    a += 1
                    cont = False
                    break
                elif seats[x][y] == 'L':
                    cont = False
                    break
                elif seats[x][y] == '.':
                    pass
                else:
                    print("ERROR")
                if not new:
                    cont = False
                    break
                x += d[0]
                y += d[1]
    return a
            


def iterate(seats,new=False):
    surr = np.zeros(np.shape(seats))
    for i in range(len(seats)):  #row
        for j in range(len(seats[i])): #column
            a = count_seats(seats.copy(),(i,j),new)
            # print(a)
            surr[i][j] = a
    # for i in range(len(surr)):
    #     for j in range(len(surr[i])):
    #         print(surr[i][j],end='')
        # print()
    # print()
    newseats = seats.copy()

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == 'L' and surr[i][j] == 0:
                newseats[i][j] = '#'
            elif seats[i][j] == '#' and surr[i][j] >=4 and not new:
                newseats[i][j] = 'L'
            elif seats[i][j] == '#' and surr[i][j] >=5 and new:
                newseats[i][j] = 'L'
    return newseats

def finds(seats,new=False):
    a = seats.copy()
    countlist = []
    while True:
        # print('hi')
        # alast = a.copy()
        a = iterate(a.copy(),new)
        count = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == '#':
                    count+= 1
        countlist.append(count)
        try:
            if countlist[-1] == countlist[-2]:
                return countlist[-1]
        except:
            pass

def solve(puzzle_input): #using numpy bc python lists baaaaaaaaaaad
    seats = readin(puzzle_input).copy()
    b = np.array(seats.copy())
    c = np.array(seats.copy())
    s1 = finds(b)
    s2 = finds(c,True)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)