#!/usr/bin/env python3
"""Independent full multiset audit of q2 CNF plus cross-product singleton clauses."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-support-cnf-check-v3.py';PIN='c95730409fec6bb10488fcfc22f96dbe19ce42fd73ca0e6c1ab4e2a12204249c'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('auditor pin')
s=importlib.util.spec_from_file_location('q2audit',H/FILE);audit=importlib.util.module_from_spec(s);s.loader.exec_module(audit)
V=range(8)
def expected(pair,pin):
 f=audit.facts(pair,pin);n,base,tri=audit.expected(f)
 A={x:tuple(t for t in V if t not in f[x][1:]) for x in range(8,64)}
 P={};idx=0
 for q in range(2):
  for x in sorted(A):
   for t in A[x]:idx+=1;P[q,x,t]=idx
 if idx!=560:raise ValueError('support numbering')
 def adj(x,y):return any(a==b for a,b in zip(f[x],f[y]))
 extra=[];npairs=0
 def add(*C):extra.append(tuple(sorted(C)))
 for x,y in itertools.combinations(range(8,64),2):
  if adj(x,y):continue
  npairs+=1;C=sorted(set(A[x])&set(A[y]));B={}
  for q in range(2):
   for t in C:n+=1;B[q,t]=n
   for t in C:
    b=B[q,t];add(-b,P[q,x,t]);add(-b,P[q,y,t]);add(b,-P[q,x,t],-P[q,y,t])
  for t in C:
   for u in C:add(-B[0,t],*(B[0,v] for v in C if v!=t),-B[1,u],*(B[1,w] for w in C if w!=u))
 if npairs!=840:raise ValueError('nonadjacent count')
 return n,base+collections.Counter(extra),len(extra),tri,npairs

def main():
 p=argparse.ArgumentParser();p.add_argument('--pair',required=True);p.add_argument('--pair-sha',required=True);p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(b).hexdigest()!=a.cnf_sha:raise ValueError('formula hash')
 n,C,k,tri,np=expected(a.pair,a.pair_sha);m,D=audit.parse(b)
 if n!=m or C!=D:raise ValueError('independent formula mismatch')
 key=next(iter(D));bad=D.copy();bad[key]-=1
 if bad[key]==0:del bad[key]
 if bad==C:raise ValueError('omission control')
 out={'result':'PASS_INDEPENDENT_FULL_Q2_PRODUCT_CNF',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'base_auditor_sha256':PIN,'pair_sha256':a.pair_sha,'formula_sha256':a.cnf_sha,
      'variables':n,'clauses':sum(C.values()),'triangle_axes':tri,'nonadjacent_pairs':np,'cross_product_clauses':k,
      'omitted_clause_mutation':'rejected','elapsed_seconds':time.monotonic()-start,
      'limits':'Independent encoding audit; physical reduction, proof validity and classification separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
