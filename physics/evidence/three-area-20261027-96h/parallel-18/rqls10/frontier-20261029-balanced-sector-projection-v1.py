#!/usr/bin/env python3
"""Exploratory 5D sector incidence search on Weisner OLS10.
No floating iterate is a witness, even if residual is tiny. Exact original
vectors plus 30-context and 100-ray replay are required for success.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
R=('00 28 59 84 67 32 15 93 71 46','82 11 30 69 05 78 43 26 94 57','95 03 22 41 79 16 80 54 37 68','48 96 14 33 52 89 27 01 65 70','76 50 97 25 44 63 09 38 12 81','23 87 61 98 36 55 74 19 40 02','51 34 08 72 90 47 66 85 29 13','39 62 45 10 83 91 58 77 06 24','17 49 73 56 21 04 92 60 88 35','64 75 86 07 18 20 31 42 53 99')
A=np.array([[int(w[0])for w in row.split()]for row in R]);L=np.array([[int(w[1])for w in row.split()]for row in R]);assert len({(int(A[r,c]),int(L[r,c]))for r,c in itertools.product(range(10),repeat=2)})==100
contexts=[[10*r+c for c in range(10)]for r in range(10)]+[[10*r+c for r in range(10)]for c in range(10)]+[[10*r+c for r,c in itertools.product(range(10),repeat=2)if L[r,c]==t]for t in range(10)]
choices=[tuple(s)for s in itertools.combinations(range(10),5)if 0 in s];rng=np.random.default_rng(4411);rng.shuffle(choices);runs=[]
for si in range(12):
 S=set(choices[si]);cells=[10*r+c for r,c in itertools.product(range(10),repeat=2)if int(A[r,c])in S];idx={v:i for i,v in enumerate(cells)}
 blocks=np.array([[idx[v]for v in B if v in idx]for B in contexts]);assert blocks.shape==(30,5)
 X=rng.normal(size=(50,5))+1j*rng.normal(size=(50,5));best=9;bestX=None;bestit=0;bestclusters=0;begin=time.monotonic()
 for it in range(1,3001):
  for B in blocks:
   u,s,vh=np.linalg.svd(X[B],full_matrices=False);X[B]=u@vh
  if it%50==0:
   err=max(float(np.max(np.abs(X[B]@X[B].conj().T-np.eye(5))))for B in blocks)
   if err<best:
    best=err;bestit=it;bestX=X.copy();G=np.abs(X@X.conj().T);remain=set(range(50));clusters=0
    while remain:
     i=min(remain);C={j for j in remain if G[i,j]>1-1e-8};remain-=C;clusters+=1
    bestclusters=clusters
   if err<1e-10:break
 runs.append({'sector_colors':sorted(S),'best_error':best,'best_iteration':bestit,'numerical_ray_clusters':bestclusters,
  'seconds':round(time.monotonic()-begin,3),'cells':cells,'vectors_real':bestX.real.tolist(),'vectors_imag':bestX.imag.tolist()})
 print('case',si,'colors',sorted(S),'best',best,'clusters',bestclusters,flush=True)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'status':'FLOATING_HEURISTIC_ONLY','runs':runs,'scope':'Only one 5D sector; full 10D construction requires the complementary sector and exact independent replay.'}
(P/'frontier-20261029-balanced-sector-projection-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print('finished',obj['clock_finish'])
