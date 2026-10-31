#!/usr/bin/env python3
"""Add sound conditional two-axis triangle clauses using actual product orthogonality."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-member-symmetry-cnf-v1.py';PIN='bde1def386275721f4168482540e8651a8c36ac90de15af600833efa177693a0'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('symmetry source pin')
spec=importlib.util.spec_from_file_location('sym',H/FILE);sym=importlib.util.module_from_spec(spec);spec.loader.exec_module(sym)
V=range(8)
def build(T):
 data,info=sym.build(T);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 pairs=list(itertools.combinations(range(8,64),2))
 E={(x,y) for x,y in pairs if any(a==b for a,b in zip(facts[x],facts[y]))}
 non=[(x,y) for x,y in pairs if (x,y) not in E]
 if len(E)!=700 or len(non)!=840:raise ValueError('pair partition')
 # Exact aux numbering used by the base q2 support and cross-product encoders.
 B={};n=560
 for q in range(2):
  for x,y in sorted(E):
   C=sorted(set(A[x])&set(A[y]))
   if len(C)>=2:
    for t in C:n+=1;B[q,x,y,t]=n
 if n!=5040:raise ValueError('line intersection auxiliary numbering')
 n=6160
 for x,y in non:
  C=sorted(set(A[x])&set(A[y]))
  for q in range(2):
   for t in C:n+=1;B[q,x,y,t]=n
 if n!=11200:raise ValueError('cross-cell intersection auxiliary numbering')
 added=[];wedges=0
 for x,y,z in itertools.combinations(range(8,64),3):
  tri=((x,y),(x,z),(y,z));missing=[p for p in tri if p not in E]
  if len(missing)!=1:continue
  wedges+=1;a,b=missing[0];Txyz=sorted(set(A[x])&set(A[y])&set(A[z]));K=sorted(set(A[a])&set(A[b]))
  for t,u in itertools.combinations(Txyz,2):
   for q in range(2):
    other=1-q
    C=[]
    # Negate the condition that each Q edge intersection is exactly {t,u}.
    for i,j in tri:
     C.extend((-B[q,i,j,t],-B[q,i,j,u]))
     C.extend(B[q,i,j,v] for v in set(A[i])&set(A[j])-{t,u})
    # Negate the condition that the other member has exactly one
    # shared coordinate on the non-net edge, for each candidate axis.
    for v in K:
     clause=C+[-B[other,a,b,v]]+[B[other,a,b,w] for w in K if w!=v]
     added.append(tuple(clause))
 L=data.decode('ascii').splitlines()
 if len(L)-1!=info['clauses']:raise ValueError('base CNF count')
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(added))+'\n'.join(L[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in added)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+len(added),'base_formula_sha256':info['formula_sha256'],
             'open_wedges':wedges,'added_conditional_triangle_clauses':len(added),'formula_bytes':len(out),
             'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--cnf',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
 T=sym.match.prod.base.pair(a.pair,a.pair_sha);data,info=build(T)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'symmetry_encoder_sha256':PIN,'pair_snapshot_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Conditional cross-member product triangles are necessary only; independent encoding/physical proof audit and certificate required.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
