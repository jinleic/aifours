import json
from pathlib import Path
from itertools import product,combinations
from collections import deque,Counter
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261029-K25-essential-band-data-v1.json').read_text())
B=J['fiveband'];S=J['source_pairs'];T=J['source_table'];actor=J['finest_actor'];n=25
assert S==[list(x) for x in product(range(5),repeat=2)]
idx={tuple(x):i for i,x in enumerate(S)}
assert all(T[i][j]==idx[B[S[i][0]][S[j][0]],B[S[j][1]][S[i][1]]] for i,j in product(range(n),repeat=2))
assert all(T[i][i]==i for i in range(n))
assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(n),repeat=3))
assert all(T[T[T[T[a][b]][c]][d]][a]==T[T[T[T[T[T[a][b]][c]][a]][c]][d]][a] for a,b,c,d in product(range(n),repeat=4))
def equiv(side):
 p=list(range(n))
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 for i,j in product(range(n),repeat=2):
  a=root(i if side=='row' else j);b=root(T[i][j]);p[b]=a
 lab={};return [lab.setdefault(root(i),len(lab)) for i in range(n)]
rows=equiv('row');cols=equiv('col')
assert actor==[list(x) for x in zip(rows,cols)] and len(set(map(tuple,actor)))==4
assert sorted(Counter(map(tuple,actor)).values())==[1,4,4,16]
assert {tuple(c['seed']) for c in J['proper_congruence_controls']}==set(combinations(range(n),2))
for ctrl in J['proper_congruence_controls']:
 p=list(range(n));todo=deque([ctrl['seed']])
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 while todo:
  a,b=todo.popleft();i=root(a);j=root(b)
  if i==j:continue
  p[j]=i
  for x in range(n):todo.append((T[a][x],T[b][x]));todo.append((T[x][a],T[x][b]))
 a,b=ctrl['source_collapse']
 assert a!=b and actor[a]==actor[b] and root(a)==root(b)
print('PASS K25 band:15625 associativity and390625 SN identities; finest rectangular actor4 withfibres1,4,4,16')
print('PASS all300 distinctsourcepair congruences force a distinctsameactor sourcecollision')
print('RESULT every band hom kernel disjoint from allCSactor kernel constraints is equality')
print('LIMIT arbitrary physical host normalization is the written rank-one Rees gauge, not a finite search')
