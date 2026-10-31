"""Independent f241 arithmetic controls. Standard-library exact integers/Fraction only.
Does not import or execute author code; bounded examples are not the universal proof.
"""
from fractions import Fraction
from itertools import product
from functools import lru_cache
from math import gcd

def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a

def divmod_poly(a,b):
    a=[Fraction(v) for v in trim(a)];b=[Fraction(v) for v in trim(b)]
    if not b:raise ZeroDivisionError
    q=[Fraction(0)]*max(0,len(a)-len(b)+1)
    while a and len(a)>=len(b):
        d=len(a)-len(b);c=a[-1]/b[-1];q[d]+=c
        for j,v in enumerate(b):a[d+j]-=c*v
        a=trim(a)
    return trim(q),a

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def monic(a):
    a=trim(a)
    return [x/a[-1] for x in a] if a else []

def pgcd(a,b):
    while trim(b):a,b=b,divmod_poly(a,b)[1]
    return monic(a)

@lru_cache(None)
def cyclo(n):
    a=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            a,r=divmod_poly(a,cyclo(d));assert not r
    assert all(v.denominator==1 for v in a)
    return tuple(int(v) for v in a)

def rem75(a):
    v=[0]*75
    for i,x in enumerate(a):v[i%75]+=x
    return v

F=[0]*15
for e in (0,1,7,13,14):F[e]+=1
assert cyclo(3)==(1,1,1) and cyclo(5)==(1,1,1,1,1)
assert cyclo(15)==(1,-1,0,1,-1,1,0,-1,1)
assert divmod_poly(F,cyclo(3))[1]==[0,2]
assert not divmod_poly(F,cyclo(5))[1]
assert divmod_poly(F,cyclo(15))[1]==[3,0,-1,1,-2,1,1,-1]
assert len(cyclo(25))-1==20 and len(cyclo(75))-1==40
x75=[-1]+[0]*74+[1]
assert pgcd(F,x75)==list(cyclo(5))
H=[int(i%5==0) for i in range(71)];G=[1]*75
assert rem75(mul(H,F))==G
C=[2,1,0,3,4];K=mul(H,C)
assert len(K)<=75 and all(K[r]==C[r%5] for r in range(75))
assert rem75(mul(K,F))==[sum(C)]*75
print('PASS exact cyclotomic divisors/remainders, gcd(F,x^75-1)=Phi5, H*F=G mod x^75-1, arbitrary multiplicity vector')

Fbad=F.copy();Fbad[14]-=1
if len(Fbad)<=15:Fbad.extend([0]*(16-len(Fbad)))
Fbad[15]+=1
assert divmod_poly(Fbad,cyclo(5))[1] and rem75(mul(H,Fbad))!=G
print('PASS intended negative: replacing tail exponent14 by15 destroys Phi5 divisibility and H*F=G')

Y=(0,1,7,13,14);A=(0,3,8,11);cases=0
for R,D,mode in product((2,3,5,7,11,13,33),(1,2,4),('anchors','shifts')):
    n=75*R*D
    starts={y:(y-75*(y%R) if mode=='anchors' else y+75*((y+2)*(R+3)-3*n)) for y in Y}
    Q={(starts[y]+75*t)%n for y in Y for t in range(R)}
    P={(5*j+75*R*k)%n for j in range(15) for k in range(D)}
    assert len(Q)==5*R and len(P)==15*D
    sums=[(p+q)%n for p in P for q in Q]
    assert len(sums)==n and len(set(sums))==n
    B={(p+starts[y])%n for p in P for y in Y}
    assert len(B)==5*len(P)
    for r in range(75):
        Br={h for h in range(R*D) if (r+75*h)%n in B}
        assert len(Br)==D
        assert all(((h in Br)==((h-R)%(R*D) in Br)) for h in range(R*D))
        assert all(sum((x-t)%(R*D) in Br for t in range(R))==1 for x in range(R*D))
    assert set(P).intersection(A)=={0}
    if mode=='anchors':assert set(Y).issubset(Q)
    cases+=1
print('PASS',cases,'direct tilings P0+Q including wrapped and independently shifted starts; 75 fibre periods; anchor-free countercontrols')

R,D=3,2;bad={1,3};L=R*D
assert any(((x in bad)!=((x-R)%L in bad)) for x in range(L))
assert any(sum((x-t)%L in bad for t in range(R))!=1 for x in range(L))
print('PASS intended negative: nonperiodic fibre fails unit-window direct tiling')

for R in range(2,151):
    for a in (-9,-1,0,1,7):
        delta=-5+75*a
        assert ((15*delta)%(75*R)==0)==(delta%(5*R)==0)
        assert (delta%(5*R)==0)==((-1+15*a)%R==0)
        if gcd(R,15)>1:assert (-1+15*a)%R!=0
    if gcd(R,5)==1:
        assert all((25*t)%R!=0 or t%R==0 for t in range(R))
    assert gcd(3,11)==1
print('PASS exact cycle-divisibility directions and gcd controls for R=2..150; bounded controls only')
print('LIMIT: no author code, no external theorem, no solver, no all-parameter conclusion from these checks')
