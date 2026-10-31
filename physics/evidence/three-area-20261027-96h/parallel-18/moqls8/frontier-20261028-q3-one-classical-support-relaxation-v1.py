#!/usr/bin/env python3
"""Bounded support/phase relaxation for three quantum and one classical QLS.

The selected classical Latin square is explicit. SAT is not a physical
witness; UNSAT is uncertified, and timeouts are UNKNOWN.
"""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-first-pair-v1.txt';PIN='710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd'
PHASE='frontier-20261028-mixed-support-phase-refinement-v1.py';PP='c6476401ae60b2bd80f61d65503844753284ccf3dcec804e6714c75d34b919fa'
if hashlib.sha256((H/PHASE).read_bytes()).hexdigest()!=PP:raise ValueError('phase module pin')
spec=importlib.util.spec_from_file_location('phaseq3',H/PHASE);phase=importlib.util.module_from_spec(spec);spec.loader.exec_module(phase)
V=range(8)
def latin():
 b=(H/SRC).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source pin')
 z=[x.strip() for x in b.decode('ascii').splitlines() if x.strip()]
 if len(z)!=17 or z[0].split()[:2]!=['8','8']:raise ValueError('source layout')
 S=[[ord(c)-97 for c in z[1+i]] for i in V]
 if any(set(row)!=set(V) for row in S) or any({S[i][j] for i in V}!=set(V) for j in V):raise ValueError('not Latin')
 return [[S[0].index(S[i][j]) for j in V] for i in V]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic();limit=12.0
 L=latin();facts={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 if any(len(z)!=6 for z in A.values()):raise ValueError('allowed')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(3) for v in V}
 if any(len(L)!=8 for L in lines.values()):raise ValueError('net')
 s=z3.Solver();P={(q,x,t):z3.Bool(f'q{q}_{x}_{t}') for q in range(3) for x in A for t in A[x]}
 for q in range(3):
  for x in A:s.add(z3.Or([P[q,x,t] for t in A[x]]))
  s.add(z3.Or([z3.And(P[q,x,t],P[q,x,u]) for x in A for t,u in itertools.combinations(A[x],2)]))
  for line in lines.values():
   for t in V:
    if t in line:continue
    cand=[P[q,x,t] for x in line if x>=8 and t in A[x]]
    if len(cand)!=6:raise ValueError('coverage')
    s.add(z3.Or(cand))
 for x in A:
  for t in A[x]:s.add(z3.AtMost(*(P[q,x,t] for q in range(3)),1))
 E=set()
 for line in lines.values():E.update(itertools.combinations((x for x in line if x>=8),2))
 for q in range(3):
  for x,y in E:
   C=set(A[x])&set(A[y])
   for t in C:s.add(z3.Implies(z3.And(P[q,x,t],P[q,y,t]),z3.Or([z3.And(P[q,x,u],P[q,y,u]) for u in C if u!=t])))
 def one(q,x,y):
  C=set(A[x])&set(A[y]);both=[z3.And(P[q,x,t],P[q,y,t]) for t in C]
  return z3.PbEq([(b,1) for b in both],1) if both else z3.BoolVal(False)
 product_cuts=[];phase_cuts=[];seen=set();result='UNKNOWN';answer=None;rounds=0
 while time.monotonic()-start<limit and rounds<500:
  s.set(timeout=max(1,int(1000*(limit-(time.monotonic()-start)))));res=s.check();rounds+=1
  if res==z3.unsat:result='UNCERTIFIED_Z3_UNSAT';break
  if res==z3.unknown:result='UNKNOWN_'+s.reason_unknown();break
  M=s.model();S=[{x:{t for t in A[x] if z3.is_true(M.eval(P[q,x,t],model_completion=True))} for x in A} for q in range(3)]
  if any(not S[q][x] for q in range(3) for x in A) or any(S[p][x]&S[q][x] for p,q in itertools.combinations(range(3),2) for x in A):raise ValueError('support/disjointness')
  if any(not any(len(S[q][x])>1 for x in A) for q in range(3)):raise ValueError('nonclassical condition')
  if any(len(S[q][x]&S[q][y])==1 for q in range(3) for x,y in E):raise ValueError('line overlap')
  for q in range(3):
   for line in lines.values():
    for t in V:
     if t not in line and not any(t in S[q][x] for x in line if x>=8):raise ValueError('axis uncovered')
  bad=[(p,q,x,y) for p,q in itertools.combinations(range(3),2) for x,y in itertools.combinations(A,2) if (x,y) not in E and len(S[p][x]&S[p][y])==1 and len(S[q][x]&S[q][y])==1]
  if bad:
   for p,q,x,y in bad:
    key=(p,q,x,y)
    if key in seen:raise ValueError('repeated product violation')
    seen.add(key);s.add(z3.Not(z3.And(one(p,x,y),one(q,x,y))));product_cuts.append(list(key))
   continue
  found=None
  for q in range(3):
   cy=phase.find_cycle(S[q],E)
   if cy is not None:found=(q,cy);break
  if found:
   q,cy=found;axes=set(cy['axes']);cells=cy['cells'];terms=[]
   for x,y in zip(cells,cells[1:]+cells[:1]):
    C=set(A[x])&set(A[y]);z=[P[q,x,t] for t in axes]+[P[q,y,t] for t in axes]
    z.extend(z3.Not(z3.And(P[q,x,t],P[q,y,t])) for t in C-axes);terms.append(z3.And(z))
   s.add(z3.Not(z3.And(terms)));phase_cuts.append({'member':q,**cy});continue
  answer=S;result='SAT_SUPPORT_ONLY_NO_CHECKED_PRODUCT_OR_ODD_CYCLE_OBSTRUCTION';break
 if result=='UNKNOWN' and rounds>=500:result='UNKNOWN_ROUND_LIMIT'
 out={'result':result,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'classical_square_source_sha256':PIN,'phase_module_sha256':PP,'z3_version':z3.get_version_string(),
      'scope':'one fixed classical QLS and 3 nonclassical QLS, arbitrary complex supports',
      'time_limit_seconds':limit,'rounds':rounds,'product_cuts_count':len(product_cuts),'phase_cuts_count':len(phase_cuts),
      'product_cuts':product_cuts,'phase_cuts':phase_cuts,
      'support_histograms':[dict(collections.Counter(len(z) for z in q.values())) for q in answer] if answer else None,
      'support_models':[{str(x):sorted(z) for x,z in q.items()} for q in answer] if answer else None,
      'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'limits':'SAT is support-only, not a physical family; UNSAT unverified; timeout UNKNOWN. Phases/magnitudes and all Gram equations remain unchecked.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('support_models','product_cuts','phase_cuts')},indent=2))
if __name__=='__main__':main()
