#!/usr/bin/env python3
"""q2 unitary-support formula plus exact support cardinalities at cell (1,0)."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-perfect-matching-cnf-v1.py';PIN='7e0d11a40e6159eeb45658e32dbecac8d1ccd63640847c8825ec3ac4d5a4aa57'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('matching module pin')
spec=importlib.util.spec_from_file_location('match',H/FILE);match=importlib.util.module_from_spec(spec);spec.loader.exec_module(match)
V=range(8);CASES=((1,1),(1,2),(1,3),(1,4),(2,2),(2,3))
def build(T,a,b):
 if (a,b) not in CASES:raise ValueError('unordered support sizes')
 data,info=match.build(T);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)};P={};i=0
 for q in range(2):
  for x in A:
   for t in A[x]:i+=1;P[q,x,t]=i
 if i!=560:raise ValueError('support numbering')
 add=[];x=8
 for q,k in ((0,a),(1,b)):
  z=[P[q,x,t] for t in A[x]]
  # At least k: each (5-k+1)-subset has a true literal.
  for U in itertools.combinations(z,6-k):add.append(tuple(U))
  # At most k: each (k+1)-subset has a false literal.
  for U in itertools.combinations(z,k+1):add.append(tuple(-v for v in U))
 L=data.decode('ascii').splitlines()
 if len(L)-1!=info['clauses']:raise ValueError('base clauses')
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(add))+'\n'.join(L[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in add)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+len(add),'base_matching_sha256':info['formula_sha256'],
             'support_sizes':[a,b],'cardinality_clauses':len(add),'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pair',required=True);ap.add_argument('--pair-sha',required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 T=match.prod.base.pair(a.pair,a.pair_sha);data,info=build(T,a.a,a.b)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'matching_encoder_sha256':PIN,'pair_snapshot_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Six cases cover unordered nonempty disjoint support-size pairs. Each UNSAT needs independent formula/proof review; UNKNOWN remains open.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
