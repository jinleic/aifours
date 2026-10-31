#!/usr/bin/env python3
"""Gauge-fixed projected Adam exploration of the 6D complement graph.
Numerical leads are never exact witnesses or proofs of impossibility.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-parity-core-6d-projection-v1.json';raw=src.read_bytes();d=json.loads(raw);E=d['edges'];blocks=np.array(d['blocks']);assert len(E)==45 and blocks.shape==(15,6)
anchor=blocks[0];pos={int(e):i for i,e in enumerate(anchor)};mask=np.ones((45,6),bool)
for b in blocks[1:]:
 for e in b:
  for a in b:
   if int(a)in pos and int(e)!=int(a):mask[e,pos[int(a)]]=False
mask[anchor]=False

def project(X):
 X[~mask]=0
 for e,i in pos.items():X[e,i]=1
 n=np.linalg.norm(X,axis=1);assert np.all(n>0);X/=n[:,None];return X

def calc(X,weight=.3,threshold=.98):
 G=X@X.conj().T;grad=np.zeros_like(X);loss=0.
 for ids in blocks:
  W=X[ids];R=W@W.conj().T-np.eye(6);loss+=float(np.sum(np.abs(R)**2));grad[ids]+=4*R@W
 v=np.maximum(np.abs(G)**2-threshold**2,0);np.fill_diagonal(v,0);loss+=float(weight*np.sum(v*v)/2);grad+=4*weight*(v*G)@X;grad[~mask]=0
 return loss,grad

def metrics(X):
 e=max(float(np.max(np.abs(X[ids]@X[ids].conj().T-np.eye(6))))for ids in blocks);G=np.abs(X@X.conj().T);np.fill_diagonal(G,0);return e,float(G.max())
# Independent finite directional derivative check on nonprojected smooth objective.
rng=np.random.default_rng(61029);X=project(rng.normal(size=(45,6))+1j*rng.normal(size=(45,6)));dX=rng.normal(size=X.shape)+1j*rng.normal(size=X.shape);dX[~mask]=0;dX/=np.linalg.norm(dX)
l,g=calc(X);eps=1e-6;fd=(calc(X+eps*dX)[0]-calc(X-eps*dX)[0])/(2*eps);ge=abs(float(np.real(np.vdot(g,dX)))-fd);assert ge<1e-5
runs=[];start=time.monotonic()
for seed in range(30):
 X=project(rng.normal(size=(45,6))+1j*rng.normal(size=(45,6)));m=np.zeros_like(X);v=np.zeros((45,6));best=(1e9,1e9,0);bestX=None
 for it in range(1,6001):
  _,g=calc(X);m=.9*m+.1*g;v=.999*v+.001*np.abs(g)**2;X=project(X-.018*(m/(1-.9**it))/(np.sqrt(v/(1-.999**it))+1e-8))
  if it%100==0:
   e,o=metrics(X)
   if e<best[0]:best=(e,o,it);bestX=X.copy()
   if e<1e-10 and o<1-1e-8:break
 runs.append({'seed':seed,'best_error':best[0],'max_ray_overlap':best[1],'best_iteration':best[2],
  'vectors_real':bestX.real.tolist(),'vectors_imag':bestX.imag.tolist()})
 print('seed',seed,'error',best[0],'overlap',best[1],'iteration',best[2],flush=True)
 if best[0]<1e-10 and best[1]<1-1e-8:break
 if time.monotonic()-start>100:break
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'gradient_directional_error':ge,'status':'FLOATING_HEURISTIC_ONLY','runs':runs,
 'scope':'One 6D complement graph only; no exact witness, no full QLS10, no no-go.'}
(P/'frontier-20261029-parity-core-6d-gauge-adam-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print('finished',obj['clock_finish'])
