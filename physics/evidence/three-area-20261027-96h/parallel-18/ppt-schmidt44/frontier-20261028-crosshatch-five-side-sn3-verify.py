#!/usr/bin/env python3
"""Exact independent replay of 130 five-coordinate PPT/SN3 range proofs."""
from itertools import combinations,product
from hashlib import sha256
from collections import Counter
import json
file='frontier-20261028-crosshatch-five-side-sn3-certificates-v1.json'
expected='ef0bb3357ee8b02bacf0f5b9fcbdd09b0934bdd5e4bf3da2ed7816a42ab94f1a'
raw=open(file,'rb').read();assert sha256(raw).hexdigest()==expected
records=json.loads(raw)['certificates'];assert len(records)==130
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
flipped=(((1,2),(0,0)),((2,2),(1,0)),((0,1),(2,0)),((0,2),(2,1)))
def matrix(es):
 m=[[0]*9 for _ in range(9)]
 for edge in es:
  v=[0]*9
  for a,b in edge:v[3*a+b]+=1
  for i in range(9):
   for j in range(9):m[i][j]+=v[i]*v[j]
 return m
rho=matrix(edges);pt=[[rho[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert pt==matrix(flipped) and sum(rho[i][i] for i in range(9))==8
coords0=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(e1,e2)) for e1,e2 in product(edges,repeat=2)]
flat=[x for q in coords0 for x in q];assert len(coords0)==16 and len(flat)==len(set(flat))==64
perms=(((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1))
def minor(cells,rr,cc,anchor,zero):
 p={}
 for perm,sgn in perms:
  ids=[cells[9*rr[k]+cc[perm[k]]] for k in range(3)]
  if all(i is not None for i in ids) and not any(i in zero for i in ids):
   m=tuple(sorted(i for i in ids if i!=anchor));p[m]=p.get(m,0)+sgn
 return{k:v for k,v in p.items() if v}
node_count=0;leaf_count=0;max_depth=0

def checktree(node,cells,anchor,zero,depth):
 global node_count,leaf_count,max_depth
 node_count+=1;max_depth=max(max_depth,depth)
 rr,cc=node['rows'],node['cols']
 assert len(rr)==len(cc)==3 and rr==sorted(set(rr)) and cc==sorted(set(cc))
 assert all(0<=x<5 for x in rr) and all(0<=x<9 for x in cc)
 p=minor(cells,rr,cc,anchor,zero);assert len(p)==1
 mon,coef=next(iter(p.items()));assert coef!=0;factors=set(mon)
 if node.get('close'):
  assert not factors and 'branches' not in node;leaf_count+=1;return
 assert factors and 'branches' in node
 labels=[idx for idx,_ in node['branches']]
 assert len(labels)==len(set(labels)) and set(labels)==factors and anchor not in factors
 for idx,child in node['branches']:checktree(child,cells,anchor,zero|{idx},depth+1)
seen=set();sidecount=Counter();ranks=Counter();traces=Counter()
for rec in records:
 side=rec['side'];keep=tuple(rec['keep']);anchor=rec['anchor']
 assert side in ('alice','bob') and keep in set(combinations(range(9),5))
 key=(side,keep);assert key not in seen;seen.add(key);sidecount[side]+=1
 coords=coords0 if side=='alice' else [tuple((b,a) for a,b in q) for q in coords0]
 idx={v:i for i,v in enumerate(keep)};cells=[None]*45;counts=[0]*16
 for j,q in enumerate(coords):
  occupied=[]
  for a,b in q:
   if a in idx:
    p=9*idx[a]+b;assert cells[p] is None;cells[p]=j;occupied.append((idx[a],b));counts[j]+=1
  assert len({a for a,b in occupied})==len(occupied) and len({b for a,b in occupied})==len(occupied)
 assert counts[anchor]==3 and max(counts)==3 and sum(counts)>0
 # Every nonzero ket is independent: their projected supports are disjoint.
 ranks[sum(n>0 for n in counts)]+=1;traces[sum(counts)]+=1
 checktree(rec['tree'],cells,anchor,set(),1)
assert sidecount=={'alice':65,'bob':65} and len(seen)==130
print(json.dumps({'certified_ppt_sn3_cut_orientations':len(seen),'side_counts':dict(sidecount),
 'proof_tree_nodes':node_count,'closed_leaves':leaf_count,'maximum_tree_depth':max_depth,
 'output_rank_histogram':dict(ranks),'trace_histogram':dict(traces),
 'crosshatch_pt_entries_checked':81,'certificate_sha256':expected,
 'limits':'Each certified source has SN exactly3; unlisted cuts are not classified and states may be locally equivalent.'},indent=2))
