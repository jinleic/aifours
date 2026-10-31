from itertools import permutations,product
G=list(permutations(range(3)));one=(0,1,2);swap=(1,0,2);cycle=(1,2,0);other=(0,2,1)
def comp(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
rho=(0,0,1);kap=(0,0,1,1);jl=(0,1,0);kl=(0,1,0,1)
a=(one,swap,cycle);b=(one,other,cycle,swap)
P0=((one,swap),(cycle,other))
P1=tuple(tuple(comp(comp(b[l],P0[kap[l]][rho[i]]),a[i]) for i in range(3)) for l in range(4))
D1=list(product(range(3),G,range(4)));D0=list(product(range(2),G,range(2)))
def dm(P,x,y):
 i,g,l=x;j,h,m=y;return i,comp(comp(g,P[l][j]),h),m
def h(x):
 i,g,l=x;return rho[i],comp(comp(a[i],g),b[l]),kap[l]
def idem(P,x):return dm(P,x,x)==x
assert len(D1)==72 and len(D0)==24 and set(map(h,D1))==set(D0)
assert all(h(dm(P1,x,y))==dm(P0,h(x),h(y)) for x,y in product(D1,repeat=2))
assert all(idem(P1,x)==idem(P0,h(x)) for x in D1)
# B is the Boolean semilattice on three points; S3 permutes the atoms.
def action(g,mask):return sum(1<<g[i] for i in range(3) if mask&(1<<i))
H1=list(product(range(8),D1))
def phi(x):
 c,(i,g,l)=x
 return (jl[i],kl[l],action(a[i],c)),h(x[1])
def hmul1(x,y):
 c,(i,g,l)=x;c2,(j,h0,m)=y
 return c&action(comp(g,P1[l][j]),c2),dm(P1,x[1],y[1])
def hmul0(x,y):
 (j,k,c),(i,g,l)=x;(j2,k2,c2),(i2,h0,m)=y
 return (j,k2,c&action(comp(g,P0[l][i2]),c2)),dm(P0,x[1],y[1])
assert len(H1)==576 and len(set(map(phi,H1)))==len(H1)
assert all(phi(hmul1(x,y))==hmul0(phi(x),phi(y)) for x,y in product(H1,repeat=2))
assert any(action(a[i],c)!=c for c,(i,g,l) in H1)
print('PASS actor 72→24 onto/pure, all 5184 actor products, noncommuting S3 row/column gauges')
print('PASS whole host 576→768, injective and all 331776 physical products, 2×2 rectangular factor')
