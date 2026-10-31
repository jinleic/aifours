#!/usr/bin/env python3
"""Finite synthetic two-power tiling controls for the Q=12 saturation."""
import json
rows=[]
for k in range(3,9):
 m=1<<k;P={r+8*t for t in range(m//8) for r in (0,1)};Q={0,2,4,6}
 assert len(P)==m//4 and len(Q)==4 and len({(p+q)%m for p in P for q in Q})==m
 assert {p%8 for p in P if p%2==0}=={0} and {p%8 for p in P if p%2}=={1}
 tails={ (j+3*v)%24 for j in range(3) for v in Q }
 assert tails=={0,1,2,6,7,8,12,13,14,18,19,20}
 rows.append({'k':k,'P_fibre':len(P),'Q_fibre':len(Q),'tail_classes':len(tails)})
print(json.dumps({'synthetic':rows,'scope':'synthetic 2-power tiles, NOT Shor completion'},indent=2))
