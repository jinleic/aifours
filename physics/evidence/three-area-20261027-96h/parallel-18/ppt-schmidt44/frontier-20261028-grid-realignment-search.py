#!/usr/bin/env python3
"""Bounded FLOATING exploratory realignment search, not a proof of any claim."""
import json
import numpy as np
rng=np.random.default_rng(20261028)

def rho_from_edges(da,db,edges):
 M=np.zeros((da*db,da*db),dtype=np.complex128)
 for weight,terms in edges:
  q=np.zeros(da*db,dtype=np.complex128)
  for a,b,c in terms:q[a*db+b]+=c
  M+=weight*np.outer(q,q.conj())
 return M

def e(weight,*pairs):return weight,[(a,b,c) for a,b,c in pairs]
S45=[e(1,(0,0,1),(1,1,1),(2,2,1)),e(1,(0,1,1),(1,2,1)),
 e(1,(1,0,1),(2,1,-1)),e(3,(0,2,1),(3,4,1)),e(3,(2,0,1),(3,3,1)),
 e(3,(2,3,1)),e(3,(3,0,1)),e(3,(3,2,1)),e(3,(0,4,1))]
S55=[e(1,(0,2,1),(1,1,1),(2,0,1)),e(1,(0,0,1)),e(1,(0,1,1)),e(1,(1,0,1)),
 e(1,(1,2,1),(3,4,1)),e(1,(1,4,1)),e(1,(2,1,1),(4,3,1)),
 e(1,(2,2,1),(3,3,1)),e(2,(2,3,1)),e(2,(3,2,1)),e(1,(4,1,1))]
def score(rho,da,db):
 tr=np.trace(rho).real
 if not tr>1e-15:return float('nan')
 mat=rho.reshape(da,db,da,db).transpose(0,2,1,3).reshape(da*da,db*db)
 return float(np.linalg.svd(mat,compute_uv=False).sum()/tr)
def randmat(a,b):
 m=rng.normal(size=(a,b))+1j*rng.normal(size=(a,b));return m/np.linalg.norm(m)
def project(rho,A,B):
 K=np.kron(A,B);return K@rho@K.conj().T
def candidate_sample(rho,da,db,count):
 best=(-1,None,None);scores=[]
 for _ in range(count):
  A=randmat(4,da);B=randmat(4,db);v=score(project(rho,A,B),4,4)
  scores.append(v)
  if v>best[0]:best=(v,A,B)
 return best,float(np.median(scores))
def hill(rho,A,B,initial,steps):
 best=initial;accepted=0
 for j in range(steps):
  fac=0.2*(0.05**(j/max(1,steps-1)))
  AA=A+fac*randmat(*A.shape);BB=B+fac*randmat(*B.shape)
  AA/=np.linalg.norm(AA);BB/=np.linalg.norm(BB)
  v=score(project(rho,AA,BB),4,4)
  if v>best:best,A,B=v,AA,BB;accepted+=1
 return best,accepted
out=[]
for da,db,edges in ((4,5,S45),(5,5,S55)):
 rho=rho_from_edges(da,db,edges);baseline=score(rho,da,db)
 (best,A,B),median=candidate_sample(rho,da,db,3000)
 refined,accepted=hill(rho,A,B,best,3000)
 out.append({'source_shape':[da,db],'source_ratio_float':baseline,
             'random_candidates':3000,'random_median_float':median,'random_best_float':best,
             'hill_steps':3000,'hill_accepted':accepted,'refined_best_float':refined})
print(json.dumps({'seed':20261028,'results':out,
 'limits':'Floating exploratory scores only. A value >2 requires exact valid-witness and PPT certification. Values <=2 do NOT exclude other maps, witnesses or SN3.'},indent=2))
