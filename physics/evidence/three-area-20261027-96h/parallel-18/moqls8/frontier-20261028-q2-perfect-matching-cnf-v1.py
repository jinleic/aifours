#!/usr/bin/env python3
"""Strengthen q2 product CNF with a perfect support matching for each actual ONB."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-cross-product-cnf-v1.py';PIN='34b8e208af2c42ff48b0f974cf1493bf73ac52d05260bbfc923c361879583857'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('product module pin')
spec=importlib.util.spec_from_file_location('product',H/FILE);prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
V=range(8)
def build(T):
 data,info=prod.build(T);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 P={};i=0
 for q in range(2):
  for x in A:
   for t in A[x]:i+=1;P[q,x,t]=i
 if i!=560:raise ValueError('support numbering')
 n=info['variables'];added=[];matching_variables=0
 def var():
  nonlocal n,matching_variables
  n+=1;matching_variables+=1;return n
 for q in range(2):
  for k in range(4):
   for sym in V:
    if k==0 and sym==0:continue
    off=[x for x in range(8,64) if facts[x][k]==sym]
    if len(off)!=(8 if k==0 else 7):raise ValueError('line size')
    M={(x,t):var() for x in off for t in A[x]}
    for x in off:
     row=[M[x,t] for t in A[x]];added.append(tuple(row))
     for t in A[x]:added.append((-M[x,t],P[q,x,t]))
     for a,b in itertools.combinations(row,2):added.append((-a,-b))
    for t in V:
     col=[M[x,t] for x in off if t in A[x]]
     for a,b in itertools.combinations(col,2):added.append((-a,-b))
 L=data.decode('ascii').splitlines()
 if len(L)-1!=info['clauses']:raise ValueError('base clause count')
 out=('p cnf %d %d\n'%(n,info['clauses']+len(added))+'\n'.join(L[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in added)).encode('ascii')
 return out,{'variables':n,'clauses':info['clauses']+len(added),'base_product_formula_sha256':info['formula_sha256'],
             'matching_variables':matching_variables,'matching_clauses':len(added),'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pair',required=True);ap.add_argument('--pair-sha',required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 T=prod.base.pair(a.pair,a.pair_sha);data,info=build(T)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'product_encoder_sha256':PIN,'pair_snapshot_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Perfect support matching is necessary for unitary line matrices; SAT not physical, UNSAT needs proof and independent audit.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
