#!/usr/bin/env python3
"""Exact F2^3 syndrome-subspace clique-lift scan for q=8 triangle code."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-syndrome-triple-cliques.py','11eeeb0001a77b8f5b349064efad909e035107668a9f3060d32fe93ab48d8305')
OUT=ROOT/'frontier-20261028-syndrome-3plane-lifts-result.json'


def load():
    raw=(ROOT/BASE[0]).read_bytes()
    if sha256(raw).hexdigest()!=BASE[1]:raise ValueError('HASH')
    spec=spec_from_file_location('syndrome3',ROOT/BASE[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod


def rowvalues(pivot,free):
    code=np.arange(1<<len(free),dtype=np.uint16);out=np.full(len(code),1<<pivot,dtype=np.uint16)
    for j,bit in enumerate(free):out|=((code>>j)&1)<<bit
    return out


def planes(inc):
    hypermask=sum(1<<(t-1) for t in (1,2,3,6,8,10));counts=[0,0,0,0];exceptions=[]
    for p,q,r in combinations(range(10),3):
        one=rowvalues(p,[x for x in range(p+1,10) if x not in (q,r)])
        two=rowvalues(q,[x for x in range(q+1,10) if x!=r]);three=rowvalues(r,list(range(r+1,10)))
        x=np.repeat(one,len(two)*len(three));y=np.tile(np.repeat(two,len(three)),len(one));z=np.tile(three,len(one)*len(two))
        counts[0]+=len(x);not_hyper=((x|y|z)&hypermask)==hypermask;counts[1]+=int(np.count_nonzero(~not_hyper))
        local=np.zeros(len(x),dtype=bool)
        for mask in inc:
            a=x&mask;b=y&mask;c=z&mask
            local|=(a!=0)&(b!=0)&(c!=0)&(a!=b)&(a!=c)&(b!=c)&((a^b)!=c)
        counts[2]+=int(np.count_nonzero(not_hyper&local));bad=np.flatnonzero(not_hyper&~local);counts[3]+=len(bad)
        exceptions.extend((int(x[j]),int(y[j]),int(z[j])) for j in bad)
    if counts!=[6347715,3487095,2835534,25086]:raise ValueError(('PLANE_COUNTS',counts))
    return counts,exceptions


def lift(basis,D,buckets):
    ordered=sorted(basis,key=lambda s:(len(buckets[s]),s));s,t,r=ordered
    for u in buckets[s]:
        for v in buckets[t]:
            if (u^v) not in D:continue
            for w in buckets[r]:
                if (u^w) in D and (v^w) in D and (u^v^w) in D:return ordered,(u,v,w)
    return ordered,None


def main():
    started=monotonic();mod=load();sm,inc=mod.setup();D,buckets=mod.differences(sm)
    counts,exceptions=planes(inc);witnesses=[];failure=None
    for basis in exceptions:
        ordered,reps=lift(basis,D,buckets)
        if reps is None:failure={'rref_basis':basis,'searched_basis':ordered};break
        witnesses.append({'rref_basis':basis,'searched_basis':ordered,'word_representatives':reps})
    out={'base_producer_sha256':BASE[1],'plane_counts':{'total':counts[0],'fixed_syndrome_hyperplane':counts[1],
         'local_rank_three':counts[2],'explicit_witness_required':counts[3]},
         'exceptional_witness_count':len(witnesses),'failure':failure,'exceptional_witnesses':witnesses,
         'elapsed_seconds':monotonic()-started,'limits':'Exact finite clique-lift scan; local/hyperplane construction and cardinality implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exceptional_witnesses'},indent=2))


if __name__=='__main__':main()
