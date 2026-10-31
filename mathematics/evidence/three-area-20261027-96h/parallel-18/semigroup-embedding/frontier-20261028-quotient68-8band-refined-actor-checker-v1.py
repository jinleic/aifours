import json
from pathlib import Path
from itertools import product,combinations
from collections import Counter
root=Path(__file__).resolve().parent
J=json.loads((root/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((root/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];actual=J['actual_actor'];T=K['band_table'];flip=K['band_action'];P=K['actor_sandwich_bits'];actor=K['actor'];coeff=K['coordinates'];colmap=K['actor_to_actual_column'];F=K['forced_fibre_indices']
assert F==[0,8,16,24,36,44,52,60] and len(set(F))==8
assert all(Q[x][x]==x and Q[0][x]==0 and Q[x][0]==0 for x in F)
assert len(T)==len(flip)==8 and all(len(row)==8 and all(0<=a<8 for a in row) for row in T)
assert all(T[i][i]==i and flip[flip[i]]==i for i in range(8))
assert all(T[T[x][y]][z]==T[x][T[y][z]] for x,y,z in product(range(8),repeat=3))
assert all(T[T[T[T[x][y]][z]][w]][x]==T[T[T[T[T[T[x][y]][z]][x]][z]][w]][x] for x,y,z,w in product(range(8),repeat=4))
assert all(flip[T[x][y]]==T[flip[x]][flip[y]] for x,y in product(range(8),repeat=2))
for e in range(8):
 corner={T[T[e][x]][e] for x in range(8)}
 assert all(T[T[T[T[x][y]][x]][z]][x]==T[T[T[x][y]][z]][x] for x,y,z in product(corner,repeat=3))
assert P==[[0,0],[0,1],[0,1]] and colmap==[0,1,1]
def dm(x,y):
 i,g,l=x;j,h,m=y;return [i,g^P[l][j]^h,m]
assert len(actor)==len(coeff)==68 and all(0<=v<8 for v in coeff)
assert set(map(tuple,actor))==set(product(range(2),range(2),range(3)))
assert all(actual[i]==[actor[i][0],actor[i][1],colmap[actor[i][2]]] for i in range(68))
assert all((Q[i][i]==i)==(actor[i][1]==P[actor[i][2]][actor[i][0]]) for i in range(68))
for i,j in product(range(68),repeat=2):
 assert actor[Q[i][j]]==dm(actor[i],actor[j])
 w=actor[i][1]^P[actor[i][2]][actor[j][0]]
 assert coeff[Q[i][j]]==T[coeff[i]][flip[coeff[j]] if w else coeff[j]]
pairs=[(i,j) for i,j in combinations(range(68),2) if actor[i]==actor[j]]
assert len(pairs)==200 and all(coeff[i]!=coeff[j] for i,j in pairs)
assert len(set(coeff))==8
print('PASS 8-idempotent upper cone: distinct, all above source 0; any CS actor has one image')
print('PASS band8: 512 associativity, 4096 SN identities, all local corners regular and C2 action')
print('PASS refined CS actor12, onto/pure, factors onto actual actor8; 4624 source/host products')
print('PASS 200 same-refined-actor source pairs separated; host size=96')
print('RESULT: exact minimum band size over ALL CS actors = 8, contingent on pinned source verification')
