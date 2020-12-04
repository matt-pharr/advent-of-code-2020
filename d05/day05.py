# today i changed my program structure 

import re
day = '05'
inp = 'day' + day + 'input.txt'

# Reading function goes here



def solve(puzzle_input):
    s1 = 0
    s2 = 0
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as inputfile:
        for s in solve(inp.read()):
            print(s)