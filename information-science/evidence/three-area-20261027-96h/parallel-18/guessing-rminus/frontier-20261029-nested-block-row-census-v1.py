#!/usr/bin/env python3
"""Exact row-set comparison: full individual-copy LP vs nested-block quotient.
Usage: python3 script.py OUT.json
No LP solve; integer coefficient vectors only. The full enumeration includes
all elemental rows and every subset-copy equality on each listed finite law.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('nb',ROOT/'frontier-20261029-nested-copy-block-lp-v1.py');nb=module_from_spec(s);s.loader.exec_module(nb)
T2=[1,4,5,6,7,8,9,10];T4=[1,2,5,6,7,8,10]

def normalized(ts):
    d={}
    for key,c in ts:
        if key is not None:d[key]=d.get(key,0)+c
    return tuple(sorted((key,c) for key,c in d.items() if c))

def check(blocks):
    specs={'blocks':blocks};compiled=nb.specification(specs);ks=[x[2] for x in compiled];starts=[];n=10
    for k in ks:starts.append(n);n+=k
    masks=[((1<<k)-1)<<start for k,start in zip(ks,starts)];full=(1<<n)-1
    def K(m):
        counts=tuple((m&mask).bit_count() for mask in masks);base=m&1023
        return None if not base and not any(counts) else (base,*counts)
    ge=set();eq=set()
    def add(ts,equality=False):
        row=normalized((K(m),c) for m,c in ts)
        if row:(eq if equality else ge).add(row)
    for i in range(n):add([(full,1),(full^(1<<i),-1)])
    for i,j in combinations(range(n),2):
        for z in nb.subsets(full^(1<<i)^(1<<j)):
            add([(z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)])
    past=1023;previous=0
    for a,(old,Y,k) in enumerate(compiled):
        for r in range(k):
            new=1<<(starts[a]+r);over=Y|previous|sum(1<<(starts[a]+j) for j in range(r))
            for u in nb.subsets(over):add([(u|new,1),(u|old,-1)],True)
            add([(past|new,1),(over,1),(past,-1),(over|new,-1)],True);past|=new
        previous|=masks[a]
    M=nb.cp.Model();nb.add_branch(M,'n0',specs);reverse={j:key for key,j in M.col.items()};actualge=set();actualeq=set()
    for row,meta in zip(M.rows,M.meta):
        ts=[]
        for j,c in row.items():
            key=reverse[j];short=(key[1],*(0 for _ in ks)) if key[0]=='o' else key[1:];ts.append((short,c))
        (actualge if meta[0] in ('nbmono','nbcmi') else actualeq).add(normalized(ts))
    if actualge!=ge:raise ValueError(('SHANNON',ks,len(actualge-ge),len(ge-actualge)))
    if actualeq!=eq:raise ValueError(('COPY',ks,len(actualeq-eq),len(eq-actualeq)))
    return {'blocks':blocks,'uncompressed_variables':n,'full_elemental_rows':n+n*(n-1)//2*(1<<(n-2)),
            'compressed_distinct_elemental_rows':len(ge),'compressed_distinct_copy_rows':len(eq),'total_generated_rows':len(M.rows),'both_row_sets_equal':True}

def main():
    t=time.monotonic();cases=[
      [{'vertex':2,'over':T2,'copies':2},{'vertex':4,'over':T4,'copies':2}],
      [{'vertex':2,'over':T2,'copies':1},{'vertex':4,'over':T4,'copies':2},{'vertex':2,'over':T2,'copies':1}],
      [{'vertex':2,'over':T2,'copies':2},{'vertex':3,'over':T2,'copies':1}]]
    results=[check(c) for c in cases]
    doc={'generator_sha256':sha256((ROOT/'frontier-20261029-nested-copy-block-lp-v1.py').read_bytes()).hexdigest(),'all_matched':True,'cases':results,
         'elapsed_s':time.monotonic()-t,'limits':'Exact finite integer row quotient checks only; nested kernel validity is a written mathematical premise.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(json.dumps(doc,indent=1))
if __name__=='__main__':main()
