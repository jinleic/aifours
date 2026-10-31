#!/usr/bin/env python3
"""Bounded exact nonlinear search for a nonstandard 5D flat rank2 projector."""
from itertools import combinations
from pathlib import Path
import json,time,z3
S=z3.SolverFor('QF_NRA');S.set(timeout=30000)
s5=z3.simplify(z3.Sqrt(z3.RealVal(5)))
c1=z3.simplify((s5-1)/4);c2=z3.simplify(-(s5+1)/4)
s1=z3.simplify(z3.Sqrt((5+s5)/8));s2=z3.simplify(z3.Sqrt((5-s5)/8))
cs=[z3.RealVal(1),c1,c2,c2,c1];sn=[z3.RealVal(0),s1,s2,-s2,-s1]
x={(r,c):z3.Real(f'x{r}{c}')for r,c in combinations(range(5),2)}
y={(r,c):z3.Real(f'y{r}{c}')for r,c in combinations(range(5),2)}
for v in list(x.values())+list(y.values()):S.add(v>=-z3.RealVal(2)/5,v<=z3.RealVal(2)/5)
def entry(r,c):
 if r<c:return x[r,c],y[r,c]
 if r>c:return x[c,r],-y[c,r]
 return z3.RealVal(2)/5,z3.RealVal(0)
for r in range(5):
 S.add(z3.Sum([x[min(r,c),max(r,c)]**2+y[min(r,c),max(r,c)]**2 for c in range(5)if c!=r])==z3.RealVal(6)/25)
for r,s in combinations(range(5),2):
 terms=[]
 for k in range(5):
  if k in (r,s):continue
  a,b=entry(r,k);c,d=entry(k,s);terms.append((a*c-b*d,a*d+b*c))
 pr,pi=entry(r,s)
 S.add(z3.Sum([a for a,b in terms])==pr/5,z3.Sum([b for a,b in terms])==pi/5)
for q in (0,4):
 for j in range(4):
  terms=[]
  for r,s in combinations(range(5),2):
   k=(q*(s*s-r*r)+3*j*(s-r))%5
   terms.append(x[r,s]*cs[k]-y[r,s]*sn[k])
  S.add(z3.Sum(terms)==0)
# Exclude all 30 standard projectors exactly, not a finite-radius neighborhood.
for q in (1,2,3):
 for a,b in combinations(range(5),2):
  dif=[]
  for r,s in combinations(range(5),2):
   i=(q*(r*r-s*s)+3*a*(r-s))%5;j=(q*(r*r-s*s)+3*b*(r-s))%5
   re=(cs[i]+cs[j])/5;im=(sn[i]+sn[j])/5
   dif.extend((x[r,s]!=re,y[r,s]!=im))
  S.add(z3.Or(*dif))
start=time.monotonic();ans=S.check();elapsed=time.monotonic()-start
out={'verdict':str(ans),'elapsed_seconds':elapsed,'timeout_ms':30000,
 'reason_unknown':S.reason_unknown() if ans==z3.unknown else None,
 'scope':'exact real constraints; search for rank2 flat P other than 30 standard; no proof certificate'}
if ans==z3.sat:out['model']={str(v):str(S.model().eval(v)) for v in list(x.values())+list(y.values())}
Path(__file__).resolve().parent.joinpath('frontier-20261028-rank2-projector-nra-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(out,flush=True)
