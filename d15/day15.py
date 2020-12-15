# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import numpy as np
from collections import defaultdict

day = '15'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

def def_value():
    return -1

def game(goal,stn):
    numarr = np.zeros(goal).astype(int)
    d = defaultdict(def_value)
    # setup
    for i in range(len(stn)):
        s = i
        numarr[i] = stn[i]
        if i < len(stn)-1:
            d[stn[i]] = i
    
    # dynamically programmed solution
    for j in range(s+1,goal):
        last = numarr[j-1]
        
        if d[last] == -1:
            diff = 0
        else:
            diff = j - d[last]-1

        d[last] = j-1
        numarr[j] = diff

    return numarr[-1]



def solve(puzzle_input):
    stn = [16,11,15,0,1,7]
    s1 = game(2020,stn)
    s2 = game(30000000,stn)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)