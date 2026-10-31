#!/usr/bin/env python3
"""Bounded nonuniform actual-vector search, Parker incidence, 24 q18 seeds."""
from pathlib import Path
import json,time,numpy as np
P=Path(__file__).resolve().parent;n=10;N=100
cases=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'];assert len(cases)==24
L=json.loads((P/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']['labels']
assert all(set(row)==set(range(n)) for row in L) and all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
inv={L[0][c]:c for c in range(n)}
blocks=[tuple(10*r+c for c in range(n)) for r in range(n)]+[tuple(10*r+c for r in range(n)) for c in range(n)]
blocks += [tuple(10*r+c for r in range(n) for c in range(n) if L[r][c]==t) for t in range(n)]
mask=np.zeros((n,N),bool)
for r in range(1,n):
 for c in range(n):
  k=inv[L[r][c]];assert k!=c
  mask[:,10*r+c]=True;mask[c,10*r+c]=False;mask[k,10*r+c]=False
def project(v):
 v[~mask]=0;v[:,:10]=np.eye(n);v[:,10:]/=np.linalg.norm(v[:,10:],axis=0);return v
def objective(v,penalty=.3,threshold=.97):
 g=np.zeros_like(v);loss=0.
 for bb in blocks:
  ix=list(bb);B=v[:,ix];e=B.conj().T@B-np.eye(n);loss+=float(np.sum(np.abs(e)**2));g[:,ix]+=4*B@e
 G=v.conj().T@v;ex=np.maximum(abs(G)**2-threshold**2,0);np.fill_diagonal(ex,0)
 loss+=float(penalty*np.sum(ex**2)/2);g+=4*penalty*v@(ex*G);g[~mask]=0
 return loss,g
def metrics(v):
 G=v.conj().T@v;err=max(float(np.max(np.abs(G[np.ix_(b,b)]-np.eye(n))))for b in blocks)
 off=abs(G.copy());np.fill_diagonal(off,0)
 return {'max_block_gram_error':err,'max_overlap':float(np.max(off)),'near_parallel_pairs':int(np.count_nonzero(np.triu(off>1-1e-8,1)))}
F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n);seeds=[]
for case in cases:
 K=np.exp(2j*np.pi*np.array(case['K_exponents_mod18'])/18)
 V=(F[:,:,None]*K[:,None,:]/np.sqrt(n)).reshape(n,N);V=V[:,:10].conj().T@V
 assert np.max(abs(V[:,:10]-np.eye(n)))<1e-12
 seeds.append(project(V))
rng=np.random.default_rng(250913);probe=seeds[0]+.03*(rng.normal(size=(n,N))+1j*rng.normal(size=(n,N)))
dir=rng.normal(size=(n,N))+1j*rng.normal(size=(n,N));dir[~mask]=0;dir/=np.linalg.norm(dir)
_,g=objective(probe);eps=1e-6;fd=(objective(probe+eps*dir)[0]-objective(probe-eps*dir)[0])/(2*eps)
error=abs(float(np.real(np.vdot(g,dir)))-fd);print('gradient error',error,flush=True);assert error<1e-5
start=time.monotonic();best=None;runs=[]
for run in range(48):
 ix=run%24;sigma=(0,.08)[(run//24)%2];v=project(seeds[ix]+sigma*(rng.normal(size=(n,N))+1j*rng.normal(size=(n,N))))
 m=np.zeros_like(v);h=np.zeros(v.shape)
 for step in range(1,4001):
  loss,g=objective(v);m=.9*m+.1*g;h=.999*h+.001*abs(g)**2
  v-=.025*(m/(1-.9**step))/(np.sqrt(h/(1-.999**step))+1e-8);project(v)
  if step%100==0 or step==1:
   met=metrics(v);score=met['max_block_gram_error']+max(0,met['max_overlap']-.999)
   if best is None or score<best[0]:best=(score,v.copy(),run,step,met)
   if met['max_block_gram_error']<1e-10 and met['max_overlap']<1-1e-8:
    print('NUMERIC_CANDIDATE_REQUIRES_EXACT_CERTIFICATION',run,step,met,flush=True);break
  if time.monotonic()-start>50:break
 runs.append({'run':run,'case':ix,'sigma':sigma,'steps':step,'loss_preupdate':loss,**met})
 print('run',run,'case',ix,'steps',step,'metrics',met,flush=True)
 if time.monotonic()-start>50:break
np.save(P/'frontier-20261028-nonbinary-parker-resolution-best-v1.npy',best[1],allow_pickle=False)
out={'scope':'Parker L, unrestricted nonuniform actual vectors, q18 seeds; float heuristic only',
 'seed':250913,'elapsed':time.monotonic()-start,'runs':runs,'best_run':best[2],'best_step':best[3],'best_metrics':best[4]}
(P/'frontier-20261028-nonbinary-parker-resolution-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best[4],flush=True)
