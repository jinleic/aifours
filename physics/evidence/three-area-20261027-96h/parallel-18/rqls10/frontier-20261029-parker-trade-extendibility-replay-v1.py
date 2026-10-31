#!/usr/bin/env python3
"""Replay all Parker forced-core exact-cover trees against independent DSU census."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;A=P/'frontier-20261029-parker-trade-dsu-replay-v1.json';B=P/'frontier-20261029-parker-trade-extendibility-v1.json';a=A.read_bytes();b=B.read_bytes()
assert hashlib.sha256(a).hexdigest()=='6446901b2381b956a76407630c0b5341650e6f41ced9cc23ed8caa6696b84fef'
X=json.loads(a);Y=json.loads(b);T=X['T'];M=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T];groups={c:[i for i,t in enumerate(T)if t[0]==c]for c in range(10)};neighbor=collections.defaultdict(set)
for z in X['trades']:u,v=z['a'],z['b'];neighbor[u].add(v);neighbor[v].add(u)
assert len(X['trades'])==len(Y['certificates'])==162
n=0;hist=collections.Counter()
def replay(q,rem,used,exclude):
 global n
 n+=1;assert rem and 'SAT' not in q;c=q['col'];assert c in rem
 expected=[i for i in groups[c]if i not in exclude and not(M[i]&used)];assert [i for i,v in q['branches']]==expected
 for i,v in q['branches']:replay(v,rem-{c},used|M[i],exclude)
for x,z in zip(X['trades'],Y['certificates']):
 u,v=x['a'],x['b'];assert (u,v)==(z['a'],z['b']);core=x['components'][0]==[7,8,9];assert core==z['core'];used=M[u]|M[v]
 cs=sorted(w for w in neighbor[u]&neighbor[v]if not(M[w]&used))if core else []
 assert cs==z['excluded_third'];replay(z['proof'],set(range(10))-{T[u][0],T[v][0]},used,set(cs))
 witness=z['mate_witness']
 if core:
  assert len(witness)==10 and len(set(witness))==10 and any(w in witness for w in cs)
  assert all(not(M[i]&M[j])for i,j in itertools.combinations(witness,2))
  assert sum(M[i]for i in witness)==(1<<100)-1
  hist['core_forced_triangle']+=1
 else:assert witness is None;hist['noncore_no_mate']+=1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'independent_census_sha256':hashlib.sha256(a).hexdigest(),
 'producer_sha256':hashlib.sha256(b).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'cases':dict(hist),'proof_nodes_replayed':n,'literal_witnesses_checked':hist['core_forced_triangle'],'status':'PASS'}
(P/'frontier-20261029-parker-trade-extendibility-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
