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
    match = 0
    for char in line[2]:
        if char == char1:
            match += 1
    if int(a) <= match and match <= int(b):
        valid += 1 

print(valid)
