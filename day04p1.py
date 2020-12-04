with open("day04input.txt") as f1:
    inp = f1.read().split("\n\n")

data = [p.split() for p in inp]
data1 = []
for d in data:
    data1.append([e.split(':') for e in d])
#print(data)

types = ["byr", "iyr", "eyr","hgt","hcl","ecl", "pid"]

valid = 0
for d in data:
    if len(d)>0:
        valid +=1
validlist = []

for i in range(len(inp)):
    validlist.append(True) 
    for t in types:
        if inp[i].find(t) == -1:
            valid -= 1
            validlist[i] = False
            break

print(valid)
