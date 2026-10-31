#!/usr/bin/env python3
"""Finite checks for the written odd-105 quotient profile caller."""
from collections import Counter
from itertools import combinations_with_replacement
G=21;h3=[0,7,14];h7=[0,3,6,9,12,15,18];hist=Counter()
for a in range(G):
 for b in range(G):
  v=[(a+x)%G for x in h3]+[(b+x)%G for x in h7]
  counts=Counter(v);assert len(counts) in (9,10) and max(counts.values())<=2
  hist[len(counts)]+=1
parts=[]
def rec(left,start,path):
 if left==0:parts.append(path);return
 for x in range(start,left+1,2):rec(left-x,x,path+[x])
rec(10,2,[])
assert parts==[[2,2,2,2,2],[2,2,2,4],[2,2,6],[2,4,4],[2,8],[4,6],[10]]
print('Z21: 3+7 quotient coset profile histogram',dict(hist),'max multiplicity2')
print('even partitions of 10',parts)
print('Finite checks only; all odd q structural argument is written separately.')
