import json
from pathlib import Path
from itertools import product,combinations
r=Path(__file__).resolve().parent
S=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
H=json.loads((r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json').read_text())
Q=S['source_multiplication'];B=H['band_table'];f=H['band_action'];a=H['actor'];c=H['coordinates'];P=H['actor_sandwich_bits']
assert all(B[B[x][y]][z]==B[B[B[B[x][z]][x]][y]][z] for x,y,z in product(range(8),repeat=3))
assert B[B[1][3]][6]!=B[B[B[B[1][3]][6]][1]][6]
assert Q[37][61]==61 and Q[61][37]==37 and Q[37][25]==37 and Q[61][25]==61 and Q[0][37]==Q[0][61]
opp_a=[[v[2],v[1],v[0]] for v in a];opp_c=[f[c[i]] if a[i][1] else c[i] for i in range(68)]
for i,j in product(range(68),repeat=2):
 k=Q[j][i];w=opp_a[i][1]^P[opp_a[j][0]][opp_a[i][2]]
 # Product in B^op reverses the two ordinary band factors.
 assert opp_c[k]==B[f[opp_c[j]] if w else opp_c[j]][opp_c[i]]
 assert opp_a[k]==[opp_a[i][0],opp_a[i][1]^P[opp_a[j][0]][opp_a[i][2]]^opp_a[j][1],opp_a[j][2]]
assert all(opp_a[i]!=opp_a[j] or opp_c[i]!=opp_c[j] for i,j in combinations(range(68),2))
print('PASS B8 RIGHTSN and explicit LEFTSN failure(1,3,6); source orientation obstruction premises')
print('PASS all4624 opposite-source products and injectivity with reversed actor and flipped-g coefficient')
print('LIMIT product-family lower bounds and all-actor target nonembedding are the written proof')
