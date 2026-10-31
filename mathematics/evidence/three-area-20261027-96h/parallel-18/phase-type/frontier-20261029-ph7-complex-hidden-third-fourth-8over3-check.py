#!/usr/bin/env python3
"""Exact negative-skew selector for r in [43/20,8/3], beta=49/20."""
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-complex-hidden-third-fourth-fraction-check.py'
ns={'__file__':str(old)}
exec(compile(old.read_text().split("stack=[('',grid(E,(6,3)),grid(J,(4,2)))]")[0],str(old),'exec'),ns)
add,scale,powp=ns['add'],ns['scale'],ns['powp'];grid,split=ns['grid'],ns['split'];tau2,tau4=ns['tau2'],ns['tau4'];E=ns['E']
J=scale(add(tau4,scale(powp(tau2,2),F(49,20))),-1)
def stretch(p):return {(i,j):c*F(31,21)**i for (i,j),c in p.items()}
deg1,deg2=(6,3),(4,2);stack=[('',grid(stretch(E),deg1),grid(stretch(J),deg2))];leaves=[0,0]
while stack:
 path,A,B=stack.pop()
 if min(A.values())>0:leaves[0]+=1;continue
 if min(B.values())>0:leaves[1]+=1;continue
 assert len(path)<24,('depth limit',path)
 axis=len(path)%2;AL,AR=split(A,deg1,axis);BL,BR=split(B,deg2,axis)
 stack.extend([(path+'1',AR,BR),(path+'0',AL,BL)])
assert leaves==[30,21]
print('PASS: r=[43/20,8/3] negative-skew selector; exact leaves 30/21')
