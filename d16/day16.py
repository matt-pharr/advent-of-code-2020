# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re

day = '16'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'
inp1 = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'fields.txt'

# Reading function goes here
def readin(puzzle_input):
    input1 = puzzle_input.strip('\n').split('\n\n')
    fields = input1[0]
    ticketsbloc = input1[2]
    myticket = [int(i) for i in input1[1].splitlines()[1].split(',')]

    nums = [int(s) for s in re.split(r'\n|,',ticketsbloc[16:])]
    ticketsblocsplit = ticketsbloc.splitlines()[1:]

    flist = []
    for field in fields.splitlines():
        a = field.split(':')[1].strip()
        params = [s.strip() for s in a.split('or')]
        ranges = [[int(s) for s in a.split('-')] for a in params]
        flist.append( ((ranges[0][0],ranges[0][1]),(ranges[1][0],ranges[1][1] )))

    tickets = [[int(s) for s in a.split(',')] for a in ticketsblocsplit]

    return nums, tickets, flist, myticket

def definefields(flist,tickets):
    badlist = []
    for t1 in tickets:
        goodlist = []
        for t in t1:
            good = False
            for f in flist:
                if f[0][0] <= t <= f[0][1] or f[1][0] <= t <= f[1][1]:
                    good = True
                    break
            goodlist.append(good)
        badlist.append(all(goodlist))

    found = []
    for i in range(len(flist)):
        f = flist[i]
        for k in range(len(tickets[0])):
            bad = False
            for j in range(len(tickets)):
                if badlist[j]:
                    t = tickets[j][k]
                    if f[0][0] <= t <= f[0][1] or f[1][0] <= t <= f[1][1]:
                        pass

                    else:
                        bad = True
                        break

                else:
                    continue

            if not bad:
                found.append((i,k))

    return found

def findbad(flist,ticketfields):
    badlist = []
    for t in ticketfields:
        good = False
        for f in flist:
            if f[0][0] <= t <= f[0][1] or f[1][0] <= t <= f[1][1]:
                good = True
                break
        if not good:
            badlist.append(t)
    return sum(badlist)

def findvalid(validlist):
    validdict = {}
    last = set()
    for i in range(len(validlist)):
        for j in range(len(validlist)):
            if len(validlist[j]) == i+1:
                diff = set(validlist[j]) - last
                for a in diff:
                    validdict[j] = a
                last = set(validlist[j])
                break
    return validdict


def solve(puzzle_input):
    nums, tickets, flist, myticket = readin(puzzle_input)
    compatible = definefields(flist,tickets)
    validlist = []
    for i in range(20):
        ilist = []
        for t in compatible:
            if t[0] == i:
                ilist.append(t[1])
        validlist.append(ilist)
        print(str(i) + ':',ilist)
    validdict = findvalid(validlist)
    
    mult = 1
    for x in [myticket[validdict[i]] for i in range(6)]:
        mult = mult*x

    s1 = findbad(flist,nums)
    s2 = mult
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)
