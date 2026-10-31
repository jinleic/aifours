#!/usr/bin/env python3
"""Finite rational spot controls, not a global verifier or proof of coverage."""
from fractions import Fraction as R
from itertools import combinations
import json
from pathlib import Path
from random import Random

Z0 = R(410210220392063003, 500000000000000000)
U0 = R(334696976789746519, 250000000000000000)
V0 = R(208405938226799943, 200000000000000000)
r = R(1, 10**16)
rho = R(1, 500)
AA = R(-13352719290130737, 10**15)
BB = R(343503525735997, 50000000000000)

def es(v, k):
    if k == 0: return R(1)
    return sum((prod(c) for c in combinations(v, k)), R(0))

def prod(v):
    z = R(1)
    for x in v: z *= x
    return z

def data(v, z):
    e = [es(v, k) for k in range(8)]
    p = e[1]-4
    q = e[2]-4*e[1]+10-2*z
    W = e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
    E3 = e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
    E2 = e[5]-(1+z)**2*p-(4+4*z)*q
    E1 = e[6]-(1+z)**2*q
    s = v[0]+v[1]
    S4 = sum(v[:4])
    K = E3-S4*W
    alpha = es(v[:4],3)-s*es(v[3:],2)
    B = v[0]*v[1]-s*s
    Z = E1-s*E2
    Y = Z-W*alpha-K*B+W*W/2
    F = Z+AA*W+BB*E3-E3*E3
    lam = AA+alpha+BB*S4-W/2-S4*E3
    mu = BB+B-E3
    return p,q,W,E3,E2,E1,s,K,Y,F,lam,mu

def grad(v,z):
    p,q,W,E3,E2,E1,s,K,Y,F,lam,mu=data(v,z)
    ans=[]
    for i in range(7):
        others=v[:i]+v[i+1:]
        q_i=es(others,1)-4
        w_i=es(others,2)-4*es(others,1)+10-2*z
        e3_i=es(others,3)-(6+2*z)*es(others,1)+20+4*z
        e2_i=es(others,4)-(1+z)**2-(4+4*z)*q_i
        e1_i=es(others,5)-(1+z)**2*q_i
        ans.append(e1_i-(i<2)*E2-s*e2_i+AA*w_i+(BB-2*E3)*e3_i)
    return ans

def phi(v,z,i,j):
    E3=data(v,z)[3]
    s=v[0]+v[1]
    o=[v[k] for k in range(7) if k not in (i,j)]
    c=s*(4+4*z)-(1+z)**2
    return es(o,4)-s*es(o,3)+(BB-2*E3)*es(o,2)+AA*es(o,1)+c-4*AA-(6+2*z)*(BB-2*E3)

vectors=[
 [R(101,100),R(109,100),R(127,100),R(13,10),R(133,100),R(14,10),R(29,20)],
 [R(109,100),R(101,100),R(29,20),R(127,100),R(14,10),R(13,10),R(133,100)],
 [R(1),R(1),R(4,3),R(4,3),R(7,5),R(13,10),R(29,20)],
]
pairs=[(0,1)]+list(combinations(range(2,7),2))
negative_hits=0
for v in vectors:
    g=grad(v,Z0)
    for i,j in pairs:
        rhs=-(v[i]-v[j])*phi(v,Z0,i,j)
        assert g[i]-g[j] == rhs
        if v[i]!=v[j] and g[i]-g[j] != -rhs: negative_hits+=1
    _,_,W,E3,_,_,_,K,Y,F,lam,mu=data(v,Z0)
    assert F == Y+lam*W+mu*K
    if mu*K: assert F != Y+lam*W-mu*K
assert negative_hits>0
print('PASS rational gradient-difference controls:',len(vectors)*len(pairs),'; wrong-sign negative detections:',negative_hits)
print('PASS rational F/Y/lambda/mu identity and flipped-mu negative controls:',len(vectors))

for a,b,c,d in [(R(5,16),R(37,64),R(5,11),R(37,27)), (R(7,16),R(5,8),R(7,9),R(5,3))]:
    assert a/(1-a)==c and b/(1-b)==d
assert R(5,16)/(1-R(5,16)) != R(5,12)
assert Z0-r <= Z0-r and Z0+r+r == Z0+2*r
assert rho-r+r == rho
assert R(3,7) < Z0-r < Z0+2*r < R(83,100)
print('PASS compactification endpoints and rational bridge margins; wrong-map negative detected')

record=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-local-global-local-certificate-v1.json')
cert=json.loads(record.read_text())
margins=[R(s) for s in cert['diagonal_dominance_margins']]
print('RECORDED_MARGINS floor:',[m.numerator//m.denominator for m in margins],'; all>3:',all(x>3 for x in margins))
assert all(x>3 for x in margins)
assert not all(x>1000 for x in margins)
print('PASS recorded margin >3; exaggerated >1000 negative control rejected')

def quantities6(v,z):
    f=[es(v,k) for k in range(7)]
    f1=f[1]
    A=f[2]-4*f1+10-2*z
    B=f[3]-4*f[2]+(10-2*z)*f1+12*z-20
    h1=f[3]-(6+2*z)*f1+20+4*z
    h0=f[4]-(6+2*z)*f[2]+(20+4*z)*f1+3*z*z+6*z-45
    S4=sum(v[:4])
    D=h1-A*S4
    E=h0-B*S4
    Q=A*A-(f1-4)*B
    H=-(h0*A-h1*B)
    assert A*E-B*D == -H
    return f1,A,B,D,E,Q,H

rng=Random(203)
found_nb=None
for k in range(50000):
    v=sorted(R(rng.randint(46,136),100) for _ in range(5))
    f1=sum(v); f2=es(v,2)
    if f1==4: continue
    x=-(f2-4*f1+10-2*Z0)/(f1-4)
    if x<v[-1] or not (R(5,11)<=x<=R(37,27)): continue
    w=v+[x]; f1,A,B,D,E,Q,H=quantities6(w,Z0)
    assert A==0
    if f1>=4 and B>=0:
        found_nb=(k,w,f1,B,Q)
        assert Q<=0
        break
print('NB_BOUNDARY_SEARCH:', 'EXACT_UNCOVERABLE_POINT' if found_nb else 'NO_POINT_FOUND_NOT_EXCLUSION', found_nb)

found_mc=None
for k in range(50000):
    v=sorted(R(rng.randint(78,166),100) for _ in range(5))
    y=sum(v[:4]); a2=es(v[:4],2); a3=es(v[:4],3)
    coef=a2-y*y+4*y-6-2*Z0
    const=a3-y*a2+4*y*y-16*y+20+4*Z0
    if not coef: continue
    beta=-const/coef
    x=beta-v[4]
    if x<v[-1] or not (R(7,9)<=x<=R(5,3)): continue
    w=v+[x]; f1,A,B,D,E,Q,H=quantities6(w,Z0)
    assert D==0
    if f1>=4 and A>0 and H<=0:
        found_mc=(k,w,f1,A,E,H)
        break
print('MC_BOUNDARY_SEARCH:', 'EXACT_UNCOVERABLE_POINT' if found_mc else 'NO_POINT_FOUND_NOT_EXCLUSION', found_mc)
print('END finite exact controls; searches do not certify absence or complete global covers')
