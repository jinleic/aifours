#!/usr/bin/env python3
"""Integer-only controls for the constructed-tail joint complement obstruction.

Checks the exact F_11 Bezout identity, bounded orders and the finite weighted
cyclic equations. The all-exponent proof and cyclotomic field-degree import
are written separately and are not established by these bounded checks.
"""
import json
from collections import Counter
from itertools import combinations
from math import gcd


def trim(a):
    a = [x % 11 for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % 11
    return trim(c)


H = [1,1,0,0,0,0,0,1,0,0,0,0,0,9,10]
S = [5,4,7,2,2,5,4,9,2,1,10,10,7,10,5,0,10,8,5,1,0,8,7,4,7,1,3,6,2]
T = [6,9,10,9,4,7,9,7,4,10,2]
X32_MINUS_1 = [10] + [0] * 31 + [1]
assert add(mul(S,H),mul(T,X32_MINUS_1)) == [10,0,1]
assert sum(H) % 11 == 0
assert sum(c*((-1)**i) for i,c in enumerate(H)) % 11 == 0

# The all-j order formula follows from the written valuation induction;
# these are finite integer controls only.
orders = {}
for j in range(3, 17):
    expected = 1 << (j-2)
    assert pow(11, expected, 1 << j) == 1
    assert pow(11, expected//2, 1 << j) != 1
    orders[j] = expected


def crt(moduli, residues):
    n = 1
    for m in moduli:
        n *= m
    assert all(gcd(a,b)==1 for a,b in combinations(moduli,2))
    return sum(r*(n//m)*pow(n//m,-1,m) for m,r in zip(moduli,residues)) % n


def base_and_tail(e,K):
    D=1<<K; m=5**(e+1); n=33*D*m; h=n//5
    Y=(0,1,7,13,14)
    f={0:0,1:1,2:13,3:14,7:7}
    q=[]
    for r in range(33):
        g=r if r in Y else (1 if r%3==1 else 0)
        q.append(crt((D,m,33),(g,f.get(r%11,0),r)))
    return n,tuple(q),{(a+j*h)%n for a in q for j in range(5)}


def multiset_pair(phi,z,D):
    left=Counter(((7+phi[(z-7)%D])%11,(2+phi[(z-13)%D])%11,
                  (3+phi[(z-14)%D])%11))
    right=Counter(((7+phi[(z-1)%D])%11,(2+phi[(z-1)%D])%11,
                   (3+phi[z%D])%11))
    return left,right


controls=[]
for e,K in ((2,4),(3,4),(2,5)):
    D=1<<K
    n,base,Q=base_and_tail(e,K)
    w=Counter((q%11,q%D) for q in Q)
    exceptions={}
    for j in range(11):
        for g in range(D):
            assert w[(j,g)]%5==0
            delta=w[(j,g)]//5-(2*int(g==0)+int(g==1))
            if delta:
                exceptions[(j,g)]=delta
    assert exceptions=={(7,1):-1,(7,7):1,(2,1):-1,(2,13):1,
                         (3,0):-1,(3,14):1}
    # The displayed complement has phi=0; direct finite sumset control.
    P={(33*(5**(e+1)*t+D*u))%n for t in range(D) for u in range(5**e)}
    assert len(P)==D*5**e and len(Q)==165
    assert len({(p+q)%n for p in P for q in Q})==n
    assert all(multiset_pair([0]*D,z,D)[0]==multiset_pair([0]*D,z,D)[1] for z in range(D))
    controls.append({'e':e,'K':K,'n':n,'head_size':len(P),'tail_size':len(Q),
                     'exception_entries':len(exceptions)})

# Negative control: anchor-consistent phi(z)=z mod11 at D=16 is not a solution.
phi=[z%11 for z in range(16)]
assert (phi[0],phi[3],phi[8],phi[11])==(0,3,8,0)
left,right=multiset_pair(phi,0,16)
assert sorted(left.elements())==[5,5,5]
assert sorted(right.elements())==[0,3,6]
assert left != right

print(json.dumps({'result':'PASS','bezout_F11':'S*H+T*(X^32-1)=X^2-1',
                  'bounded_11_orders':orders,'constructed_tail_controls':controls,
                  'anchor_consistent_nonperiodic_phi_negative_control':
                    {'left_z0':sorted(left.elements()),'right_z0':sorted(right.elements())},
                  'scope':'finite identities and controls only; universal proof is written'},
                 indent=1,sort_keys=True))
