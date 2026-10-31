#!/usr/bin/env python3
"""Exact finite check of compressed rows against independently enumerated FULL rows.

Usage: python3 script.py OUT.json
Checks (k,tail)=(1,F),(2,F),(3,F),(1,T),(2,T). The uncompressed enumeration uses
individual copy bits and every elemental row and every copy-marginal subset.
It collapses only the number of selected iid copies, then compares the sets of
integer coefficient vectors with the implementation's actual generated rows.
No floating arithmetic, LP solver, entropy-realizability or novelty claim.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('ec',ROOT/'frontier-20261029-exchangeable-copy-lp-v1.py');ec=module_from_spec(s);s.loader.exec_module(ec)

def normal(terms):
    d={}
    for key,c in terms:
        if key is not None:d[key]=d.get(key,0)+c
    return tuple(sorted((key,c) for key,c in d.items() if c))

def check(k,tail):
    b=12 if tail else 11;n=b+k;bm=(1<<b)-1;fm=(1<<n)-1
    def K(mask):
        m=mask&bm;r=(mask>>b).bit_count()
        return None if m==r==0 else (m,r)
    ge=set();eq=set();count=0
    def add(terms,equality=False):
        nonlocal count
        t=normal((K(m),c) for m,c in terms)
        if t:(eq if equality else ge).add(t)
        count+=1
    for i in range(n):add([(fm,1),(fm^(1<<i),-1)])
    for i,j in combinations(range(n),2):
        for z in ec.subsets(fm^(1<<i)^(1<<j)):
            add([(z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)])
    shannon_count=count
    def step(new,old,over,existing):
        for u in ec.subsets(over):add([(u|new,1),(u|old,-1)],True)
        add([(existing|new,1),(over,1),(existing,-1),(over|new,-1)],True)
    step(1<<10,1<<1,ec.T2,1023)
    past=1023|(1<<10)
    for j in range(k):
        new=1<<(b+j);over=ec.T4|(1<<10)|sum(1<<(b+t) for t in range(j))
        step(new,1<<3,over,past);past|=new
    if tail:step(1<<11,1<<1,ec.T2|(1<<10)|sum(1<<(b+t) for t in range(k)),past)
    M=ec.cp.Model();ec.add_branch(M,'e0',{'copies':k,'tail':tail});rev={j:key for key,j in M.col.items()}
    actualge=set();actualeq=set()
    for row,meta in zip(M.rows,M.meta):
        terms=[]
        for j,c in row.items():
            key=rev[j];short=(key[1],0) if key[0]=='o' else (key[1],key[2]);terms.append((short,c))
        (actualge if meta[0] in ('ecmono','eccmi') else actualeq).add(normal(terms))
    if actualge!=ge:raise ValueError(('SHANNON_MISMATCH',k,tail,len(actualge-ge),len(ge-actualge)))
    if actualeq!=eq:raise ValueError(('COPY_MISMATCH',k,tail,len(actualeq-eq),len(eq-actualeq)))
    return {'copies':k,'tail':tail,'uncompressed_variables':n,'uncompressed_shannon_rows':shannon_count,
            'compressed_shannon_distinct_rows':len(ge),'compressed_copy_distinct_rows':len(eq),'actual_total_rows':len(M.rows),
            'shannon_row_sets_equal':True,'copy_row_sets_equal':True}

def main():
    t=time.monotonic();cases=[check(k,tail) for k,tail in ((1,False),(2,False),(3,False),(1,True),(2,True))]
    report={'generator_sha256':sha256((ROOT/'frontier-20261029-exchangeable-copy-lp-v1.py').read_bytes()).hexdigest(),
            'all_row_sets_equal':True,'cases':cases,'elapsed_s':time.monotonic()-t,
            'limits':'Exact integer row enumeration and exchangeability-quotient equality for the listed finite cases only. Validity of exchangeability is the written conditional-kernel lemma, not certified here.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f,indent=1);f.write('\n')
    print(json.dumps(report,indent=1))
if __name__=='__main__':main()
