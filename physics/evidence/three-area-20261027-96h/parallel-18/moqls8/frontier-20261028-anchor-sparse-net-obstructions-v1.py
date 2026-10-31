#!/usr/bin/env python3
"""Exact one-overlap or odd-phase-cycle obstruction for each net and anchor line."""
import argparse,collections,hashlib,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
   ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
V=range(8)
def read_catalogue(name,sha,n):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=sha:raise ValueError('snapshot hash')
 L=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if L[0].split()[:3]!=['8','8',str(n)] or len(L)!=1+8*n:raise ValueError('snapshot size')
 S=[[[ord(c)-97 for c in L[1+8*k+i]] for i in V] for k in range(n)]
 for A in S:
  if any(set(row)!=set(V) for row in A) or any({A[i][j] for i in V}!=set(V) for j in V):raise ValueError('not Latin')
 T=[]
 for k in range(0,n,3):
  Q=S[k:k+3]
  for a,b in itertools.combinations(range(3),2):
   if len({(Q[a][i][j],Q[b][i][j]) for i in V for j in V})!=64:raise ValueError('not MOLS')
  T.append(Q)
 return T

def orient(T,r,c,s):
 rows=[s]+[x for x in V if x!=s];relabel={v:i for i,v in enumerate(rows)}
 points=[(i,j,*(T[a][i][j] for a in range(3))) for i in V for j in V]
 grid={(relabel[p[r]],p[c]):p for p in points}
 if len(grid)!=64:raise ValueError('OA strength two')
 other=[k for k in range(5) if k not in (r,c)]
 inv=[{grid[0,j][k]:j for j in V} for k in other]
 return [[[inv[a][grid[i,j][k]] for j in V] for i in V] for a,k in enumerate(other)]

def setup(T):
 facts={8*i+j:(i,j,*(L[i][j] for L in T)) for i in range(1,8) for j in V}
 A={x:set(V)-set(f[1:]) for x,f in facts.items()}
 if any(len(z)!=4 for z in A.values()):raise ValueError('four distinct forbidden labels')
 lines={(k,v):[x for x in facts if facts[x][k]==v] for k in range(5) for v in V}
 return facts,A,lines

def one_overlap(A,lines):
 for (k,v),line in lines.items():
  for x,y in itertools.combinations(line,2):
   q=A[x]&A[y]
   if len(q)==1:return {'kind':'one_overlap','line':[k,v],'cells':[x,y],'allowed':[sorted(A[x]),sorted(A[y])],'intersection':sorted(q)}
 return None

def odd_cycle(A,lines):
 edgeinfo={}
 for (k,v),line in lines.items():
  for x,y in itertools.combinations(line,2):
   common=tuple(sorted(A[x]&A[y]))
   if len(common)==2:edgeinfo[(x,y)]=(common,k,v)
 for pair in itertools.combinations(V,2):
  adj={x:[] for x in A if set(pair)<=A[x]}
  for (x,y),(common,k,v) in edgeinfo.items():
   if common==pair:adj[x].append(y);adj[y].append(x)
  parent={};depth={}
  for root in adj:
   if root in depth:continue
   parent[root]=None;depth[root]=0;queue=collections.deque([root])
   while queue:
    x=queue.popleft()
    for y in adj[x]:
     if y not in depth:parent[y]=x;depth[y]=depth[x]+1;queue.append(y)
     elif depth[x]%2==depth[y]%2:
      # Root paths intersect at LCA; the closing edge x--y makes an odd cycle.
      px=[];z=x
      while z is not None:px.append(z);z=parent[z]
      py=[];z=y
      while z is not None:py.append(z);z=parent[z]
      common_root=next(z for z in px if z in set(py))
      ix=px.index(common_root);iy=py.index(common_root)
      cycle=px[:ix+1]+list(reversed(py[:iy]))
      if len(cycle)<3 or len(cycle)%2!=1:raise ValueError('bad odd cycle')
      edge_lines=[]
      for u,w in zip(cycle,cycle[1:]+cycle[:1]):
       k,v=edgeinfo[tuple(sorted((u,w)))][1:];edge_lines.append([k,v])
      return {'kind':'odd_phase_cycle','axes':list(pair),'cells':cycle,'edge_lines':edge_lines,
              'allowed':[sorted(A[z]) for z in cycle]}
 return None

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 triples=sum((read_catalogue(*q) for q in P),[])
 if len(triples)!=39:raise ValueError('species count')
 records=[];counts=collections.Counter();lengths=collections.Counter()
 for sp,T in enumerate(triples):
  for r in range(5):
   c=next(z for z in range(5) if z!=r)
   for anchor in V:
    mates=orient(T,r,c,anchor);_,A,lines=setup(mates)
    ob=one_overlap(A,lines)
    if ob is None:ob=odd_cycle(A,lines)
    if ob is None:raise ValueError('uncovered species/anchor '+repr((sp,r,anchor)))
    counts[ob['kind']]+=1
    if ob['kind']=='odd_phase_cycle':lengths[len(ob['cells'])]+=1
    records.append({'species_index':sp,'row_class':r,'column_class':c,'anchor_symbol':anchor,**ob})
 out={'result':'ALL_1560_NET_ANCHORS_HAVE_SUPPORT_OR_ODD_PHASE_OBSTRUCTION',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'snapshots':{name:sha for name,sha,n in P},'species':39,'row_classes':5,'anchors_per_class':8,
      'contexts':len(records),'obstruction_counts':dict(counts),'odd_cycle_lengths':dict(lengths),
      'records':records,'elapsed_seconds':time.monotonic()-start,
      'limits':'Finite incidence/odd-cycle certificates; mathematical forcing and external catalogue completeness are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
