#!/usr/bin/env python3
"""Tracked-group diagnostic for the bounded n=1320 border model."""
import sys,json
from itertools import combinations
from math import gcd
import z3
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
pc=[x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)]
qc=[x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)]
P={x:z3.Bool('p%d'%x) for x in pc};Q={x:z3.Bool('q%d'%x) for x in qc}
groups=sorted({gcd(x-y,n) for x,y in combinations(pc,2)}|{gcd(x-y,n) for x,y in combinations(qc,2)})
side={g:z3.Bool('side%d'%g) for g in groups};s=z3.Solver();s.set(timeout=30000,unsat_core=True)
def track(name,*terms):s.assert_and_track(z3.And(*terms),name)
track('anchor_P',*(P[x] for x in A));track('anchor_Q',*(Q[y] for y in Y))
if sys.argv[1]!='none':
 d=int(sys.argv[1]);q=n//d
 track('size_P',z3.PbEq([(v,1) for v in P.values()],d))
 track('size_Q',z3.PbEq([(v,1) for v in Q.values()],q))
for kind,vals,V in [('P',pc,P),('Q',qc,Q)]:
 bins={g:[] for g in groups}
 for x,y in combinations(vals,2):
  g=gcd(x-y,n);lim=side[g] if kind=='P' else z3.Not(side[g])
  bins[g].append(z3.Or(z3.Not(V[x]),z3.Not(V[y]),lim))
 for g,clauses in bins.items():
  if clauses:track(kind+'_gcd_'+str(g),*clauses)
if sys.argv[1]!='none' and len(sys.argv)>2 and sys.argv[2]=='spectral':
 def counts(D,mod):return [z3.Sum([z3.If(v,1,0) for x,v in D.items() if x%mod==r]) for r in range(mod)]
 for p in (3,5,11):
  R=P if d%p==0 else Q;total=d if R is P else q
  track('balance_'+str(p),*(x==total//p for x in counts(R,p)))
 for k in (1,2,3):
  mod=2**k;h=mod//2;cp=counts(P,mod);cq=counts(Q,mod)
  track('balance_2pow_'+str(k),z3.Or(z3.And(*(cp[r]==cp[r+h] for r in range(h))),
                                     z3.And(*(cq[r]==cq[r+h] for r in range(h)))))
r=s.check();print(json.dumps({'P_size':sys.argv[1],'spectral':len(sys.argv)>2 and sys.argv[2]=='spectral',
 'result':str(r),'core':[str(x) for x in s.unsat_core()] if r==z3.unsat else [],
 'reason':s.reason_unknown() if r==z3.unknown else ''},indent=2))
