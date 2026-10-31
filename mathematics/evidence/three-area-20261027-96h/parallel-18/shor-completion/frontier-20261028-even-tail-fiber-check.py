#!/usr/bin/env python3
"""Synthetic controls for the two-power fibre-factorization deduction."""
from math import gcd
import json
n=2640;m=16;P=list(range(12));Q=list(range(0,n,12))
assert len(P)==12 and len(Q)==220 and 0 in P and 3 in P
assert len({(p+q)%n for p in P for q in Q})==n
Pf=[[((p-i)//3)%m for p in P if p%3==i] for i in range(3)]
Qf=[[((q-j)//55)%m for q in Q if q%55==j] for j in range(55)]
assert all(len(v)==len(set(v))==4 for v in Pf+Qf)
assert all(len({(p+q)%m for p in pf for q in qf})==m for pf in Pf for qf in Qf)
assert all(len({x%2 for x in qf})==1 for qf in Qf)
# This is only a control: the old Shor tails other than0 are absent.
assert not {0,1,7,13,14}<=set(Q)
print(json.dumps({'n':n,'synthetic_P':len(P),'synthetic_Q':len(Q),
 'fibre_pairs':len(Pf)*len(Qf),'direct_pairs_checked':len(Pf)*len(Qf),
 'all_Q_fibres_single_parity':True,'scope':'synthetic tiling, NOT a Shor completion'},indent=2))
