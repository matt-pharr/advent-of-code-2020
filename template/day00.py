day = '00'
inp = 'day' + day + 'input.txt'

# Reading function goes here



def solve(puzzle_input):
    s1 = 0
    s2 = 0
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)