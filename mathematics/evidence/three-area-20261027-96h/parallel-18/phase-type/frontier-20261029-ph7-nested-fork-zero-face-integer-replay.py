#!/usr/bin/env python3
"""Independent stdlib replay for O25>=0 OR O45>=0 zero-vertex cover."""
from pathlib import Path
import json,runpy,sys
ROOT=Path(__file__).resolve().parent
sys.argv=['nested-fork-replay','0']
ns=runpy.run_path(str(ROOT/'frontier-20261029-ph7-nested-fork-simplex-integer-replay.py'))
H,V,D,sub,scale,add=ns['H'],ns['V'],ns['D'],ns['sub'],ns['scale'],ns['add'];replay,digest=ns['replay'],ns['digest'];polys=ns['polys']
zero=[{} for _ in range(4)];D5=H(zero)
for i in (2,4):
 mid=[scale(x,ns['F'](1,2))for x in V[i]];polys[f'O{i}5']=sub(scale(H(mid),4),add(D[i],D5))
C=json.loads((ROOT/'frontier-20261029-ph7-nested-fork-zero-face-certificate-v1.json').read_text())
for name,rec in C['records'].items():assert len(polys[name])==rec['terms'] and digest(polys[name])==rec['sha256']and rec['degrees']==[2]*6
assert len(C['covers'])==1 and C['covers'][0]['label']=='face245_OR'
counts=replay(C['covers'][0]);assert counts==[2406,51]
print('PASS: independent reconstruction and exact zero-vertex OR cover 2406/51')
