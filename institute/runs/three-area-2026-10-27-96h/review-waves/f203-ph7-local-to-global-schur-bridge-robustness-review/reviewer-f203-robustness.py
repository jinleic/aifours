#!/usr/bin/env python3
"""Small rational identities and explicitly intended robustness negatives."""
from fractions import Fraction as Q
from itertools import combinations

def product(a):
    x=Q(1)
    for y in a: x*=y
    return x

def es(v,k): return sum((product(c) for c in combinations(v,k)),Q(0))

def values(v,z,x):
    f=[es(v,k) for k in range(7)]
    f1=f[1]
    A=f[2]-4*f1+10-2*z
    B=f[3]-4*f[2]+(10-2*z)*f1+12*z-20
    h1=f[3]-(6+2*z)*f1+20+4*z
    h0=f[4]-(6+2*z)*f[2]+(20+4*z)*f1+3*z*z+6*z-45
    W=A*x+B
    E3=h0+h1*x
    full=v+[x]
    e=[es(full,k) for k in range(8)]
    p=e[1]-4
    q=e[2]-4*e[1]+10-2*z
    E2=e[5]-(1+z)**2*p-(4+4*z)*q
    s3=sum(v[:3])
    L4=sum(v[3:])+x
    Y2=E2-W*es(v[:4],2)-s3*(E3-W*L4)
    g=product(v[:3])-W
    Y0=e[7]-W*es(v[:4],4)+W*W*x/2-g*(E3-W*L4)
    return A,Y0,Y2

samples=[
 [Q(1,2),Q(3,4),Q(1),Q(1),Q(5,4),Q(4,3)],
 [Q(4,5),Q(9,10),Q(1),Q(11,10),Q(6,5),Q(13,10)],
 [Q(1),Q(1),Q(4,3),Q(4,3),Q(4,3),Q(4,3)],
]
z=Q(41,50)
for v in samples:
    got=[values(v,z,Q(i)) for i in range(5)]
    A=got[0][0]
    ys=[t[1] for t in got]
    third=ys[3]-3*ys[2]+3*ys[1]-ys[0]
    assert third==-3*A*A
    assert ys[4]-3*ys[3]+3*ys[2]-ys[1]==third
    quad=[t[2] for t in got]
    assert (quad[2]-2*quad[1]+quad[0])/2==sum(v[:3])*A
    if A: assert third!=3*A*A
print('PASS exact cubic and concave-quadratic leading controls; reversed-cubic sign rejected')

for w in ([Q(1),Q(1),Q(1),Q(1)],[Q(1,2),Q(3,4),Q(5,4),Q(2)]):
    y=sum(w); a2=es(w,2); a3=es(w,3)
    assert a2<=Q(3,8)*y*y and a3<=y*a2/6
assert es([Q(1)]*4,3)>sum([Q(1)]*4)*es([Q(1)]*4,2)/7
print('PASS four-rate elementary bounds; wrong 1/7 constant rejected at equality')

# Exact model of round-to-nearest near 1, no floating evaluation used.
L=Q(1)-Q(1,2**55)
x=Q(1)-Q(1,2**56)
prev=Q(1)-Q(1,2**53)
assert L-prev>Q(1)-L  # binary64 nearest is 1, not prev
assert L<x<1
exact_floor=(1024*L).numerator//(1024*L).denominator
assert Q(exact_floor,1024)==Q(1023,1024)
assert Q(1)>x
print('PASS intended floor negative: rounded-up anchor 1 exceeds admissible x; exact floor is 1023/1024')

# On the local cell s in [1/2,1], Bernstein coefficients (0,1)
# yield P=0 at s=1/2, an interior point of the global unit cube.
local_t=Q(0)
global_s=Q(1,2)+local_t/2
assert 0<global_s<1 and local_t==0
# Reversed midpoints alone do not prove disjointness from sorted spectra.
lo1,hi1,lo2,hi2=Q(1),Q(4),Q(0),Q(3)
assert (lo1+hi1)/2>(lo2+hi2)/2 and lo1<=2<=hi1 and lo2<=2<=hi2
assert not(lo1>hi2)
print('PASS intended Bernstein-face and reversed-midpoint negatives')
print('END bounded exact robustness controls; no global leaf tree checked')
