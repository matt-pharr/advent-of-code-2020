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
    vi = []
    ei = []
    terms = []
    nt = 1
    for pair in l1:
        a.append(pair[0] % pair[1])
        n.append(pair[1])
    
    for ni in n:
        nt = nt*ni
    nh = [nt//ni for ni in n]
    # print(nt)
    for i in range(len(n)):
        vi.append(euclidalg(n[i],nh[i])[1])
        ei.append( (vi[i]*nh[i]) )
        terms.append(a[i]*ei[i])
    # print(nh)
    # print(a)
    # print(vi)
    return sum(terms) % nt

l1 = [(0,17),(-2,13),(-3,19)]
x = crt(l1)
print(x)

# print(euclidalg(3,35)[1]%3) 