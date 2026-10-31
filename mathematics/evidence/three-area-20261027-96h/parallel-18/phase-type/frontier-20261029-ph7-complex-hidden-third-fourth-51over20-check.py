#!/usr/bin/env python3
"""Fresh exact dual cover on r in [43/20,51/20].

Dynamically loads only definitions from the pinned preceding stdlib checker,
then substitutes R -> (8/7)R to extend its parametric interval. No old file
is modified; it builds and checks its own complete binary selector tree.
"""
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-complex-hidden-third-fourth-fraction-check.py'
ns={'__file__':str(old)}
exec(compile(old.read_text().split("stack=[('',grid(E,(6,3)),grid(J,(4,2)))]")[0],str(old),'exec'),ns)
E,J=ns['E'],ns['J'];grid,split=ns['grid'],ns['split'];deg1=(6,3);deg2=(4,2)
def stretch(p):return {(i,j):c*F(8,7)**i for (i,j),c in p.items()}
stack=[('',grid(stretch(E),deg1),grid(stretch(J),deg2))];leaves=[[],[]]
while stack:
 path,A,B=stack.pop()
 if min(A.values())>0:leaves[0].append(path);continue
 if min(B.values())>0:leaves[1].append(path);continue
 assert len(path)<24,('depth limit',path)
 axis=len(path)%2;AL,AR=split(A,deg1,axis);BL,BR=split(B,deg2,axis)
 stack.extend([(path+'1',AR,BR),(path+'0',AL,BL)])
assert [len(x)for x in leaves]==[18,13]
print('PASS: full r=[43/20,51/20] tau3<=0 selector cover, exact strict leaves 18/13')
