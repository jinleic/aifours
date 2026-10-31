#!/usr/bin/env python3
"""Independent replay (different method) of the K5,5,5 / K7,7,7 / half-resolved QLS(10) certificates.

Method: every inner product N*<u,v> = sum_j zeta_N^(e_j) is an algebraic integer s in Z[zeta_N].  s = 0 iff its
field norm prod_{k in (Z/N)^*} sigma_k(s) is 0; a nonzero algebraic integer has |norm| >= 1.  We evaluate all Galois
conjugates with mpmath at 60 digits and declare s = 0 iff |norm| < 1/2 (each conjugate is bounded by the number of
terms, so 60-digit evaluation leaves an error margin of many orders).  Non-parallelism of flat vectors is tested
combinatorially (exponent differences not constant).  The vectors are regenerated here from the published integer
data (characters, phase exponents, incidence) without importing the producer scripts.
"""
import datetime,hashlib,itertools,json,math
from pathlib import Path
import mpmath as mp
mp.mp.dps=60
P=Path(__file__).resolve().parent
def make(N,m,T,PHI2,quadmap):
    # quadmap: list of (q, label function) -> returns dict cell->(exponents tuple) and incidence lists
    vecs={}
    for q in range(len(PHI2)):
        for x in itertools.product(range(m),repeat=2):
            e=tuple(((N//m)*((c[0]*x[0]+c[1]*x[1])%m)+PHI2[q][j])%N for j,c in enumerate(T))
            vecs[(q,x)]=e
    return vecs
def is_zero(N,exps):
    units=[k for k in range(1,N) if math.gcd(k,N)==1];prod=mp.mpf(1)
    for k in units:
        s=mp.mpc(0)
        for e in exps:s+=mp.expjpi(mp.mpf(2*((k*e)%N))/N)
        prod*=abs(s)
    return prod<mp.mpf('0.5')
def diff(a,b,N):return [(y-x)%N for x,y in zip(a,b)]
results={}
# ---- K5,5,5 (zeta20)
T5=[(0,0),(0,1),(1,0),(1,3),(2,2),(2,4),(3,1),(3,4),(4,2),(4,3)]
PH5=[[-35,-25,-25,-15,-20,-10,-15,-5,-10,0],[-10,-10,-10,-5,0,5,-10,0,0,0],[0]*10]
V=make(20,5,T5,PH5,None);inc={}
for (q,x),e in V.items():
    s,t=x;u=(s+t)%5
    ends=[('A',s),('B',t)] if q==0 else ([('A',s),('C',u)] if q==1 else [('B',t),('C',u)])
    for v in ends:inc.setdefault(v,[]).append(e)
ok=all(is_zero(20,diff(a,b,20)) for vs in inc.values() for a,b in itertools.combinations(vs,2))
nonpar=all(len(set(diff(a,b,20)))>1 for a,b in itertools.combinations(list(V.values()),2))
results['K555']={'contexts':len(inc),'all_context_pairs_zero':ok,'rays_nonparallel':nonpar}
# ---- K7,7,7 (zeta28)
T7=[(0,0),(0,1),(1,0),(1,1),(2,3),(2,5),(3,5),(3,6),(4,2),(4,6),(5,2),(5,4),(6,3),(6,4)]
PH7=[[-63,-49,-14,0,-84,-70,-56,-42,-42,-28,-28,-14,-14,0],[-49,-70,-14,-35,-56,-14,-14,0,-14,0,-14,0,0,0],[0]*14]
V7=make(28,7,T7,PH7,None);inc7={}
for (q,x),e in V7.items():
    s,t=x;u=(s+t)%7
    ends=[('A',s),('B',t)] if q==0 else ([('A',s),('C',u)] if q==1 else [('B',t),('C',u)])
    for v in ends:inc7.setdefault(v,[]).append(e)
ok7=all(is_zero(28,diff(a,b,28)) for vs in inc7.values() for a,b in itertools.combinations(vs,2))
nonpar7=all(len(set(diff(a,b,28)))>1 for a,b in itertools.combinations(list(V7.values()),2))
results['K777']={'contexts':len(inc7),'all_context_pairs_zero':ok7,'rays_nonparallel':nonpar7}
# ---- half-resolved QLS(10) (zeta20)
PHH=[[-65,-40,-40,-25,-25,-15,-20,-10,-10,0],[-40,-30,-25,-15,-15,-5,-20,-10,-10,0],[-25,-10,-15,-10,-10,-10,0,0,0,0],[0]*10]
VH=make(20,5,T5,PHH,None);grid={}
for (q,x),e in VH.items():
    r,c={0:(x[0],x[1]),1:(x[0],5+x[1]),2:(5+x[0],x[1]),3:(5+x[0],5+x[1])}[q];grid[(r,c)]=e
rows=all(is_zero(20,diff(grid[(r,a)],grid[(r,b)],20)) for r in range(10) for a,b in itertools.combinations(range(10),2))
cols=all(is_zero(20,diff(grid[(a,c)],grid[(b,c)],20)) for c in range(10) for a,b in itertools.combinations(range(10),2))
T1=[[(x0,5+x1) for x0 in range(5) for x1 in range(5) if (x0+x1)%5==u]+[(5+x0,x1) for x0 in range(5) for x1 in range(5) if (x0+x1)%5==u] for u in range(5)]
t1=all(is_zero(20,diff(grid[a],grid[b],20)) for cl in T1 for a,b in itertools.combinations(cl,2))
nonparH=all(len(set(diff(grid[a],grid[b],20)))>1 for a,b in itertools.combinations(sorted(grid),2))
# exact orthogonality graph and transversal count (independent DFS)
cells=sorted(grid);O={}
for a,b in itertools.combinations(cells,2):O[(a,b)]=O[(b,a)]=is_zero(20,diff(grid[a],grid[b],20))
cnt=0
def dfs(r,used,ch):
    global cnt
    if r==10:cnt+=1;return
    for c in range(10):
        if c in used:continue
        if all(O[((r,c),z)] for z in ch):dfs(r+1,used|{c},ch+[(r,c)])
dfs(0,frozenset(),[])
results['half_resolved_qls10']={'rows_onb':rows,'cols_onb':cols,'T1_onb':t1,'rays_nonparallel':nonparH,'orthogonal_pairs':sum(O.values())//2,'orthogonal_transversals':cnt}
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'method':'Galois-norm zero test at 60 digits (independent of polynomial reduction)','results':results,
 'status':'PASS' if all([ok,nonpar,ok7,nonpar7,rows,cols,t1,nonparH,cnt==5]) else 'FAIL'}
(P/'frontier-20261029-norm-test-independent-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
