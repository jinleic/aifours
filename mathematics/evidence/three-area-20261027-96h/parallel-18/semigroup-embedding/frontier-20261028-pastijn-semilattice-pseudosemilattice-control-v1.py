from itertools import product

B=range(4)  # Boolean diamond, bitwise meet
D=list(product(range(2), repeat=3))

def act(g,b):
    return b if g == 0 else ((b & 1) << 1) | ((b & 2) >> 1)

def dm(d,f):
    i,g,lam=d; j,h,mu=f
    return i, g ^ (lam & j) ^ h, mu

def mul(x,y):
    b,(i,g,lam)=x; c,(j,h,mu)=y
    return b & act(g ^ (lam & j),c), dm(x[1],y[1])

H=list(product(B,D))
E=[x for x in H if mul(x,x)==x]
assert len(H)==32 and len(E)==16

def wedge(x,y):
    b,(i,g,lam)=x; c,(j,h,mu)=y
    return b & act((mu & i) ^ (mu & j),c), (i,mu & i,mu)

def lower(x,y):
    return mul(x,y)==x and mul(y,x)==x

for x,y in product(E,repeat=2):
    w=wedge(x,y)
    assert w in E and mul(x,w)==w and mul(w,y)==w
    cand=[z for z in E if mul(x,z)==z and mul(z,y)==z]
    assert all(lower(z,w) for z in cand)
    assert (wedge(x,y)==wedge(y,x)) == (x[1][0]==y[1][0] and x[1][2]==y[1][2])
for i,lam in product(range(2),repeat=2):
    cell=[x for x in E if x[1][0]==i and x[1][2]==lam]
    assert len(cell)==4
    assert all(wedge(x,y)==wedge(y,x) for x,y in product(cell,repeat=2))
    assert all(wedge(wedge(x,y),z)==wedge(x,wedge(y,z)) for x,y,z in product(cell,repeat=3))
print('H=32 E=16; 256 wedge formulas meet the greatest-sandwich criterion')
print('4 cells of 4; each a semilattice; wedge commutation iff same cell')
