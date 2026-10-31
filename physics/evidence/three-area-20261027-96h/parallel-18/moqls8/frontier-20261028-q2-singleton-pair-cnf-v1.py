#!/usr/bin/env python3
"""Exact q2 singleton/singleton split into ten unordered coordinate pairs."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-cell-cardinality-cnf-v1.py';PIN='fbd15d78f11a878bca1696bbb395715d0902686fd1a5aaaf0377f40565fc5fb8'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('cardinality encoder pin')
spec=importlib.util.spec_from_file_location('card',H/FILE);card=importlib.util.module_from_spec(spec);spec.loader.exec_module(card)
V=range(8)
def build(T,t,u):
 data,info=card.build(T,1,1);facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(a for a in V if a not in facts[x][1:]) for x in range(8,64)};P={};n=0
 for q in range(2):
  for x in A:
   for a in A[x]:n+=1;P[q,x,a]=n
 if n!=560 or (t,u) not in set(itertools.combinations(A[8],2)):raise ValueError('invalid unordered singleton pair')
 added=[(P[0,8,t],),(P[1,8,u],)];L=data.decode('ascii').splitlines()
 if len(L)-1!=info['clauses']:raise ValueError('base clauses')
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+2)+'\n'.join(L[1:])+'\n'+''.join(' '.join(map(str,C))+' 0\n' for C in added)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+2,'base_card11_sha256':info['formula_sha256'],
             'chosen_axes':[t,u],'all_unordered_axes':[list(x) for x in itertools.combinations(A[8],2)],
             'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--u',type=int,required=True);p.add_argument('--cnf',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
 T=card.match.prod.base.pair(a.pair,a.pair_sha);data,info=build(T,a.t,a.u)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'cardinality_encoder_sha256':PIN,'pair_sha256':a.pair_sha,'elapsed_seconds':time.monotonic()-start,
              'limits':'Ten unordered axes cover singleton/singleton after Q/R swap; each case needs independent proof and review.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
