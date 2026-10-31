#!/usr/bin/env python3
"""Fresh exact positive-skew selector cover on r in [43/20,51/20].

Loads only definitions from the pinned preceding stdlib checker, stretches the
r coordinate by 8/7, and builds a complete exact binary tree with its own leaf
counts. This is independent code from the numeric exploration, not an audit.
"""
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-complex-hidden-positive-skew-fraction-check.py'
ns={'__file__':str(old)}
exec(compile(old.read_text().split("stack=[('',[grid(p,d)for p,d in zip(polys,degs)])]")[0],str(old),'exec'),ns)
polys,degs=ns['polys'],ns['degs'];grid,split=ns['grid'],ns['split']
def stretch(p):return {(i,j):c*F(8,7)**i for (i,j),c in p.items()}
stack=[('',[grid(stretch(p),d)for p,d in zip(polys,degs)])];counts=[0,0]
while stack:
 path,arr=stack.pop()
 if min(arr[0].values())>=0:counts[0]+=1;continue
 if min(arr[1].values())>0 and min(arr[2].values())>0:counts[1]+=1;continue
 assert len(path)<24,('depth limit',path)
 axis=len(path)%2;parts=[split(g,d,axis)for g,d in zip(arr,degs)]
 stack.extend([(path+'1',[q[1]for q in parts]),(path+'0',[q[0]for q in parts])])
assert counts==[14,11]
print('PASS: full r=[43/20,51/20] positive-skew selector cover, exact leaves 14/11')
