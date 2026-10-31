#!/usr/bin/env python3
"""Independent full CNF and unordered singleton-pair coverage audit."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-cell-cardinality-cnf-check-v1.py';PIN='c57acc43bf2366fa66e7088b302b643b21d1e2e0ba3d0201c94b4a6390e4fa85'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('cardinality auditor pin')
spec=importlib.util.spec_from_file_location('card_audit',H/FILE);card=importlib.util.module_from_spec(spec);spec.loader.exec_module(card)
V=range(8)
def expected(pair,pin,t,u):
 n,C,_,_,_=card.expected(pair,pin,1,1);f=card.sym.prod.audit.facts(pair,pin)
 A={x:tuple(k for k in V if k not in f[x][1:]) for x in range(8,64)};P={};v=0
 for q in range(2):
  for x in sorted(A):
   for k in A[x]:v+=1;P[q,x,k]=v
 pairs=list(itertools.combinations(A[8],2))
 if v!=560 or (t,u) not in pairs:raise ValueError('invalid singleton axes')
 # Every ordered pair of distinct singletons maps by Q/R swap to one pair.
 ordered=[(x,y) for x in A[8] for y in A[8] if x!=y]
 if len(ordered)!=20 or {tuple(sorted(p)) for p in ordered}!=set(pairs) or len(pairs)!=10:raise ValueError('pair coverage')
 C[(P[0,8,t],)]+=1;C[(P[1,8,u],)]+=1
 return n,C,pairs

def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--u',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(b).hexdigest()!=a.cnf_sha:raise ValueError('formula pin')
 n,C,pairs=expected(a.pair,a.pair_sha,a.t,a.u);m,D=card.sym.prod.audit.parse(b)
 if n!=m or C!=D:raise ValueError('CNF mismatch')
 key=next(iter(D));bad=D.copy();bad[key]-=1
 if not bad[key]:del bad[key]
 if bad==C:raise ValueError('mutation')
 out={'result':'PASS_INDEPENDENT_SINGLETON_PAIR_CNF','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'base_auditor_sha256':PIN,'pair_sha256':a.pair_sha,'formula_sha256':a.cnf_sha,'axes':[a.t,a.u],
      'all_unordered_pairs':[list(z) for z in pairs],'ordered_disjoint_singletons_checked':20,
      'variables':n,'clauses':sum(C.values()),'omitted_clause_mutation':'rejected','elapsed_seconds':time.monotonic()-start,
      'limits':'Case coverage and encoding only; swap justification, physical reduction and proof require review.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
