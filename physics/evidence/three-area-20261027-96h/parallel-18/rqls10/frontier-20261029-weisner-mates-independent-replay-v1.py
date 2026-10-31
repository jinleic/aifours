#!/usr/bin/env python3
"""Independent MRV/DSU re-enumeration and literal branch-tree checker."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=('00 28 59 84 67 32 15 93 71 46','82 11 30 69 05 78 43 26 94 57','95 03 22 41 79 16 80 54 37 68','48 96 14 33 52 89 27 01 65 70','76 50 97 25 44 63 09 38 12 81','23 87 61 98 36 55 74 19 40 02','51 34 08 72 90 47 66 85 29 13','39 62 45 10 83 91 58 77 06 24','17 49 73 56 21 04 92 60 88 35','64 75 86 07 18 20 31 42 53 99')
A=[[int(x[0])for x in row.split()]for row in S];L=[[int(x[1])for x in row.split()]for row in S]
for a in (A,L):
 assert all(len(set(row))==10 for row in a) and all(len({a[r][c]for r in range(10)})==10 for c in range(10))
assert len({(A[r][c],L[r][c])for r,c in itertools.product(range(10),repeat=2)})==100
T=[];nodes=0
def rec(rem,C,S,cur):
 global nodes
 nodes+=1
 if not rem:T.append(tuple(cur));return
 r=min(rem,key=lambda r:sum(c not in C and L[r][c]not in S for c in range(10)))
 for c in range(10):
  if c not in C and L[r][c]not in S:cur[r]=c;rec(rem-{r},C|{c},S|{L[r][c]},cur);cur[r]=-1
rec(set(range(10)),set(),set(),[-1]*10);T.sort();assert len(T)==len(set(T))
masks=[sum(1<<(10*r+c)for r,c in enumerate(t))for t in T]
def comps(a,b):
 x,y=T[a],T[b];par=list(range(20))
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 def merge(i,j):
  i=find(i);j=find(j)
  if i!=j:par[j]=i
 ci={y[r]:r for r in range(10)};li={L[r][y[r]]:r for r in range(10)}
 for r in range(10):merge(r,10+r);merge(r,10+ci[x[r]]);merge(r,10+li[L[r][x[r]]])
 out=collections.defaultdict(list)
 for r in range(10):out[find(r)].append(r)
 return tuple(sorted((tuple(v)for v in out.values()),key=lambda x:(len(x),x)))
trades=[];compatible=0
for a,b in itertools.combinations(range(len(T)),2):
 if masks[a]&masks[b]:continue
 compatible+=1;C=comps(a,b)
 if len(C)>1:trades.append((a,b,C))
source=P/'frontier-20261029-weisner-all-mates-trade-census-v1.json';raw=source.read_bytes();data=json.loads(raw)
assert [list(t)for t in T]==data['T'];cert=data['trade_certificates'];assert len(cert)==len(trades)
groups={c:[i for i,t in enumerate(T)if t[0]==c]for c in range(10)};checked=0
def replay(q,rem,used):
 global checked
 checked+=1;assert rem and 'SAT' not in q
 c=q['column'];assert c in rem
 opts=[i for i in groups[c]if not(masks[i]&used)];branches=q['branches'];assert [i for i,ch in branches]==opts
 for i,ch in branches:replay(ch,rem-{c},used|masks[i])
for (a,b,C),q in zip(trades,cert):
 assert (a,b)==(q['a'],q['b']) and [list(z)for z in C]==q['components']
 replay(q['proof'],set(range(10))-{T[a][0],T[b][0]},masks[a]|masks[b])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'transversals':len(T),'MRV_nodes':nodes,'compatible_pairs':compatible,
 'disconnected_pairs':len(trades),'literal_proof_nodes_replayed':checked,'all_mate_extensions_rejected':True,'status':'PASS'}
(P/'frontier-20261029-weisner-mates-independent-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
