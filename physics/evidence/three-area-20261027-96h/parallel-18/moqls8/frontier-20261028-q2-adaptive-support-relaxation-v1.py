#!/usr/bin/env python3
"""Adaptive arbitrary-complex q2 support relaxation with necessary product cuts."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-q2-two-classical-support-relaxation-v1.py';PIN='8909e9b86c4c078de497dc408a82787236e32b765ccf64d99fcad6f677aeef9d'
if hashlib.sha256((H/SRC).read_bytes()).hexdigest()!=PIN:raise ValueError('source pin')
spec=importlib.util.spec_from_file_location('q2',H/SRC);q2=importlib.util.module_from_spec(spec);spec.loader.exec_module(q2)
V=range(8)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic();limit=12.0
 T=q2.actual_net();facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 if any(len(S)!=5 for S in A.values()):raise ValueError('allowed')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(4) for v in V}
 if any(len(L)!=8 for L in lines.values()):raise ValueError('net lines')
 s=z3.Solver();P={(q,x,t):z3.Bool(f'q{q}_{x}_{t}') for q in range(2) for x in A for t in A[x]}
 for q in range(2):
  for x in A:s.add(z3.Or([P[q,x,t] for t in A[x]]))
  s.add(z3.Or([z3.And(P[q,x,t],P[q,x,u]) for x in A for t,u in itertools.combinations(A[x],2)]))
  for L in lines.values():
   for t in V:
    if t in L:continue
    v=[P[q,x,t] for x in L if x>=8 and t in A[x]]
    if len(v)!=5:raise ValueError('line coverage')
    s.add(z3.Or(v))
 for x in A:
  for t in A[x]:s.add(z3.Not(z3.And(P[0,x,t],P[1,x,t])))
 E=set()
 for L in lines.values():E.update(itertools.combinations((x for x in L if x>=8),2))
 for q in range(2):
  for x,y in E:
   C=set(A[x])&set(A[y])
   for t in C:s.add(z3.Implies(z3.And(P[q,x,t],P[q,y,t]),z3.Or([z3.And(P[q,x,u],P[q,y,u]) for u in C if u!=t])))
 def singleton(q,x,y):
  C=set(A[x])&set(A[y]);both=[z3.And(P[q,x,t],P[q,y,t]) for t in C]
  return z3.PbEq([(z,1) for z in both],1) if both else z3.BoolVal(False)
 cuts=[];phase_cuts=[];seen=set();result='UNKNOWN';answer=None;rounds=0
 while time.monotonic()-start<limit and rounds<500:
  s.set(timeout=max(1,int(1000*(limit-(time.monotonic()-start)))));res=s.check();rounds+=1
  if res==z3.unsat:result='UNCERTIFIED_Z3_UNSAT';break
  if res==z3.unknown:result='UNKNOWN_'+s.reason_unknown();break
  M=s.model();S=[{x:{t for t in A[x] if z3.is_true(M.eval(P[q,x,t],model_completion=True))} for x in A} for q in range(2)]
  if any(not S[q][x] for q in range(2) for x in A) or any(S[0][x]&S[1][x] for x in A):raise ValueError('support model')
  if any(not any(len(S[q][x])>1 for x in A) for q in range(2)):raise ValueError('nonclassical')
  if any(len(S[q][x]&S[q][y])==1 for q in range(2) for x,y in E):raise ValueError('net overlap')
  for q in range(2):
   for L in lines.values():
    for t in V:
     if t not in L and not any(t in S[q][x] for x in L if x>=8):raise ValueError('coverage')
  bad=[(x,y) for x,y in itertools.combinations(A,2) if (x,y) not in E and len(S[0][x]&S[0][y])==1 and len(S[1][x]&S[1][y])==1]
  if bad:
   for x,y in bad:
    if (x,y) in seen:raise ValueError('repeated violated product cut')
    s.add(z3.Not(z3.And(singleton(0,x,y),singleton(1,x,y))));seen.add((x,y));cuts.append([x,y])
   continue
  found=None
  for q in range(2):
   cycle=q2.phase.find_cycle(S[q],E)
   if cycle is not None:found=(q,cycle);break
  if found is not None:
   q,cy=found;axes=set(cy['axes']);cells=cy['cells'];parts=[]
   for x,y in zip(cells,cells[1:]+cells[:1]):
    common=set(A[x])&set(A[y]);g=[P[q,x,t] for t in axes]+[P[q,y,t] for t in axes]
    g.extend(z3.Not(z3.And(P[q,x,t],P[q,y,t])) for t in common-axes);parts.append(z3.And(g))
   s.add(z3.Not(z3.And(parts)));phase_cuts.append({'member':q,**cy});continue
  answer=S;result='SAT_SUPPORT_ONLY_NO_CHECKED_PRODUCT_OR_ODD_CYCLE_OBSTRUCTION';break
 if result=='UNKNOWN' and rounds>=500:result='UNKNOWN_ROUND_LIMIT'
 out={'result':result,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'import_sha256':PIN,'net_source_sha256':q2.PIN,'z3_version':z3.get_version_string(),
      'time_limit_seconds':limit,'rounds':rounds,'product_cuts_count':len(cuts),'product_cuts':cuts,
      'phase_cuts_count':len(phase_cuts),'phase_cuts':phase_cuts,
      'support_histograms':[dict(collections.Counter(len(z) for z in S.values())) for S in answer] if answer else None,
      'support_models':[{str(x):sorted(z) for x,z in S.items()} for S in answer] if answer else None,
      'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'limits':'SAT is necessary-support relaxation, not an actual physical QLS/family. UNSAT is uncertified. No magnitude or phase assignments.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('support_models','product_cuts','phase_cuts')},indent=2))
if __name__=='__main__':main()
