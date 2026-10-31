#!/usr/bin/env python3
"""Compressed Shannon/copy LP for an exchangeable block of conditional iid copies.

A branch first copies X2 as c0 over T2={1,4,5,6,7,8,9,10}, then samples k
conditionally iid copies of X4 given Y=T4+c0, T4={1,2,5,6,7,8,10}, independently
of the originals and c0 given Y. An optional tail is a copy of X2 over T2+c0
and ALL k iid copies. This law is invariant under all permutations of the k
copies, including after sampling the tail from the invariant conditional law.
Coordinates are (base-mask, number-of-copies); the base is originals+c0(+tail).
Every elemental Shannon row on the uncompressed variable set has one of the
four forms below, so the compressed LP contains all of them, not a sample.

Usage: python3 script.py OUT.json PRIOR.json PRIOR_SHA SPECS.json SPECS_SHA
SPECS.json: {"branches":[{"copies":3,"tail":false}, ...]}. PRIOR supplies its
DFZ cuts and extra_single_copies; its old 'programs' are REPLACED by these
branches. All raw publisher branches, symmetry, FDs and caps remain. Floating
proposal only; certificate production/checking are separate.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent

def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3ec','frontier-20261029-dfz-cutting-plane-v3.py')
v5=load('cp5ec','frontier-20261029-dfz-cutting-plane-v5.py')
v6=load('cp6ec','frontier-20261029-copy-cutting-plane-v6.py')
v8=load('cp8ec','frontier-20261029-central-cutting-plane-v8.py')
T2=sum(1<<(v-1) for v in (1,4,5,6,7,8,9,10))
T4=sum(1<<(v-1) for v in (1,2,5,6,7,8,10))
C0=1<<10;TAIL=1<<11;ORIG=1023

def subsets(m):
    u=m
    while True:
        yield u
        if not u:return
        u=(u-1)&m

def add_branch(M,tag,spec):
    k=spec['copies'];tail=spec.get('tail',False)
    if isinstance(k,bool) or not isinstance(k,int) or k<1 or not isinstance(tail,bool):raise ValueError('SPEC')
    b=12 if tail else 11;full=(1<<b)-1
    def key(m,r=0):
        if m==0 and r==0:return None
        return ('o',m) if r==0 and m<1024 else (tag,m,r)
    def add(t,kind,*data):M.add([(key(m,r),c) for m,r,c in t],0,cp.INF if kind in ('ecmono','eccmi') else 0,(kind,tag,*data))
    # All conditional entropy rows: ordinary variable, or one iid copy.
    for i in range(b):add([(full,k,1),(full^(1<<i),k,-1)],'ecmono',i)
    add([(full,k,1),(full,k-1,-1)],'ecmono',-1)
    # Conditional mutual information: two ordinary variables.
    for i in range(b):
        for j in range(i+1,b):
            for z in subsets(full^(1<<i)^(1<<j)):
                for r in range(k+1):add([(z|1<<i,r,1),(z|1<<j,r,1),(z|1<<i|1<<j,r,-1),(z,r,-1)],'eccmi','bb',i,j,z,r)
    # One ordinary variable and one copy.
    for i in range(b):
        for z in subsets(full^(1<<i)):
            for r in range(k):add([(z|1<<i,r,1),(z,r+1,1),(z|1<<i,r+1,-1),(z,r,-1)],'eccmi','bc',i,-1,z,r)
    # Two distinct copies.
    if k>=2:
        for z in range(full+1):
            for r in range(k-1):add([(z,r+1,2),(z,r+2,-1),(z,r,-1)],'eccmi','cc',-1,-2,z,r)
    # First copy c0 of X2 over T2.
    for u in subsets(T2):add([(u|C0,0,1),(u|2,0,-1)],'ecfirstcopy',u)
    add([(ORIG|C0,0,1),(T2,0,1),(ORIG,0,-1),(T2|C0,0,-1)],'ecfirstind')
    # k copies of X4 given T4+c0, independent of all previous variables.
    Y=T4|C0;E=ORIG|C0
    for r in range(k):
        for u in subsets(Y):add([(u,r+1,1),(u|8,r,-1)],'ecblockcopy',u,r)
        add([(E,r+1,1),(Y,r,1),(E,r,-1),(Y,r+1,-1)],'ecblockind',r)
    if tail:
        Yt=T2|C0
        for u in subsets(Yt):
            for r in range(k+1):add([(u|TAIL,r,1),(u|2,r,-1)],'ectailcopy',u,r)
        add([(full,k,1),(Yt,k,1),(E,k,-1),(Yt|TAIL,k,-1)],'ectailind')
    return b,k

def build(res,specs):
    M=cp.build('gurpinar-sym');keys=sorted(cp.coefficients());extra=res['extra_single_copies']
    for i,(S,T) in enumerate(extra):v6.add_single_copy(M,i,S[0],T)
    for i,spec in enumerate(specs):add_branch(M,f'e{i}',spec)
    seen=set()
    for c in res['cuts']:
        tag=c.get('tag','o')
        if tag not in ('o','b1','b2','b3') and not tag.startswith('x'):raise ValueError(('CUT_TAG_NOT_IN_NEW_MODEL',tag))
        kk=keys.index(tuple(c['coefficients']));ident=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if ident in seen:continue
        seen.add(ident);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
    return M

def main():
    out=ROOT/sys.argv[1];pr=(ROOT/sys.argv[2]).read_bytes();sr=(ROOT/sys.argv[4]).read_bytes()
    if sha256(pr).hexdigest()!=sys.argv[3] or sha256(sr).hexdigest()!=sys.argv[5]:raise ValueError('HASH')
    res=json.loads(pr);specs=json.loads(sr)['branches'];M=build(res,specs)
    print('rows',len(M.rows),'columns',len(M.col),flush=True)
    status,obj,x,dt=v8.solve_central(M)
    doc={'prior_sha256':sys.argv[3],'specs_sha256':sys.argv[5],'exchangeable_copies':specs,'extra_single_copies':res['extra_single_copies'],'cuts':res['cuts'],
         'status':status,'objective_ipm':obj,'rows':len(M.rows),'columns':len(M.col),'solve_s':dt,
         'final_columns_float':{repr(key):float(x[j]) for key,j in M.col.items()},'limits':'Floating proposal, not an exact certificate.'}
    with open(out,'x') as f:json.dump(doc,f);f.write('\n')
    print(status,obj,round(dt,2),flush=True)
if __name__=='__main__':main()
