# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute

# today i changed my program structure 

import re

day = '05'
inp = 'day' + day + 'input.txt'

# Reading function goes here
def read_seats(puzzle_input:str):
    return puzzle_input.splitlines()

def findseat(s: str):
    s = s.strip()
    fb = s[:7]
    lr = s[7:]
    lp = list(range(128))
    lp1 = list(range(8))
    for c in fb:
        if c == 'F':
            lp = lp[:int(len(lp)/2)]
        elif c == 'B':
            lp = lp[int(len(lp)/2):]

    for d in lr:
        if d == 'L':
            lp1 = lp1[:int(len(lp1)/2)]
        elif d == 'R':
            lp1 = lp1[int(len(lp1)/2):]
    
    return (lp[0],lp1[0])



def solve(puzzle_input):
    a = [findseat(x) for x in read_seats(puzzle_input)]
    b = [(y[0]*8 + y[1]) for y in a]

    fullset = set()
    for i in range(128):
        for j in range(8):
            fullset.add((i,j))


    s1 = max(b)
    s2 = fullset - set(a)

    for s in s2:
        if re.match('\d{2}$', str(s[0])) is not None:
            print(s)

    yield s1
    yield s2

    #literally printed this set difference and jus looked for a seat in the middle lol -- the 69 ended up sticking out

if __name__ == "__main__":
    with open(inp) as inputfile:
        for s in solve(inputfile.read()):
            print(s)