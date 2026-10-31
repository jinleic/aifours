# Joint exact search in a genuinely two-parameter asymmetric scaling family.
# Five fixed sign markers enforce stable parity root geometry; 12 support atoms
# carry reversals in all six bands. QF_NRA timeout never implies impossibility.
from fractions import Fraction as Q
import z3
bx=asym_results[1];lower=[Q(x) for x in bx['lower']];upper=[Q(x) for x in bx['upper']]
nominal=center_from_factors(bx['real_root'],bx['pairs']);dm=[nominal[j]-lower[j] for j in range(7)];dp=[upper[j]-nominal[j] for j in range(7)]
mks=[((a1bands[j][1]+a1bands[j+1][0])/2).limit_denominator(1000) for j in range(5)]
req=[((1,-1),(2,1)),((1,-1),(3,-1)),((0,1),(3,-1)),((0,1),(2,1)),((1,-1),(2,1))]
if not all(sign*oe(lower,upper,t)[idx]>0 for t,r in zip(mks,req) for idx,sign in r):raise ValueError('MARKER_SEED')
# Node order alternates even and odd bands; pick the appropriate early/late endpoints.
support=[]
for j in range(6):
 t1,t2=a1nodes[2*j:2*j+2];i=j//2
 if j%2==0:ci1,ci2=((0,2) if i%2==0 else (2,0))
 else:ci1,ci2=((0,1) if i%2==0 else (1,0))
 support.extend(((ci1,t1),(ci2,t2)))
RE=z3.Real('asym_RE');RO=z3.Real('asym_RO');W=[z3.Real('asym_W%d'%i) for i in range(len(support))]
lv=[zval(nominal[j])- (RE if j%2==0 else RO)*zval(dm[j]) for j in range(7)]
uv=[zval(nominal[j])+ (RE if j%2==0 else RO)*zval(dp[j]) for j in range(7)]
S=z3.SolverFor('QF_NRA');S.set(timeout=20000)
S.add(RE>zval(Q(1,10)),RO>zval(Q(1,10)),RE<zval(3),RO<zval(3))
for j in range(7):S.add(lv[j]>0,uv[j]>lv[j])
for t,rs in zip(mks,req):
 vals=oe(lv,uv,zval(t))
 for idx,sign in rs:S.add(sign*vals[idx]>0)
for w in W:S.add(w>0)
S.add(sum(W)==1)
for k in range(8):S.add(sum(w*actual_vector(lv,uv,ci,zval(t))[k]/zval((1+t)**7) for (ci,t),w in zip(support,W))<0)
status=S.check();result={'solver_status':str(status),'timeout_ms':20000,'markers':[str(x) for x in mks],
 'support':[{'corner':ci,'t':str(t)} for ci,t in support],'family':'independent even/odd radius multipliers of asym_results[1]'}
if status==z3.sat:
 model=S.model()
 def qapprox(v,bits):
  val=model.eval(v,model_completion=True)
  if z3.is_rational_value(val):return Q(val.numerator_as_long(),val.denominator_as_long())
  if z3.is_algebraic_value(val):
   r=val.approx(bits);return Q(r.numerator_as_long(),r.denominator_as_long())
  raise ValueError('MODEL')
 for bits in (40,80,160,320,640):
  re,ro=qapprox(RE,bits),qapprox(RO,bits);weights=[qapprox(w,bits) for w in W];total=sum(weights)
  if total<=0:continue
  weights=[w/total for w in weights]
  lo=[nominal[j]-(re if j%2==0 else ro)*dm[j] for j in range(7)];hi=[nominal[j]+(re if j%2==0 else ro)*dp[j] for j in range(7)]
  if not all(w>0 for w in weights) or not all(0<lo[j]<hi[j] for j in range(7)):continue
  if not all(sign*oe(lo,hi,t)[idx]>0 for t,r in zip(mks,req) for idx,sign in r):continue
  F=[sum(w*actual_vector(lo,hi,ci,t)[k]/(1+t)**7 for (ci,t),w in zip(support,weights)) for k in range(8)]
  if not all(v<0 for v in F):continue
  if not all(routh_ok(a) and integer_hurwitz(a) for a in local_corners(lo,hi)):raise ValueError('STABILITY_REPLAY')
  result.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','even_scale':str(re),'odd_scale':str(ro),'lower':[str(x) for x in lo],
   'upper':[str(x) for x in hi],'weights':[str(w) for w in weights],'normalized_coefficient_sums':[str(v) for v in F],'precision':bits});break
 else:result['status']='SAT_MODEL_RATIONAL_REPLAY_FAILED'
elif status==z3.unsat:result['status']='UNSAT_ONLY_FOR_THIS_SUPPORT_MARKERS_AND_SCALING'
else:result['status']='INCONCLUSIVE_'+S.reason_unknown()
print('asymmetric two-parity NRA result:',result)
