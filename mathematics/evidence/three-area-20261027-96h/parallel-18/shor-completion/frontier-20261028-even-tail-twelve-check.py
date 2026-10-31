#!/usr/bin/env python3
"""Finite 2-power factor controls for the written Q=12 fibre theorem."""
import json
rows=[]
for k in range(3,11):
 m=1<<k;eligible=[]
 for z in range(m):
  if z in (0,2,4):continue
  S={0,2,4,z};owned=[]
  for s in range(1,k+1):
   mod=1<<s;half=mod//2
   cnt=[sum(x%mod==r for x in S) for r in range(mod)]
   if all(cnt[r]==cnt[r+half] for r in range(half)):owned.append(s)
  if len(owned)>=2:
   assert owned==[2,3] and z%8==6
   eligible.append(z)
 rows.append({'k':k,'m':m,'eligible_fourth_residues':len(eligible),
              'all_spectra':[2,3],'all_fourth_mod8':6})
print(json.dumps({'bounded_cases':rows,'scope':'finite coefficient controls; all-k proof is written'},indent=2))
