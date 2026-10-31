#!/usr/bin/env python3
"""Bounded exact checks of all-k saturated 2310-family Q55 proof."""
from itertools import combinations
from math import gcd
import json
A={0,3,8,11};Y={0,1,7,13,14};rows=[]
for k in range(6):
 n=2310*(1<<k);N=n//165;t=k+1;m=1<<t
 GY={gcd(a-b,n) for a,b in combinations(Y,2)}
 assert GY==({1,6,7,14} if t==1 else {1,6,7,12,14})
 V={x for x in range(n) if x%3==1 and all(x==a or gcd(x-a,n) not in GY for a in A)}
 Z={x for x in V if x%165==88};T=V-Z
 assert len(Z)==N and all(x%165 in (85,91) for x in T)
 # Compare full gcd screen against the independent modular characterization.
 expectedT=set()
 for x in range(n):
  if x%165==85 and x%2:
   if (t==1 and x%7 not in (3,4)) or (t>=2 and (x%4==3 or x%7 not in (3,4))):expectedT.add(x)
  if x%165==91 and x%2==0:
   if (t==1 and x%7 not in (0,1)) or (t>=2 and (x%4==0 or x%7 not in (0,1))):expectedT.add(x)
 assert T==expectedT
 degT=[sum(gcd(x-z,n) in GY for z in Z) for x in T]
 degZ=[sum(gcd(x-z,n) in GY for x in T) for z in Z]
 target=6 if t==1 else 12 if t==2 else 9*m//4
 assert degT and min(degT)==max(degT)==target and max(degZ)<target
 divisors=[h for h in range(1,N+1) if N%h==0]
 for h in divisors:
  for a,g in ((3,5),(0,11)):
   assert any(gcd((z-a)%n,n)==g*h for z in Z)
 for h in divisors:
  if h<N:assert gcd(165*h,n)==165*h
 rows.append({'k':k,'n':n,'Z':len(Z),'T':len(T),'T_degree':target,'max_Z_degree':max(degZ)})
X=[x for x in range(165) if x%11==7 and all(x==y or gcd(x-y,165) not in {5,11} for y in Y)]
assert X==[7,62,73,106,117] and gcd(62-73,165)==11
print(json.dumps({'bounded_k':rows,'projected_class7':X,
                  'scope':'finite CRT/degree controls; all-k proof is written'},indent=2))
