"""Planted satisfiable variant; full C(12,6) search at relaxed bound 44."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from itertools import combinations
import numpy as np
from radius6_hypergraph import build


def main():
    domain=list(range(12))
    planted=(0,1,2,3,4,5)
    f=[(x&1)^(((x>>1)&1)&((x>>2)&1))^(((x>>3)&1)&((x>>4)&1))^(((x>>5)&1)&((x>>6)&1))^(((x>>7)&1)&((x>>8)&1)) for x in range(512)]
    g=f.copy()
    for x in planted:
        g[x]^=1
    H=np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int32)
    W=H@(1-2*np.array(g,dtype=np.int32))
    bound=int(max(abs(W)))
    assert bound==44
    _,bad,fourths=build(g,bound=bound)
    dmask=sum(1<<x for x in domain)
    for x,y,z in combinations(domain,3):
        observed=fourths(bad[x]&bad[y]&bad[z],dmask)
        expected=sum(1<<u for u in domain if not (bad[x]&bad[y]&bad[z]&bad[u]))
        assert observed==expected
    anchors=[a for a in combinations(domain,4) if (a[0]^a[1]^a[2]^a[3]) and not (bad[a[0]]&bad[a[1]]&bad[a[2]]&bad[a[3]])]
    candidates=set()
    for anchor in anchors:
        extras=[]
        for x in domain:
            if x not in anchor and all(not (bad[a]&bad[b]&bad[c]&bad[x]) for a,b,c in combinations(anchor,3)):
                extras.append(x)
        for x,y in combinations(extras,2):
            if all(not (bad[a]&bad[b]&bad[x]&bad[y]) for a,b in combinations(anchor,2)):
                candidates.add(tuple(sorted(anchor+(x,y))))
    expected_candidates=set()
    direct_targets=set()
    for points in combinations(domain,6):
        if all(not (bad[a]&bad[b]&bad[c]&bad[d]) for a,b,c,d in combinations(points,4)):
            expected_candidates.add(points)
        h=np.array(g,dtype=np.int32)
        for x in points:
            h[x]^=1
        wh=H@(1-2*h)
        if int(max(abs(wh)))<=bound and np.any(wh==0):
            direct_targets.add(points)
    assert candidates==expected_candidates
    assert planted in direct_targets<=candidates
    assert sum(f)==256 and max(abs(H@(1-2*np.array(f,dtype=np.int32))))==32
    print('PASS planted six-flip hypergraph control: domain=12; all 924 six-sets; bound=44;',
          'hypergraph candidates',len(candidates),'zero-bearing bound-preserving',len(direct_targets),
          'known planted set',planted)


if __name__=='__main__':
    main()
