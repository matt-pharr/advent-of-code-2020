with open("day03input.txt") as f1:
    inp = f1.read().split()

def findtrees(dx,dy):
    trees = 0

    x=0
    y=0

    while y < len(inp):
        if inp[y][(x)%(len(inp[0]))] == '#':
            trees += 1
            #print("tree!")
        #print(x,x%11,y)
        x+= dx
        y+= dy
        
    
    return trees

#l1 = [findtrees(3,1)]
l1 = [findtrees(1,1), findtrees(3,1), findtrees(5,1), findtrees(7,1), findtrees(1,2)]
p = 1

for e in l1:
    print(e)
    p = p*e

print(p)