#!/usr/bin/env python3
"""Independent per-spectrum algebraic-real SMT replay of the Q(sqrt5) census."""
import datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import z3
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-qroot5-spectrum-census-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='fa4f2fcfa29b8ed7f4daf875eb8d3df5601321cf357977d3120d8ed702451a3f';D=json.loads(raw)
z=(F(0),F(0));o=(F(1),F(0))
def a(x,y):return(x[0]+y[0],x[1]+y[1])
def n(x):return(-x[0],-x[1])
def sub(x,y):return a(x,n(y))
def m(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def oa(x,y):return(a(x[0],y[0]),a(x[1],y[1]))
def on(x):return(n(x[0]),n(x[1]))
def om(x,y):
 ac=m(x[0],y[0]);bd=m(x[1],y[1]);return(sub(ac,bd),sub(a(m(x[0],y[1]),m(x[1],y[0])),bd))
# K=Q(sqrt5)[omega,eta], omega²=-1-omega and eta²=c eta-1.
c=(F(-1,2),F(1,2))
def km(x,y):
 ac=om(x[:2],y[:2]);bd=om(x[2:],y[2:]);bc=om(x[2:],y[:2]);ad=om(x[:2],y[2:]);cbd=(m(c,bd[0]),m(c,bd[1]));return oa(ac,on(bd))+oa(oa(ad,bc),cbd)
one=(o,z,z,z);zeta=(o,o,n(c),n(c));powers=[one]
for _ in range(15):powers.append(km(powers[-1],zeta))
assert powers[15]==one
root5=z3.simplify(z3.Sqrt(z3.RealVal(5)))
def zv(x):return z3.RealVal(str(x[0]))+z3.RealVal(str(x[1]))*root5
sat=[];unsat=unknown=0;tested=0
for rest in itertools.combinations_with_replacement(range(15),5):
 ex=(0,)+rest
 if len({a%3 for a in ex})<3 or math.gcd(15,*ex)!=1:continue
 tested+=1;S=sorted(set(ex));mult=[ex.count(a)for a in S];q=[z3.Real('x'+str(j))for j in range(len(S))]
 solver=z3.SolverFor('QF_NRA');solver.set(timeout=3000)
 for v,k in zip(q,mult):solver.add(6*v>=k,2*v<=k)
 for k in range(4):solver.add(z3.Sum([q[j]*zv(powers[(-2*e)%15][k])for j,e in enumerate(S)])==0)
 for r in range(3):
  nr=sum(k for e,k in zip(S,mult)if e%3==r)
  solver.add(6*z3.Sum([q[j]for j,e in enumerate(S)if e%3==r])==3*nr-2)
 result=solver.check()
 if result==z3.sat:sat.append(ex)
 elif result==z3.unsat:unsat+=1
 else:unknown+=1
assert tested==7740 and unknown==0 and sat==[tuple(x)for x in D['survivors']]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'census_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'solver':'Z3 '+z3.get_version_string()+' QF_NRA algebraic reals',
 'tested':tested,'sat':len(sat),'unsat':unsat,'unknown':unknown,'exact_survivor_list_matches':True,
 'field_realizability_note':'bounded polytope with Q(sqrt5) coefficients has Q(sqrt5) vertices whenever nonempty',
 'status':'PASS'}
(P/'frontier-20261029-cyclic15-qroot5-spectrum-smt-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
