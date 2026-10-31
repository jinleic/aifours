#!/usr/bin/env python3
"""Independent stdlib replay of nested-fork down-closure zero-vertex covers.

Loads only the stdlib Fraction polynomial definitions of the pinned nested-fork
replay (not its 40-second tree replay), reconstructs the new polynomials and
hashes, and fully replays the four new selector trees.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
src=ROOT/'frontier-20261029-ph7-nested-fork-simplex-integer-replay.py'
sys.argv=['replay-definitions','0'];ns={'__file__':str(src),'__name__':'replay_definitions'}
exec(compile(src.read_text().split("start,end=[(0,5),(5,10),(10,14)][part]")[0],str(src),'exec'),ns)
H,V,D,O,sub,scale,add,mul=ns['H'],ns['V'],ns['D'],ns['O'],ns['sub'],ns['scale'],ns['add'],ns['mul'];replay,digest,polys=ns['replay'],ns['digest'],ns['polys']
D5=H([{},{},{},{}]);O5={}
for i in range(5):
 mid=[scale(x,F(1,2))for x in V[i]];O5[i]=sub(scale(H(mid),4),add(D[i],D5));polys[f'O{i}5']=O5[i]
for c in (0,1,3):
 pair=tuple(sorted((c,2)));polys[f'Z{c}']=sub(scale(mul(O5[2],D[c]),2),mul(O5[c],O[pair]))
C=json.loads((ROOT/'frontier-20261029-ph7-nested-fork-down-closure-certificate-v1.json').read_text())
for name,rec in C['records'].items():
 p=polys[name];assert len(p)==rec['terms'] and digest(p)==rec['sha256'];assert rec['degrees']==([2]*6 if name.startswith('O')else[4]*6)
expected=[('O25',['O25'],[False])]+[(f'face5{c}2',[f'O{c}5','O'+''.join(map(str,tuple(sorted((c,2))))),f'Z{c}'],[False,False,False])for c in (0,1,3)]
assert len(C['covers'])==4
for rec,(label,names,strict)in zip(C['covers'],expected):
 assert rec['label']==label and rec['names']==names and rec['strict']==strict
 print(label,'checked',replay(rec),flush=True)
print('PASS: independent Fraction reconstruction, hashes and four complete down-closure selector trees')
