#!/usr/bin/env python3
"""Synthetic two-power fibre controls across every divisor split of165."""
import json
n=2640;m=16;rows=[]
for d in (1,3,5,11,15,33,55,165):
 e=165//d;P=list(range(4*d));Q=list(range(0,n,4*d))
 assert len(P)==4*d and len(Q)==4*e and len({(p+q)%n for p in P for q in Q})==n
 Pf=[[((p-i)//d)%m for p in P if p%d==i] for i in range(d)]
 Qf=[[((q-j)//e)%m for q in Q if q%e==j] for j in range(e)]
 assert all(len(v)==len(set(v))==4 for v in Pf+Qf)
 assert all(len({(p+q)%m for p in a for q in b})==m for a in Pf for b in Qf)
 if d in (1,3,5,11):assert all(len({x%2 for x in q})==1 for q in Qf)
 rows.append({'d':d,'e':e,'fibre_pairs':len(Pf)*len(Qf)})
# Reciprocal endpoint control: Q has old tails0,1; P is NOT the Shor code.
d=165;e=1;P=list(range(0,n,4));Q=list(range(4))
Pf=[[((p-i)//d)%m for p in P if p%d==i] for i in range(d)]
assert all(len({x%2 for x in f})==1 for f in Pf) and {0,1}<=set(Q)
assert not {0,3,8,11}<=set(P)
print(json.dumps({'splits':rows,'reciprocal_d165_control':'PASS',
                  'scope':'synthetic tilings, NOT Shor completions'},indent=2))
