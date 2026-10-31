#!/usr/bin/env python3
"""Bounded SMT proof attempt: pure-base exclusion and fixed-hybrid orbit."""
import collections,datetime,hashlib,itertools,json,time
from fractions import Fraction
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-search-v1.py';raw=src.read_bytes();assert hashlib.sha256(raw).hexdigest()=='40baaa1a7d25e32c12aa9117707422bb3159a697da1d076dcba9f36ec7cd3561'
g={'__file__':str(src)};exec(compile(raw.decode().split('t0=time.monotonic();res=S.check()',1)[0],str(src),'exec'),g);S=g['S'];X=g['X'];B=g['B'];V=[tuple(tuple(x)for x in v)for v in g['V']];S.set(timeout=45000,random_seed=81)
def key(v):
 a,b=next(x for x in v if x!=(0,0));d=a*a+b*b;return tuple((Fraction(c*a+e*b,d),Fraction(e*a-c*b,d))for c,e in v)
lookup={key(v):i for i,v in enumerate(V)};index={b:i for i,b in enumerate(B)}
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def ii(a):return(-a[1],a[0])
def H(v):return(add(v[0],v[2]),add(v[1],v[3]),sub(v[0],v[2]),sub(v[1],v[3]))
def SS(v):return(v[0],v[1],ii(v[2]),ii(v[3]))
def SW(v):return(v[0],v[2],v[1],v[3])
def CX(v):return(v[0],v[1],v[3],v[2])
gens=[]
for f in (H,SS,SW,CX):
 r=[lookup[key(f(v))]for v in V];gens.append([index[tuple(sorted(r[i]for i in q))]for q in B])
pure={index[tuple(range(i,i+4))]for i in range(0,60,4)};assert len(pure)==15
S.push();S.add(z3.Or(*[X[i]for i in sorted(pure)]));start=time.monotonic();q=S.check();pure_status=str(q);pure_reason=S.reason_unknown()if q==z3.unknown else None;pure_seconds=time.monotonic()-start;S.pop()
seed=json.loads((P/'frontier-20261029-pauli60-tripartite-core-search-v1.json').read_bytes());core=tuple(sorted(index[tuple(x-1 for x in b)]for b in seed['bases_1indexed']));assert not(set(core)&pure)
hybrid=core[0];basis_orbit={hybrid};stack=[hybrid]
while stack:
 x=stack.pop()
 for h in gens:
  y=h[x]
  if y not in basis_orbit:basis_orbit.add(y);stack.append(y)
assert len(basis_orbit)==90 and not(basis_orbit&pure)
core_orbit={core};stack=[core]
while stack:
 x=stack.pop()
 for h in gens:
  y=tuple(sorted(h[i]for i in x))
  if y not in core_orbit:core_orbit.add(y);stack.append(y)
rooted=[q for q in core_orbit if hybrid in q];assert len(core_orbit)==1920 and len(rooted)==320
S.push();S.add(X[hybrid]);S.add(*[z3.Or(*[z3.Not(X[i])for i in q])for q in rooted]);start=time.monotonic();q=S.check();root_status=str(q);root_reason=S.reason_unknown()if q==z3.unknown else None;root_seconds=time.monotonic()-start
new=None
if q==z3.sat:
 m=S.model();new=[i for i,x in enumerate(X)if z3.is_true(m.eval(x))]
S.pop()
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_setup_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'solver':'Z3 '+z3.get_version_string(),
 'pure_selected_status':pure_status,'pure_unknown_reason':pure_reason,'pure_seconds':round(pure_seconds,4),
 'hybrid_orbit_size':len(basis_orbit),'known_core_orbit_size':len(core_orbit),'rooted_known_cores':len(rooted),
 'outside_known_rooted_orbit_status':root_status,'outside_unknown_reason':root_reason,'outside_seconds':round(root_seconds,4),'different_core':new,
 'scope':'SMT outcomes are solver-scoped; UNKNOWN is no conclusion. Balanced partitions per core still require checking.'}
(P/'frontier-20261029-pauli60-core-pure-hybrid-orbit-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
