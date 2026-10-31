#!/usr/bin/env python3
"""Bounded arbitrary-complex q2 support relaxation on one explicit 4-net.

SAT is only a support pattern; UNSAT is uncertified; no quantum witness is
claimed. Full pair-product necessary singleton-overlap constraints retained.
"""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-first-pair-v1.txt';PIN='710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd'
PHASE='frontier-20261028-mixed-support-phase-refinement-v1.py';PHASEPIN='c6476401ae60b2bd80f61d65503844753284ccf3dcec804e6714c75d34b919fa'
if hashlib.sha256((H/PHASE).read_bytes()).hexdigest()!=PHASEPIN:raise ValueError('phase module hash')
spec=importlib.util.spec_from_file_location('phase',H/PHASE);phase=importlib.util.module_from_spec(spec);spec.loader.exec_module(phase)
V=range(8)

def actual_net():
 b=(H/SRC).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source hash')
 L=[z.strip() for z in b.decode('ascii').splitlines() if z.strip()]
 if L[0].split()[:3]!=['8','8','4254'] or len(L)!=17:raise ValueError('first pair extraction')
 S=[[[ord(c)-97 for c in L[1+8*k+i]] for i in V] for k in range(2)]
 for M in S:
  if any(set(r)!=set(V) for r in M) or any({M[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
 if len({(S[0][i][j],S[1][i][j]) for i in V for j in V})!=64:raise ValueError('not MOLS')
 return [[[S[k][0].index(S[k][i][j]) for j in V] for i in V] for k in range(2)]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 T=actual_net();facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 if any(len(a)!=5 for a in A.values()):raise ValueError('three forbidden axes')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(4) for v in V}
 if any(len(line)!=8 for line in lines.values()):raise ValueError('net lines')
 s=z3.Solver();P={(q,x,t):z3.Bool(f'p_{q}_{x}_{t}') for q in range(2) for x in A for t in A[x]}
 for q in range(2):
  for x in A:s.add(z3.Or([P[q,x,t] for t in A[x]]))
  s.add(z3.Or([z3.And(P[q,x,t],P[q,x,u]) for x in A for t,u in itertools.combinations(A[x],2)]))
  for line in lines.values():
   for t in V:
    if t in line:continue
    cells=[x for x in line if x>=8 and t in A[x]]
    if len(cells)!=5:raise ValueError('line-axis coverage')
    s.add(z3.Or([P[q,x,t] for x in cells]))
 for x in A:
  for t in A[x]:s.add(z3.Not(z3.And(P[0,x,t],P[1,x,t])))
 edges=set()
 for line in lines.values():edges.update(itertools.combinations((x for x in line if x>=8),2))
 for q in range(2):
  for x,y in edges:
   C=set(A[x])&set(A[y])
   for t in C:s.add(z3.Implies(z3.And(P[q,x,t],P[q,y,t]),z3.Or([z3.And(P[q,x,u],P[q,y,u]) for u in C if u!=t])))
 # If both member inner products have exactly one supported term, their product is nonzero.
 def one(q,x,y):
  C=set(A[x])&set(A[y]);disj=[]
  for t in C:
   disj.append(z3.And(P[q,x,t],P[q,y,t],*[z3.Not(z3.And(P[q,x,u],P[q,y,u])) for u in C if u!=t]))
  return z3.Or(disj)
 for x,y in itertools.combinations(A,2):
  if (x,y) not in edges:s.add(z3.Not(z3.And(one(0,x,y),one(1,x,y))))
 cuts=[];answer=None;result='UNKNOWN';limit=6.0
 while time.monotonic()-start<limit and len(cuts)<400:
  s.set(timeout=max(1,int(1000*(limit-(time.monotonic()-start)))));status=s.check()
  if status==z3.unsat:result='UNCERTIFIED_Z3_UNSAT';break
  if status==z3.unknown:result='UNKNOWN_'+s.reason_unknown();break
  M=s.model();S=[{x:{t for t in A[x] if z3.is_true(M.eval(P[q,x,t],model_completion=True))} for x in A} for q in range(2)]
  if any(not S[q][x] for q in range(2) for x in A) or any(S[0][x]&S[1][x] for x in A):raise ValueError('support assignment')
  if any(not any(len(S[q][x])>1 for x in A) for q in range(2)):raise ValueError('nonclassical condition')
  if any(len(S[q][x]&S[q][y])==1 for q in range(2) for x,y in edges):raise ValueError('same-line singleton')
  if any(len(S[0][x]&S[0][y])==1 and len(S[1][x]&S[1][y])==1 for x,y in itertools.combinations(A,2)):raise ValueError('product singleton')
  for q in range(2):
   for line in lines.values():
    for t in V:
     if t not in line and not any(t in S[q][x] for x in line if x>=8):raise ValueError('axis uncovered')
  found=None
  for q in range(2):
   cy=phase.find_cycle(S[q],edges)
   if cy is not None:found=(q,cy);break
  if found is None:answer=S;result='SAT_SUPPORT_ONLY_NO_ODD_2_AXIS_CYCLE';break
  q,cy=found;axes=set(cy['axes']);cells=cy['cells'];expr=[]
  for x,y in zip(cells,cells[1:]+cells[:1]):
   common=set(A[x])&set(A[y]);b=[P[q,x,t] for t in axes]+[P[q,y,t] for t in axes]
   b.extend(z3.Not(z3.And(P[q,x,t],P[q,y,t])) for t in common-axes);expr.append(z3.And(b))
  s.add(z3.Not(z3.And(expr)));cuts.append({'member':q,**cy})
 if result=='UNKNOWN' and len(cuts)>=400:result='UNKNOWN_CUT_LIMIT'
 out={'result':result,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'net_source_sha256':PIN,'phase_module_sha256':PHASEPIN,'z3_version':z3.get_version_string(),
      'source':'first two squares of maximal-2-MOLS order-8 catalogue; not entire classification',
      'time_limit_seconds':limit,'cuts':cuts,'cut_count':len(cuts),
      'model_support_histograms':[dict(collections.Counter(len(z) for z in S.values())) for S in answer] if answer else None,
      'support_models':[{str(x):sorted(z) for x,z in S.items()} for S in answer] if answer else None,
      'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'limits':'SAT is support-only and not a physical MOQLS witness; UNSAT requires independent proof. No magnitude or phase solution is claimed.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('support_models','cuts')},indent=2))
if __name__=='__main__':main()
