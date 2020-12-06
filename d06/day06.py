# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute

import re

day = '06'
inp = 'day' + day + 'input.txt'

# Reading function goes here

def readin(puzzle_input):
    a = []
    #print(puzzle_input.split('\n\n'))
    #print('\n\n')
    for y in puzzle_input.split('\n\n'):
        #print(y)
        aset = set()
        for x in y:
            if x in 'abcdefghijklmnopqrstuvwxyz':
                aset.add(x)
        a.append(aset)
    #[[x if (x in 'abcdefghijklmnopqrstuvwxyz') for x in y] for y in puzzle_input.split('\n\n')]
    #print(a)
    
    return a

def readin2(puzzle_input):
    a = []
    al = 'abcdefghijklmnopqrstuvwxyz'
    
    for y in puzzle_input.split('\n\n'):
        al1 = 'abcdefghijklmnopqrstuvwxyz'
        for c in al:
            for x in y.split('\n'):
                if not (c in x):
                    try:
                        al1 = al1.replace(c,'')
                    except:
                        pass
        print(al1)
        a.append(al1)
    
    return a

def solve(puzzle_input):
    a = readin(puzzle_input)
    x = [len(s) for s in a]

    b = readin2(puzzle_input)
    a1 = sum([len(x) for x in b])

    s1 = sum(x)
    s2 = a1
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)