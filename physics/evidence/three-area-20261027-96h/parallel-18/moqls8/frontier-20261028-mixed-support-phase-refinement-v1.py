#!/usr/bin/env python3
"""Bounded support relaxation with sound odd two-axis phase-cycle blocking."""
import argparse,collections,hashlib,importlib.util,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
IMPORT='frontier-20261028-anchor-sparse-net-obstructions-v1.py';PIN='6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'
if hashlib.sha256((H/IMPORT).read_bytes()).hexdigest()!=PIN:raise ValueError('module pin')
spec=importlib.util.spec_from_file_location('anchor_net',H/IMPORT);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
V=range(8)
def find_cycle(S,edges):
 for t,u in itertools.combinations(V,2):
  points=[x for x in S if {t,u}<=S[x]];G={x:[] for x in points}
  for x,y in edges:
   if x in G and y in G and S[x]&S[y]=={t,u}:G[x].append(y);G[y].append(x)
  depth={};parent={}
  for root in G:
   if root in depth:continue
   depth[root]=0;parent[root]=None;q=collections.deque([root])
   while q:
    x=q.popleft()
    for y in G[x]:
     if y not in depth:depth[y]=depth[x]+1;parent[y]=x;q.append(y)
     elif depth[x]%2==depth[y]%2:
      px=[];p=x
      while p is not None:px.append(p);p=parent[p]
      py=[];p=y
      while p is not None:py.append(p);p=parent[p]
      meet=next(p for p in px if p in set(py));cycle=px[:px.index(meet)+1]+list(reversed(py[:py.index(meet)]))
      if len(cycle)<3 or len(cycle)%2!=1:raise ValueError('not odd')
      return {'axes':[t,u],'cells':cycle}
 return None

def solve(T,case,secs):
 start=time.monotonic();facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:sorted(set(V)-set(facts[x][1:])) for x in range(8,64)}
 if any(len(z)!=4 for z in A.values()):raise ValueError('allowed')
 dom={x:[z for n in range(1,5) for z in itertools.combinations(A[x],n)] for x in A}
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in V}
 if any(len(z)!=8 for z in lines.values()):raise ValueError('lines')
 s=z3.Solver();Q={x:[z3.Bool(f'q_{x}_{j}') for j in range(15)] for x in A};P={}
 for x in A:
  s.add(z3.PbEq([(q,1) for q in Q[x]],1))
  for t in A[x]:P[x,t]=z3.Or([Q[x][j] for j,D in enumerate(dom[x]) if t in D])
 for line in lines.values():
  for t in V:
   target=12-sum(12 for x in line if x<8 and x==t)
   C=[(Q[x][j],12//len(D)) for x in line if x>=8 for j,D in enumerate(dom[x]) if t in D]
   if C:s.add(z3.PbEq(C,target))
   elif target:raise ValueError('missing axis')
 edges=set()
 for line in lines.values():edges.update(itertools.combinations((x for x in line if x>=8),2))
 for x,y in edges:
  C=set(A[x])&set(A[y])
  for t in C:s.add(z3.Implies(z3.And(P[x,t],P[y,t]),z3.Or([z3.And(P[x,u],P[y,u]) for u in C if u!=t])))
 s.add(z3.Or([Q[x][j] for x in A for j,D in enumerate(dom[x]) if len(D)>1]))
 cuts=[];result='UNKNOWN';modelS=None
 while time.monotonic()-start<secs and len(cuts)<500:
  ms=max(1,int(1000*(secs-(time.monotonic()-start))));s.set(timeout=ms);status=s.check()
  if status==z3.unsat:result='UNCERTIFIED_Z3_UNSAT';break
  if status==z3.unknown:result='UNKNOWN_'+s.reason_unknown();break
  M=s.model();S={x:set(next(D for j,D in enumerate(dom[x]) if z3.is_true(M.eval(Q[x][j],model_completion=True))) ) for x in A}
  checkS={**S,**{j:{j} for j in V}}
  if any(sum(12//len(checkS[x]) for x in line if t in checkS[x])!=12 for line in lines.values() for t in V):raise ValueError('model line weights')
  if any(len(S[x]&S[y])==1 for x,y in edges):raise ValueError('model singleton overlap')
  cycle=find_cycle(S,edges)
  if cycle is None:result='SAT_RELAXATION_NO_ODD_TWO_AXIS_CYCLE';modelS=S;break
  axes=set(cycle['axes']);cells=cycle['cells'];expr=[]
  for x,y in zip(cells,cells[1:]+cells[:1]):
   if tuple(sorted((x,y))) not in edges or S[x]&S[y]!=axes:raise ValueError('invalid cycle cut')
   common=set(A[x])&set(A[y]);e=[P[x,t] for t in axes]+[P[y,t] for t in axes]
   e.extend(z3.Not(z3.And(P[x,t],P[y,t])) for t in common-axes)
   expr.append(z3.And(e))
  s.add(z3.Not(z3.And(expr)));cuts.append(cycle)
 if result=='UNKNOWN' and len(cuts)>=500:result='UNKNOWN_CUT_LIMIT'
 return {'case':case,'result':result,'cuts':cuts,'cut_count':len(cuts),
         'final_model_supports':{str(x):sorted(v) for x,v in modelS.items()} if modelS is not None else None,
         'final_model_support_histogram':dict(collections.Counter(len(v) for v in modelS.values())) if modelS else None,
         'elapsed_seconds':time.monotonic()-start}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 triples=sum((mod.read_catalogue(*p) for p in mod.P),[])
 cases=[(4,2,2),(6,2,0),(20,3,0),(38,0,0)];out=[]
 for sp,r,anchor in cases:
  c=next(x for x in range(5) if x!=r);out.append(solve(mod.orient(triples[sp],r,c,anchor),[sp,r,c,anchor],4.0))
 report={'result':'BOUNDED_PHASE_REFINEMENT_NO_PROOF_CERTIFICATE',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'import_sha256':PIN,
         'z3_version':z3.get_version_string(),'case_time_limit_seconds':4,'cases':out,
         'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'limits':'Every recorded cycle is a sound necessary phase obstruction; UNSAT is unverified, SAT is only a support relaxation, timeout is UNKNOWN.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2));print('case_outcomes',[(x['case'],x['result'],x['cut_count'],x['final_model_support_histogram']) for x in out])
if __name__=='__main__':main()
