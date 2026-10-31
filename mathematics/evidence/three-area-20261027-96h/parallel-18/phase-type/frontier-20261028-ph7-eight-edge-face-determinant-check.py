#!/usr/bin/env python3
"""Direct full 7x7 determinant of the variable eight-edge row generator."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
y,x1,x2,x3,x4,a,b,v1,v2=S.symbols('y x1 x2 x3 x4 a b v1 v2')
G=S.zeros(7);xs=[x1,x2,x3,x4]
for i,x in enumerate(xs):G[i,i]=-x;G[i,i+1]=x
G[4,4]=-a-b;G[4,0]=a;G[4,5]=b;G[5,5]=-v1;G[5,6]=v1;G[6,6]=-v2;G[6,0]=v2
p=S.prod(y+x for x in xs)*(y+a+b)*(y+v1)*(y+v2)-S.prod(xs)*(a*(y+v1)*(y+v2)+b*v1*v2)
assert S.expand((y*S.eye(7)-G).det(method='berkowitz')-p)==0
print('SymPy',S.__version__,'full symbolic variable eight-edge 7x7 determinant PASS')
