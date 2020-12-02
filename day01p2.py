
inp = []

with open("day01input.txt") as f1:
    for line in f1:
        inp.append(int(line))

for i in range(len(inp)):
    for j in range(i,len(inp)):
        for k in range(j,len(inp)):
            if inp[i] + inp[j] + inp[k] == 2020:
                pos = (i,j,k)

print(inp[pos[0]]*inp[pos[1]]*inp[pos[2]])