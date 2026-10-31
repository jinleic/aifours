#!/usr/bin/env python3
"""Generate explicit spanning-tree/support contradictions for exceptional 5-net."""
import argparse,collections,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
SRC='95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67'
SCR='121fe7b1b4fafd47593c042ade5f8b18c1d9a6be43d69ea605884f12f1b1b68c'
V=range(8)
def source(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('input pin')
 return b

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 rows=[s.strip() for s in source('frontier-20261028-source-wanless-max3-order8-v1.txt',SRC).decode('ascii').splitlines() if s.strip()]
 if rows[0].split()[:3]!=['8','8','114'] or len(rows)!=913:raise ValueError('catalogue layout')
 rows=rows[1:];trip=[]
 for s in range(66,69):
  sq=[[ord(ch)-97 for ch in rows[8*s+i]] for i in V]
  if any(set(row)!=set(V) for row in sq) or any({sq[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
  trip.append(sq)
 for u,v in itertools.combinations(range(3),2):
  if len({(trip[u][i][j],trip[v][i][j]) for i in V for j in V})!=64:raise ValueError('orthogonal')
 mates=[]
 for sq in trip:
  norm={sq[0][j]:j for j in V}
  mates.append([[norm[sq[i][j]] for j in V] for i in V])
 screen=json.loads(source('frontier-20261028-wanless-q1-xor-core-receipt-v1.json',SCR))
 o=screen['records'][22]['orientations'][0]
 if (o['row_class'],o['column_class'])!=(0,1) or [(i,c) for i,c in enumerate(o['core_counts_by_geometry']) if c]!=[(2,32),(5,32)]:raise ValueError('screen residual mismatch')
 records=[]
 for gi in (2,5):
  f=screen['geometry_representatives'][gi]
  if sorted(f)!=list(V):raise ValueError('geometry')
  E=[];forbidden={};facts={}
  for i in range(1,8):
   for j in V:
    z=(j,*(m[i][j] for m in mates))
    if len(set(z))!=4:raise ValueError('net collision')
    if f[z[0]]^f[z[1]]^f[z[2]]^f[z[3]]==0:
     x=8*i+j;E.append(x);forbidden[x]=sorted(z);facts[x]=(i,j,*(m[i][j] for m in mates))
  if len(E)!=32:raise ValueError('eligible size')
  lines=[[x for x in E if facts[x][k]==h] for k in range(5) for h in V]
  counts=[[len(lines[8*k+h]) for h in V] for k in range(5)]
  if counts[0]!=[0,8,4,4,4,4,4,4] or any(row!=[4]*8 for row in counts[1:]):raise ValueError('line counts')
  # For each 4-eligible line, every heavy cell forces every other cell heavy.
  adjacency={x:[] for x in E}
  for k in range(5):
   for h in V:
    z=lines[8*k+h]
    if len(z)==4:
     for x in z:
      for y in z:
       if x!=y:adjacency[x].append((y,k,h))
  root=E[0];seen={root};queue=collections.deque([root]);tree=[]
  while queue:
   x=queue.popleft()
   for y,k,h in adjacency[x]:
    if y not in seen:seen.add(y);queue.append(y);tree.append({'parent':x,'child':y,'class':k,'symbol':h})
  if len(seen)!=32 or len(tree)!=31:raise ValueError('heavy implication graph disconnected')
  row2=lines[2]
  mismatch=next(((x,y) for x,y in itertools.combinations(row2,2) if forbidden[x]!=forbidden[y]),None)
  if mismatch is None:raise ValueError('no unequal support pair on row 2')
  x,y=mismatch
  records.append({'geometry_index':gi,'geometry_map':f,'eligible_cells':E,'line_count_matrix':counts,
                  'tree_root':root,'forcing_tree':tree,'row2_four_heavy_cells':row2,
                  'mismatch_cells':[x,y],'forbidden_labels':[forbidden[x],forbidden[y]],
                  'support_labels':[sorted(set(V)-set(forbidden[x])),sorted(set(V)-set(forbidden[y]))]})
 result={'result':'TWO_EXPLICIT_FOUR_HEAVY_SUPPORT_OBSTRUCTIONS','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'catalogue_snapshot_sha256':SRC,'complete_screen_sha256':SCR,'species_index':22,'row_class':0,'column_class':1,
         'normalized_classical_mates':mates,'cases':records,
         'limits':'Finite incidence certificate; mathematical inference and external catalogue completeness are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(result,h,indent=2);h.write('\n')
 print(json.dumps({'result':result['result'],'source_sha256':result['source_sha256'],
                   'cases':[{'geometry':r['geometry_index'],'eligible':len(r['eligible_cells']),'tree_edges':len(r['forcing_tree']),
                             'row2':r['row2_four_heavy_cells'],'mismatch':r['mismatch_cells'],
                             'forbidden':r['forbidden_labels']} for r in records]},indent=2))
if __name__=='__main__':main()
