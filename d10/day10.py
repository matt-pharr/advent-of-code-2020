# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import numpy as np

day = '10'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    a = [int(s) for s in puzzle_input.splitlines()]
    a.append(0)
    a.append(max(a)+3)
    a.sort()
    return a

def count(joltages):
    jl = np.asarray(joltages)
    # print(jl)
    a = np.diff(jl)
    # print(a)
    d1 = 0
    d3 = 0
    for i in range(len(a)):
        if a[i] == 1:
            d1 += 1
        elif a[i] == 3:
            d3 += 1
    return (d1*d3) 

def countperms(jl,k): # O(a lot oh god)
    a = 1
    for i in range(k,len(jl)-1):
        # print(np.delete(jl,i))
        if max(np.diff(np.delete(jl,i))) <= 3:
            # print(np.delete(jl,i))
            a += countperms(np.delete(jl,i),i)
    return a

def countperms2(jl): # O(a lot less than the last one, never would have figured this out w/o some discussion though)
    count = {}
    for i in range(-3,max(jl)+1):
        count[i] = 0
    count[0] = 1
    for num in jl[1:]:
        count[num] = count[num - 1] + count[num - 2] + count[num-3]
    return count[max(jl)]

def solve(puzzle_input):
    joltages = readin(puzzle_input)
    j1 = [int(j) for j in puzzle_input.splitlines()]
    # print(joltages)
    s1 = count(joltages)
    s2 = countperms2(joltages)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)