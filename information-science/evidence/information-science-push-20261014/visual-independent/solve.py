import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
import argparse, collections, json, time
from pathlib import Path
import numpy as np
from witness_search import CASES, access

ROOT=Path(__file__).resolve().parent

def load(case,m):
    _, qs, _, fs = access(CASES[case-1])
    arrays=[np.fromfile(ROOT/f'case{case}_m{m}_{c}.bin',dtype=np.uint8).reshape((-1,m)) for c in ('white','black')]
    weights=[np.stack([(a&q!=0).sum(axis=1) for q in qs],axis=1).astype(np.int8) for a in arrays]
    projections=[np.stack([np.sum(np.sort(a&f,axis=1).astype(np.uint64)<<np.arange(0,5*m,5,dtype=np.uint64),axis=1) for f in fs],axis=1) for a in arrays]
    return qs,fs,arrays,weights,projections


def propagate(weights,projections,iw,ib,trace):
    # A deletion has a finite exact combinatorial reason. Updates are synchronous.
    while len(iw) and len(ib):
        keepw=np.ones(len(iw),dtype=bool); keepb=np.ones(len(ib),dtype=bool)
        counts=[]
        for k in range(projections[0].shape[1]):
            groups=[collections.defaultdict(list),collections.defaultdict(list)]
            for t,ids in enumerate((iw,ib)):
                for j,code in enumerate(projections[t][ids,k]): groups[t][int(code)].append(j)
            matchedw=np.zeros(len(iw),dtype=bool); matchedb=np.zeros(len(ib),dtype=bool)
            for code,wa in groups[0].items():
                ba=groups[1].get(code)
                if ba is None: continue
                # Row-by-row chunks avoid a large broadcast temporary.
                for wj in wa:
                    good=np.all(weights[1][ib[ba]] > weights[0][iw[wj]],axis=1)
                    if np.any(good):
                        matchedw[wj]=True
                        matchedb[np.asarray(ba)[good]]=True
            keepw &= matchedw; keepb &= matchedb
            counts.append([int(matchedw.sum()),int(matchedb.sum())])
        nw,nb=iw[keepw],ib[keepb]
        trace.append({'before':[len(iw),len(ib)],'matched_per_forbidden':counts,'after':[len(nw),len(nb)]})
        if len(nw)==len(iw) and len(nb)==len(ib): return nw,nb
        iw,ib=nw,nb
    return iw,ib


def run(case,m):
    start=time.monotonic(); qs,fs,arrays,weights,projections=load(case,m)
    trace=[]
    iw,ib=propagate(weights,projections,np.arange(len(arrays[0])),np.arange(len(arrays[1])),trace)
    result={'case':case,'m':m,'qualified':qs,'maximal_forbidden':fs,'initial':[len(a) for a in arrays], 'arc_trace':trace,'surviving':[len(iw),len(ib)],'seconds':time.monotonic()-start}
    for color,ids in [('white',iw),('black',ib)]: np.save(ROOT/f'case{case}_m{m}_{color}_ids.npy',ids)
    (ROOT/f'case{case}_m{m}_arc.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--case',type=int);p.add_argument('--m',type=int);args=p.parse_args()
    if args.case: run(args.case,args.m)
    else:
        for case,m in [(1,5),(2,6),(3,5),(4,6),(5,6),(5,7)]: run(case,m)
