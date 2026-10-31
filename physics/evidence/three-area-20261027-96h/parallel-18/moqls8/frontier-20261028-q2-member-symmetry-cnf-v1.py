#!/usr/bin/env python3
"""q2 support matching formula plus exact Q/R swap symmetry at cell (1,0)."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-perfect-matching-cnf-v1.py';PIN='7e0d11a40e6159eeb45658e32dbecac8d1ccd63640847c8825ec3ac4d5a4aa57'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base source hash')
spec=importlib.util.spec_from_file_location('match',H/FILE);match=importlib.util.module_from_spec(spec);spec.loader.exec_module(match)
V=range(8)
def build(T):
 data,info=match.build(T);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 P={};i=0
 for q in range(2):
  for x in A:
   for t in A[x]:i+=1;P[q,x,t]=i
 if i!=560:raise ValueError('support numbering')
 # Nonempty disjoint supports at x=8 have distinct minima. Swapping Q,R
 # makes min(S_Q) < min(S_R) WLOG. Reject every reversed pair of minima.
 x=8;add=[]
 for t,u in itertools.product(A[x],repeat=2):
  if t>u:
   add.append(tuple([-P[0,x,t],-P[1,x,u]]+[P[0,x,v] for v in A[x] if v<t]+[P[1,x,w] for w in A[x] if w<u]))
 if len(add)!=10:raise ValueError('minimum comparison coverage')
 L=data.decode('ascii').splitlines()
 if len(L)-1!=info['clauses']:raise ValueError('base count')
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(add))+'\n'.join(L[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in add)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+len(add),'base_matching_formula_sha256':info['formula_sha256'],
             'member_swap_clauses':len(add),'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pair',required=True);ap.add_argument('--pair-sha',required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 T=match.prod.base.pair(a.pair,a.pair_sha);data,info=build(T)
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'matching_encoder_sha256':PIN,'pair_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Q/R exchange is exact; proof, full independent encoding and physical symmetry audit required.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
