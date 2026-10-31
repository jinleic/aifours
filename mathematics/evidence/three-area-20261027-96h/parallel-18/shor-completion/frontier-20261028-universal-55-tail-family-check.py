#!/usr/bin/env python3
"""Bounded controls for the all-k Q55, P=3*2^k border no-go."""
from itertools import combinations
from math import gcd
import json
A={0,3,8,11};Y={0,1,7,13,14};O={33,88,143};H={3,5,11,15,30,55}
counts=[]
for k in range(2,11):
 m=1<<k;n=165*m
 GY={gcd(a-b,n) for a,b in combinations(Y,2)}
 assert GY=={1,2,6,12}
 forced=[x for x in range(n) if (x%m)%4 in (1,2) and all(x==a or gcd(x-a,n) not in GY for a in A)]
 expected=[x for x in range(n) if (x%m)%4 in (1,2) and x%165 in O]
 assert forced==expected and len(forced)==3*m//2
 lookup={(x%m,x%165):x for x in forced}
 for a in range(2,k):assert gcd(lookup[(1,33)]-lookup[(1+(1<<a),33)],n)==165*(1<<a)
 witness=[(3,0),(8,3),(11,0),(lookup[(1,143)],8),
          (lookup[(1,33)],3),(lookup[(1,33)],lookup[(2,88)])]
 assert {gcd(a-b,n) for a,b in witness}==H
 counts.append({'k':k,'n':n,'forced_heads':len(forced),'projection_gcd_checks':max(0,k-2)})
Q7=[x for x in range(660) if x%11==7 and all(x==y or gcd(x-y,660) not in H for y in Y)]
assert Q7==[7,73,337,601]
print(json.dumps({'bounded_orders':counts,'projected_Q_mod11_7':Q7,
                  'scope':'finite CRT/gcd controls; all-k proof is written'},indent=2))
