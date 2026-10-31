#!/usr/bin/env python3
"""Replay all 299 support-orbit resultants in independent Q(sqrt5)[omega,eta] coordinates."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-support5-resultant-proof-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='b04b155374c5802a4f910b7531bb050d4af19ec7226aec9244300e0dc1d44e43';D=json.loads(raw)
z=(F(0),F(0));o=(F(1),F(0))
def a(x,y):return(x[0]+y[0],x[1]+y[1])
def n(x):return(-x[0],-x[1])
def s(x,y):return a(x,n(y))
def m(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def oa(x,y):return(a(x[0],y[0]),a(x[1],y[1]))
def on(x):return(n(x[0]),n(x[1]))
def om(x,y):
 ac=m(x[0],y[0]);bd=m(x[1],y[1]);return(s(ac,bd),s(a(m(x[0],y[1]),m(x[1],y[0])),bd))
c=(F(-1,2),F(1,2))
def km(x,y):
 ac=om(x[:2],y[:2]);bd=om(x[2:],y[2:]);bc=om(x[2:],y[:2]);ad=om(x[:2],y[2:]);cbd=(m(c,bd[0]),m(c,bd[1]));return oa(ac,on(bd))+oa(oa(ad,bc),cbd)
KZ=(z,z,z,z);KO=(o,z,z,z)
def ka(x,y):return tuple(a(v,w)for v,w in zip(x,y))
def kn(x):return tuple(n(v)for v in x)
def ks(x,y):return ka(x,kn(y))
def conj(x):
 A,B,C,D=x;return (s(a(s(A,B),m(c,C)),m(c,D)),s(n(B),m(c,D)),s(D,C),D)
zeta=(o,o,n(c),n(c));powers=[KO]
for _ in range(15):powers.append(km(powers[-1],zeta))
assert powers[15]==KO and conj(zeta)==powers[14]
C=[ka(KO,powers[k])for k in range(15)];Inv=[]
for k in range(15):
 q=KZ
 for j in range(15):q=ka(q,powers[k*j%15]if j%2==0 else kn(powers[k*j%15]))
 q=tuple((x[0]/2,x[1]/2)for x in q);assert km(C[k],q)==KO;Inv.append(q)
g=[conj(km(C[2*a%15],Inv[7*a%15]))for a in range(15)];H={}
for a0 in range(15):
 for b in range(15):
  if a0==b:continue
  d=(b-a0)%15;H[a0,b]=(kn(km(C[2*d%15],Inv[5*d%15])),kn(km(km(km(g[a0],conj(g[b])),C[7*d%15]),Inv[5*d%15])))
def pp(A,B):return(km(A[0],B[0]),ka(km(A[0],B[1]),km(A[1],B[0])),km(A[1],B[1]))
def minors(S):
 out=[]
 for a0,b,c0,d in itertools.combinations(S,4):
  out.append(tuple(ks(x,y)for x,y in zip(pp(H[a0,b],H[c0,d]),pp(H[a0,d],H[c0,b]))))
  out.append(tuple(ks(x,y)for x,y in zip(pp(H[a0,c0],H[b,d]),pp(H[a0,d],H[b,c0]))))
 return out
def res(P,Q):
 c0,b,a0=P;f,e,d=Q;t=ks(km(a0,f),km(c0,d));return ks(km(t,t),km(ks(km(a0,e),km(b,d)),ks(km(b,f),km(c0,e))))
units=[u for u in range(1,15)if math.gcd(u,15)==1];remaining={S for S in itertools.combinations(range(15),5)if len({a%3 for a in S})==3};counts=collections.Counter()
for rec in D['records']:
 S=tuple(rec['representative']);assert S==min(remaining);orb={tuple(sorted(u*a%15 for a in S))for u in units};assert orb<=remaining and len(orb)==rec['orbit_size'];remaining-=orb;counts[len(orb)]+=1
 pol=minors(S);i,j=rec['minor_indices'];assert 0<=i<j<len(pol);v=res(pol[i],pol[j]);assert v!=KZ
 expected=KZ
 for k,x in enumerate(rec['resultant_phi15_basis']):
  q=F(x)
  if q:expected=ka(expected,tuple((q*t[0],q*t[1])for t in powers[k]))
 assert v==expected
assert not remaining and len(D['records'])==299 and sum(k*v for k,v in counts.items())==2250
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'orbits_checked':len(D['records']),'support_sets_covered':2250,
 'orbit_sizes':dict(counts),'all_nonzero_resultants_match_across_field_bases':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-support5-resultant-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
