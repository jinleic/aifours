#!/usr/bin/env python3
"""Bounded q1 support relaxation; SAT model is NOT a quantum family."""
import argparse,collections,hashlib,itertools,json,pathlib,resource,time
import z3
H=pathlib.Path(__file__).parent
PIN='95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67'
V=range(8)
def net():
 b=(H/'frontier-20261028-source-wanless-max3-order8-v1.txt').read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('snapshot hash')
 L=[x.strip() for x in b.decode('ascii').splitlines() if x.strip()]
 if L[0].split()[:3]!=['8','8','114'] or len(L)!=913:raise ValueError('layout')
 T=[[[ord(ch)-97 for ch in L[1+8*k+i]] for i in V] for k in range(3)]
 for A in T:
  if any(set(row)!=set(V) for row in A) or any({A[i][j] for i in V}!=set(V) for j in V):raise ValueError('Latin')
 for a,b in itertools.combinations(range(3),2):
  if len({(T[a][i][j],T[b][i][j]) for i in V for j in V})!=64:raise ValueError('MOLS')
 return [[[T[a][0].index(T[a][i][j]) for j in V] for i in V] for a in range(3)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 T=net();facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:sorted(set(V)-set(facts[x][1:])) for x in range(8,64)}
 if any(len(z)!=4 for z in A.values()):raise ValueError('allowed set')
 domains={x:[tuple(z) for k in range(1,5) for z in itertools.combinations(A[x],k)] for x in A}
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in V}
 if any(len(z)!=8 for z in lines.values()):raise ValueError('not five-net')
 solver=z3.Solver();solver.set(timeout=7000)
 choices={x:[z3.Bool(f'q_{x}_{i}') for i in range(len(domains[x]))] for x in A}
 contains={}
 for x in A:
  solver.add(z3.PbEq([(q,1) for q in choices[x]],1))
  for t in A[x]:contains[x,t]=z3.Or([choices[x][i] for i,S in enumerate(domains[x]) if t in S])
 # In each actual line, uniform support sizes 1,2,3,4 contribute 12,6,4,3 units.
 for (k,v),line in lines.items():
  for t in V:
   target=12-sum(12 for x in line if x<8 and x==t)
   terms=[(choices[x][i],12//len(S)) for x in line if x>=8 for i,S in enumerate(domains[x]) if t in S]
   if terms:solver.add(z3.PbEq(terms,target))
   elif target!=0:raise ValueError('missing candidate for required coordinate')
 # Orthogonality is impossible if the two support sets meet at exactly one axis.
 edges=set()
 for line in lines.values():
  edges.update(itertools.combinations((x for x in line if x>=8),2))
 for x,y in sorted(edges):
  common=sorted(set(A[x])&set(A[y]))
  for t in common:
   alternatives=[z3.And(contains[x,u],contains[y,u]) for u in common if u!=t]
   solver.add(z3.Implies(z3.And(contains[x,t],contains[y,t]),z3.Or(alternatives)))
 solver.add(z3.Or([choices[x][i] for x in A for i,S in enumerate(domains[x]) if len(S)>1]))
 status=solver.check();S={};counts=None;verification=None
 if status==z3.sat:
  M=solver.model()
  for x in A:
   z=[domains[x][i] for i,q in enumerate(choices[x]) if z3.is_true(M.eval(q,model_completion=True))]
   if len(z)!=1:raise ValueError('model choice')
   S[x]=set(z[0])
  S.update({j:{j} for j in V})
  line_errors=0
  for line in lines.values():
   for t in V:
    if sum(12//len(S[x]) for x in line if t in S[x])!=12:line_errors+=1
  pair_errors=sum(len(S[x]&S[y])==1 for x,y in edges)
  if line_errors or pair_errors or not any(len(S[x])>1 for x in A):raise ValueError('independent model verification')
  counts=dict(collections.Counter(len(S[x]) for x in A));verification={'integer_line_weight_errors':line_errors,'single_intersection_pair_errors':pair_errors}
 elif status==z3.unknown:why=solver.reason_unknown()
 else:why=None
 report={'result':'SAT_RELAXATION_ONLY_NOT_A_PHYSICAL_QLS' if status==z3.sat else 'UNKNOWN_OR_UNCHECKED_SOLVER_RESULT',
  'solver_status':str(status),'solver_reason_unknown':solver.reason_unknown() if status==z3.unknown else None,
  'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'source_snapshot_sha256':PIN,
  'species_index':0,'orientation':[0,1],'anchor_symbol':0,'solver_version':z3.get_version_string(),
  'timeout_milliseconds':7000,'offrow_cells':56,'onehot_choices':sum(map(len,choices.values())),
  'net_line_count':len(lines),'pair_edges_checked':len(edges),'model_support_histogram':counts,
  'model_supports':{str(x):sorted(S[x]) for x in sorted(S)} if S else None,'model_integer_checks':verification,
  'elapsed_seconds':time.monotonic()-start,'max_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  'limits':'Only necessary support and diagonal line-weight constraints; excludes singleton intersections but does not impose phase/Gram identities. A SAT model is not a QLS; UNSAT lacks independent certificate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k!='model_supports'},indent=2))
if __name__=='__main__':main()
