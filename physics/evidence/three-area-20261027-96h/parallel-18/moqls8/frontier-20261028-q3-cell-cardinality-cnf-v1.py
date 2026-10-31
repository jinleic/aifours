#!/usr/bin/env python3
"""Split q3 at one cell into all unordered disjoint support-size triples."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q3-cross-product-cnf-v1.py';PIN='303215b3208352e1c7e025ce36bcfd656b308d83b2441853fc633f87ceb4f1c0'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('q3 product encoder pin')
spec=importlib.util.spec_from_file_location('q3prod',H/FILE);prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
V=range(8);CASES=((1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,2),(1,2,3),(2,2,2))
def build(L,a,b,c):
 if (a,b,c) not in CASES:raise ValueError('unordered support-size triple')
 raw,info=prod.build(L);braw,binfo=prod.base.build(L);full=raw.decode('ascii').splitlines();base=braw.decode('ascii').splitlines()
 if full[1:1+binfo['clauses']]!=base[1:] or binfo['member_order_clauses']!=30:raise ValueError('base-prefix/symmetry binding')
 # Remove the old min-axis S3 ordering.  Size ordering is the sole WLOG here;
 # imposing both different orderings could cut a valid orbit.
 body=full[1:1+binfo['clauses']-30]+full[1+binfo['clauses']:]
 facts={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)};P={};v=0
 for q in range(3):
  for x in A:
   for t in A[x]:v+=1;P[q,x,t]=v
 if v!=1008:raise ValueError('support numbering')
 add=[];x=8
 for q,k in enumerate((a,b,c)):
  z=[P[q,x,t] for t in A[x]]
  for U in itertools.combinations(z,7-k):add.append(tuple(U))
  for U in itertools.combinations(z,k+1):add.append(tuple(-u for u in U))
 out=('p cnf %d %d\n'%(info['variables'],len(body)+len(add))+'\n'.join(body)+'\n'+''.join(' '.join(map(str,z))+' 0\n' for z in add)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':len(body)+len(add),'source_product_sha256':info['formula_sha256'],
             'removed_incompatible_min_order_clauses':30,'support_sizes':[a,b,c],'cardinality_clauses':len(add),
             'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--c',type=int,required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 data,info=build(prod.base.net.latin(),a.a,a.b,a.c)
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'product_encoder_sha256':PIN,'classical_source_sha256':prod.base.net.PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'Seven unordered size triples cover this cell after S3 member permutation. SAT not physical; every UNSAT needs audit and replay.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
