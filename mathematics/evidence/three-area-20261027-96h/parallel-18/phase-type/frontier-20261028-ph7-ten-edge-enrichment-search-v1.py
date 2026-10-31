#!/usr/bin/env python3
"""Bounded numerical PH search on 10-edge enrichments of triangle templates.

Searches actual common row generator, input, exit, characteristic, and
adjugate equations. A near-fit is a proposal, NOT a witness or exclusion.
Only 9-edge disjoint-triangle templates plus one extra arc are sampled.
"""
from collections import deque
from itertools import combinations,product
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20270119);started=time.monotonic();WALL=45

def graph(k,ell):
    return {(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(3+k,6),(6,(-ell)%3)}


def supports(edges):
    adj=[[j for i,j in edges if i==v] for v in range(7)]
    dist=[[99]*7 for _ in range(7)];path5=[[False]*7 for _ in range(7)]
    for src in range(7):
        dist[src][src]=0;todo=deque([src])
        while todo:
            i=todo.popleft()
            for j in adj[i]:
                if dist[src][j]>dist[src][i]+1:dist[src][j]=dist[src][i]+1;todo.append(j)
        def visit(i,seen):
            if len(seen)==6:path5[src][i]=True;return
            for j in adj[i]:
                if j not in seen:visit(j,seen+(j,))
        visit(src,(src,))
    valid=[]
    for mask in range(1,128):
        I=tuple(i for i in range(7)if mask>>i&1)
        allowed=[j for j in range(7)if all(dist[i][j]>=4 for i in I)]
        for emask in range(1,1<<len(allowed)):
            E=tuple(allowed[j]for j in range(len(allowed))if emask>>j&1)
            if any(dist[i][j]==4 for i in I for j in E) and any(path5[i][j]for i in I for j in E):valid.append((I,E))
    valid.sort(key=lambda pair:(len(pair[0])+len(pair[1]),pair))
    return [v for v in valid if not any(set(a)<=set(v[0])and set(b)<=set(v[1])and(a,b)!=v for a,b in valid)]


def residual(x,edges,I,E):
    n=len(edges);G=np.zeros((7,7))
    for value,(i,j)in zip(x[:n],edges):G[i,j]=value
    G[np.arange(7),np.arange(7)]=-G.sum(1)
    alpha=np.zeros(7);alpha[list(I)]=x[n:n+len(I)];alpha/=alpha.sum()
    gamma=np.zeros(7);gamma[list(E)]=x[n+len(I):];gamma/=gamma.sum()
    B=np.eye(7);cs=[1.];adj=[B.copy()]
    for k in range(1,8):
        Z=G@B;v=-np.trace(Z)/k;cs.append(v);B=Z+v*np.eye(7)
        if k<=6:adj.append(B.copy())
    z=8/9;p=cs[1]-4;q=cs[2]-4*p-(6+2*z)
    target=np.convolve([1,4,6+2*z,4+4*z,(1+z)**2,0],[1,p,q])
    spectrum=(np.array(cs[3:7])-target[3:7])/(1+np.abs(target[3:7]))
    nums=np.array([alpha@adj[k]@gamma for k in (4,5,6)]);lead=nums[0]
    numerator=np.array([nums[1]-p*lead,nums[2]-q*lead])/(1+abs(lead)+np.abs(nums[1:]))
    return np.r_[spectrum,numerator,min(p,0),min(q,0),min(lead,0)],p,q,lead,G,alpha,gamma

pairs=[(i,j)for i in range(7)for j in range(7)if i!=j]
rows=[];best=None;stop=False
for k,ell in product(range(3),repeat=2):
    base=graph(k,ell);extras=[e for e in pairs if e not in base];rng.shuffle(extras)
    for extra in extras[:4]:
        if time.monotonic()-started>WALL:stop=True;break
        edges=sorted(base|{extra});choices=supports(edges)
        if not choices:continue
        I,E=choices[int(rng.integers(min(4,len(choices))))]
        n=len(edges)+len(I)+len(E)
        lo=np.full(n,1e-7);hi=np.r_[np.full(len(edges),20.),np.full(len(I)+len(E),1.)]
        x0=np.r_[rng.uniform(.2,2.5,len(edges)),rng.uniform(.1,1.,len(I)+len(E))]
        fit=least_squares(lambda v:residual(v,edges,I,E)[0],x0,bounds=(lo,hi),max_nfev=900,
                          ftol=1e-11,xtol=1e-11,gtol=1e-11)
        v,p,q,lead,G,alpha,gamma=residual(fit.x,edges,I,E);err=float(np.linalg.norm(v,np.inf))
        row={'k':k,'ell':ell,'extra_edge':extra,'input':I,'exit':E,'inf_scaled_residual':err,
             'p':float(p),'q':float(q),'lead':float(lead),'evaluations':int(fit.nfev),'success':bool(fit.success)}
        rows.append(row);print(row,flush=True)
        if best is None or err<best[0]:best=(err,row,edges,fit.x.copy(),G.copy(),alpha.copy(),gamma.copy())
        if err<1e-9:stop=True;break
    if stop:break
out=ROOT/'frontier-20261028-ph7-ten-edge-enrichment-search-result-v1.json'
out.write_text(json.dumps({'runs':rows,'attempted':len(rows),'elapsed_seconds':time.monotonic()-started,
  'best_residual':best[0]if best else None,'best_case':best[1]if best else None,'best_edges':best[2]if best else None,
  'best_variables':best[3].tolist()if best else None,'best_generator':best[4].tolist()if best else None,
  'best_input':best[5].tolist()if best else None,'best_exit':best[6].tolist()if best else None,
  'scope':'bounded numerical search over sampled 10-edge enrichments and one support rectangle each; no witness, infeasibility, or global optimum'},indent=2)+'\n')
print('best',best[0]if best else None,'saved',out)
