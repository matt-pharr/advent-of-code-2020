lines = []
splitlines = []

with open("day02input.txt") as day02:
    for line in day02:
        lines.append(line)

for line in lines:
    splitlines.append(line.split())

valid = 0

for line in splitlines:
    a,b = line[0].split('-')
    char1 = line[1][0]
    if (line[2][int(a)-1] == char1 or line[2][int(b)-1] == char1) and line[2][int(a)-1] != line[2][int(b)-1]:
        valid += 1
    

print(valid)
