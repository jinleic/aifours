import json
from pathlib import Path
from itertools import product,combinations
from collections import deque
r=Path(__file__).resolve().parent
K=json.loads((r/'frontier-20261029-source45-15band-compression-data-v1.json').read_text())
R=json.loads((r/'frontier-20261029-source45-rightSN-canonical-host-data-v1.json').read_text())
B=K['band_table'];action=K['band_action'];co=K['source_coordinates'];h=K['canonical_right_to_band'];labels=K['band_pairs']
B5=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
assert len(B)==len(action)==len(labels)==15 and len(co)==45 and len(h)==306
assert all(labels[B[i][j]]==[B5[labels[i][0]][labels[j][0]],B5[labels[i][1]][labels[j][1]]] for i,j in product(range(15),repeat=2))
assert all(labels[action[i]]==labels[i][::-1] and action[action[i]]==i and B[i][i]==i for i in range(15))
assert all(B[B[i][j]][k]==B[i][B[j][k]] for i,j,k in product(range(15),repeat=3))
assert all(B[B[i][j]][k]==B[B[B[B[i][k]][i]][j]][k] for i,j,k in product(range(15),repeat=3))
assert set(h)==set(range(15)) and all(h[R['band_table'][i][j]]==B[h[i]][h[j]] for i,j in product(range(306),repeat=2))
assert all(h[R['band_action'][i]]==action[h[i]] for i in range(306))
assert all(h[R['coordinates'][s]]==co[s] for s in range(45))
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S=list(product(range(3),range(5),range(3)));idx={x:i for i,x in enumerate(S)}
def sm(a,b):return idx[(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])]
def q(a):return a[0],th[a[1]],a[2]
for i,j in product(range(45),repeat=2):
 w=th[S[i][1]]^th[P[S[i][2]][S[j][0]]]
 assert co[sm(S[i],S[j])]==B[co[i]][action[co[j]] if w else co[j]]
assert all(i==j or q(S[i])!=q(S[j]) or co[i]!=co[j] for i,j in product(range(45),repeat=2))
assert {tuple(c['seed']) for c in K['proper_quotient_controls']}==set(combinations(range(15),2))
for ctrl in K['proper_quotient_controls']:
 p=list(range(15));todo=deque([ctrl['seed']])
 def root(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 while todo:
  a,b=todo.popleft();i=root(a);j=root(b)
  if i==j:continue
  p[j]=i;todo.append((action[a],action[b]))
  for x in range(15):todo.append((B[a][x],B[b][x]));todo.append((B[x][a],B[x][b]))
 i,j=ctrl['source_collapse'];assert i!=j and q(S[i])==q(S[j]) and root(co[i])==root(co[j])
print('PASS 15band⊂B5²,3375 associativity/rightSN identities,C2 action,2025 source products and faithful source')
print('PASS canonicalright306→15 onto equivariant hom:93636 product equations and source coefficients')
print('PASS all105 distinctbandpair merges force sourcecollision: no proper equivariantquotient staysfaithful')
print('LIMIT quotient-irreducibility is NOT a global minimum-band certificate')
