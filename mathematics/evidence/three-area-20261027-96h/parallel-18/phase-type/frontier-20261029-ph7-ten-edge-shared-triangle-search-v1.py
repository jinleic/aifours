#!/usr/bin/env python3
"""Bounded numerical search on ten-edge, no-2-cycle shared-triangle graphs.

Enumerates a particular root-triangle/two-ear/nine-edge core and one extra
edge, then searches actual generator + path-normalized input/exit equations.
This core generation is NOT proved exhaustive for all 10-edge graphs. Results
are numerical diagnostics only, never a PH witness or an exclusion.
"""
from collections import Counter
from itertools import combinations,permutations,product
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
source=ROOT/'frontier-20261028-ph7-ten-edge-path-normalized-search-v1.py'
ns={'__file__':str(source)}
exec(compile(source.read_text().split('pairs=[(i,j)for i in range(7)')[0],str(source),'exec'),ns)
from scipy.optimize import least_squares
rng=np.random.default_rng(20270222);started=time.monotonic();wall=50
base={(0,1),(1,2),(2,0)};cores=set()
for n1 in range(5):
    n2=4-n1;old=3+n1
    for a,b in product(range(3),repeat=2):
        if n1==0 and a==b:continue
        p=[a]+list(range(3,old))+[b];E=set(zip(p,p[1:]))
        if len(E)!=len(p)-1 or E&base:continue
        for c,d in product(range(old),repeat=2):
            if n2==0 and c==d:continue
            q=[c]+list(range(old,7))+[d];F=set(zip(q,q[1:]));G=frozenset(base|E|F)
            if len(F)==len(q)-1 and not(F&(base|E)) and len(G)==9:cores.add(G)
allpairs=[(i,j)for i in range(7)for j in range(7)if i!=j];graphs=set()
for G in cores:
    if any((b,a)in G for a,b in G):continue
    for edge in allpairs:
        if edge not in G and (edge[1],edge[0])not in G:graphs.add(frozenset(G|{edge}))

def triangles(G):
    return {frozenset(t)for t in permutations(range(7),3)if t[0]==min(t)and all((t[i],t[(i+1)%3])in G for i in range(3))}

def canonical(G,tr):
    best=None
    for triple in tr:
        for a in permutations(triple):
            if not all((a[i],a[(i+1)%3])in G for i in range(3)):continue
            for tail in permutations([v for v in range(7)if v not in triple]):
                m={v:i for i,v in enumerate(a+tail)};key=sum(1<<(7*m[i]+m[j])for i,j in G)
                best=key if best is None else min(best,key)
    return best
unique={}
for G in graphs:
    tr=triangles(G)
    if not any(a.isdisjoint(b)for a,b in combinations(tr,2)):continue
    if not any(len(a&b)==2 for a,b in combinations(tr,2)):continue
    key=canonical(G,tr);unique.setdefault(key,(G,tr))
cases=sorted(unique.items());print('cores',len(cores),'anchored candidate isomorphs',len(cases),
                                   'triangle histogram',dict(Counter(len(tr)for _,(_,tr)in cases)),flush=True)
rows=[];best=None;stopped=False
for index,(key,(G,tr))in enumerate(cases):
    if time.monotonic()-started>=wall:stopped=True;break
    edges=sorted(G);supports,paths=ns['graph_data'](edges)
    if not supports:continue
    I,E=supports[index%min(3,len(supports))];n=len(edges)+len(I)+len(E)
    low=np.full(n,1e-7);high=np.r_[np.full(len(edges),20.),np.full(len(I)+len(E),1.)]
    seed=np.r_[rng.uniform(.2,2.5,len(edges)),rng.uniform(.1,1.,len(I)+len(E))]
    fit=least_squares(lambda x:ns['residual'](x,edges,I,E,paths)[0],seed,bounds=(low,high),max_nfev=700,
                      ftol=1e-11,xtol=1e-11,gtol=1e-11)
    f,p,q,lead,M,alpha,gamma=ns['residual'](fit.x,edges,I,E,paths);err=float(np.linalg.norm(f,np.inf))
    row={'index':index,'canonical':str(key),'triangles':[sorted(v)for v in sorted(tr,key=lambda z:sorted(z))],
         'input':I,'exit':E,'residual_inf':err,'p':float(p),'q':float(q),'lead':float(lead),'evaluations':int(fit.nfev)}
    rows.append(row);print('case',index,'residual',err,'lead',lead,flush=True)
    if best is None or err<best[0]:best=(err,row,edges,fit.x.copy(),M.copy(),alpha.copy(),gamma.copy())
    if err<1e-9:stopped=True;break
out=ROOT/'frontier-20261029-ph7-ten-edge-shared-triangle-search-result-v1.json'
out.write_text(json.dumps({'anchored_cores':len(cores),'anchored_candidate_isomorphs':len(cases),
 'attempted':len(rows),'stopped_early':stopped,'seconds':time.monotonic()-started,'rows':rows,
 'best_residual':best[0]if best else None,'best_case':best[1]if best else None,'best_edges':best[2]if best else None,
 'best_variables':best[3].tolist()if best else None,'best_generator':best[4].tolist()if best else None,
 'best_input':best[5].tolist()if best else None,'best_exit':best[6].tolist()if best else None,
 'scope':'bounded numeric, one support/restart per anchored graph; not exhaustive, not a witness or exclusion'},indent=2)+'\n')
print('best residual',best[0]if best else None,'saved',out)
