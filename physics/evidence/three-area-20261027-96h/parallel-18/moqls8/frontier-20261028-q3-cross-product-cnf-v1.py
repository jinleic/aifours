#!/usr/bin/env python3
"""Add all three actual pair-product singleton constraints to a q3 support CNF."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q3-one-classical-support-cnf-v1.py';PIN='936563584169a2cf361e55c4b247ff95ed51ec17b92c296cb86618f5e4d45cd8'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base source pin')
spec=importlib.util.spec_from_file_location('q3base',H/FILE);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
V=range(8)
def build(L):
 data,info=base.build(L);f={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:tuple(t for t in V if t not in f[x][1:]) for x in range(8,64)};P={};v=0
 for q in range(3):
  for x in A:
   for t in A[x]:v+=1;P[q,x,t]=v
 if v!=1008:raise ValueError('support map')
 n=info['variables'];extra=[];npairs=0
 def var():
  nonlocal n
  n+=1;return n
 for x,y in itertools.combinations(range(8,64),2):
  if any(a==b for a,b in zip(f[x],f[y])):continue
  npairs+=1;common=sorted(set(A[x])&set(A[y]));B={}
  for q in range(3):
   for t in common:B[q,t]=var()
   for t in common:
    b=B[q,t];extra.extend([(-b,P[q,x,t]),(-b,P[q,y,t]),(b,-P[q,x,t],-P[q,y,t])])
  for q,r in itertools.combinations(range(3),2):
   for t in common:
    for u in common:
     extra.append(tuple([-B[q,t]]+[B[q,v] for v in common if v!=t]+[-B[r,u]]+[B[r,w] for w in common if w!=u]))
 if npairs!=1008:raise ValueError('nonadjacent pair count')
 z=data.decode('ascii').splitlines()
 if len(z)-1!=info['clauses']:raise ValueError('base clauses')
 out=('p cnf %d %d\n'%(n,info['clauses']+len(extra))+'\n'.join(z[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in extra)).encode('ascii')
 return out,{'variables':n,'clauses':info['clauses']+len(extra),'base_formula_sha256':info['formula_sha256'],
             'nonadjacent_pairs':npairs,'cross_product_clauses':len(extra),'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 data,info=build(base.net.latin())
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'base_encoder_sha256':PIN,'classical_source_sha256':base.net.PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'Necessary q3 support and pair-product conditions only; physical soundness/encoding/certificate require independent audit.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
