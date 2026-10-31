#!/usr/bin/env python3
"""Bounded nonuniform full-vector resolution search seeded from q18 QLS."""
from pathlib import Path
import json,time,numpy as np
P=Path(__file__).resolve().parent
S=json.loads((P/'frontier-20261028-nonbinary-best-transversal-v1.json').read_text())
case=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'][S['case_0based']]
K=np.exp(2j*np.pi*np.array(case['K_exponents_mod18'])/18);n=10
F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/10)
orig=(F[:,:,None]*K[:,None,:]/np.sqrt(n)).reshape(10,100)
V0=orig[:,:10].conj().T@orig
assert np.max(np.abs(V0[:,:10]-np.eye(n)))<1e-12
perm=S['columns_by_row'];assert set(perm)==set(range(10))
rowof=[0]*10
for r,c in enumerate(perm):rowof[c]=r
L=[[(r-rowof[c])%10 for c in range(10)]for r in range(10)]
blocks=[tuple(10*r+c for c in range(n)) for r in range(n)]
blocks += [tuple(10*r+c for r in range(n)) for c in range(n)]
blocks += [tuple(10*r+c for r in range(n) for c in range(n) if L[r][c]==t) for t in range(n)]
assert len(blocks)==30 and all(len(b)==10 for b in blocks)
mask=np.zeros((10,100),bool)
for r in range(1,10):
 for c in range(10):
  other=perm[(rowof[c]-r)%10];assert c!=other
  mask[:,10*r+c]=True;mask[c,10*r+c]=False;mask[other,10*r+c]=False
def project(v):
 v[~mask]=0;v[:,:10]=np.eye(10);v[:,10:]/=np.linalg.norm(v[:,10:],axis=0);return v
def obj(v,penalty=.3,threshold=.97):
 g=np.zeros_like(v);loss=0.
 for bb in blocks:
  ix=list(bb);B=v[:,ix];E=B.conj().T@B-np.eye(10)
  loss+=float(np.sum(np.abs(E)**2));g[:,ix]+=4*B@E
 G=v.conj().T@v;ex=np.maximum(np.abs(G)**2-threshold**2,0);np.fill_diagonal(ex,0)
 loss+=float(penalty*np.sum(ex**2)/2);g+=4*penalty*v@(ex*G);g[~mask]=0
 return loss,g
def metrics(v):
 G=v.conj().T@v;err=max(float(np.max(np.abs(G[np.ix_(b,b)]-np.eye(10)))) for b in blocks)
 B=np.abs(G.copy());np.fill_diagonal(B,0)
 return {'max_block_gram_error':err,'max_overlap':float(np.max(B)),
         'near_parallel_pairs':int(np.count_nonzero(np.triu(B>1-1e-8,1)))}
seed=project(V0.copy());rng=np.random.default_rng(410223)
probe=seed+.03*(rng.normal(size=(10,100))+1j*rng.normal(size=(10,100)))
direction=rng.normal(size=(10,100))+1j*rng.normal(size=(10,100))
direction[~mask]=0;direction/=np.linalg.norm(direction)
_,g0=obj(probe);eps=1e-6
fd=(obj(probe+eps*direction)[0]-obj(probe-eps*direction)[0])/(2*eps)
err=abs(float(np.real(np.vdot(g0,direction)))-fd)
print('gradient finite-difference error',err,flush=True);assert err<1e-5
start=time.monotonic();best=None;runs=[]
for run in range(24):
 sigma=(0,.01,.03,.08,.15,.3,.6,1.0)[run%8]
 v=project(seed+sigma*(rng.normal(size=(10,100))+1j*rng.normal(size=(10,100))))
 m=np.zeros_like(v);h=np.zeros(v.shape)
 for step in range(1,4001):
  loss,g=obj(v);m=.9*m+.1*g;h=.999*h+.001*np.abs(g)**2
  v-=.025*(m/(1-.9**step))/(np.sqrt(h/(1-.999**step))+1e-8);project(v)
  if step%100==0 or step==1:
   met=metrics(v);score=met['max_block_gram_error']+max(0,met['max_overlap']-.999)
   if best is None or score<best[0]:best=(score,v.copy(),run,step,met)
   if met['max_block_gram_error']<1e-10 and met['max_overlap']<1-1e-8:
    print('NUMERIC_CANDIDATE_REQUIRES_EXACT_VECTOR_CERTIFICATE',run,step,met,flush=True);break
  if time.monotonic()-start>50:break
 runs.append({'run':run,'sigma':sigma,'steps':step,'loss_before_update':loss,**met})
 print('run',run,'sigma',sigma,'steps',step,'metrics',met,flush=True)
 if time.monotonic()-start>50:break
np.save(P/'frontier-20261028-nonbinary-seeded-resolution-best-v1.npy',best[1],allow_pickle=False)
out={'scope':'fixed cyclic-isotope L, coupled nonuniform actual-vector float search; no exact witness/no-go',
 'source_case':S['case_0based'],'base_transversal_permutation':perm,'seed':410223,
 'elapsed':time.monotonic()-start,'runs':runs,'best_run':best[2],'best_step':best[3],'best_metrics':best[4]}
(P/'frontier-20261028-nonbinary-seeded-resolution-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best[4],flush=True)
