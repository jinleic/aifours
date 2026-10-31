#!/usr/bin/env python3
"""Bounded candidate search at z=8/9 on three genuine nine-edge graphs.

Uses literal row-generator determinant and adjugate coefficients, preserving
single-source/single-exit shortest-path distance4. Any numerical near-fit is a
proposal only, not an exact algebraic or PH witness; misses never exclude.
"""
from collections import deque
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20261209);z=8/9;START=time.monotonic();WALL=100
GRAPHS={
 'triangle-crossing-2-long5':[(0,1),(1,2),(2,0),(0,3),(3,0),(3,4),(4,5),(5,6),(6,0)],
 'three-triangles':[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(0,5),(5,6),(6,0)],
 'triangle-4cycle-2cycle':[(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,0),(0,6),(6,0)]}

def pairs(edges):
 out=[]
 for src in range(7):
  dist=[99]*7;dist[src]=0;todo=deque([src])
  while todo:
   i=todo.popleft()
   for a,b in edges:
    if a==i and dist[b]>dist[i]+1:dist[b]=dist[i]+1;todo.append(b)
  out.extend((src,dst)for dst in range(7)if dist[dst]==4)
 return out

def calc(x,edges,src,dst):
 G=np.zeros((7,7))
 for rate,(i,j)in zip(x,edges):G[i,j]=rate
 G[np.arange(7),np.arange(7)]=-G.sum(axis=1)
 B=np.eye(7);coeff=[1.];adj=[B.copy()]
 for k in range(1,8):
  A=G@B;c=-np.trace(A)/k;coeff.append(c);B=A+c*np.eye(7)
  if k<=6:adj.append(B.copy())
 p=coeff[1]-4;q=coeff[2]-4*p-(6+2*z)
 target=np.convolve([1.,4.,6+2*z,4+4*z,(1+z)**2,0.],[1.,p,q]);cs=np.array(coeff)
 num=np.array([adj[k][src,dst]for k in (4,5,6)]);lead=num[0]
 f=(cs[3:7]-target[3:7])/(1+np.abs(target[3:7]));g=np.array([num[1]-p*lead,num[2]-q*lead])/(1+abs(lead)+np.abs(num[1:]))
 return np.r_[f,g,min(p,0.),min(q,0.),min(lead,0.)],p,q,lead,G

rows=[];best=None
for name,edges in GRAPHS.items():
 ps=pairs(edges);print('graph',name,'distance-four pairs',ps,flush=True)
 for src,dst in ps:
  for j in range(5):
   if time.monotonic()-START>WALL:break
   x0=rng.uniform(.3,2.5,len(edges))
   fit=least_squares(lambda x:calc(x,edges,src,dst)[0],x0,bounds=(np.full(len(edges),1e-7),np.full(len(edges),20.)),
      max_nfev=1200,ftol=1e-12,xtol=1e-12,gtol=1e-12)
   residual,p,q,lead,G=calc(fit.x,edges,src,dst);err=float(np.linalg.norm(residual,np.inf))
   row={'graph':name,'source':src,'exit':dst,'start':j,'max_scaled_residual':err,'nfev':int(fit.nfev),
        'p':p,'q':q,'numerator_lead':lead};rows.append(row)
   if best is None or err<best[0]:best=(err,name,src,dst,fit.x.copy(),G.copy())
   if err<1e-9:print('NUMERICAL CANDIDATE only:',row,flush=True);break
  if time.monotonic()-START>WALL or (best and best[0]<1e-9):break
 if time.monotonic()-START>WALL or (best and best[0]<1e-9):break
out=ROOT/'frontier-20261028-ph7-nine-edge-transfer-search-result.json'
out.write_text(json.dumps({'z':'8/9','runs':rows,'best_scaled_residual':best[0]if best else None,
 'best_graph':best[1]if best else None,'best_source_exit':list(best[2:4])if best else None,
 'best_edge_rates':best[4].tolist()if best else None,'best_generator':best[5].tolist()if best else None,
 'elapsed_seconds':time.monotonic()-START,'scope':'three specific nine-edge graphs/single source-exit; numerical proposal only, not exact witness or exclusion'},indent=2)+'\n')
print('best numerical residual:',best[0]if best else None,'saved:',out)
