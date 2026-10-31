import json
from pathlib import Path
from itertools import product
from collections import Counter
root=Path(__file__).resolve().parent
J=json.loads((root/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((root/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];q=J['actual_actor'];a=K['actor'];n=68

def partition(side):
 p=list(range(n))
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 def union(i,j):
  i=root(i);j=root(j)
  if i!=j:p[j]=i
 for i,j in product(range(n),repeat=2):union(i if side=='row' else j,Q[i][j])
 labels={};return [labels.setdefault(root(i),len(labels)) for i in range(n)]
rows=partition('row');cols=partition('col')
assert rows==[x[0] for x in a] and cols==[x[2] for x in a]
assert len(set(rows))==2 and len(set(cols))==3
assert sorted(Counter(rows).values())==[34,34]
assert sorted(Counter(cols).values())==[8,28,32]
assert all(rows[Q[i][j]]==rows[i] and cols[Q[i][j]]==cols[j] for i,j in product(range(n),repeat=2))
assert all(q[i]==[a[i][0],a[i][1],[0,1,1][a[i][2]]] for i in range(n))
assert len(set(map(tuple,a)))==12 and len(set(map(tuple,q)))==8
print('PASS all 4624 row and column relations; finest actor partitions sizes [34,34] and [8,28,32]')
print('PASS refined D12 actor realizes those partitions and factors onto actual D8')
print('LIMIT group order and arbitrary CS actor factorization are proved in the accompanying text')
