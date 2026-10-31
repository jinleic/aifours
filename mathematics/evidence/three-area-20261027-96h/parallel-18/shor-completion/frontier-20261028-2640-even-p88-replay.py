#!/usr/bin/env python3
"""Complement-seed and direct-class independent replay of n2640 P88."""
from collections import Counter,defaultdict
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
def conflict(a,b,F):return a!=b and gcd(a-b,n) in F
# Directly enumerate every admissible eight-subset in each of the two head
# residue classes, then test all cross pairs; this is independent of matchings.
for g,j1,j2 in ((4,1,4),(55,5,2),(240,2,10)):
 F=GY|{g};groups=[]
 for j in (j1,j2):
  C=[x for x in range(n) if x%11==j and all(not conflict(x,a,F) for a in A)]
  groups.append([s for s in combinations(C,8) if all(not conflict(a,b,F) for a,b in combinations(s,2))])
 assert groups[0] and groups[1]
 if any(all(not conflict(a,b,F) for a in x for b in y) for x in groups[0] for y in groups[1]):
  raise AssertionError(('head class remains possible',g))
F=GA|{4,55,240};C={x for x in range(n) if all(not conflict(x,y,F) for y in Y)}
assert not any(x%5 in (0,4) and x%3==1 for x in C)
N={x for x in C if x%5 in (1,2,3) and x%3!=1};assert len(N)==16
slots=defaultdict(set)
for x in C:
 if x%5 in (1,2,3) and x%3==1:slots[(x%5,x%16)].add(x)
assert len(slots)==24 and all(x%2 for vals in slots.values() for x in vals)
stats=Counter()
for omitted in combinations(sorted(N),8):
 S=N-set(omitted);stats['seeds']+=1
 if any(conflict(a,b,F) for a,b in combinations(S,2)):
  stats['internal_conflicts']+=1;continue
 if any(sum(x%5==r for x in S)>6 for r in (1,2,3)):
  stats['group_excess']+=1;continue
 viable=Counter()
 for (r,mod16),vals in slots.items():
  if any(all(not conflict(x,y,F) for y in S) for x in vals):viable[r]+=1
 if any(viable[r]<6-sum(x%5==r for x in S) for r in (1,2,3)):
  stats['slot_shortage']+=1;continue
 stats['residual']+=1
assert (stats['seeds'],stats['internal_conflicts'],stats['group_excess'],stats['slot_shortage'],stats['residual'])==(12870,12657,33,180,0)
print(json.dumps({'seed_stats':dict(stats),'head_gcds':[4,55,240],
                  'scope':'independent n2640 P88 even-tail replay'},indent=2))
