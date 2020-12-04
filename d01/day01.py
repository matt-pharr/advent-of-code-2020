day = '01'
inp = 'day' + day + 'input.txt'

def lines(puzzle_input: str) -> list:
    return [int(p.strip()) for p in puzzle_input.splitlines()]

def findtwo2020(ints: list) -> tuple:
    for i in range(len(ints)):
        for j in range(i,len(ints)):
            if ints[i] + ints[j] == 2020:
                return (i,j)

def findthree2020(ints: list) -> tuple:
    for i in range(len(ints)):
        for j in range(i,len(ints)):
            for k in range(j,len(ints)):
                if ints[i] + ints[j] + ints[k] == 2020:
                    return (i,j,k)

def solve(puzzle_input: str):
    ints = lines(puzzle_input)
    i0,j0 = findtwo2020(ints)
    i1,j1,k1 = findthree2020(ints)

    s1 = ints[i0]*ints[j0]
    s2 = ints[i1]*ints[j1]*ints[k1]
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as inputfile:
        for s in solve(inputfile.read()):
            print(s)