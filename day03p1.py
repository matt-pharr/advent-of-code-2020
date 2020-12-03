with open("day03input.txt") as f1:
    inp = f1.read().split()

trees = 0

x=0
y=0

while y < len(inp):
    if inp[y][x%(len(inp[y])-1)] == '#':
        trees += 1
    x+= 3
    y+= 1

print(trees)
    