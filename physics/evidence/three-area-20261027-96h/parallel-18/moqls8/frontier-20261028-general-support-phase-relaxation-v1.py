#!/usr/bin/env python3
"""General q1 support relaxation plus arbitrary-complex odd-cycle cuts; no amplitude assumption."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
MODULES=[('anchor_net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'),
         ('phase_refine','frontier-20261028-mixed-support-phase-refinement-v1.py','c6476401ae60b2bd80f61d65503844753284ccf3dcec804e6714c75d34b919fa')]
mods={}
for name,file,pin in MODULES:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('import hash')
 sp=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);mods[name]=m
net=mods['anchor_net'];phase=mods['phase_refine'];V=range(8)

def solve(T,case,secs):
 start=time.monotonic();facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:sorted(set(V)-set(facts[x][1:])) for x in range(8,64)}
 if any(len(a)!=4 for a in A.values()):raise ValueError('bad support allowance')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in V}
 if any(len(line)!=8 for line in lines.values()):raise ValueError('bad net')
 s=z3.Solver();P={(x,t):z3.Bool(f'p_{x}_{t}') for x in A for t in A[x]}
 for x in A:s.add(z3.Or([P[x,t] for t in A[x]]))
 for line in lines.values():
  for t in V:
   if t in line and t<8:continue
   candidates=[P[x,t] for x in line if x>=8 and t in A[x]]
   if not candidates:raise ValueError('axis missing')
   s.add(z3.Or(candidates))
 edges=set()
 for line in lines.values():edges.update(itertools.combinations((x for x in line if x>=8),2))
 for x,y in edges:
  C=set(A[x])&set(A[y])
  for t in C:s.add(z3.Implies(z3.And(P[x,t],P[y,t]),z3.Or([z3.And(P[x,u],P[y,u]) for u in C if u!=t])))
 s.add(z3.Or([z3.And(P[x,t],P[x,u]) for x in A for t,u in itertools.combinations(A[x],2)]))
 cuts=[];result='UNKNOWN';answer=None
 while time.monotonic()-start<secs and len(cuts)<500:
  s.set(timeout=max(1,int(1000*(secs-(time.monotonic()-start)))));status=s.check()
  if status==z3.unsat:result='UNCERTIFIED_Z3_UNSAT';break
  if status==z3.unknown:result='UNKNOWN_'+s.reason_unknown();break
  M=s.model();S={x:{t for t in A[x] if z3.is_true(M.eval(P[x,t],model_completion=True))} for x in A}
  if any(not S[x] for x in A) or not any(len(S[x])>1 for x in A):raise ValueError('empty/classical model')
  if any(len(S[x]&S[y])==1 for x,y in edges):raise ValueError('model overlap1')
  for line in lines.values():
   for t in V:
    if t in line and t<8:continue
    if not any(t in S[x] for x in line if x>=8):raise ValueError('coverage')
  cycle=phase.find_cycle(S,edges)
  if cycle is None:answer=S;result='SAT_SUPPORT_RELAXATION_NO_ODD_TWO_AXIS_CYCLE';break
  axes=set(cycle['axes']);cells=cycle['cells'];clauses=[]
  for x,y in zip(cells,cells[1:]+cells[:1]):
   if tuple(sorted((x,y))) not in edges or S[x]&S[y]!=axes:raise ValueError('bad cut')
   common=set(A[x])&set(A[y]);parts=[P[x,t] for t in axes]+[P[y,t] for t in axes]
   parts.extend(z3.Not(z3.And(P[x,t],P[y,t])) for t in common-axes)
   clauses.append(z3.And(parts))
  s.add(z3.Not(z3.And(clauses)));cuts.append(cycle)
 if result=='UNKNOWN' and len(cuts)>=500:result='UNKNOWN_CUT_LIMIT'
 return {'case':case,'result':result,'cut_count':len(cuts),'cuts':cuts,
         'support_histogram':dict(collections.Counter(len(v) for v in answer.values())) if answer else None,
         'support_model':{str(x):sorted(v) for x,v in answer.items()} if answer else None,
         'elapsed_seconds':time.monotonic()-start}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 triples=sum((net.read_catalogue(*p) for p in net.P),[])
 cases=[(0,0,0),(4,2,2),(22,0,0),(38,0,0)];out=[]
 for sp,r,anchor in cases:
  c=next(x for x in range(5) if x!=r);out.append(solve(net.orient(triples[sp],r,c,anchor),[sp,r,c,anchor],4.0))
 result={'result':'BOUNDED_UNRESTRICTED_SUPPORT_RELAXATION',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'imports':{f:p for n,f,p in MODULES},'z3_version':z3.get_version_string(),
         'case_time_limit_seconds':4,'cases':out,'elapsed_seconds':time.monotonic()-start,
         'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'limits':'No uniform amplitude premise. SAT is a support pattern only, not a QLS or witness. Solver UNSAT lacks proof; timeout UNKNOWN.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2));print('case_outcomes',[(r['case'],r['result'],r['cut_count'],r['support_histogram']) for r in out])
if __name__=='__main__':main()
