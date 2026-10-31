#!/usr/bin/env python3
"""Complete Parker disconnected-pair extensions and forced-core certificates."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-parker-all-mates-trade-census-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='68c116e3ad50438a30ec33de141561f177caf720332f7dcd7e188ff1f0e9c170';d=json.loads(raw);T=d['T'];trades=d['trades'];M=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T]
G={c:[i for i,t in enumerate(T)if t[0]==c]for c in range(10)};neigh=collections.defaultdict(set)
for x in trades:a,b=x['a'],x['b'];neigh[a].add(b);neigh[b].add(a)
nodecount=0
def prove(rem,used,exclude):
 global nodecount
 nodecount+=1
 if not rem:return {'SAT':True}
 choices={c:[i for i in G[c]if i not in exclude and not(M[i]&used)]for c in rem};c=min(rem,key=lambda c:(len(choices[c]),c))
 return {'col':c,'branches':[[i,prove(rem-{c},used|M[i],exclude)]for i in choices[c]]}
def first(rem,used):
 if not rem:return []
 choices={c:[i for i in G[c]if not(M[i]&used)]for c in rem};c=min(rem,key=lambda c:(len(choices[c]),c))
 for i in choices[c]:
  z=first(rem-{c},used|M[i])
  if z is not None:return [i]+z
 return None
def sat(tree):return tree.get('SAT',False)or any(sat(q)for _,q in tree.get('branches',[]))
cert=[];hist=collections.Counter()
for x in trades:
 a,b=x['a'],x['b'];core=x['components'][0]==[7,8,9];rem=set(range(10))-{T[a][0],T[b][0]};used=M[a]|M[b]
 third=sorted(c for c in neigh[a]&neigh[b]if not(M[c]&used)) if core else []
 if core:assert third
 tree=prove(rem,used,set(third));assert not sat(tree)
 witness=first(rem,used) if core else None
 if core:assert witness is not None and any(c in witness for c in third)
 hist['core_forced_triangle' if core else 'noncore_no_mate']+=1
 cert.append({'a':a,'b':b,'core':core,'excluded_third':third,'proof':tree,'mate_witness':[a,b]+witness if witness else None})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'census_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'cases':dict(hist),'proof_nodes':nodecount,'certificates':cert,
 'scope':'All disconnected pairs in this L: noncore cannot extend; core extends but only if a third core trade transversal is included.'}
(P/'frontier-20261029-parker-trade-extendibility-v1.json').write_text(json.dumps(obj,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='certificates'},indent=2))
