"""Exact Parseval screen for fixed hyperplane halves of balanced NL240 tables."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from seeds import fwht


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--compare',action='store_true')
    a=p.parse_args()
    starts=json.loads(Path('results/continuation-heuristic-starts.json').read_text())
    extra=[json.loads(Path('results/continuation-heuristic-best-tail.json').read_text())]
    extra += [json.loads(Path('results/%s-flat-attainer.json'%s).read_text()) for s in ('dsbf40','dsbf32','rsbf56')]
    texts=sorted(set(r['bits'] for r in starts+extra))
    sources=[]; cases=[]; candidates=[]
    indices=np.arange(512,dtype=np.int32)
    for source_id,text in enumerate(texts):
        f=list(map(int,text))
        assert len(f)==512 and sum(f)==256
        W=np.array(fwht(f),dtype=np.int32)
        assert max(abs(W))==32
        support_xor=0
        for x,b in enumerate(f):
            if b:
                support_xor^=x
        if not support_xor:
            continue
        source_index=len(sources)
        sources.append({'bits':text,'sha256_ascii_bits':hashlib.sha256(text.encode()).hexdigest(),
                        'support_xor':support_xor,'weight':256,'nonlinearity':240,'walsh':W.tolist()})
        for v in range(1,512):
            if bin(v&support_xor).count('1')%2==0:
                continue
            pivot=v&-v
            reps=indices[(indices&pivot)==0]
            G=(W[reps]+W[reps^v])//2
            assert int(G@G)==256**2 and np.all(G%4==2)
            M=int(max(abs(G)))
            l1=int(sum(abs(G)))
            small=int(max(abs(G)[abs(G)<=14]))
            rejected=[]
            if M>26:
                rejected.append('slice-max>26')
            if l1>3570+small:
                rejected.append('Parseval-zero-capacity')
            record={'source':source_index,'normal':v,'slice_max_abs_W':M,'slice_l1':l1,
                    'largest_slice_magnitude_at_most_14':small,'rejections':rejected}
            cases.append(record)
            if not rejected:
                candidates.append(record)
    out={'bit_order':'bits[x]=f(x); x_i=(x>>i)&1','scope':'For each listed source f and normal v, arbitrary changes on v.x=1, values on v.x=0 fixed to f, then any linear output shift. Only rejected cases are excluded.',
         'sources':sources,'cases':cases,'total_cases':len(cases),'excluded_cases':sum(bool(r['rejections']) for r in cases),
         'unresolved_cases':len(candidates),'unresolved_case_records':candidates}
    path=Path('results/slice-screen.json.gz')
    if a.compare:
        with gzip.open(path,'rt') as fh:
            assert json.load(fh)==out
    else:
        path.write_bytes(gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0))
    print('sources',len(sources),'half-table classes',len(cases),'exact balanced maximum 240 established for',out['excluded_cases'],
          'unresolved by screen',len(candidates),flush=True)
    print('first viable cases',candidates[:6],flush=True)


if __name__=='__main__':
    main()
