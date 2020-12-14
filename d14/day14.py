# Matthew Pharr
# Advent of Code 2020
# Rensselaer Polytechnic Institute
import os 
import re

day = '14'
inp = os.path.dirname(os.path.realpath(__file__)) + '/day' + day + 'input.txt'

# Reading function goes here
def readin(puzzle_input):
    preproc = puzzle_input.splitlines()
    instr = []

    for i in range(len(preproc)):
        if re.match("mask",preproc[i]) is not None:
            instr.append( ( 0, preproc[i][7:] ) )
        else:
            instr.append( (1, ( int(preproc[i].split('[')[1].split(']')[0]), int(preproc[i].split('=')[1].strip()) ) ) )
    
    return tuple(instr)

def dectobin(dec):
    return int(bin(dec).replace('0b',''))

def bintodec(bin): 
    dec = 0
    i = 0
    n = 0
    while(bin != 0): 
        decval = bin % 10
        dec = dec + decval*(2**i) 
        bin = bin//10
        i += 1
    return dec

def maskrep(dec,mask):
    bin = str(dectobin(dec))
    maskedbin = ""
    for i in range(1,len(mask)+1):
        if mask[-i] == 'X':
            if i <= len(bin):
                maskedbin += bin[-i]
            else:
                maskedbin += '0'
        else:
            maskedbin += mask[-i]
    return int(maskedbin[::-1])

def maskrep2(dec,mask):
    bin = str(dectobin(dec))
    maskedbin = ""
    for i in range(1,len(mask)+1):
        if mask[-i] == 'X' or mask[-i] == '1':
            maskedbin += mask[-i]
        else:
            if i <= len(bin):
                maskedbin += bin[-i]
            else:
                maskedbin += '0'
            
    return maskedbin[::-1]

def ftlrecur(floatbit,i):
    a = list(floatbit)
    l1 = []
    broken = False
    for j in range(i,len(a)):
        if a[j] == 'X':
            a0 = a.copy()
            a0[j] = '0'
            a1 = a.copy()
            a1[j] = '1'
            a0s = "".join(a0)
            a1s = "".join(a1)
            zs = ftlrecur(a0s, j)
            os = ftlrecur(a1s, j)
            for z in zs:
                l1.append(z)
            for o in os:
                l1.append(o)
            broken = True
            break
    if not broken:
        l1.append(floatbit)
    return l1
            
def floattolist(floatbit):
    return ftlrecur(floatbit,0)


def part1followinst(instructions):
    mem = {}
    for inst in instructions:
        if inst[0] == 0:
            mask = inst[1]
        elif inst[0] == 1:
            addr = inst[1][0]
            decval = inst[1][1]
            masked = maskrep(decval,mask)
            mem[addr] = bintodec(masked)
    return sum(mem.values())

def part2followinst(instructions):
    mem = {}
    for inst in instructions:
        if inst[0] == 0:
            mask = inst[1]
        elif inst[0] == 1:
            addr0 = inst[1][0]
            val = inst[1][1]
            maskedaddr = maskrep2(addr0,mask)
            addrlist = floattolist(maskedaddr)
            addrs = [ bintodec(int(a)) for a in addrlist ]
            for addr in addrs:
                mem[addr] = val
    return sum(mem.values())

def solve(puzzle_input):
    instr = readin(puzzle_input)
    s1 = part1followinst(instr)
    s2 = part2followinst(instr)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)