#!/usr/bin/env python3
"""Exact generic halfgraphs for literal Bruzda A.30, no phase guessing."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
# Each entry is (power of zeta12, power of a, power of b).
def z(e):return (e%12,0,0)
def a(e=0):return (e%12,1,0)
def b(e=0):return (e%12,0,1)
K=[
 [z(0)]*10,
 [z(0),z(0),z(9),z(3),z(3),z(9),z(4),z(4),z(8),z(8)],
 [z(0),z(0),z(3),z(6),z(6),z(3),z(11),z(11),z(7),z(7)],
 [z(0),z(3),z(8),z(10),z(7),z(11),a(),a(6),z(4),z(4)],
 [z(0),z(3),z(4),z(2),z(11),z(7),z(8),z(8),b(),b(6)],
 [z(0),z(9),z(8),z(4),z(7),z(5),a(3),a(9),z(1),z(1)],
 [z(0),z(9),z(4),z(8),z(11),z(1),z(5),z(5),b(3),b(9)],
 [z(0),z(6),z(0),z(6),z(0),z(6),a(11),a(5),b(7),b(1)],
 [z(0),z(6),z(9),z(9),z(3),z(3),a(7),a(1),b(11),b(5)],
 [z(0),z(6),z(3),z(0),z(6),z(9),a(6),a(),b(6),b()]]
Z=(0,0,0,0);one=(1,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 c=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 for i in range(6,3,-1):
  q=c[i];c[i-4]-=q;c[i-2]+=q
 return tuple(c[:4])
R=[one]
for _ in range(11):
 x=R[-1];R.append((-x[3],x[0],x[1]+x[3],x[2]))
assert R[6]==neg(one)
def cj(x):
 v=Z
 for i,y in enumerate(x):v=add(v,tuple(y*k for k in R[(-i)%12]))
 return v
def terms(rows,c,d):
 S={}
 for t in rows:
  e,p,q=K[t][c];f,u,v=K[t][d];key=(u-p,v-q);S[key]=add(S.get(key,Z),R[(f-e)%12])
 return {k:v for k,v in S.items()if v!=Z}
# unit-phase Laurent identities: all original row and column Hadamard conditions
for c,d in itertools.combinations(range(10),2):assert terms(range(10),c,d)=={}
# row inner products, same coefficient arithmetic
def rowgram(i,j):
 S={}
 for c in range(10):
  e,p,q=K[i][c];f,u,v=K[j][c];key=(u-p,v-q);S[key]=add(S.get(key,Z),R[(f-e)%12])
 return {k:v for k,v in S.items()if v!=Z}
for i,j in itertools.combinations(range(10),2):assert rowgram(i,j)=={}

def admissible(poly):
 if not poly:return 'identically_zero'
 if len(poly)==1:return 'monomial_nonzero'
 if len(poly)==2:
  x,y=poly.values()
  return 'binomial_possible' if mul(x,cj(x))==mul(y,cj(y)) else 'binomial_impossible'
 return 'multinomial'

def matchings(mask,adj,prefix):
 if not mask:yield tuple(prefix);return
 c=(mask&-mask).bit_length()-1
 for d in range(c+1,10):
  if mask>>d&1 and adj[c][d] not in ('monomial_nonzero','binomial_impossible'):
   yield from matchings(mask&~(1<<c)&~(1<<d),adj,prefix+[(c,d)])
case_counts=collections.Counter();profiles=collections.Counter();maxmatches=0;matchinghalves=0;rows=[]
for E0 in itertools.combinations(range(1,10),4):
 E=(0,)+E0;P0={(c,d):terms(E,c,d)for c,d in itertools.combinations(range(10),2)}
 typ={k:admissible(v)for k,v in P0.items()};case_counts.update(typ.values());adj=[['']*10 for _ in range(10)]
 for (c,d),v in typ.items():adj[c][d]=adj[d][c]=v
 ms=list(matchings((1<<10)-1,adj,[]));matchinghalves+=bool(ms);maxmatches=max(maxmatches,len(ms))
 for match in ms:profiles[tuple(sorted(typ[e]for e in match))]+=1
 rows.append({'E':E,'matchings':len(ms),'matching_profiles':[list(sorted(typ[e]for e in mat)) for mat in ms]})
obj={'source':'https://arxiv.org/html/2204.11727v2#A1, literal A.30 (text says Y10D; equation label Y10C)',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'original_symbolic_Hadamard_conditions':{'column_pairs':45,'row_pairs':45,'passed':True},
 'halves':len(rows),'edge_types':dict(case_counts),'matching_halves':matchinghalves,'max_matchings':maxmatches,
 'matching_profiles':{str(k):v for k,v in profiles.items()},'cases':rows,
 'boundary':'Only individually impossible edges removed; remaining multi-edge phase compatibility is not assumed.'}
(P/'frontier-20261028-n10-a30-halfgraph-symbolic-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='cases'},indent=2))
