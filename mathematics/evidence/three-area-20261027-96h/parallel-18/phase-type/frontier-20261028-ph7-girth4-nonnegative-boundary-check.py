#!/usr/bin/env python3
"""Strengthen existing 6D Q/H positivity from positive to nonnegative rates.

Reuses the separately implemented stdlib replay's exact polynomials and binary
trees, and checks EVERY finite boundary vertex, including zero coordinates.
No file writes, floats, NumPy or SymPy.
"""
import itertools,runpy
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
x=runpy.run_path(str(ROOT/'frontier-20261028-ph7-girth4-critical-integer-replay.py'))

def boundary(poly,leaves):
 leaves=set(leaves);prefixes={p[:j]for p in leaves for j in range(len(p)+1)};arr,m,stride=x['grid'](poly);seen=set()
 def walk(path,A,bounds):
  dep=len(path)
  if path in leaves:
   seen.add(path);assert dep>=6 and min(A)>=0;finite=0
   for corner in itertools.product((0,1),repeat=6):
    coords=[bounds[j][corner[j]]for j in range(6)]
    if all(v<1 for v in coords):
     finite+=1;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(6));assert A[idx]>0
   assert finite>0;return
  assert path+'0'in prefixes and path+'1'in prefixes
  axis=dep%6;L,R=x['split'](A,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  p=list(bounds);p[axis]=(lo,mid);walk(path+'0',L,tuple(p))
  p=list(bounds);p[axis]=(mid,hi);walk(path+'1',R,tuple(p))
 walk('',arr,tuple((Q(0),Q(1))for _ in range(6)));assert seen==leaves
 return len(seen)
q=boundary(x['P'],x['C']['Q_positive_compactified_binary_leaf_paths']);h=boundary(x['H'],x['C']['H_positive_compactified_binary_leaf_paths'])
assert (q,h)==(5332,5334)
print('Exact stdlib integer PASS: Q and H strictly positive also on ALL finite zero-rate boundary faces; 10666 leaves')
