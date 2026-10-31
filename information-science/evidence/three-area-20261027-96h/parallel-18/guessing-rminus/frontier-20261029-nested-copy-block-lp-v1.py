#!/usr/bin/env python3
"""Full Shannon relaxation of nested exchangeable conditional-iid copy blocks.

Usage: python3 script.py OUT.json PRIOR.json PRIOR_SHA SPECS.json SPECS_SHA
SPECS: {"branches":[{"blocks":[{"vertex":2,"over":[...],"copies":2}, ...]}, ...]}.
Block a samples k_a iid copies of the stated ORIGINAL variable conditionally on
its listed original over-set plus ALL copies of ALL earlier blocks, independently
of the existing original law given that conditioning tuple. The resulting law
is invariant under permutations within each block (induction over the blocks).
No assertion is made for programs using only selected earlier copies.

Coordinates: original subset mask, count selected from each copy block. This
is the exact orbit quotient of full elemental Shannon and sequential-copy
constraints under blockwise permutations. Original coordinates are shared;
other coordinates stay branch-local. PRIOR's old raw programs are replaced.
Floating proposal only; exact arithmetic certification is separate.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations,product
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent

def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3nb','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5nb','frontier-20261029-dfz-cutting-plane-v5.py')
v6=load('cp6nb','frontier-20261029-copy-cutting-plane-v6.py');v8=load('cp8nb','frontier-20261029-central-cutting-plane-v8.py')

def subsets(m):
    u=m
    while True:
        yield u
        if not u:return
        u=(u-1)&m

def specification(spec):
    blocks=spec['blocks'];out=[]
    if not blocks:raise ValueError('EMPTY_BLOCKS')
    for bl in blocks:
        v=bl['vertex'];k=bl['copies'];over=bl['over']
        if isinstance(v,bool) or not isinstance(v,int) or not 1<=v<=10:raise ValueError('VERTEX')
        if isinstance(k,bool) or not isinstance(k,int) or k<1:raise ValueError('COPIES')
        if any(isinstance(x,bool) or not isinstance(x,int) or not 1<=x<=10 for x in over) or len(set(over))!=len(over) or v in over:raise ValueError('OVER')
        out.append((1<<(v-1),sum(1<<(x-1) for x in over),k))
    return out

def add_branch(M,tag,spec):
    blocks=specification(spec);ks=tuple(t[2] for t in blocks);d=len(ks);zero=(0,)*d;full=1023
    def K(m,r):
        if m==0 and r==zero:return None
        return ('o',m) if r==zero else (tag,m,*r)
    def add(ts,kind,*meta):M.add([(K(m,r),c) for m,r,c in ts],0,cp.INF if kind in ('nbmono','nbcmi') else 0,(kind,tag,*meta))
    def vectors(decrements=()):
        maxima=list(ks)
        for a in decrements:maxima[a]-=1
        return product(*(range(k+1) for k in maxima))
    def bump(r,a):q=list(r);q[a]+=1;return tuple(q)
    for i in range(10):add([(full,ks,1),(full^(1<<i),ks,-1)],'nbmono','o',i)
    for a in range(d):
        q=list(ks);q[a]-=1;add([(full,ks,1),(full,tuple(q),-1)],'nbmono','c',a)
    # Ordinary-variable pair.
    for i,j in combinations(range(10),2):
        for z in subsets(full^(1<<i)^(1<<j)):
            for r in vectors():add([(z|1<<i,r,1),(z|1<<j,r,1),(z|1<<i|1<<j,r,-1),(z,r,-1)],'nbcmi','oo',i,j,z,r)
    # Ordinary variable and a copy in block a.
    for i in range(10):
        for a in range(d):
            for z in subsets(full^(1<<i)):
                for r in vectors((a,)):
                    ra=bump(r,a);add([(z|1<<i,r,1),(z,ra,1),(z|1<<i,ra,-1),(z,r,-1)],'nbcmi','oc',i,a,z,r)
    # Copies from two distinct blocks.
    for a,b in combinations(range(d),2):
        for z in range(1024):
            for r in vectors((a,b)):
                ra=bump(r,a);rb=bump(r,b);rab=bump(ra,b)
                add([(z,ra,1),(z,rb,1),(z,rab,-1),(z,r,-1)],'nbcmi','cc',a,b,z,r)
    # Two copies within one block.
    for a in range(d):
        if ks[a]<2:continue
        for z in range(1024):
            for r in vectors((a,a)):
                ra=bump(r,a);raa=bump(ra,a)
                add([(z,ra,2),(z,raa,-1),(z,r,-1)],'nbcmi','same',a,a,z,r)
    # Each block's ordered steps, quotienting the subsets of earlier copies.
    for a,(old,Y,ka) in enumerate(blocks):
        for prefix in product(*(range(ks[b]+1) for b in range(a))):
            for r in range(ka):
                q=tuple(prefix)+(r,)+(0,)*(d-a-1);qn=bump(q,a)
                for u in subsets(Y):add([(u,qn,1),(u|old,q,-1)],'nbcopy',a,u,q)
        for r in range(ka):
            q=ks[:a]+(r,)+(0,)*(d-a-1);qn=bump(q,a)
            add([(full,qn,1),(Y,q,1),(full,q,-1),(Y,qn,-1)],'nbind',a,r)

def build(res,specs):
    M=cp.build('gurpinar-sym');keys=sorted(cp.coefficients())
    for i,(S,T) in enumerate(res['extra_single_copies']):v6.add_single_copy(M,i,S[0],T)
    for i,sp in enumerate(specs):add_branch(M,f'n{i}',sp)
    seen=set()
    for c in res['cuts']:
        tag=c.get('tag','o')
        if tag not in ('o','b1','b2','b3') and not tag.startswith('x'):raise ValueError('CUT_TAG')
        kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
    return M

def main():
    pr=(ROOT/sys.argv[2]).read_bytes();sr=(ROOT/sys.argv[4]).read_bytes()
    if sha256(pr).hexdigest()!=sys.argv[3] or sha256(sr).hexdigest()!=sys.argv[5]:raise ValueError('HASH')
    res=json.loads(pr);specs=json.loads(sr)['branches'];M=build(res,specs)
    print('rows',len(M.rows),'columns',len(M.col),flush=True)
    status,obj,x,dt=v8.solve_central(M)
    doc={'prior_sha256':sys.argv[3],'specs_sha256':sys.argv[5],'nested_copy_blocks':specs,'extra_single_copies':res['extra_single_copies'],'cuts':res['cuts'],
         'status':status,'objective_ipm':obj,'rows':len(M.rows),'columns':len(M.col),'solve_s':dt,
         'final_columns_float':{repr(key):float(x[j]) for key,j in M.col.items()},'limits':'Floating proposal; nested conditional-kernel construction is a written validity premise, not certified by the solver.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f);f.write('\n')
    print(status,obj,round(dt,2),flush=True)
if __name__=='__main__':main()
