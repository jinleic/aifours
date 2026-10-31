#!/usr/bin/env python3
"""Bounded FLOATING covariance Schmidt-number screen, never a proof."""
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
import numpy as np
path='frontier-20261028-grid-realignment-search.py'
expected='31b039391e0076e6812b26d93d09fb5646fa8adacf59482ae098feabacaa33f1'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['results'])==2
rng=np.random.default_rng(2026102801)
def mat(a,b):
 x=rng.normal(size=(a,b))+1j*rng.normal(size=(a,b));return x/np.linalg.norm(x)
def score(rho,da,db):
 rho=rho/np.trace(rho).real;v=rho.reshape(da,db,da,db)
 A=np.trace(v,axis1=1,axis2=3);B=np.trace(v,axis1=0,axis2=2)
 pa=np.trace(A@A).real;pb=np.trace(B@B).real
 C=(rho-np.kron(A,B)).reshape(da,db,da,db).transpose(0,2,1,3).reshape(da*da,db*db)
 cn=np.linalg.svd(C,compute_uv=False).sum()
 return float(cn-1-np.sqrt(max(0,1-pa)*max(0,1-pb)))
def proj(rho,A,B):
 K=np.kron(A,B);return K@rho@K.conj().T
out=[]
for da,db,edges in ((4,5,h['S45']),(5,5,h['S55'])):
 rho=h['rho_from_edges'](da,db,edges);baseline=score(rho,da,db);best=(-1e99,None,None);vals=[]
 for _ in range(3000):
  A=mat(4,da);B=mat(4,db);v=score(proj(rho,A,B),4,4);vals.append(v)
  if v>best[0]:best=(v,A,B)
 value,A,B=best;accepted=0
 for j in range(3000):
  f=.2*(.05**(j/2999));AA=A+f*mat(4,da);BB=B+f*mat(4,db);AA/=np.linalg.norm(AA);BB/=np.linalg.norm(BB)
  v=score(proj(rho,AA,BB),4,4)
  if v>value:value,A,B=v,AA,BB;accepted+=1
 out.append({'source_shape':[da,db],'source_covariance_gap_float':baseline,
 'random_candidates':3000,'random_median_gap_float':float(np.median(vals)),
 'random_best_gap_float':best[0],'hill_steps':3000,'hill_accepted':accepted,'refined_best_gap_float':value})
print(json.dumps({'seed':2026102801,'results':out,'criterion':'Liu et al arXiv:2208.04909v3 Corollary 1, r=2: ||R(rho-rho_A⊗rho_B)||_1 <= 1+sqrt((1-purity_A)(1-purity_B))',
 'limits':'Floating exploratory only. Positive gap requires exact inequality/PPT and an explicit valid 2-block-positive witness; nonpositive gaps exclude nothing outside the sampled maps/criterion.',
 'previous_realign_search_replayed':True,'previous_checker_sha256':expected},indent=2))
