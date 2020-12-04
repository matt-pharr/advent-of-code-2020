day = '03'
inp = 'day' + day + 'input.txt'

# Reading function goes here
def landscaperead(infile: str) -> list:
    l1 = infile.strip().splitlines()
    return l1

def counttrees(l1: list, dx: int, dy: int) -> int:
    count = 0
    x = 0
    for y in range(0,len(l1),dy):
        if l1[y][x % len(l1[y])] == '#':
            count += 1
        x += dx
    return count

def product(l: list) -> int:
    a = 1
    for m in l:
        a = a*m
    return a

def solve(puzzle_input):
    l1 = landscaperead(puzzle_input)
    s1 = counttrees(l1,3,1)
    s2 = product([counttrees(l1,1,1), counttrees(l1,3,1), counttrees(l1,5,1), counttrees(l1,7,1), 
        counttrees(l1,1,2)])
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)