#!/usr/bin/env python3
"""Exact positive-skew selector for r in [43/20,103/40], beta=29/4."""
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
old=ROOT/'frontier-20261029-ph7-complex-hidden-positive-skew-fraction-check.py'
ns={'__file__':str(old)}
exec(compile(old.read_text().split("stack=[('',[grid(p,d)for p,d in zip(polys,degs)])]")[0],str(old),'exec'),ns)
add,scale,sub,mul,powp=ns['add'],ns['scale'],ns['sub'],ns['mul'],ns['powp'];grid,split=ns['grid'],ns['split'];tau2,tau3,tau4=ns['tau2'],ns['tau3'],ns['tau4']
J=add(tau4,scale(powp(tau2,2),F(29,4)))
polys=[scale(tau3,-1),scale(J,-1),sub(powp(J,2),scale(mul(tau2,powp(tau3,2)),F(49,9)))];degs=[(3,1),(4,2),(8,4)]
def stretch(p):return {(i,j):c*F(17,14)**i for (i,j),c in p.items()}
stack=[('',[grid(stretch(p),d)for p,d in zip(polys,degs)])];leaves=[0,0]
while stack:
 path,arr=stack.pop()
 if min(arr[0].values())>=0:leaves[0]+=1;continue
 if min(arr[1].values())>0 and min(arr[2].values())>0:leaves[1]+=1;continue
 assert len(path)<24,('depth limit',path)
 axis=len(path)%2;parts=[split(g,d,axis)for g,d in zip(arr,degs)]
 stack.extend([(path+'1',[q[1]for q in parts]),(path+'0',[q[0]for q in parts])])
assert leaves==[15,12]
print('PASS: r=[43/20,103/40] positive-skew selector; exact leaves 15/12')
