# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re

day = '09'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here

def readin(puzzle_input):
    a = [int(x) for x in puzzle_input.splitlines()]
    # print(a)
    return a

def iterate(encryption):
    buffer = 25
    for i in range(buffer,len(encryption)):
        found = False
        considered = encryption[:i][-buffer:]
        # print(considered)
        for j in range(len(considered)):
            for k in range(j,len(considered)):
                if (considered[j] + considered[k]) == encryption[i]:
                    found = True
        if not found:
            return encryption[i]
                
def findset(target,encryption):
    for i in range(len(encryption)):
        for j in range(i,len(encryption)):
            test = encryption[i:j+1]
            sum1 = sum(test)
            if sum1 == target:
                return (min(test) + max(test))
            elif sum1 > target:
                break


def solve(puzzle_input):
    encryption = readin(puzzle_input)
    s1 = iterate(encryption)
    s2 = findset(s1,encryption)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)