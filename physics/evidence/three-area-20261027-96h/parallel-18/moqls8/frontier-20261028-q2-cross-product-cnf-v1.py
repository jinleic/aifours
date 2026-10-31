#!/usr/bin/env python3
"""Strengthen q2 support CNF with actual cross-cell pair-product singleton clauses."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-net-triangle-cnf-v1.py';PIN='f2db8cd92f24ed93ace21d9971dede1832df30bc4c893220c2dcc8d268d51d0a'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base module pin')
spec=importlib.util.spec_from_file_location('q2tri',H/FILE);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
V=range(8)
def build(T):
 data,info=base.build(T);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 P={};n=0
 for q in range(2):
  for x in A:
   for t in A[x]:n+=1;P[q,x,t]=n
 if n!=560:raise ValueError('support numbering')
 n=info['variables'];extra=[];pairs=0
 def var():
  nonlocal n
  n+=1;return n
 for x,y in itertools.combinations(range(8,64),2):
  if any(a==b for a,b in zip(facts[x],facts[y])):continue
  pairs+=1;C=sorted(set(A[x])&set(A[y]));B={}
  for q in range(2):
   for t in C:B[q,t]=var()
   for t in C:
    b=B[q,t];extra.extend([(-b,P[q,x,t]),(-b,P[q,y,t]),(b,-P[q,x,t],-P[q,y,t])])
  for t in C:
   for u in C:
    extra.append(tuple([-B[0,t]]+[B[0,v] for v in C if v!=t]+[-B[1,u]]+[B[1,w] for w in C if w!=u]))
 lines=data.decode('ascii').splitlines()
 if len(lines)-1!=info['clauses']:raise ValueError('base clause count')
 out=('p cnf %d %d\n'%(n,info['clauses']+len(extra))+'\n'.join(lines[1:])+'\n'+''.join(' '.join(map(str,c))+' 0\n' for c in extra)).encode('ascii')
 return out,{'variables':n,'clauses':info['clauses']+len(extra),'base_formula_sha256':info['formula_sha256'],
             'nonadjacent_offrow_pairs':pairs,'added_clauses':len(extra),'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pair',required=True);ap.add_argument('--pair-sha',required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 T=base.pair(a.pair,a.pair_sha);data,info=build(T)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'base_encoder_sha256':PIN,'pair_snapshot_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Necessary support/triangle/product-singleton clauses; any SAT is not physical, UNSAT requires independent proof and encoding review.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
