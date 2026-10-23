"""Independent exact four-flip audit by forbidden-triple enumeration.

Reconstructs direct Walsh characters from literature (no producer imports).
For every triple S and saturated a, count the opposing signs directly
using precomputed Boolean values. An admissible triple has count <=2
at all saturated coefficients. Enumerate all possible quadruples from
these triples, then use fresh direct sums to check every quadruple hit.
"""
import argparse
from itertools import combinations
import json
from pathlib import Path
import re
import numpy as np
import hashlib


def main():
    p=argparse.ArgumentParser()
    p.add_argument('path',nargs='?',default='results/radius4.json')
    p.add_argument('--output')
    args=p.parse_args()
    out=json.loads(Path(args.path).read_text())
    text=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text().split('#### 3.2')[0]
    raw=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',text)
    assert len(raw)==3
    H=np.array([[(-1)**(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int16)
    for name,(left,right) in zip(('dsbf40','dsbf32','rsbf56'),raw):
        f=np.array([int(b) for c in left+right for b in format(int(c,16),'04b')],dtype=np.int16)
        s=1-2*f
        w=H.astype(np.int32)@s.astype(np.int32)
        assert set(abs(w).tolist())=={4,12,20,28}
        sat=np.flatnonzero(abs(w)==28)
        # This 0/1 matrix explicitly records sign disagreement; no bitsets.
        opposing=(H[sat,:]*s[None,:]*np.sign(w[sat])[:,None]<0).T.astype(np.uint8)
        triples=[]
        examined=0
        for x in range(510):
            for y in range(x+1,511):
                count=opposing[x]+opposing[y]
                violation=(count==2)
                valid=np.flatnonzero(~np.any(opposing[y+1:,violation],axis=1))
                triples.extend((x,y,y+1+int(z)) for z in valid)
                examined+=511-y
        assert examined==22238720
        tripleset=set(triples)
        foursets=set()
        # Every legal four-set has all four of its triples in tripleset.
        # A complete finite list of 195 triples makes this enumeration small.
        for x,y,z in triples:
            for u in range(z+1,512):
                if (x,y,u) in tripleset and (x,z,u) in tripleset and (y,z,u) in tripleset:
                    foursets.add((x,y,z,u))
        legal=[]
        balanced=[]
        for points in sorted(foursets):
            g=f.copy()
            for x in points:
                g[x]^=1
            wg=np.array([sum((1-2*int(g[x]))*int(H[a,x]) for x in range(512)) for a in range(512)],dtype=np.int32)
            assert max(abs(wg))<=28
            legal.append(list(points))
            zeros=np.flatnonzero(wg==0).tolist()
            if zeros:
                balanced.append({'flips':list(points),'zero_indices':zeros})
        rec=out['seeds'][name]
        assert rec['triples_examined']==examined
        assert rec['admissible_triples']==len(triples)==195
        assert rec['pairs_with_admissible_third']==len({t[:2] for t in triples})
        assert rec['four_sets_preserving_bound']==legal
        assert rec['four_sets_preserving_bound_and_giving_a_zero']==balanced==[]
        assert len(legal)==45
        print(name,'PASS exhaustive triples',examined,'admissible',len(triples),'four-sets',len(legal),'zero-bearing',len(balanced),flush=True)
    assert out['radius']==4 and out['bound']==28
    print('PASS independent complete radius-four audit')
    if args.output:
        Path(args.output).write_text(json.dumps({'status':'PASS','method':'independent direct-character exhaustive triple reconstruction','per_seed_triples':22238720,'per_seed_admissible_triples':195,'per_seed_bound_preserving_four_sets':45,'per_seed_zero_bearing_four_sets':0,'checked_result_sha256':hashlib.sha256(Path(args.path).read_bytes()).hexdigest()},indent=2)+'\n')


if __name__=='__main__':
    main()
