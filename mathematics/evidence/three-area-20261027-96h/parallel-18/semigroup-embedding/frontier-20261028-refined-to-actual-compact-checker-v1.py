import json
from itertools import product,combinations
from pathlib import Path
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
K=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=J['source_multiplication'];q=J['actual_actor'];rr=K['actor'];B=K['band_table'];flip=K['band_action'];coef=K['coordinates']
col_label=[0,0,1];coord=[(col_label[rr[i][2]],coef[i]) for i in range(68)]
def bm(x,y):return y[0],B[x[1]][y[1]]
def action(g,x):return x[0],(flip[x[1]] if g else x[1])
assert all(q[i]==[rr[i][0],rr[i][1],[0,1,1][rr[i][2]]] for i in range(68))
for i,j in product(range(68),repeat=2):
 w=q[i][1]^(q[i][2]&q[j][0])
 assert coord[Q[i][j]]==bm(coord[i],action(w,coord[j]))
pairs=[(i,j) for i,j in combinations(range(68),2) if q[i]==q[j]]
assert len(pairs)==256 and all(coord[i]!=coord[j] for i,j in pairs)
assert len(set(coord))<=16
print('PASS compact forgetful lift B8×rightzero2: 4624 equations and 256 same-q injectivity pairs')
print('band size16; source group actions checked on coordinates; no whole-band enumeration')
