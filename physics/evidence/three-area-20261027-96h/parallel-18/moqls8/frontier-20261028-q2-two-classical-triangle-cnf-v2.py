#!/usr/bin/env python3
"""Add sound two-axis orthogonality-triangle clauses to the pinned q2 CNF."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-two-classical-support-cnf-v1.py';PIN='3bd85257dddab938638903ef737200791adf47c6a4869636b819d718cbda2ad8'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base module pin')
spec=importlib.util.spec_from_file_location('basecnf',H/FILE);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
V=range(8)
def build():
 T=base.net.actual_net();data,info=base.build(T,True)
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 P={};n=0
 for q in range(2):
  for x in A:
   for t in A[x]:n+=1;P[q,x,t]=n
 if n!=info['support_variables']:raise ValueError('support numbering')
 L=[set(x for x in A if facts[x][k]==v) for k in range(4) for v in V];E=set()
 for line in L:E.update(itertools.combinations(sorted(line),2))
 # Reconstruct the base formula's exact intersection auxiliaries B[q,x,y,t].
 B={}
 for q in range(2):
  for x,y in sorted(E):
   common=sorted(set(A[x])&set(A[y]))
   if len(common)>=2:
    for t in common:n+=1;B[q,x,y,t]=n
 if n!=info['variables']-1120:raise ValueError('intersection auxiliary numbering')
 added=[];triangles=[]
 for t,u in itertools.combinations(V,2):
  G={x:set() for x in A if t in A[x] and u in A[x]}
  for x,y in E:
   if x in G and y in G:G[x].add(y);G[y].add(x)
  for x in sorted(G):
   for y in sorted(z for z in G[x] if z>x):
    for z in sorted(z for z in G[x]&G[y] if z>y):
     triangles.append((t,u,x,y,z))
     for q in range(2):
      C=[]
      for a,b in ((x,y),(x,z),(y,z)):
       common=sorted(set(A[a])&set(A[b]))
       C.extend((-B[q,a,b,t],-B[q,a,b,u]))
       C.extend(B[q,a,b,v] for v in common if v not in (t,u))
      added.append(tuple(C))
 lines=data.decode('ascii').splitlines();header=lines[0].split()
 if header[:2]!=['p','cnf'] or int(header[2])!=info['variables'] or len(lines)-1!=info['clauses']:raise ValueError('base CNF')
 all_data=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(added))+'\n'.join(lines[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in added)).encode()
 return all_data,{'variables':info['variables'],'clauses':info['clauses']+len(added),'base_formula_sha256':info['formula_sha256'],
                  'nonclassical_required':True,'triangles':len(triangles),'added_triangle_clauses':len(added),
                  'formula_sha256':hashlib.sha256(all_data).hexdigest(),'formula_bytes':len(all_data)}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 data,info=build()
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'base_module_sha256':PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'Triangle constraints are necessary only; proof and independent physical/encoder audit required.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
