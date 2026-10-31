#!/usr/bin/env python3
"""q3 necessary support/product CNF plus >=8 mixed cells per nonclassical member.

The >=8 premise is a separately review-pending written theorem, not an
unconditional computational axiom. Sequential counters only underapproximate
cardinality: existence of an assignment with >=8 mixed cells extends to them.
"""
import argparse,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q3-cross-product-cnf-v1.py';PIN='303215b3208352e1c7e025ce36bcfd656b308d83b2441853fc633f87ceb4f1c0'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('product encoder pin')
spec=importlib.util.spec_from_file_location('q3prod',H/FILE);prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)

def build(L):
 data,info=prod.build(L);_,baseinfo=prod.base.build(L)
 if baseinfo['variables']!=14112 or info['variables']!=27216:raise ValueError('base variable layout')
 # Base Q3 allocates the final 3*56*15 variables to per-cell support pairs.
 first=baseinfo['variables']-3*56*15+1
 if first!=11593:raise ValueError('pair auxiliary start')
 N={(q,x,j):first+q*56*15+(x-8)*15+j for q in range(3) for x in range(8,64) for j in range(15)}
 n=info['variables'];added=[]
 def var():
  nonlocal n
  n+=1;return n
 for q in range(3):
  Hq={x:var() for x in range(8,64)}
  for x in range(8,64):added.append(tuple([-Hq[x]]+[N[q,x,j] for j in range(15)]))
  S={}
  for i in range(1,57):
   x=7+i
   for j in range(1,min(i,8)+1):
    z=var();S[i,j]=z;previous=S.get((i-1,j));lower=True if j==1 else S.get((i-1,j-1))
    # z implies (previous OR H_i) AND (previous OR lower).
    added.append(tuple([-z]+([previous] if previous is not None else [])+[Hq[x]]))
    if lower is not True:added.append(tuple([-z]+([previous] if previous is not None else [])+([lower] if lower is not None else [])))
  added.append((S[56,8],))
 lines=data.decode('ascii').splitlines()
 if len(lines)-1!=info['clauses']:raise ValueError('base clauses')
 out=('p cnf %d %d\n'%(n,info['clauses']+len(added))+'\n'.join(lines[1:])+'\n'+''.join(' '.join(map(str,z))+' 0\n' for z in added)).encode('ascii')
 return out,{'variables':n,'clauses':info['clauses']+len(added),'base_product_formula_sha256':info['formula_sha256'],
             'mixed_lower_bound_per_member':8,'added_budget_clauses':len(added),'formula_bytes':len(out),
             'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
 data,info=build(prod.base.net.latin())
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'product_encoder_sha256':PIN,'written_mixed8_premise_sha256':'9f3882c9e5b8add15ccc097f3567ab89d4c150cf728e09e9860546a4dc008ad6',
              'elapsed_seconds':time.monotonic()-start,
              'limits':'Conditional on unreviewed mixed8 written premise; SAT not physical, UNSAT needs full independent audit and replay.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
