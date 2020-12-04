day = '02'
inp = 'day' + day + 'input.txt'

# Reading function goes here

def readtodict(infile: str) -> list:
    l1 = infile.splitlines()
    l2 = [l.split() for l in l1]

    endl = []
    for l in l2:
        indict = {}
        indict['bound'] = [int(s) for s in l[0].split('-')]
        indict['char'] = l[1].strip(':')
        indict['pass'] = l[2].strip()
        endl.append(indict)

    return endl

def check1(l1: list) -> list:
    validlist = []
    for l in l1:
        range = l['bound']
        x = l['pass'].count(l['char'])
        if range[0] <= x <= range[1]:
            validlist.append(True)
        else:
            validlist.append(False)
    
    return validlist

def check2(l1: list) -> list:
    validlist = []
    for l in l1:
        range = l['bound']
        x0 = l['pass'][range[0]-1]
        x1 = l['pass'][range[1]-1]
        if (x1 != x0) and (l['char'] == x0 or l['char'] == x1):
            validlist.append(True)
        else:
            validlist.append(False)
    
    return validlist


def solve(puzzle_input):
    endl = readtodict(puzzle_input)
    gl1 = check1(endl)
    gl2 = check2(endl)

    s1 = sum(gl1)
    s2 = sum(gl2)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as inputfile:
        for s in solve(inputfile.read()):
            print(s)