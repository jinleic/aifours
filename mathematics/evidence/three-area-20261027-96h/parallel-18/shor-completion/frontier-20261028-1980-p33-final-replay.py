#!/usr/bin/env python3
"""Independent set-based replay of the last 1980 P33 border branch."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
# Verify the forced-36 parity bound via independently built incompatibility sets.
G=GA|{36};C={x for x in range(n) if all(x==y or gcd(x-y,n) not in G for y in Y)}
summary={}
for r in (1,2,3):
 ev={x for x in C if x%5==r and x%2==0};od={x for x in C if x%5==r and x%2==1}
 assert len(ev)==4
 lists=[{x for x in od if all(gcd(x-y,n) not in G for y in S)} for S in combinations(sorted(ev),1 if r in (1,3) else 3)]
 maxodd=max(map(len,lists));assert maxodd<=6;summary[r]={'even_candidates':len(ev),'max_odd_compatible':maxodd}
# Check head matching and triple implications directly.
F=GY|{36,180}
p5={x for x in range(n) if x%11==5 and all(x==a or gcd(x-a,n) not in F for a in A)}
p9={x for x in range(n) if x%11==9 and all(x==a or gcd(x-a,n) not in F for a in A)}
assert len(p5)==len(p9)==4
edges=[(a,b) for a in p5 for b in p9 if gcd(a-b,n)==180]
assert len(edges)==4 and {a for a,b in edges}==p5 and {b for a,b in edges}==p9
F=GY|{36,660};v={x for x in range(n) if x%11==9 and all(x==a or gcd(x-a,n) not in F for a in A)}
tri=[{548,1208,1868},{603,1263,1923}]
assert set.union(*tri)==v and all(gcd(a-b,n)==660 for t in tri for a,b in combinations(t,2))
# Separately ordered, set-based exhaustive Q quota search.
F=GA|{180,660};C={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)};assert len(C)==332
adj={x:{y for y in C if y!=x and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%4==r} for r in range(4)]+[{x for x in C if x%5==r} for r in range(5)]
need=[15]*4+[12]*5;active=set(C)
for x in sorted(Y):
 assert x in active;active.remove(x);active-=adj[x]
 for j,g in enumerate(groups):need[j]-=int(x in g)
stats={'nodes':0,'prunes':0}
def dfs(active,need):
 stats['nodes']+=1
 if any(k<0 for k in need):return False
 active=set(active)
 for g,k in zip(groups,need):
  if k==0:active-=g
 if any(len(active&g)<k for g,k in zip(groups,need)):
  stats['prunes']+=1;return False
 if all(k==0 for k in need):return True
 j=min((j for j,k in enumerate(need) if k),key=lambda j:(Fraction(len(active&groups[j]),need[j]),-j))
 x=max(active&groups[j],key=lambda x:(len(adj[x]&active),-x))
 nxt=[k-int(x in g) for k,g in zip(need,groups)]
 return dfs(active-{x}-adj[x],nxt) or dfs(active-{x},need)
if dfs(active,need):raise AssertionError('unexpected tail quota witness')
print(json.dumps({'parity':summary,'Q_core':len(C),'search':stats,'result':'UNSAT',
                  'scope':'separate exact n1980 P33 branch replay'},indent=2))
