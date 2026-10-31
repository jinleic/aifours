import json
from pathlib import Path
from itertools import product
r=Path(__file__).resolve().parent
R=json.loads((r/'frontier-20261029-source45-rightSN-canonical-host-data-v1.json').read_text())
L=json.loads((r/'frontier-20261029-source45-leftSN-canonical-host-data-v1.json').read_text())
J=json.loads((r/'frontier-20261029-source45-fullSN-pullback-data-v1.json').read_text())
for label,T,f in [('R',R['band_table'],R['band_action']),('L',L['band_table'],L['band_action']),('N',J['normal_table'],J['normal_action'])]:
 n=len(T);assert len(f)==n and all(0<=x<n for x in f)
 assert all(f[f[i]]==i for i in range(n))
 assert all(f[T[i][j]]==T[f[i]][f[j]] for i,j in product(range(n),repeat=2))
 print('PASS',label,'full C2 involution and',n*n,'automorphism product equations')
mR=J['right_to_normal'];mL=J['left_to_normal'];fN=J['normal_action']
assert all(mR[R['band_action'][i]]==fN[mR[i]] for i in range(306))
assert all(mL[L['band_action'][i]]==fN[mL[i]] for i in range(270))
assert all(mR[R['coordinates'][s]]==mL[L['coordinates'][s]] for s in range(45))
print('PASS both normal reflection maps equivariant and all45 source coefficient pairs compatible')
