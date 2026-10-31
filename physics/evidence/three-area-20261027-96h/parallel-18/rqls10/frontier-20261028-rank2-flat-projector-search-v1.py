#!/usr/bin/env python3
"""Bounded float search for rank-two 5D projections flat in three fixed MUBs."""
from itertools import combinations
from pathlib import Path
import json,time,numpy as np
n=5;omega=np.exp(2j*np.pi/n);v=np.arange(n)
U=omega**(3*np.outer(v,v))/np.sqrt(n);D=np.diag(omega**(4*v*v));V=D@U
bases=[np.eye(n),U,V]
known=[]
for power in (2,3,4):
    W=np.linalg.matrix_power(D,power)@U
    for pair in combinations(range(n),2):
        Y=W[:,pair];known.append(Y@Y.conj().T)
def evaluate(Y):
    cost=0.;g=np.zeros_like(Y)
    for B in bases:
        W=B.conj().T@Y;e=np.sum(np.abs(W)**2,axis=1)-.4
        cost+=float(e@e);g+=4*B@(e[:,None]*W)
    return cost,g-Y@((Y.conj().T@g+g.conj().T@Y)/2)
rng=np.random.default_rng(65240);start=time.monotonic();runs=[];best_exotic=None;best_any=None
for run in range(250):
    Y,_=np.linalg.qr(rng.normal(size=(n,2))+1j*rng.normal(size=(n,2)))
    for step in range(1,4001):
        cost,g=evaluate(Y)
        if cost<1e-20:break
        Y,_=np.linalg.qr(Y-.25*g)
        if time.monotonic()-start>60:break
    cost,_=evaluate(Y);proj=Y@Y.conj().T
    distance=min(float(np.linalg.norm(proj-p)) for p in known)
    runrec={'run':run,'steps':step,'cost':cost,'nearest_30_standard_distance':distance}
    runs.append(runrec)
    if best_any is None or cost<best_any[0]:best_any=(cost,proj.copy(),distance,run)
    if cost<1e-14 and (best_exotic is None or distance>best_exotic[0]):best_exotic=(distance,proj.copy(),cost,run)
    if run%25==0:print('run',run,'cost',cost,'distance',distance,flush=True)
    if time.monotonic()-start>60:break
P=Path(__file__).resolve().parent
if best_exotic is not None:np.save(P/'frontier-20261028-rank2-flat-projector-exotic-v1.npy',best_exotic[1],allow_pickle=False)
out={'scope':'floating rank2 projection only; not full MUB triple or QLS',
     'seed':65240,'elapsed':time.monotonic()-start,'runs':runs,
     'best_cost':best_any[0],'best_distance':best_any[2],'best_run':best_any[3],
     'largest_distance_below_1e-14':best_exotic[0] if best_exotic else None,
     'exotic_cost':best_exotic[2] if best_exotic else None}
(P/'frontier-20261028-rank2-flat-projector-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('best',best_any[0],'largest_near_zero_distance',best_exotic[0] if best_exotic else None,flush=True)
