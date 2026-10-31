#!/usr/bin/env python3
"""Independent full q2 matching + exact-cell-cardinality CNF audit."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-matching-symmetry-cnf-check-v1.py';PIN='c1a72b1338a3f83c7e2e59094deb6ff28ea6564f81eb64d21a1e6c40321dc6eb'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('matching auditor pin')
spec=importlib.util.spec_from_file_location('sym_audit',H/FILE);sym=importlib.util.module_from_spec(spec);spec.loader.exec_module(sym)
CASES={(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)}
def expected(pair,pin,a,b):
 if (a,b) not in CASES:raise ValueError('sizes')
 n,C,_,_,truth=sym.expected(pair,pin);f=sym.prod.audit.facts(pair,pin)
 A={x:tuple(t for t in range(8) if t not in f[x][1:]) for x in range(8,64)};P={};v=0
 for q in range(2):
  for x in sorted(A):
   for t in A[x]:v+=1;P[q,x,t]=v
 if v!=560:raise ValueError('support IDs')
 x=8
 # sym.expected includes 10 min-order clauses: remove them because cardinality
 # ordering is the sole symmetry convention in this split.
 for t,u in itertools.product(A[x],repeat=2):
  if t>u:
   clause=tuple(sorted([-P[0,x,t],-P[1,x,u]]+[P[0,x,z] for z in A[x] if z<t]+[P[1,x,z] for z in A[x] if z<u]))
   if C[clause]<1:raise ValueError('missing symmetry clause')
   C[clause]-=1
   if C[clause]==0:del C[clause]
 add=[]
 for q,k in ((0,a),(1,b)):
  z=[P[q,x,t] for t in A[x]]
  local=[tuple(U) for U in itertools.combinations(z,6-k)]+[tuple(-v for v in U) for U in itertools.combinations(z,k+1)]
  for bits in itertools.product((False,True),repeat=5):
   values=dict(zip(z,bits));ok=all(any(values[abs(l)] if l>0 else not values[abs(l)] for l in clause) for clause in local)
   if ok!=(sum(bits)==k):raise ValueError('cardinality comparator')
  add.extend(tuple(sorted(z)) for z in local)
 # Prove coverage of all unordered nonempty disjoint support-size pairs.
 covered=set()
 for word in itertools.product((0,1,2),repeat=5):
  x0=word.count(1);y0=word.count(2)
  if x0 and y0:covered.add(tuple(sorted((x0,y0))))
 if covered!=CASES:raise ValueError('split coverage')
 return n,C+collections.Counter(add),len(add),sorted(covered),truth

def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 raw=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=a.cnf_sha:raise ValueError('CNF pin')
 n,C,k,cases,truth=expected(a.pair,a.pair_sha,a.a,a.b);nv,D=sym.prod.audit.parse(raw)
 if n!=nv or C!=D:raise ValueError('formula mismatch')
 key=next(iter(D));bad=D.copy();bad[key]-=1
 if not bad[key]:del bad[key]
 if bad==C:raise ValueError('omission mutation')
 out={'result':'PASS_INDEPENDENT_CARDINALITY_CNF_AND_COVERAGE','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'matching_auditor_sha256':PIN,'pair_sha256':a.pair_sha,'formula_sha256':a.cnf_sha,'variables':n,'clauses':sum(C.values()),
      'support_sizes':[a.a,a.b],'cardinality_clauses':k,'all_unordered_disjoint_size_pairs':cases,
      'base_symmetry_truth_assignments_checked':truth,'omitted_clause_mutation':'rejected','elapsed_seconds':time.monotonic()-start,
      'limits':'Encoding/case-coverage only; physical matching, member exchange and proof validity need review.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
