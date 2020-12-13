# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re

day = '13'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    a = puzzle_input.splitlines()
    time = int(a[0])
    l = []
    for x in a[1].split(','):
        if re.match('\d',x) is not None:
            l.append(int(x))

    return (time,tuple(l),tuple(a[1].split(',')))

def finddeparttime(time,buslist):
    percent = [time%x for x in buslist]
    waittimes = []
    for i in range(len(percent)):
        waittimes.append(buslist[i] - percent[i])

    minwaittime = min(waittimes)
    i = waittimes.index(minwaittime)
    id = buslist[i]
    # print(time)
    # print(buslist)
    # print(percent)
    # print(waittimes)
    # print(i)
    # print(buslist[i])
    # print(minwaittime)
    return minwaittime*id

def euclidrecur(r,s,t):
    rnew = r[1]%r[0]
    q = (r[1]-(r[1]%r[0]))/r[0]
    snew = s[1] - q*s[0]
    tnew = t[1] - q*t[0]

    if rnew == 0:
        return (r[0],s[0],t[0])
    else:
        return euclidrecur((rnew,r[0]),(snew,s[0]),(tnew,t[0]))

def euclidalg(u,v):
    # find integers x,y such that xu+yv = 1 when u and v are coprime.
    a = max((u,v))
    b = min((u,v))
    r0 = (b,a) # (r1, r0)
    s0 = (0,1)
    t0 = (1,0)
    return euclidrecur(r0,s0,t0)

def crt(l1):
    a = []
    n = []
    M = []
    terms = []
    nt = 1
    for pair in l1:
        a.append(pair[0] % pair[1])
        n.append(pair[1])
    
    for ni in n:
        nt = nt*ni                         # final product
    nh = [nt//ni for ni in n]
    # print(nt)
    for i in range(len(n)):
        M.append(euclidalg(n[i],nh[i])[1]) # get multiplicative inverses
        terms.append(a[i]*M[i]*nh[i])     # sum list
    # print(nh)
    # print(a)
    # print(vi)
    return int(sum(terms) % nt)

def findsubseqtimes(buslist,oglist):
    l1 = [(-1*oglist.index(str(b)),b) for b in buslist]
    return crt(l1)

def solve(puzzle_input):
    time, buslist,oglist = readin(puzzle_input)
    s1 = finddeparttime(time,buslist)
    s2 = findsubseqtimes(buslist,oglist)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)