#!/usr/bin/env python3
"""Generate q2 support+two-axis triangles for any pinned two-MOLS pair."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-two-classical-support-cnf-v1.py';PIN='3bd85257dddab938638903ef737200791adf47c6a4869636b819d718cbda2ad8'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base module hash')
spec=importlib.util.spec_from_file_location('q2base',H/FILE);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
V=range(8)
def pair(path,pin):
 b=pathlib.Path(path).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('pair pin')
 L=[x.strip() for x in b.decode('ascii').splitlines() if x.strip()]
 if len(L)!=17 or L[0].split()[:2]!=['8','8']:raise ValueError('two-square extraction')
 T=[[[ord(ch)-97 for ch in L[1+8*k+i]] for i in V] for k in range(2)]
 for S in T:
  if any(set(row)!=set(V) for row in S) or any({S[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
 if len({(T[0][i][j],T[1][i][j]) for i in V for j in V})!=64:raise ValueError('orthogonality')
 return [[[T[k][0].index(T[k][i][j]) for j in V] for i in V] for k in range(2)]
def build(T):
 data,info=base.build(T,True);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 E=[(x,y) for x,y in itertools.combinations(range(8,64),2) if any(a==b for a,b in zip(facts[x],facts[y]))]
 if len(E)!=700:raise ValueError('net edge count')
 n=info['support_variables'];B={}
 for q in range(2):
  for x,y in E:
   C=sorted(set(A[x])&set(A[y]))
   if len(C)>=2:
    for t in C:n+=1;B[q,x,y,t]=n
 if n!=info['variables']-1120:raise ValueError('aux numbering')
 edges=set(E);added=[];triangles=0
 for x,y,z in itertools.combinations(range(8,64),3):
  if (x,y) not in edges or (x,z) not in edges or (y,z) not in edges:continue
  C=sorted(set(A[x])&set(A[y])&set(A[z]))
  for t,u in itertools.combinations(C,2):
   triangles+=1
   for q in range(2):
    d=[]
    for i,j in ((x,y),(x,z),(y,z)):
     d.extend((-B[q,i,j,t],-B[q,i,j,u]));d.extend(B[q,i,j,w] for w in set(A[i])&set(A[j])-{t,u})
    added.append(tuple(d))
 lines=data.decode('ascii').splitlines();body='\n'.join(lines[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in added)
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(added))+body).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+len(added),'axis_triangles':triangles,
             'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pair',required=True);ap.add_argument('--pair-sha',required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 T=pair(a.pair,a.pair_sha);data,info=build(T)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'base_encoder_sha256':PIN,'pair_snapshot_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Necessary q2 support/phase constraints only; any SAT is not physical, UNSAT needs certificate and review.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
