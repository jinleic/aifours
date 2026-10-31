# Exact finite-site search over ALL h>=0 through the order-two moment cone.
# P(h)=P0+h P1+h² P2. Nonnegative combinations of I+hD and D rows are
# exactly mu0,mu1,mu2>=0 with mu0*mu2>=mu1²; each interior triple has an
# explicit two-atom realization at h=0 and h=mu2/mu1.
from fractions import Fraction as Q
import z3
box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
sites=[(0,Q(289)),(0,Q(2043,5)),(1,Q(4043,53)),(1,Q(1011,13)),(2,Q(29,3)),(3,Q(117,10)),(2,Q(289))]
rows=[]
for ci,t in sites:
 v0=op_vector(cs[ci],0,Q(0),t);v1=op_vector(cs[ci],0,Q(1),t);v2=op_vector(cs[ci],0,Q(2),t)
 quadratic=[(v2[j]-2*v1[j]+v0[j])/2 for j in range(8)];linear=[v1[j]-v0[j]-quadratic[j] for j in range(8)]
 rows.append(([v/(1+t)**7 for v in v0],[v/(1+t)**7 for v in linear],[v/(1+t)**7 for v in quadratic]))
M=[[z3.Real('moment_%d_%d'%(i,j)) for j in range(3)] for i in range(len(sites))]
S=z3.SolverFor('QF_NRA');S.set(timeout=20000)
for x,y,z in M:S.add(x>=0,y>=0,z>=0,x*z>=y*y)
S.add(sum(x+z for x,y,z in M)==1)
for k in range(8):S.add(sum(M[i][j]*zval(rows[i][j][k]) for i in range(len(sites)) for j in range(3))<0)
status=S.check();mom_result={'solver_status':str(status),'timeout_ms':20000,'sites':[{'corner':ci,'t':str(t)} for ci,t in sites]}
if status==z3.sat:
 model=S.model()
 def rat(v,bits):
  v=model.eval(v,model_completion=True)
  if z3.is_rational_value(v):return Q(v.numerator_as_long(),v.denominator_as_long())
  if z3.is_algebraic_value(v):
   z=v.approx(bits);return Q(z.numerator_as_long(),z.denominator_as_long())
  raise ValueError('MODEL')
 for bits in (40,80,160,320,640):
  mm=[[rat(v,bits) for v in trip] for trip in M]
  if any(x<0 or y<0 or z<0 for x,y,z in mm):continue
  # Rational interior correction only when needed; strict coordinate signs are replayed.
  for trip in mm:
   x,y,z=trip
   if x*z<y*y:
    if x<=0:break
    trip[2]=y*y/x+Q(1,2**bits)
  else:
   total=sum(x+z for x,y,z in mm)
   if total<=0:continue
   mm=[[v/total for v in trip] for trip in mm]
   if any(x*z<y*y for x,y,z in mm):continue
   F=[sum(mm[i][j]*rows[i][j][k] for i in range(len(sites)) for j in range(3)) for k in range(8)]
   if not all(v<0 for v in F):continue
   atoms=[]
   for i,((ci,t),(x,y,z)) in enumerate(zip(sites,mm)):
    if y>0:
     if z<=0:raise ValueError('MOMENT')
     h=z/y;wh=y*y/z;w0=x-wh
     if w0<0:raise ValueError('MOMENT')
     if w0:atoms.append((ci,t,Q(0),w0/(1+t)**7,'I+hD'))
     if wh:atoms.append((ci,t,h,wh/(1+t)**7,'I+hD'))
    else:
     if x:atoms.append((ci,t,Q(0),x/(1+t)**7,'I+hD'))
     if z:atoms.append((ci,t,Q(0),z/(1+t)**7,'D'))
   check=[]
   for k in range(8):
    check.append(sum(w*(op_vector(cs[ci],0,h,t)[k] if typ=='I+hD' else op_vector(cs[ci],1,Q(0),t)[k]*49) for ci,t,h,w,typ in atoms))
   # D rows use unnormalized a',b'; order-1 normalized vector must be multiplied by 7².
   if any(v>=0 for v in check) or check!=F:raise ValueError('DECOMPOSITION')
   mom_result.update({'status':'STRICT_OPERATOR_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
     'moments':[[str(v) for v in trip] for trip in mm],'coefficient_sums':[str(v) for v in F],
     'atoms':[{'corner':ci,'t':str(t),'h':str(h),'weight':str(w),'operator':typ} for ci,t,h,w,typ in atoms]});break
 else:mom_result['status']='SAT_MODEL_RATIONAL_REPLAY_FAILED'
elif status==z3.unsat:mom_result['status']='UNSAT_ONLY_FOR_SEVEN_SITES_AND_FIXED_BOX'
else:mom_result['status']='INCONCLUSIVE_'+S.reason_unknown()
print('continuous-operator moment cone:',mom_result)
