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

colorlist = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
c1 = [str(c) for c in colorlist]

for i in range(len(inp)):
    validlist.append(True) 
    for t in types:
        if inp[i].find(t) == -1:
            valid -= 1
            validlist[i] = False
            break

for i in range(len(inp)):
    if validlist[i]:

        notfound = True
        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'byr':
                    if int(data1[i][j][1]) > 2002 or int(data1[i][j][1]) < 1920:
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        #print("hi")
                        break
                    
        
        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'iyr':
                    if int(data1[i][j][1]) < 2010 or int(data1[i][j][1]) > 2020:
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        break

        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'eyr':
                    if int(data1[i][j][1]) < 2020 or int(data1[i][j][1]) > 2030:
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        break
                    
        
        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'hgt':
                    measure = -1
                    if data1[i][j][1].find('cm') != -1:
                        if int(data1[i][j][1][:-2]) < 150 or int(data1[i][j][1][:-2]) > 193:
                            valid, validlist[i] = valid - 1, False
                            notfound = False
                            break
                        
                    elif data1[i][j][1].find('in') != -1:
                        if int(data1[i][j][1][:-2]) < 59 or int(data1[i][j][1][:-2]) > 76:
                            valid, validlist[i] = valid - 1, False
                            notfound = False
                            break
                    else: 
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        break
        
        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'hcl':
                    
                    if data1[i][j][1][0] != '#':
                        
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        
                        break
                    
                    else:
                        c = False
                        if len(data1[i][j][1][1:].strip()) != 6:
                            
                            valid, validlist[i] = valid - 1, False
                            notfound = False
                            break
                        for k in range(len(data1[i][j][1][1:].strip())):
                            if not (data1[i][j][1][k+1] in c1):
                                
                                c = True
                                break
                            
                        if c:
                            valid, validlist[i] = valid - 1, False
                            notfound = False
                            break
        
        ec = ['amb', 'blu', 'brn','gry','grn','hzl','oth']

        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'ecl':
                    if not (data1[i][j][1] in ec):
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        break
        
        if notfound:
            for j in range(len(data1[i])):
                if data1[i][j][0] == 'pid':
                    if len(data1[i][j][1].strip()) != 9:
                        valid, validlist[i] = valid - 1, False
                        notfound = False
                        break
                    else:
                        try:
                            int(data1[i][j][1].strip())
                        except:
                            valid, validlist[i] = valid - 1, False
                            notfound = False
                            break


print(valid)
#print(validlist)