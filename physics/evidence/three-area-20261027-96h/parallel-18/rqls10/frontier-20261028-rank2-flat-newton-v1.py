#!/usr/bin/env python3
"""Bounded floating LM search on Gr(2,5) for three flat diagonals only."""
from pathlib import Path
from itertools import combinations
import json,time,numpy as np
p=5;o=np.exp(2j*np.pi/p);v=np.arange(p);U=o**(3*np.outer(v,v))/np.sqrt(p)
D=np.diag(o**(4*v*v));bases=[np.eye(p),U,D@U]
known=[]
for power in (2,3,4):
 W=np.linalg.matrix_power(D,power)@U
 for cs in combinations(range(5),2):
  A=W[:,cs];known.append(A@A.conj().T)
def residual(Y):
 return np.concatenate([(np.sum(np.abs(B.conj().T@Y)**2,axis=1)-.4)[:4] for B in bases])
def jac(Y,Q):
 out=np.empty((12,12))
 for l in range(3):
  for k in range(2):
   for z in range(2):
    delta=Q[:,l:l+1]@np.eye(2,dtype=complex)[k:k+1,:]*(1 if z==0 else 1j)
    for h,B in enumerate(bases):
     BY=B.conj().T@Y;BD=B.conj().T@delta
     out[4*h:4*h+4,2*(2*l+k)+z]=(2*np.real(np.sum(np.conj(BY)*BD,axis=1)))[:4]
 return out
def retract(Y,Q,x):
 T=np.array([x[2*k]+1j*x[2*k+1] for k in range(6)]).reshape(3,2)
 return np.linalg.qr(Y+Q@T)[0]
rng=np.random.default_rng(55817);start=time.monotonic();runs=[];exotic=None
for run in range(200):
 Y=np.linalg.qr(rng.normal(size=(5,2))+1j*rng.normal(size=(5,2)))[0];lam=1e-3
 for step in range(1,501):
  r=residual(Y);cost=float(r@r)
  if cost<1e-22:break
  Q=np.linalg.qr(Y,mode='complete')[0][:,2:];J=jac(Y,Q)
  dx=np.linalg.solve(J.T@J+lam*np.eye(12),-J.T@r)
  if np.linalg.norm(dx)>1:dx/=np.linalg.norm(dx)
  candidate=retract(Y,Q,dx);rr=residual(candidate);cc=float(rr@rr)
  if cc<cost:Y=candidate;lam=max(lam/3,1e-14)
  else:lam=min(lam*10,1e8)
  if time.monotonic()-start>50:break
 r=residual(Y);cost=float(r@r);proj=Y@Y.conj().T
 dist=min(float(np.linalg.norm(proj-P)) for P in known)
 runs.append({'run':run,'step':step,'cost':cost,'distance_to_30_standard':dist})
 if cost<1e-18 and (exotic is None or dist>exotic[0]):exotic=(dist,cost,proj.copy(),run)
 if run%20==0:print('run',run,'cost',cost,'dist',dist,flush=True)
 if time.monotonic()-start>50:break
p=Path(__file__).resolve().parent
if exotic is not None:np.save(p/'frontier-20261028-rank2-flat-newton-best-v1.npy',exotic[2],allow_pickle=False)
out={'scope':'floating projections flat in three MUBs only; not full cross-phase or QLS',
     'seed':55817,'elapsed':time.monotonic()-start,'runs':runs,
     'max_distance_near_zero':exotic[0] if exotic else None,
     'associated_cost':exotic[1] if exotic else None}
(p/'frontier-20261028-rank2-flat-newton-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('largest distance at cost<1e-18',exotic[0] if exotic else None,'cost',exotic[1] if exotic else None,flush=True)
