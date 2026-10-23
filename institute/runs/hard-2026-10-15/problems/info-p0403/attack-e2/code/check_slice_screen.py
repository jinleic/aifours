"""Independent direct-sum recheck of every source and every fixed half."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--broken',action='store_true')
    p.add_argument('--output')
    a=p.parse_args()
    with gzip.open('results/slice-screen.json.gz','rt') as fh:
        data=json.load(fh)
    if a.broken:
        data['cases'][0]['slice_l1']+=8
    sources=data['sources']
    F=[]; support=[]
    H9=np.array([[1-2*(bin(u&x).count('1')%2) for x in range(512)] for u in range(512)],dtype=np.int32)
    for r in sources:
        text=r['bits']
        assert len(text)==512 and set(text)<={'0','1'}
        assert hashlib.sha256(text.encode()).hexdigest()==r['sha256_ascii_bits']
        f=np.array(list(map(int,text)),dtype=np.int32)
        W=H9@(1-2*f)
        assert W.tolist()==r['walsh'] and int(f.sum())==r['weight']==256
        assert W[0]==0 and max(abs(W))==32 and r['nonlinearity']==240
        s=0
        for x in np.flatnonzero(f):
            s^=int(x)
        assert s==r['support_xor'] and s!=0
        F.append(f); support.append(s)
    F=np.array(F,dtype=np.int32)
    H8=np.array([[1-2*(bin(u&x).count('1')%2) for x in range(256)] for u in range(256)],dtype=np.int32)
    case_map={(r['source'],r['normal']):r for r in data['cases']}
    assert len(case_map)==len(data['cases'])
    expected_keys={(i,v) for i,s in enumerate(support) for v in range(1,512) if bin(v&s).count('1')%2}
    assert set(case_map)==expected_keys
    excluded=controls=0
    seen=set()
    for v in range(1,512):
        source_ids=[i for i,s in enumerate(support) if bin(v&s).count('1')%2]
        if not source_ids:
            continue
        pivot=(v&-v).bit_length()-1
        basis=[(1<<j)^((1<<pivot) if (v>>j)&1 else 0) for j in range(9) if j!=pivot]
        points=[]
        for t in range(256):
            x=0
            for j,b in enumerate(basis):
                if (t>>j)&1:
                    x^=b
            points.append(x)
        assert len(set(points))==256 and all(bin(v&x).count('1')%2==0 for x in points)
        # Direct 256-term sums of directly read restrictions. The producer
        # instead averages pairs of nine-variable spectral coefficients.
        restrictions=F[np.ix_(source_ids,points)]
        G=(1-2*restrictions)@H8.T
        assert np.all(np.sum(restrictions,axis=1)%2==1)
        for j,i in enumerate(source_ids):
            values=abs(G[j]); M=int(max(values)); l1=int(sum(values))
            assert int(G[j]@G[j])==65536 and np.all(G[j]%4==2)
            small=int(max(values[values<=14]))
            rejected=[]
            if M>26:
                rejected.append('slice-max>26')
            if l1>3570+small:
                rejected.append('Parseval-zero-capacity')
            r=case_map[i,v]
            assert r['slice_max_abs_W']==M and r['slice_l1']==l1
            assert r['largest_slice_magnitude_at_most_14']==small and r['rejections']==rejected
            excluded+=bool(rejected); seen.add((i,v))
            # Bound-32 planted controls: the stored source is a genuine
            # completion with a zero. All 31744 cases must pass the same
            # necessary-condition derivation at relaxed bound 32.
            small32=int(max(values[values<=16]))
            assert M<=30 and l1<=4080+small32
            controls+=1
    viable=[r for r in data['cases'] if not r['rejections']]
    assert seen==expected_keys
    assert data['total_cases']==len(expected_keys)==31744
    assert data['excluded_cases']==excluded==31492
    assert data['unresolved_cases']==len(viable)==252
    assert data['unresolved_case_records']==viable
    result={'status':'PASS','sources_directly_checked':len(sources),
            'half_table_classes_directly_checked':len(seen),'classes_with_exact_balanced_maximum_240':excluded,
            'unresolved_classes':len(viable),'bound32_planted_controls':controls,
            'result_sha256':hashlib.sha256(Path('results/slice-screen.json.gz').read_bytes()).hexdigest(),
            'scope':'every listed class and every complete source spectrum; no sampling; classes can overlap'}
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__':
    main()
