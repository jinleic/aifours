#!/usr/bin/env python3
"""Exact CNF necessary conditions for arbitrary complex Q with three classical mates.

Supports use the actual five-net and one anchor ONB; no amplitude flatness.
Triangles are valid two-coordinate projection obstructions. UNSAT requires
separate proof replay and independent verification of this reduction/encoding.
"""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
M='frontier-20261028-anchor-sparse-net-obstructions-v1.py';MP='6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'
if hashlib.sha256((H/M).read_bytes()).hexdigest()!=MP:raise ValueError('source input hash')
s=importlib.util.spec_from_file_location('anchor_net',H/M);net=importlib.util.module_from_spec(s);s.loader.exec_module(net)
V=range(8)

def build(species,r,c,anchor,require_nonclassical=True):
 triples=sum((net.read_catalogue(*p) for p in net.P),[])
 if species not in range(39) or r not in range(5) or c not in range(5) or c==r or anchor not in V:raise ValueError('case')
 T=net.orient(triples[species],r,c,anchor)
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 if any(len(a)!=4 for a in A.values()):raise ValueError('forbidden collision')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in V}
 if any(len(z)!=8 for z in lines.values()):raise ValueError('invalid line')
 count=0;clauses=[]
 def var():
  nonlocal count
  count+=1;return count
 def clause(*z):
  if not z or any(q==0 or abs(q)>count for q in z):raise ValueError('malformed clause')
  clauses.append(tuple(z))
 P={(x,t):var() for x in A for t in A[x]}
 for x in A:clause(*(P[x,t] for t in A[x]))
 for line in lines.values():
  for t in V:
   if t in line:continue
   eligible=[x for x in line if x>=8 and t in A[x]]
   if len(eligible)!=4:raise ValueError('axis-on-line four-candidate count')
   clause(*(P[x,t] for x in eligible))
 edges=set()
 for line in lines.values():edges.update(itertools.combinations((x for x in line if x>=8),2))
 for x,y in sorted(edges):
  common=sorted(set(A[x])&set(A[y]))
  if len(common)==1:
   t=common[0];clause(-P[x,t],-P[y,t]);continue
  if len(common)<2:continue
  B={t:var() for t in common}
  for t in common:
   b=B[t];clause(-b,P[x,t]);clause(-b,P[y,t]);clause(b,-P[x,t],-P[y,t])
  for t in common:clause(-B[t],*(B[u] for u in common if u!=t))
 triangles=[]
 for t,u in itertools.combinations(V,2):
  G={x:set() for x in A if t in A[x] and u in A[x]}
  for x,y in edges:
   if x in G and y in G and set(A[x])&set(A[y])=={t,u}:G[x].add(y);G[y].add(x)
  for x in sorted(G):
   for y in sorted(z for z in G[x] if z>x):
    for z in sorted(z for z in G[x]&G[y] if z>y):
     triangles.append((t,u,x,y,z));clause(-P[x,t],-P[x,u],-P[y,t],-P[y,u],-P[z,t],-P[z,u])
 if require_nonclassical:
  N=[]
  for x in A:
   for t,u in itertools.combinations(A[x],2):
    n=var();N.append(n);clause(-n,P[x,t]);clause(-n,P[x,u])
  clause(*N)
 data=('p cnf %d %d\n'%(count,len(clauses)) + ''.join(' '.join(map(str,z))+' 0\n' for z in clauses)).encode('ascii')
 return data,{'species':species,'row_class':r,'column_class':c,'anchor_symbol':anchor,
              'nonclassical_required':require_nonclassical,'variables':count,'clauses':len(clauses),
              'support_variables':len(P),'five_net_pairs':len(edges),'sound_two_axis_triangles':len(triangles),
              'formula_sha256':hashlib.sha256(data).hexdigest(),'formula_bytes':len(data)}

def main():
 p=argparse.ArgumentParser();p.add_argument('--species',type=int,required=True);p.add_argument('--row-class',type=int,default=0);p.add_argument('--column-class',type=int,default=1);p.add_argument('--anchor',type=int,default=0);p.add_argument('--without-nonclassical',action='store_true');p.add_argument('--cnf',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
 data,summary=build(a.species,a.row_class,a.column_class,a.anchor,not a.without_nonclassical)
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 summary.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
                 'net_module_sha256':MP,'elapsed_seconds':time.monotonic()-start,
                 'limits':'Necessary-support CNF only; proof, independent encoder check, Hcat and written theorem remain separate.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(summary,h,indent=2);h.write('\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
