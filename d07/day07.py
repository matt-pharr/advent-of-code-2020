# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute

# beware this one is UGLY

import re

day = '07'
inp = 'day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    a = puzzle_input.splitlines()
    b = [x.split('contain') for x in a]
    bagsdict = {}
    for y in b:
        if y[1] == ' no other bags.':
            bagsdict[y[0].strip().rstrip('s')] = 0
        else: 
            bagsdict[y[0].strip().rstrip('s')] = [s[2:].strip('s.').strip() for s in y[1].split(',')]
    return bagsdict

def readin2(puzzle_input):
    a = puzzle_input.splitlines()
    b = [x.split('contain') for x in a]
    bagsdict = {}
    for y in b:
        if y[1] == ' no other bags.':
            bagsdict[y[0].strip().rstrip('s')] = 0
        else:
            bagsdict[y[0].strip().rstrip('s')] = [[s[2:].strip('s.').strip(),int(s[1])] for s in y[1].split(',')]
    return bagsdict

def iter1(bagdict, bag1, findbag):
    if bagdict[bag1] == 0:
        return 0
    elif findbag in bagdict[bag1]:
        return 1
    else:
        found = []
        for bag in bagdict[bag1]:
            found.append(iter1(bagdict, bag, findbag))
        for j in found:
            if j:
                return j
        return 0

def findcombos(bd,findbag):
    num = 0
    a = set(bd.keys())
    for bag in a:
        b = iter1(bd, bag, findbag)
        num += b
    return num

def count(bd, bag0):
    if bd[bag0] == 0:
        return 0
    l1 = [(count(bd,bag[0]) + 1)*bag[1] for bag in bd[bag0]]
    x = sum(l1)
    return x

def solve(puzzle_input):
    bag1 = 'shiny gold bag'
    bagsdict = readin(puzzle_input)
    qb = readin2(puzzle_input)
    s1 = findcombos(bagsdict,bag1)
    s2 = count(qb,bag1)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)