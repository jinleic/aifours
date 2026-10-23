"""Independent complete six-flip audit; no producer imports.

Uses direct character sums, reversed coefficient order, ten-coefficient
exclusion-union tables, and pair extensions of four anchors (rather than
the producer's five-set extension). Every triple is exhausted. Every
surviving six-set is transformed by direct integer character sums.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import argparse
import gzip
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import time
import numpy as np


def audit(path, broken=False):
    started = time.monotonic()
    with gzip.open(path, 'rt') as fh:
        data = json.load(fh)
    source = Path('selection-inputs/literature/kavut-yucel.reader.md').read_text()
    raw = re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$', source)
    assert len(raw) == 5
    name = data['seed']
    hx = ''.join(dict(zip(('dsbf40','dsbf32','rsbf56','perm104-ac48','perm74-ac64'), raw))[name])
    assert hx == data['seed_hex']
    f = np.array([int(b) for c in hx for b in format(int(c,16),'04b')], dtype=np.int32)
    H = np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)], dtype=np.int32)
    W = H @ (1-2*f)
    high = np.flatnonzero(abs(W)==28)[::-1]
    assert len(high)>0 and set(abs(W).tolist())=={4,12,20,28}
    opposing = (H[high,:]*(1-2*f)[None,:]*np.sign(W[high])[:,None]<0).T
    bad = [int.from_bytes(np.packbits(row,bitorder='little').tobytes(),'little') for row in opposing]
    excluded_columns = [int.from_bytes(np.packbits(opposing[:,j],bitorder='little').tobytes(),'little') for j in range(len(high))]
    # Exhaust all local subset unions. Their semantics is simply OR of
    # the forbidden-point columns; coefficient order differs from producer.
    tables = []
    for start in range(0,len(high),10):
        row = [0]*1024
        for mask in range(1,1024):
            low = mask & -mask
            index = start + low.bit_length()-1
            row[mask] = row[mask^low] | (excluded_columns[index] if index<len(high) else 0)
        tables.append(row)
    full = (1<<512)-1
    upper = [full^((1<<(z+1))-1) for z in range(512)]
    def allowed(common, candidates):
        i=0
        while candidates and common:
            candidates &= ~tables[i][common&1023]
            common >>= 10
            i+=1
        return candidates
    anchors=[]
    examined=zero_xor_fours=0
    for x in range(510):
        for y in range(x+1,511):
            pair=bad[x]&bad[y]
            for z in range(y+1,512):
                examined+=1
                common=pair&bad[z]
                flat=x^y^z
                if flat>z and not common&bad[flat]:
                    zero_xor_fours+=1
                candidates=allowed(common,upper[z]&~(1<<flat))
                while candidates:
                    low=candidates&-candidates
                    candidates^=low
                    anchors.append((x,y,z,low.bit_length()-1))
        if x%128==0:
            print(name,'independent x',x,'anchors',len(anchors),'seconds',round(time.monotonic()-started,3),flush=True)
    assert examined==data['triples_examined']==22238720
    assert zero_xor_fours==data['admissible_zero_xor_fours']
    assert anchors==[tuple(a) for a in data['admissible_nonzero_xor_fours']]
    digest=hashlib.sha256()
    for anchor in anchors:
        for x in anchor:
            digest.update(x.to_bytes(2,'little'))
    assert digest.hexdigest()==data['anchor_sha256_u16le']
    fives=set()
    sixes=set()
    # Every possible six-set has an admissible nonzero-XOR four anchor.
    # Both extra points must individually extend it to five, and the six
    # remaining four-subsets involving both points are checked directly.
    for anchor in anchors:
        candidates=full
        for x,y,z in combinations(anchor,3):
            candidates=allowed(bad[x]&bad[y]&bad[z],candidates)
        for x in anchor:
            candidates &= ~(1<<x)
        extra=[]
        while candidates:
            low=candidates&-candidates
            candidates^=low
            e=low.bit_length()-1
            extra.append(e)
            fives.add(tuple(sorted(anchor+(e,))))
        for e,u in combinations(extra,2):
            common=bad[e]&bad[u]
            if all(not (bad[x]&bad[y]&common) for x,y in combinations(anchor,2)):
                sixes.add(tuple(sorted(anchor+(e,u))))
    assert len(fives)==data['admissible_fives_count']
    assert len(sixes)==data['admissible_sixes_count']
    survivors=[]
    targets=[]
    for points in sorted(sixes):
        g=f.copy()
        for x in points:
            g[x]^=1
        # Full direct 512-term integer character sums, not FWHT updates.
        wg=H @ (1-2*g)
        assert int(wg@wg)==512**2
        if max(abs(wg))<=28:
            zeros=np.flatnonzero(wg==0).tolist()
            rec={'flips':list(points),'zero_indices':zeros}
            survivors.append(rec)
            if zeros:
                targets.append(rec)
    if broken:
        data['six_sets_preserving_bound'].pop()
    assert survivors==data['six_sets_preserving_bound']
    assert targets==data['target_six_sets']==[]
    assert data['status']=='complete' and data['radius_exact']==6 and data['bound']==28
    out={'status':'PASS','seed':name,'triples_examined':examined,
         'zero_xor_admissible_fours':zero_xor_fours,'nonzero_xor_admissible_fours':len(anchors),
         'admissible_fives':len(fives),'admissible_sixes':len(sixes),
         'bound_preserving_six_sets':len(survivors),'zero_bearing_six_sets':len(targets),
         'result_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),
         'scope':'complete triple enumeration, all pair extensions, direct Walsh sums on all resulting six-sets; no sampling'}
    print(json.dumps(out,sort_keys=True),flush=True)
    print('seconds',round(time.monotonic()-started,3),flush=True)
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('path')
    p.add_argument('--output')
    p.add_argument('--broken',action='store_true')
    a=p.parse_args()
    result=audit(a.path,a.broken)
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
