#!/usr/bin/env python3
"""Exact integer graph replay for the D6-equivariant 6D reduction."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;c=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=c.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';G=[set()for _ in range(15)]
for z in json.loads(raw)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
assert all(len(g)==6 for g in G)
r=(6,7,5,9,8,10,11,12,13,14,2,1,0,3,4)
s=(0,1,2,4,3,10,12,11,13,14,5,7,6,8,9)
e=tuple(range(15));comp=lambda a,b:tuple(a[b[i]]for i in range(15))
rs=[e]
for k in range(1,7):rs.append(comp(rs[-1],r))
assert rs[6]==e and len(set(rs[:6]))==6 and comp(s,s)==e and comp(comp(s,r),s)==rs[5]
group=rs[:6]+[comp(s,q)for q in rs[:6]];assert len(set(group))==12
for a in group:
 assert all((j in G[i])==(a[j]in G[a[i]])for i in range(15)for j in range(15))
reflections=[]
for k in range(6):
 a=comp(s,rs[k]);fixed=[v for v in range(15)if a[v]==v]
 assert len(fixed)==3 and all(all(a[w]!=w for w in G[v])for v in fixed)
 reflections.append({'k':k,'fixed_vertices':fixed})
center={2,5,10};assert all(b in G[a] for a in center for b in center if a!=b)
assert [r[v]for v in (2,5,10)]==[5,10,2]
r3=rs[3];assert {v for v in range(15)if r3[v]==v}==center
for v in center:
 assert {w for w in G[v]if r3[w]==w}==center-{v}
# Four center-to-outer spokes are a transitive orbit of each center stabilizer.
for v in center:
 H=[a for a in group if a[v]==v];sp=G[v]-center
 assert len(H)==4 and len(sp)==4 and {a[min(sp)]for a in H}==sp
edges={tuple(sorted((u,v)))for u in center for v in G[u]-center}
assert len(edges)==12
seed=(2,8);orbit={tuple(sorted((a[seed[0]],a[seed[1]])))for a in group};assert orbit==edges
sr=comp(s,r);assert sr[8]==8 and sr[2]==10 and 2 in G[8]and 10 in G[8]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'rotation':r,'reflection':s,'subgroup_order':len(group),
 'triangle':sorted(center),'reflections':reflections,'spoke_edges':sorted(edges),
 'center_stabilizer_transitive_on_four_spokes':True,'reflection_sr_fixes_8_and_swaps_2_10':True,'status':'PASS'}
(P/'frontier-20261029-g6-dihedral-symmetry-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
