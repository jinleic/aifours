#!/usr/bin/env python3
"""Bounded, explicitly unproved SAT-relaxation screening of mixed uniform supports."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
IMPORT='frontier-20261028-anchor-sparse-net-obstructions-v1.py';PIN='6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'
b=(H/IMPORT).read_bytes()
if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('module hash')
spec=importlib.util.spec_from_file_location('anchor_obstruction',H/IMPORT);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
V=range(8)
def mul(a,b):
 out=0
 for _ in V[:3]:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out

def solve(T,mode,limit=1000):
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:sorted(set(V)-set(facts[x][1:])) for x in range(8,64)}
 if any(len(z)!=4 for z in A.values()):raise ValueError('allowed')
 dom={x:[z for k in range(1,5) for z in itertools.combinations(A[x],k)] for x in A}
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in V}
 if any(len(x)!=8 for x in lines.values()):raise ValueError('line')
 s=z3.Solver();s.set(timeout=limit);Q={x:[z3.Bool(f'a_{x}_{k}') for k in range(15)] for x in A}
 P={}
 for x in A:
  s.add(z3.PbEq([(q,1) for q in Q[x]],1))
  for t in A[x]:P[x,t]=z3.Or([Q[x][i] for i,z in enumerate(dom[x]) if t in z])
 for line in lines.values():
  for t in V:
   target=12-sum(12 for x in line if x<8 and x==t)
   z=[(Q[x][i],12//len(D)) for x in line if x>=8 for i,D in enumerate(dom[x]) if t in D]
   if z:s.add(z3.PbEq(z,target))
   elif target:raise ValueError('coordinate uncovered')
 edges=set()
 for line in lines.values():edges.update(itertools.combinations((x for x in line if x>=8),2))
 for x,y in edges:
  C=set(A[x])&set(A[y])
  for t in C:s.add(z3.Implies(z3.And(P[x,t],P[y,t]),z3.Or([z3.And(P[x,u],P[y,u]) for u in C if u!=t])))
 if mode=='nonclassical':s.add(z3.Or([Q[x][i] for x in A for i,D in enumerate(dom[x]) if len(D)>1]))
 else:
  # Exact affine extension Q(i,j)=j+4i; negative control duplicates one cell.
  for x in A:
   i,j=divmod(x,8);v=j^mul(4,i)
   if mode=='control_bad' and x==9:v=mul(4,1)
   if (v,) not in dom[x]:
    if mode=='control_bad':s.add(z3.BoolVal(False));continue
    raise ValueError('control symbol not allowed')
   s.add(Q[x][dom[x].index((v,))])
 result=s.check();supports=None;err=None
 if result==z3.sat:
  model=s.model();supports={x:set(next(D for i,D in enumerate(dom[x]) if z3.is_true(model.eval(Q[x][i],model_completion=True)))) for x in A}
  supports.update({j:{j} for j in V})
  badline=sum(sum(12//len(supports[x]) for x in line if t in supports[x])!=12 for line in lines.values() for t in V)
  badpair=sum(len(supports[x]&supports[y])==1 for x,y in edges)
  nonclass=sum(len(supports[x])>1 for x in A)
  if badline or badpair or (mode=='nonclassical' and not nonclass):raise ValueError('invalid solver model')
  err={'weight_errors':badline,'overlap1_errors':badpair,'nonclassical_cells':nonclass}
 return {'solver_status':str(result),'reason_unknown':s.reason_unknown() if result==z3.unknown else None,
         'model_support_size_histogram':dict(collections.Counter(len(supports[x]) for x in A)) if supports else None,
         'model_integer_checks':err,'model_supports':{str(x):sorted(supports[x]) for x in sorted(supports)} if supports and mode=='nonclassical' else None}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 triples=sum((mod.read_catalogue(*q) for q in mod.P),[])
 if len(triples)!=39:raise ValueError('catalogue size')
 affine=[[[j^mul(s,i) for j in V] for i in V] for s in (1,2,3)]
 positive=solve(affine,'control_good');negative=solve(affine,'control_bad')
 if positive['solver_status']!='sat' or negative['solver_status']!='unsat':raise ValueError('control outcomes')
 cases=[(1,0,0),(4,2,2),(6,2,0),(20,3,0),(22,0,0),(38,0,0),(38,1,0)]
 out=[]
 for sp,r,anchor in cases:
  if time.monotonic()-start>15:break
  c=next(x for x in range(5) if x!=r)
  out.append({'species':sp,'row_class':r,'column_class':c,'anchor':anchor,**solve(mod.orient(triples[sp],r,c,anchor),'nonclassical')})
 result={'result':'BOUNDED_SUPPORT_RELAXATION_NO_INDEPENDENT_UNSAT_CERTIFICATES',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'import_sha256':PIN,
         'z3_version':z3.get_version_string(),'timeout_per_case_ms':1000,'case_limit_seconds':15,
         'positive_affine_classical_control':positive,'duplicate_affine_negative_control':negative,
         'cases_requested':len(cases),'cases_completed':len(out),'cases':out,
         'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'limits':'Support/diagonal-weight relaxation only. No solver UNSAT output is certified; SAT models need full physical Gram checks.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2));print('case_statuses',[(x['species'],x['row_class'],x['anchor'],x['solver_status']) for x in out])
if __name__=='__main__':main()
