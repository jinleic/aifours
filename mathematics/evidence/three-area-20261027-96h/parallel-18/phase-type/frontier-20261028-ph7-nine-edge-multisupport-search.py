#!/usr/bin/env python3
"""Search genuine nine-edge disjoint-triangle graphs with multiple PH supports.

Graph-ear generation and a rooted-triangle canonical form select candidates
with two disjoint triangle triples and a supported 4/5-path rectangle. Uses
actual row-generator and full determinant/adjugate coefficients; numerical
near-fits are proposals only, never PH witnesses or family exclusions.
"""
from collections import deque
from itertools import combinations,permutations,product
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
rng=np.random.default_rng(20270102);start=time.monotonic();WALL=100;z=8/9
base={(0,1),(1,2),(2,0)};graphs=set()
for n1 in range(5):
 n2=4-n1;old=3+n1
 for a,b in product(range(3),repeat=2):
  if n1==0 and a==b:continue
  p=[a]+list(range(3,old))+[b];E=set(zip(p,p[1:]))
  if len(E)!=len(p)-1 or E&base:continue
  for c,d in product(range(old),repeat=2):
   if n2==0 and c==d:continue
   q=[c]+list(range(old,7))+[d];F=set(zip(q,q[1:]));gg=frozenset(base|E|F)
   if len(F)==len(q)-1 and not(F&(base|E)) and len(gg)==9:graphs.add(gg)

def facts(G):
 adj=[[]for _ in range(7)]
 for i,j in G:adj[i].append(j)
 ori=[a for a in permutations(range(7),3)if a[0]==min(a)and all((a[i],a[(i+1)%3])in G for i in range(3))]
 triangles=set(frozenset(a)for a in ori);dist=[[99]*7 for _ in range(7)];p5=[[False]*7 for _ in range(7)]
 for src in range(7):
  dist[src][src]=0;queue=deque([src])
  while queue:
   i=queue.popleft()
   for j in adj[i]:
    if dist[src][j]>dist[src][i]+1:dist[src][j]=dist[src][i]+1;queue.append(j)
  def dfs(i,path):
   if len(path)==6:p5[src][i]=True;return
   for j in adj[i]:
    if j not in path:dfs(j,path+[j])
  dfs(src,[src])
 return ori,triangles,dist,p5

def canon(G,ori):
 best=None
 for tri in ori:
  for shift in range(3):
   anchor=tri[shift:]+tri[:shift];rest=[i for i in range(7)if i not in tri]
   for tail in permutations(rest):
    mp={v:i for i,v in enumerate(anchor+tail)};bits=sum(1<<(7*mp[i]+mp[j])for i,j in G)
    if best is None or bits<best:best=bits
 return best

def supports(dist,p5):
 result=[]
 for mask in range(1,128):
  I=tuple(i for i in range(7)if mask>>i&1);allowed=[j for j in range(7)if all(dist[i][j]>=4 for i in I)]
  for emask in range(1,1<<len(allowed)):
   E=tuple(allowed[j]for j in range(len(allowed))if emask>>j&1)
   if any(dist[i][j]==4 for i in I for j in E)and any(p5[i][j]for i in I for j in E):result.append((I,E))
 result.sort(key=lambda v:(len(v[0])+len(v[1]),v))
 return [v for v in result if not any(set(a)<=set(v[0])and set(b)<=set(v[1])and(a,b)!=v for a,b in result)]

uniq={}
for G in sorted(graphs,key=lambda g:tuple(sorted(g))):
 ori,tr,dist,p5=facts(G);key=canon(G,ori)
 if key not in uniq:uniq[key]=(G,tr,dist,p5)
candidates=[]
for key,(G,tr,dist,p5)in sorted(uniq.items()):
 if not any(a.isdisjoint(b)for a,b in combinations(tr,2)):continue
 su=supports(dist,p5)
 if su:candidates.append((key,G,su))
print('rooted ear labelled',len(graphs),'isomorphs',len(uniq),'disjoint-triangle support candidates',len(candidates),flush=True)

def calc(x,edges,I,E):
 G=np.zeros((7,7));m=len(edges)
 for rate,(i,j)in zip(x[:m],edges):G[i,j]=rate
 G[np.arange(7),np.arange(7)]=-G.sum(1)
 beta=np.zeros(7);beta[list(I)]=x[m:m+len(I)];beta/=beta.sum()
 gam=np.zeros(7);gam[list(E)]=x[m+len(I):];gam/=gam.sum()
 B=np.eye(7);co=[1.];ad=[B.copy()]
 for k in range(1,8):
  A=G@B;c=-np.trace(A)/k;co.append(c);B=A+c*np.eye(7)
  if k<=6:ad.append(B.copy())
 p=co[1]-4;q=co[2]-4*p-(6+2*z);target=np.convolve([1.,4.,6+2*z,4+4*z,(1+z)**2,0.],[1.,p,q]);cs=np.array(co)
 num=np.array([beta@ad[k]@gam for k in (4,5,6)]);lead=num[0]
 f=(cs[3:7]-target[3:7])/(1+np.abs(target[3:7]));g=np.array([num[1]-p*lead,num[2]-q*lead])/(1+abs(lead)+np.abs(num[1:]))
 return np.r_[f,g,min(p,0.),min(q,0.),min(lead,0.)],p,q,lead,G,beta,gam

rows=[];best=None
for graph_index,(key,G,sus)in enumerate(candidates):
 edges=sorted(G);chosen=sus[:2]
 for I,E in chosen:
  for run in range(4):
   if time.monotonic()-start>WALL:break
   n=len(edges)+len(I)+len(E);x0=np.r_[rng.uniform(.3,2.5,len(edges)),rng.uniform(.1,1.,len(I)+len(E))]
   fit=least_squares(lambda x:calc(x,edges,I,E)[0],x0,bounds=(np.full(n,1e-8),np.full(n,20.)),max_nfev=1200,
       ftol=1e-12,xtol=1e-12,gtol=1e-12)
   f,p,q,lead,mat,beta,gam=calc(fit.x,edges,I,E);err=float(np.linalg.norm(f,np.inf))
   row={'graph_index':graph_index,'canonical_key':str(key),'I':I,'E':E,'start':run,'max_scaled_residual':err,'nfev':int(fit.nfev)};rows.append(row)
   if best is None or err<best[0]:best=(err,key,edges,I,E,fit.x.copy(),mat.copy(),beta.copy(),gam.copy())
   if err<1e-9:print('NUMERICAL CANDIDATE, not witness:',row,flush=True);break
  if time.monotonic()-start>WALL or (best and best[0]<1e-9):break
 if time.monotonic()-start>WALL or (best and best[0]<1e-9):break
out=ROOT/'frontier-20261028-ph7-nine-edge-multisupport-search-result.json'
out.write_text(json.dumps({'generated_labeled_graphs':len(graphs),'isomorph_count':len(uniq),'candidate_graphs':len(candidates),
 'runs':rows,'best_scaled_residual':best[0]if best else None,'best_key':str(best[1])if best else None,
 'best_edges':best[2]if best else None,'best_supports':best[3:5]if best else None,
 'best_variables':best[5].tolist()if best else None,'best_generator':best[6].tolist()if best else None,
 'best_beta':best[7].tolist()if best else None,'best_gamma':best[8].tolist()if best else None,
 'elapsed_seconds':time.monotonic()-start,
 'scope':'selected nine-edge graphs with disjoint triangles, first two minimal multi-support patterns; numeric near-fit only, no witness or exclusion'},indent=2)+'\n')
print('best numerical residual',best[0]if best else None,'saved:',out)
