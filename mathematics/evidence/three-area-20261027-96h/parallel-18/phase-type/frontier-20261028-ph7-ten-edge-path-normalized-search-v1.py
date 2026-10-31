#!/usr/bin/env python3
"""Bounded 10-edge PH search with path-normalized numerator equations.

Uses positive simple-path products for the degree-two numerator, avoiding the
vanishing-leading-coefficient weakness of the prior adjugate search. Floating
results are proposals only, not exact witnesses, completeness, or exclusions.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20270120);start=time.monotonic();WALL=45

def graph(k,l):
    return {(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(3+k,6),(6,(-l)%3)}


def graph_data(edges):
    adj=[[j for i,j in edges if i==v]for v in range(7)];paths={};dist=[[99]*7 for _ in range(7)]
    for src in range(7):
        dist[src][src]=0;todo=deque([src])
        while todo:
            i=todo.popleft()
            for j in adj[i]:
                if dist[src][j]>dist[src][i]+1:dist[src][j]=dist[src][i]+1;todo.append(j)
        def dfs(i,path):
            if len(path)>=5:
                used=set(path);paths.setdefault((src,i),[]).append((tuple(zip(path,path[1:])),tuple(v for v in range(7)if v not in used)))
            for j in adj[i]:
                if j not in path:dfs(j,path+(j,))
        dfs(src,(src,))
    valid=[]
    for mask in range(1,128):
        I=tuple(i for i in range(7)if mask>>i&1);allow=[j for j in range(7)if all(dist[i][j]>=4 for i in I)]
        for emask in range(1,1<<len(allow)):
            E=tuple(allow[j]for j in range(len(allow))if emask>>j&1)
            if any(dist[i][j]==4 for i in I for j in E) and any(len(p[1])==1 for i in I for j in E for p in paths.get((i,j),[])):valid.append((I,E))
    valid.sort(key=lambda v:(len(v[0])+len(v[1]),v))
    valid=[v for v in valid if not any(set(a)<=set(v[0])and set(b)<=set(v[1])and(a,b)!=v for a,b in valid)]
    return valid,paths


def residual(v,edges,I,E,allpaths):
    n=len(edges);G=np.zeros((7,7))
    for rate,(i,j)in zip(v[:n],edges):G[i,j]=rate
    u=G.sum(1);G[np.arange(7),np.arange(7)]=-u
    alpha=np.zeros(7);alpha[list(I)]=v[n:n+len(I)];alpha/=alpha.sum()
    gamma=np.zeros(7);gamma[list(E)]=v[n+len(I):];gamma/=gamma.sum()
    B=np.eye(7);cs=[1.]
    for j in range(1,8):
        Z=G@B;c=-np.trace(Z)/j;cs.append(c);B=Z+c*np.eye(7)
    z=8/9;p=cs[1]-4;q=cs[2]-4*p-(6+2*z)
    target=np.convolve([1,4,6+2*z,4+4*z,(1+z)**2,0],[1,p,q])
    spectral=(np.array(cs[3:7])-target[3:7])/(1+np.abs(target[3:7]))
    c2=c1=c0=0.
    for i in I:
        for j in E:
            for steps,comp in allpaths.get((i,j),[]):
                w=alpha[i]*gamma[j]
                for a,b in steps:w*=G[a,b]
                if len(comp)==2:
                    a,b=comp;c2+=w;c1+=w*(u[a]+u[b]);c0+=w*(u[a]*u[b]-G[a,b]*G[b,a])
                elif len(comp)==1:c1+=w;c0+=w*u[comp[0]]
                elif not comp:c0+=w
                else:raise AssertionError('support admitted a shorter path')
    assert c2>0
    num=np.array([(c1/c2-p)/(1+abs(p)),(c0/c2-q)/(1+abs(q))])
    return np.r_[spectral,num,min(p,0),min(q,0)],p,q,c2,G,alpha,gamma

pairs=[(i,j)for i in range(7)for j in range(7)if i!=j];rows=[];best=None;stop=False
for k,l in product(range(3),repeat=2):
    base=graph(k,l);extras=[e for e in pairs if e not in base];rng.shuffle(extras)
    for extra in extras[:4]:
        if time.monotonic()-start>WALL:stop=True;break
        edges=sorted(base|{extra});choices,paths=graph_data(edges)
        if not choices:continue
        I,E=choices[int(rng.integers(min(4,len(choices))))];n=len(edges)+len(I)+len(E)
        lo=np.full(n,1e-7);hi=np.r_[np.full(len(edges),20.),np.full(len(I)+len(E),1.)]
        seed=np.r_[rng.uniform(.2,2.5,len(edges)),rng.uniform(.1,1.,len(I)+len(E))]
        fit=least_squares(lambda x:residual(x,edges,I,E,paths)[0],seed,bounds=(lo,hi),max_nfev=800,
                          ftol=1e-11,xtol=1e-11,gtol=1e-11)
        f,p,q,lead,G,alpha,gamma=residual(fit.x,edges,I,E,paths);err=float(np.linalg.norm(f,np.inf))
        row={'k':k,'ell':l,'extra_edge':extra,'input':I,'exit':E,'inf_scaled_residual':err,
             'p':float(p),'q':float(q),'lead':float(lead),'evaluations':int(fit.nfev),'success':bool(fit.success)}
        rows.append(row);print(row,flush=True)
        if best is None or err<best[0]:best=(err,row,edges,fit.x.copy(),G.copy(),alpha.copy(),gamma.copy())
        if err<1e-9:stop=True;break
    if stop:break
out=ROOT/'frontier-20261028-ph7-ten-edge-path-normalized-search-result-v1.json'
out.write_text(json.dumps({'attempted':len(rows),'runs':rows,'seconds':time.monotonic()-start,
 'best_residual':best[0]if best else None,'best_case':best[1]if best else None,'best_edges':best[2]if best else None,
 'best_variables':best[3].tolist()if best else None,'best_generator':best[4].tolist()if best else None,
 'best_input':best[5].tolist()if best else None,'best_exit':best[6].tolist()if best else None,
 'scope':'sampled 10-edge enrichments; path-normalized floating generator/numerator equations; no exact witness or exclusion'},indent=2)+'\n')
print('best',best[0]if best else None,'saved',out)
