import json
from pathlib import Path
from itertools import product
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
Q=J['source_multiplication'];n=len(Q);E={i for i in range(n) if Q[i][i]==i}
assert n==68 and len(E)==34
checks=0;below=0
for s in range(n):
 left={Q[e][s] for e in E};right={Q[s][f] for f in E};w=left&right&E
 checks+=1;below+=len(w)
 assert not w or s in E
print('PASS S68 full natural-order WEU:',checks,'elements,',len(E),'idempotents,',below,'distinct idempotent-below pairs')
T=[[0,0,0,0],[0,1,2,3],[3,2,1,0],[3,3,3,3]]
ET={i for i in range(4) if T[i][i]==i}
assert ET=={0,1,3} and T[0][2]==0 and T[2][3]==0 and T[2][2]!=2
assert not any(T[e][2]==e and T[2][e]==e for e in ET)
print('CONTROL four-element false alarm: 0=0·2=2·3 ≤2 although 0·2≠2·0; NOT weak-E')
