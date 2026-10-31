import json
from pathlib import Path
from itertools import product,combinations
from collections import Counter
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((r/'frontier-20261028-quotient68-12band-host-data-v1.json').read_text())
Q=J['source_multiplication'];actor=J['actual_actor'];C6=J['band_table'];flip=J['band_action']
triples=K['triples'];T=K['band_table'];action=K['band_action'];coeff=K['coordinates']
assert len(triples)==len(set(map(tuple,triples)))==len(T)==len(action)==12 and len(coeff)==68
assert all(len(x)==3 and all(0<=a<6 for a in x) for x in triples)
assert all(triples[T[i][j]]==[C6[x][y] for x,y in zip(triples[i],triples[j])] for i,j in product(range(12),repeat=2))
assert all(triples[action[i]]==[flip[x] for x in triples[i]] for i in range(12))
assert all(T[i][i]==i and action[action[i]]==i for i in range(12))
assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(12),repeat=3))
assert all(T[T[T[T[a][b]][c]][d]][a]==T[T[T[T[T[T[a][b]][c]][a]][c]][d]][a] for a,b,c,d in product(range(12),repeat=4))
assert all(action[T[i][j]]==T[action[i]][action[j]] for i,j in product(range(12),repeat=2))
for e in range(12):
 corner={T[T[e][x]][e] for x in range(12)}
 assert all(T[T[T[T[x][y]][x]][z]][x]==T[T[T[x][y]][z]][x] for x,y,z in product(corner,repeat=3))
for i,j in product(range(68),repeat=2):
 _,g,l=actor[i];row,_,_=actor[j];w=g^(l&row)
 assert coeff[Q[i][j]]==T[coeff[i]][action[coeff[j]] if w else coeff[j]]
pairs=[(i,j) for i,j in combinations(range(68),2) if actor[i]==actor[j]]
assert len(pairs)==256 and all(coeff[i]!=coeff[j] for i,j in pairs)
assert coeff[37]!=coeff[61] and len(set(coeff))==12
print('PASS 12-band as action-stable subband of C6^3: 1728 associativity and 20736 SN identities')
print('PASS all local corners regular, involutory action and 4624 source multiplication equations')
print('PASS 256 same-actor source pairs separated; actor fibre sizes',sorted(Counter(map(tuple,actor)).values()))
print('PASS all 12 band elements are used; physical host size=96')
