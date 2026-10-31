import json
from pathlib import Path
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
Q=J['source_multiplication']
assert Q[27][27]==25 and Q[39][39]==61
assert Q[8][27]==39 and Q[8][25]==37
assert Q[37][61]==61 and Q[61][37]==37 and Q[37][37]==37 and Q[61][61]==61
assert Q[0][37]==Q[0][61]==32 and 37!=61
assert all(any(Q[s][u]==Q[u][s] and Q[Q[s][u]][s]==s and Q[Q[u][s]][u]==u for u in range(68)) for s in range(68))
R=[frozenset([i]+Q[i]) for i in range(68)]
L=[frozenset([i]+[Q[j][i] for j in range(68)]) for i in range(68)]
H=[(R[i],L[i]) for i in range(68)]
assert H[24]==H[26] and Q[8][24]==36 and Q[8][26]==38 and H[36]!=H[38]
print('PASS any band hom identifies27=25, hence39=37, and39=61, so37=61')
print('PASS source37,61 actors forced equal under everyCSmap by ef=f,fe=e,0e=0f')
print('PASS S68 completelyregular, but H not a congruence: 24 H26 while8·24=36 notH38=8·26')
print('RESULT no faithful trivial-action band-by-CS host for S68, ANY band and ANY CSactor')
