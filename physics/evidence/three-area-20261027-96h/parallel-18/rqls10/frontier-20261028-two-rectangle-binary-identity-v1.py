#!/usr/bin/env python3
"""Exact 144-case check of the universal two-rectangle F3 gauge formula."""
from itertools import product
count=0
for a,b,x1,x2,y1,y2 in product(range(3),range(3),range(2),range(2),range(2),range(2)):
 def pos(co,x):return 0 if co==0 else (x if co==1 else 1-x)
 X1,X2=pos(a,x1),pos(b,x2)
 raw=a*x1*y1+b*x2*y2
 correction=(y1 if a==2 else 0)+(y2 if b==2 else 0)-X1*X2+(1-y1)*(1-y2)
 val=(raw+correction)%3
 assert val in (0,1),(a,b,x1,x2,y1,y2,val)
 count+=1
assert count==144
print('PASS 9 coefficient pairs x 16 row/column bit patterns: exact F3 binary gauge')
