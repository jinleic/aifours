"""Bounded Z3 search for a faithful SN-band-by-CS physical host of an explicit source S over its
GIVEN actor coordinates (Rees coordinates (i,g,l) with additive C2 group and sandwich P).  SAT gives a
host that is rechecked exactly in Python; UNSAT at a size n only says: no host with band size n over
THIS actor and THIS coordinate gauge.  It is not a nonembedding theorem."""
from itertools import product
import z3
def find_host(S,mul,actor,n,P,timeout_ms=300000):
 global _CALLS;_CALLS=globals().get('_CALLS',0)+1
 Bs,el=z3.EnumSort(f'B{n}_{_CALLS}',[f'e{k}_{_CALLS}' for k in range(n)])
 m=z3.Function(f'm_{_CALLS}',Bs,Bs,Bs);sg=z3.Function(f'sg_{_CALLS}',Bs,Bs)
 beta={s:z3.Const(f'b_{s}_{_CALLS}',Bs) for s in S}
 so=z3.Solver();so.set('timeout',timeout_ms)
 for x in el:
  so.add(m(x,x)==x,sg(sg(x))==x)
 for x,y in product(el,repeat=2):so.add(sg(m(x,y))==m(sg(x),sg(y)))
 for x,y,z in product(el,repeat=3):so.add(m(m(x,y),z)==m(x,m(y,z)))
 for x,y,z,w in product(el,repeat=4):
  so.add(m(m(m(m(x,y),z),w),x)==m(m(m(m(m(m(x,y),z),x),z),w),x))
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];wt=g^P[l][j]
  so.add(beta[mul[(s,t)]]==m(beta[s],sg(beta[t]) if wt else beta[t]))
 for s,t in product(S,repeat=2):
  if s<t and actor[s]==actor[t]:so.add(beta[s]!=beta[t])
 r=so.check()
 if r!=z3.sat:return str(r),None
 mod=so.model();idx={str(e):k for k,e in enumerate(el)}
 ev=lambda term:idx[str(mod.eval(term,model_completion=True))]
 Mv=[[ev(m(x,y)) for y in el] for x in el];sv=[ev(sg(x)) for x in el];bv={s:ev(beta[s]) for s in S}
 return 'sat',(Mv,sv,bv)
def recheck(S,mul,actor,P,Mv,sv,bv):
 n=len(Mv);R=range(n)
 assert all(Mv[x][x]==x for x in R)
 assert all(Mv[Mv[x][y]][z]==Mv[x][Mv[y][z]] for x,y,z in product(R,repeat=3))
 assert all(Mv[Mv[Mv[Mv[x][y]][z]][w]][x]==Mv[Mv[Mv[Mv[Mv[Mv[x][y]][z]][x]][z]][w]][x] for x,y,z,w in product(R,repeat=4))
 assert all(sv[sv[x]]==x and sv[Mv[x][y]]==Mv[sv[x]][sv[y]] for x,y in product(R,repeat=2))
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];wt=g^P[l][j]
  assert bv[mul[(s,t)]]==Mv[bv[s]][sv[bv[t]] if wt else bv[t]]
 assert len({(bv[s],actor[s]) for s in S})==len(S)
 return True
