# Exact QF_NRA stress of the high-gain sufficient condition on fixed nodes
# 1,2,3,6,8 with continuous u,v,lambda and a free test frequency.
# SAT requires rational replay; unknown/UNSAT is never a global claim.
from fractions import Fraction as Q
import z3

def cmul(a,b):
 out=[zval(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return out
def cp(roots,scale):
 out=[zval(1)]
 for r in roots:out=cmul(out,[-r,zval(1)])
 return [-scale*x for x in out]
def cev(poly,t):return sum(v*t**j for j,v in enumerate(poly))
def cder(poly,t):return sum(j*poly[j]*t**(j-1) for j in range(1,len(poly)))
u=z3.Real('hg_u');v=z3.Real('hg_v');lam=z3.Real('hg_lambda');T=z3.Real('hg_t');B=[zval(0)]+[z3.Real('hg_b%d'%j) for j in range(1,6)]+[zval(1),zval(0)]
N=[zval(x) for x in (1,2,3,6,8)];em=cp([u,N[2],N[3]],lam);ep=cp([N[0],N[1],N[4]],zval(1));om=cp([N[0],N[3],N[4]],zval(1));op=cp([N[1],N[2],v],zval(1))
cs=[(em,om),(em,op),(ep,om),(ep,op)];cts=[(2,N[0]),(3,N[1]),(1,N[2]),(0,N[3]),(2,N[4])]
S=z3.SolverFor('QF_NRA');S.set(timeout=20000);S.add(u>0,u<1,v>8,v<20,lam>1,lam<20,T>0,T<100)
for j in range(4):S.add(ep[j]-em[j]>0)
for j in range(3):S.add(op[j]-om[j]>0)
F=lambda t:B[0]-B[2]*t+B[4]*t*t-B[6]*t**3
G=lambda t:B[1]-B[3]*t+B[5]*t*t-B[7]*t**3
for ci,t in cts:S.add(cder(cs[ci][0],t)*F(t)+t*cder(cs[ci][1],t)*G(t)==0)
# Search a strict negative pairing at actual boundary corner 0.
S.add(cev(em,T)*F(T)+T*cev(om,T)*G(T)<0)
status=S.check();fixed_hg={'solver_status':str(status),'timeout_ms':20000,'fixed_nodes':['1','2','3','6','8'],'tested_corner':0}
if status==z3.sat:
 model=S.model()
 def rat(x,bits):
  q=model.eval(x,model_completion=True)
  if z3.is_rational_value(q):return Q(q.numerator_as_long(),q.denominator_as_long())
  if z3.is_algebraic_value(q):
   a=q.approx(bits);return Q(a.numerator_as_long(),a.denominator_as_long())
  raise ValueError('MODEL')
 # Tangency equalities are reconstructed exactly from rational u,v,lambda;
 # direct rounding of b would break those equalities.
 for bits in (40,80,160,320):
  uu,vv,qq,tt=[rat(x,bits) for x in (u,v,lam,T)]
  design=(Q(1),Q(2),Q(3),Q(6),Q(8),vv,str(uu),str(qq),'','')
  try:lo,hi,center,vertices,contacts=five_box(design)
  except ValueError:continue
  rows=[]
  for ci,t in contacts:
   a=vertices[ci];ep1=-a[2]+2*a[4]*t-3*a[6]*t*t;op1=-a[3]+2*a[5]*t-3*t*t
   rows.append([ep1*(-t)**(j//2) if j%2==0 else t*op1*(-t)**((j-1)//2) for j in range(8)])
  bb=[Q(0)]*8;bb[6]=Q(1)
  try:xs=solve5([[row[j] for j in (1,2,3,4,5)] for row in rows],[-row[6] for row in rows])
  except ValueError:continue
  for j,x in zip((1,2,3,4,5),xs):bb[j]=x
  value=independent_pair_t(vertices[0],bb,tt)
  if value<0:
   fixed_hg.update({'status':'EXACT_HIGH_GAIN_CRITERION_COUNTEREXAMPLE','u':str(uu),'v':str(vv),'lambda':str(qq),'t':str(tt),
    'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],'numerator':[str(x) for x in bb],'negative_pairing':str(value),'precision':bits});break
 else:fixed_hg['status']='SAT_MODEL_RATIONAL_REPLAY_FAILED'
elif status==z3.unsat:fixed_hg['status']='UNSAT_FIXED_NODES_CORNER_AND_BOUNDS_ONLY'
else:fixed_hg['status']='INCONCLUSIVE_'+S.reason_unknown()
print('fixed-node high-gain continuum:',fixed_hg)
