"""Independent full pair/triple audit for two additional explicit tables."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import numpy as np


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--broken',action='store_true')
    a=p.parse_args()
    data=json.loads(Path('results/extra-seed-neighborhoods.json').read_text())
    if a.broken:
        data['seeds']['perm104-ac48']['radius2']['walsh'][17]+=4
    source=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text()
    raw=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',source)
    assert len(raw)==5
    H=np.array([[1-2*(bin(t&x).count('1')%2) for x in range(512)] for t in range(512)],dtype=np.int32)
    for name,parts,indicator in zip(('perm104-ac48','perm74-ac64'),raw[3:],(48,64)):
        rec=data['seeds'][name]
        hx=''.join(parts)
        assert rec['hex']==hx
        text=''.join(format(int(c,16),'04b') for c in hx)
        assert rec['sha256_ascii_bits']==hashlib.sha256(text.encode()).hexdigest()
        f=np.array(list(map(int,text)),dtype=np.int32)
        W=H@(1-2*f)
        r2=rec['radius2']; r4=rec['radius4']
        assert r2['walsh']==W.tolist()
        assert r2['weight']==int(f.sum())
        assert r2['W0']==int(W[0])
        assert r2['original_minimum_balancing_distance']==abs(int(W[0]))//2
        assert r2['minimum_over_linear_shifts']==min(abs(W))//2==2
        assert r2['max_abs_walsh']==max(abs(W))==28
        assert r2['zero_count']==int(np.count_nonzero(W==0))==0
        assert r2['absolute_spectrum_histogram']=={str(k):v for k,v in sorted(Counter(map(int,abs(W))).items())}
        assert r2['linear_shift_indices_with_minimum_distance_2']==np.flatnonzero(abs(W)==4).tolist()
        C=(H*(1-2*f)[None,:]).T
        legal2=[]; zero2=[]
        for x in range(511):
            candidates=W[None,:]-2*C[x,None,:]-2*C[x+1:,:]
            for j in np.flatnonzero(np.max(abs(candidates),axis=1)<=28):
                y=x+1+int(j)
                legal2.append([x,y])
                zeros=np.flatnonzero(candidates[j]==0).tolist()
                if zeros:
                    zero2.append({'flips':[x,y],'zero_indices':zeros})
        assert r2['pairs_examined']==130816
        assert r2['pairs_preserving_bound']==legal2
        assert r2['pairs_preserving_bound_and_giving_a_zero']==zero2==[]
        sat=np.flatnonzero(abs(W)==28)
        opposite=(H[sat,:]*(1-2*f)[None,:]*np.sign(W[sat])[:,None]<0).T
        triples=[]; examined=0
        for x in range(510):
            for y in range(x+1,511):
                common=opposite[x]&opposite[y]
                triples.extend((x,y,y+1+int(z)) for z in np.flatnonzero(~np.any(opposite[y+1:,common],axis=1)))
                examined+=511-y
        ts=set(triples)
        fours=set()
        for x,y,z in triples:
            for u in range(z+1,512):
                if (x,y,u) in ts and (x,z,u) in ts and (y,z,u) in ts:
                    fours.add((x,y,z,u))
        legal4=[]; zero4=[]
        for points in sorted(fours):
            g=f.copy()
            for x in points:
                g[x]^=1
            w=H@(1-2*g)
            assert max(abs(w))<=28
            legal4.append(list(points))
            zeros=np.flatnonzero(w==0).tolist()
            if zeros:
                zero4.append({'flips':list(points),'zero_indices':zeros})
        assert examined==r4['triples_examined']==22238720
        assert r4['admissible_triples']==len(triples)
        assert r4['pairs_with_admissible_third']==len({t[:2] for t in triples})
        assert r4['pairs_preserving_bound_at_distance_two']==len(legal2)
        assert r4['four_sets_preserving_bound']==legal4
        assert r4['four_sets_preserving_bound_and_giving_a_zero']==zero4==[]
        ac=[sum((1-2*int(f[x]))*(1-2*int(f[x^t])) for x in range(512)) for t in range(512)]
        assert rec['autocorrelation']==ac
        assert rec['absolute_indicator']==max(map(abs,ac[1:]))==indicator
        print(name,'PASS direct spectra, all 130816 pairs and 22238720 triples;',
              'legal pairs',len(legal2),'triples',len(triples),'fours',len(legal4),'indicator',indicator,flush=True)


if __name__=='__main__':
    main()
