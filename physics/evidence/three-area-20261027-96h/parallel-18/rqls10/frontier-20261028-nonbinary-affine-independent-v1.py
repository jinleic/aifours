#!/usr/bin/env python3
"""Independent Q(sqrt(-3)) reciprocal gcd and Q(zeta8,zeta9) endpoint replay."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'][0]
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
R=[[sum(co*int(t in f['rows'] and c in f['columns']) for co,f in zip(D['coefficients'],D['rectangles']))for c in range(10)]for t in range(10)]
N=max(map(max,R));assert N==6
Z=(Q(0),Q(0));O=(Q(1),Q(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a):return a[0],-a[1]
def div(a,b):
 n=b[0]*b[0]+3*b[1]*b[1];assert n>0
 x=mul(a,conj(b));return x[0]/n,x[1]/n
def trim(v):
 v=list(v)
 while v and v[-1]==Z:v.pop()
 return v
def rem(a,b):
 a=trim(a);b=trim(b)
 while a and len(a)>=len(b):
  k=len(a)-len(b);q=div(a[-1],b[-1])
  for j,x in enumerate(b):a[k+j]=sub(a[k+j],mul(q,x))
  a=trim(a)
 return a
def gcd(a,b):
 a,b=trim(a),trim(b)
 while b:a,b=b,rem(a,b)
 return [div(x,a[-1]) for x in a] if a else []
# zeta6=(1+sqrt(-3))/2; direct powers.
six=[];z=O;unit=(Q(1,2),Q(1,2))
for e in range(6):six.append(z);z=mul(z,unit)
assert z==O
@lru_cache(None)
def unit_possible_order72(p):
 star=tuple(conj(x) for x in reversed(p));g=gcd(p,star)
 if len(g)<=1:return True,0
 f=[(-Q(1),Q(0))]+[Z]*71+[O]
 return not rem(f,g),len(g)-1

def matching(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
polys=set();generic=0;total=0
for E in combinations(range(10),5):
 adj=[set() for _ in range(10)]
 for c,d in combinations(range(10),2):
  v=[Z]*(2*N+1)
  for t in E:
   k=R[t][d]-R[t][c]+N;v[k]=add(v[k],six[(H[t][d]-H[t][c])%6])
  while v and v[-1]==Z:v.pop()
  while v and v[0]==Z:v.pop(0)
  if not v:adj[c].add(d);adj[d].add(c)
  else:
   lead=v[-1];ky=tuple(div(x,lead) for x in v);polys.add(ky)
   ok,_=unit_possible_order72(ky);assert ok
  total+=1
 if matching(adj):generic+=1
assert total==11340 and len(polys)==648 and generic==0
print('PASS 11340 literal half-polynomials, 648 classes, reciprocal gcds divide z^72-1, generic no match',flush=True)
# zeta72=zeta8*zeta9^8, product field degree 4*6=24.
eight=[]
for e in range(8):
 a=[0]*4;a[e%4]=1 if e<4 else -1;eight.append(a)
nine=[]
for e in range(9):
 a=[0]*6
 if e<6:a[e]=1
 else:a[e-6]-=1;a[e-3]-=1
 nine.append(a)
pw=[tuple(a*b for a in eight[e%8] for b in nine[(8*e)%9])for e in range(72)]
def zero(v):return all(sum(pw[x%72][j] for x in v)==0 for j in range(24))
graphs=0
for s in range(72):
 K=[[(12*H[t][c]+s*R[t][c])%72 for c in range(10)]for t in range(10)]
 for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)])
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if zero([K[t][d]-K[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
  assert not matching(adj),(s,E)
  graphs+=1
assert graphs==72*252
out={'half_polynomials':total,'unique_classes':len(polys),'generic_matching_halves':generic,
 'root_order_bound':72,'phases':72,'phase_halfgraphs':graphs,'matching_halves':0,
 'scope':'one explicit 4-mask one-parameter family; no general classification'}
(P/'frontier-20261028-nonbinary-affine-independent-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS all72 parameters and',graphs,'halfgraphs, no perfect matching',flush=True)
