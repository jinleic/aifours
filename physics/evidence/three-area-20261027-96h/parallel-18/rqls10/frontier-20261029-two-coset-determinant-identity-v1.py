#!/usr/bin/env python3
"""Check all symbolic row-coefficient identities in Z[omega][rho]."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
W=[(1,0),(0,1),(-1,-1)];one=(1,0);zero=(0,0)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def w(n):return W[n%3]
def term(d,delta):return {0:one,d:w(-d*delta)}
assert add(add(one,w(1)),w(2))==zero and mul(w(1),w(2))==one
same=0;cross=0
for delta in (1,2):
 for d in (2,5,7):
  actual=add(one,w(-d*delta));expected=mul(neg(w(2*delta)),w(-delta)if d==7 else one)
  assert actual==expected;same+=1
for delta in (0,1,2):
 for d in (2,5,7):
  actual=term(d,delta)
  expected={0:one,d:(w(-delta)if d==7 else w(delta))}
  assert actual==expected;cross+=1
assert sum([0,0,7])==sum([2,5,0])==7 and w(3)==one
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'same_coset_nonzero_delta_checks':same,'cross_coset_symbolic_rho_checks':cross,
 'both_diagonal_determinant_rho_exponent':7,'omega_determinant':'1',
 'scope':'symbolic coefficient identities; unitarity and odd-dimensional determinant contradiction are written mathematics','status':'PASS'}
(P/'frontier-20261029-two-coset-determinant-identity-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
