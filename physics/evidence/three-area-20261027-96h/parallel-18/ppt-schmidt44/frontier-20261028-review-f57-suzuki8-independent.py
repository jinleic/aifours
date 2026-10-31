#!/usr/bin/env python3
"""Independent bounded GF(8) Sz(8) matrix and normalizer count.

Implements the cited source's matrices, not an imported classification. The
finite check is not a proof of all-q maximal subgroup completeness or Sun5.
"""
from collections import deque
import json


def gf_mult(a,b):
    out=0
    while b:
        if b&1: out ^= a
        a <<= 1
        if a&8: a ^= 0b1011
        b >>= 1
    return out

TBL=[[gf_mult(a,b) for b in range(8)] for a in range(8)]

def pow8(a,n):
    if n<0: n%=7
    out=1
    for _ in range(n): out=TBL[out][a]
    return out

def mm(a,b):
    return tuple(TBL[a[4*i]][b[j]] ^ TBL[a[4*i+1]][b[4+j]] ^
                 TBL[a[4*i+2]][b[8+j]] ^ TBL[a[4*i+3]][b[12+j]]
                 for i in range(4) for j in range(4))

IDENTITY=(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1)

def smat(a,b):
    ap=pow8(a,4); bp=pow8(b,4)
    return (1,0,0,0, a,1,0,0, b,ap,1,0,
            TBL[pow8(a,2)][ap]^TBL[a][b]^bp,TBL[a][ap]^b,a,1)

def mdiag(lam):
    return (pow8(lam,3),0,0,0, 0,pow8(lam,2),0,0,
            0,0,pow8(lam,-2),0, 0,0,0,pow8(lam,-3))

REV=(0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0)
GENS=(smat(1,0),smat(2,0),smat(0,1),mdiag(2),REV)


def inverse_by_order(g):
    x=IDENTITY
    for _ in range(1,100):
        nxt=mm(x,g)
        if nxt==IDENTITY: return x
        x=nxt
    raise AssertionError('generator order bound exceeded')


def main():
    seen={IDENTITY}; todo=deque([IDENTITY])
    while todo:
        x=todo.popleft()
        for g in GENS:
            y=mm(x,g)
            if y not in seen:
                seen.add(y); todo.append(y)
                if len(seen)>30000: raise AssertionError('group cap exceeded')
    roots=frozenset(smat(a,b) for a in range(8) for b in range(8))
    if len(roots)!=64 or any(mm(a,b) not in roots for a in roots for b in roots):
        raise AssertionError('root subgroup failure')
    if not roots.issubset(seen): raise AssertionError('root subgroup not in generated group')
    inverses=[inverse_by_order(g) for g in GENS]
    if any(mm(g,gi)!=IDENTITY or mm(gi,g)!=IDENTITY for g,gi in zip(GENS,inverses)):
        raise AssertionError('generator inverse failure')
    orbit={roots}; queue=deque([roots])
    while queue:
        subgroup=queue.popleft()
        for g,gi in zip(GENS,inverses):
            conjugate=frozenset(mm(gi,mm(x,g)) for x in subgroup)
            if conjugate not in orbit:
                orbit.add(conjugate); queue.append(conjugate)
                if len(orbit)>100: raise AssertionError('orbit cap exceeded')
    diag=GENS[3]; dinv=inverses[3]
    if frozenset(mm(dinv,mm(x,diag)) for x in roots)!=roots:
        raise AssertionError('diagonal does not normalize roots')
    complements=[mdiag(a) for a in range(1,8)]
    B={mm(x,h) for x in roots for h in complements}
    if not B.issubset(seen): raise AssertionError('normalizer candidate not contained')
    if len(seen)%len(orbit): raise AssertionError('nonintegral orbit-stabilizer')
    normalizer=len(seen)//len(orbit)
    if len(B)!=normalizer: raise AssertionError('candidate size not normalizer size')
    print(json.dumps({'GF8':'x^3+x+1','generators':len(GENS),'group_order':len(seen),
                      'root_subgroup':len(roots),'root_conjugacy_orbit':len(orbit),
                      'normalizer_by_orbit_stabilizer':normalizer,'explicit_FH_size':len(B),
                      'limits':'one source-defined q=8 model; no all-q maximality classification or Sun5 proof'},indent=2))


if __name__=='__main__': main()
