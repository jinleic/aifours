#!/usr/bin/env python3
"""Independent A8A halfgraph proof in Z[i,sqrt2], all 35 normalized halves.

A halfgraph has no perfect matching if it has an isolated vertex or two
leaves sharing their sole neighbor. Both are recorded as literal witnesses.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
S=[['a','1','-a','1','-a','-a','a','1'],['1','-a','1','a','-a','a','-a','1'],['-a','1','-a','a','1','a','1','-a'],['1','a','a','1','1','-a','-a','-a'],['-a','-a','1','1','a','-a','1','a'],['-a','a','a','-a','-a','1','1','1'],['a','-a','1','-a','1','1','a','-a'],['1','1','-a','-a','a','1','-a','a']]
Z=(0,0,0,0);N=(9,0,0,0);A=(1,0,0,2);ONE=(3,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def cj(a):return (a[0],-a[1],a[2],-a[3])
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b1+2*(a2*b2-a3*b3),a0*b1+a1*b0+2*(a2*b3+a3*b2),a0*b2+a2*b0-a1*b3-a3*b1,a0*b3+a3*b0+a1*b2+a2*b1)
def total(xs):
 v=Z
 for x in xs:v=add(v,x)
 return v
K=[[A if x=='a' else neg(A) if x=='-a' else ONE for x in row]for row in S]
for r in range(8):
 for c in range(8):assert mul(cj(K[r][c]),K[r][c])==N
for a,b in itertools.combinations(range(8),2):
 assert total(mul(cj(K[t][a]),K[t][b])for t in range(8))==Z
 assert total(mul(cj(K[a][t]),K[b][t])for t in range(8))==Z
hist=collections.Counter();cert=[]
for E0 in itertools.combinations(range(1,8),3):
 E=(0,)+E0;adj=[set()for _ in range(8)]
 for c,d in itertools.combinations(range(8),2):
  if total(mul(cj(K[t][c]),K[t][d])for t in E)==Z:adj[c].add(d);adj[d].add(c)
 iso=[c for c in range(8)if not adj[c]]
 if iso:
  witness={'kind':'isolated','vertex':iso[0]};hist['isolated']+=1
 else:
  pair=next((c,d,next(iter(adj[c])))for c,d in itertools.combinations(range(8),2)if len(adj[c])==len(adj[d])==1 and adj[c]==adj[d])
  witness={'kind':'two_leaves_one_neighbor','leaves':pair[:2],'neighbor':pair[2]};hist['two_leaves_one_neighbor']+=1
 cert.append({'even_half':E,'adjacency':[sorted(v)for v in adj],'witness':witness})
assert len(cert)==35
obj={'source_url':'https://arxiv.org/html/2505.22947v1#S3.SS2',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'basis':'1,i,sqrt2,i*sqrt2; K entries common denominator 3',
 'norms':64,'row_gram_pairs':28,'column_gram_pairs':28,'halves':35,'witness_counts':dict(hist),'certificates':cert}
(P/'frontier-20261028-isolated-a8a-halfgraph-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({k:v for k,v in obj.items()if k!='certificates'},indent=2))
