
inp = []

with open("day01input.txt") as f1:
    for line in f1:
        inp.append(int(line))

for i in range(len(inp)):
    for j in range(i,len(inp)):
        if inp[i] + inp[j] == 2020:
            pos = (i,j)

print(inp[pos[0]]*inp[pos[1]])