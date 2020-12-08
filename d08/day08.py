# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re

day = '08'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here

def readin(puzzle_input):
    a = puzzle_input.splitlines()
    b = [[x.split()[0].strip(), int(x.split()[1].strip())] for x in a]
    # print(b)
    return b

def executefix(code):
    flip={'jmp':'nop','nop':'jmp','acc':'acc'}

    for j in range(len(code)):
        # print(j)
        acc = 0
        i = 0
        executed = []
        loop  = True
        #print(code[296])
        while True:
            if i == (len(code)-1):
                loop = False
                break
            switched = False
            dir = code[i][0]
            num = code[i][1]
            if i == j:
                dir = flip[dir]

            # print(dir,num)
            # print(executed)
            # print('i = ', i,'/',len(code), (dir, num))

            if not (i in executed):
                executed.append(i)
            else:
                break

            if dir == 'acc':
                acc += num
                i += 1
            elif dir == 'jmp':
                i += num
            elif dir == 'nop':
                i += 1
            else:
                print("ERROR")
        if not loop:
            print("no loop!")
            break
    # print(loop)
    return acc

def execute(code):
    acc = 0
    i = 0
    executed = []

    
    while True:
        dir = code[i][0]
        num = code[i][1]
        # print(dir,num)
        # print(executed)
        # print('i,', i)

        if not (i in executed):
            executed.append(i)
        else:
            break

        if dir == 'acc':
            acc += num
            i += 1
        elif dir == 'jmp':
            i += num
        elif dir == 'nop':
            i += 1
        else:
            print("ERROR")
        
    return acc


def solve(puzzle_input):
    code = readin(puzzle_input)
    s1 = execute(code)
    s2 = executefix(code)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)