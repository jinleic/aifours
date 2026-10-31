import json
from pathlib import Path
from itertools import product
J=json.loads((Path(__file__).resolve().parent/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
Q=J['source_multiplication'];A=J['actual_actor'];T=J['band_table'];C=J['coordinates']
relations=[(8,25,37),(8,53,61),(24,53,25),(60,25,61),(37,61,61),(61,37,37)]
for i,j,k in relations:
 assert Q[i][j]==k
 assert (A[i][1]^(A[i][2]&A[j][0]))==0
assert A[37]==A[61] and Q[37][37]==37 and Q[61][61]==61 and 37!=61
assert [C[i][3] for i in (8,24,53,60,37,61)]==[5,3,2,0,1,0]
assert T[T[5][3]][2]==1 and T[5][2]==T[T[0][3]][2]==0
assert T[1][0]==0 and T[0][1]==1
assert all(T[i][i]==i for i in range(6))
assert all(T[T[i][j]][k]==T[i][T[j][k]] for i,j,k in product(range(6),repeat=3))
assert all(T[T[T[T[x][y]][z]][w]][x]==T[T[T[T[T[T[x][y]][z]][x]][z]][w]][x] for x,y,z,w in product(range(6),repeat=4))
print('PASS six source products and zero weights; e=37,f=61 distinct same-q R-idempotents')
print('PASS SN six-band countermodel to arbitrary-band collapse: (v,p,q,u,e,f)=(5,3,2,0,1,0)')
