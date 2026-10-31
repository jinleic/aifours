#!/usr/bin/env python3
"""Independent audit of q2 product CNF, ONB perfect-matchings and member swap."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-cross-product-cnf-check-v1.py';PIN='d67566048cffeec09dded934ea250078d965e45a60baae357cb129b59bc065fb'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('base auditor pin')
spec=importlib.util.spec_from_file_location('prod_audit',H/FILE);prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
V=range(8)
def expected(pair,pin):
 n,C,extra,tri,np=prod.expected(pair,pin);f=prod.audit.facts(pair,pin)
 A={x:tuple(t for t in V if t not in f[x][1:]) for x in range(8,64)}
 P={};i=0
 for q in range(2):
  for x in sorted(A):
   for t in A[x]:i+=1;P[q,x,t]=i
 if i!=560:raise ValueError('support mapping')
 D=[];mcount=0
 def new():
  nonlocal n,mcount
  n+=1;mcount+=1;return n
 def add(*z):D.append(tuple(sorted(z)))
 for q in range(2):
  for k in range(4):
   for sym in V:
    if k==0 and sym==0:continue
    X=[x for x in range(8,64) if f[x][k]==sym]
    if len(X)!=(8 if k==0 else 7):raise ValueError('line size')
    B={(x,t):new() for x in X for t in A[x]}
    for x in X:
     opts=[B[x,t] for t in A[x]];add(*opts)
     for t in A[x]:add(-B[x,t],P[q,x,t])
     for u,v in itertools.combinations(opts,2):add(-u,-v)
    for t in V:
     opts=[B[x,t] for x in X if t in A[x]]
     for u,v in itertools.combinations(opts,2):add(-u,-v)
 # Independently enumerate all nonempty disjoint support-pairs at x=8.
 x=8;sym=[]
 for t,u in itertools.product(A[x],repeat=2):
  if t>u:sym.append(tuple(sorted([-P[0,x,t],-P[1,x,u]]+[P[0,x,v] for v in A[x] if v<t]+[P[1,x,w] for w in A[x] if w<u])))
 if len(sym)!=10:raise ValueError('symmetry count')
 checked=0
 for choice in itertools.product((0,1,2),repeat=5):
  Q={A[x][j] for j,v in enumerate(choice) if v==1};R={A[x][j] for j,v in enumerate(choice) if v==2}
  if not Q or not R:continue
  values={P[0,x,t]:(t in Q) for t in A[x]};values.update({P[1,x,t]:(t in R) for t in A[x]})
  ok=all(any(values[abs(l)] if l>0 else not values[abs(l)] for l in clause) for clause in sym)
  if ok!=(min(Q)<min(R)):raise ValueError('swap comparator unsound')
  checked+=1
 D.extend(sym)
 return n,C+collections.Counter(D),mcount,len(D)-len(sym),checked

def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(b).hexdigest()!=a.cnf_sha:raise ValueError('formula hash')
 n,C,matches,nclauses,checked=expected(a.pair,a.pair_sha);nv,D=prod.audit.parse(b)
 if n!=nv or C!=D:raise ValueError('clause mismatch')
 key=next(iter(D));mut=D.copy();mut[key]-=1
 if not mut[key]:del mut[key]
 if mut==C:raise ValueError('omission control')
 out={'result':'PASS_INDEPENDENT_MATCHING_SYMMETRY_CNF',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'base_auditor_sha256':PIN,'pair_sha256':a.pair_sha,'formula_sha256':a.cnf_sha,
      'variables':n,'clauses':sum(C.values()),'matching_variables':matches,'matching_clauses':nclauses,
      'symmetry_clauses':10,'all_disjoint_support_pairs_checked':checked,'omitted_clause_mutation':'rejected',
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Independent encoding audit and finite swap truth table; mathematical unitary-matching/swap proof and UNSAT certificate still separately reviewed.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
