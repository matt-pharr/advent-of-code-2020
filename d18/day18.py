# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re
import pyparsing
import copy

day = '18'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    a = puzzle_input.splitlines()
    data = []
    find = pyparsing.Word(pyparsing.nums) | '+' | '*'
    parengroup = pyparsing.nestedExpr( '(', ')', content=find)

    for line in a:
        data.append(parengroup.parseString('(' + line + ')').asList())
    
    return data

def evaluate(nested_eq, new = False):
    if not new:
        inpeq = nested_eq
    else:
        inpeq = evalpatch(nested_eq)
    
    if type(inpeq[0]) is str:
        v = int(inpeq[0])
    elif type(inpeq[0]) is list:
        v = evaluate(inpeq[0],new)
    else:
        print("TYPE ERROR")

    mode = 0 #mode = 0: no mode. 1: add. 2: multiply. 
    for i in range(1,len(inpeq)):
        if inpeq[i] == '+':
            mode = 1
            continue
        elif inpeq[i] == '*':
            mode = 2
            continue
        else:
            if type(inpeq[i]) is str:
                if mode == 0:
                    print("ERROR")
                    break
                elif mode == 1: 
                    v = v + int(inpeq[i])
                    mode = 0
                    continue
                elif mode == 2:
                    v = v * int(inpeq[i])
                    mode = 0
                    continue
            elif type(inpeq[i]) is list:
                posval = evaluate(inpeq[i],new)
                if mode == 0:
                    print("ERROR")
                    break
                elif mode == 1: 
                    v = v + posval
                    mode = 0
                    continue
                elif mode == 2:
                    v = v * posval
                    mode = 0
                    continue

    return v 

def evalpatch(eqn):
    # adds functional parenths around multiplication operations
    found = False
    neweqn = []
    try:
        m_ind = eqn.index('+')
        found = True
        badspots = [m_ind, m_ind - 1, m_ind + 1]
    except:
        return eqn
    
    for i in range(len(eqn)):
        if i < m_ind - 1:
            neweqn.append(eqn[i])
        elif i == m_ind - 1:
            neweqn.append([ eqn[i], eqn[i+1], eqn[i+2] ])
        elif i > m_ind + 1:
            neweqn.append(eqn[i])
    temp = evalpatch(neweqn)
    if len(temp) == 1:
        return temp[0]
    else:
        return temp

def solve(puzzle_input):
    data = readin(puzzle_input)
    sums0 = []
    sums1 = []
    for eqn in data:
        a = evaluate(eqn)
        b = evaluate(eqn,True)
        sums0.append(a)
        sums1.append(b)
    s1 = sum(sums0)
    s2 = sum(sums1)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)