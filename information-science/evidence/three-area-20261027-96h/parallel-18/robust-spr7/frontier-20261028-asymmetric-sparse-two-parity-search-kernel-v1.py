# Exact two-radius nonlinear search with 8-atom supports carrying even and
# odd inversions. Each query has 12s bound; unknown/UNSAT is support-local.
from fractions import Fraction as Q
import z3
bx=asym_results[1];lower=[Q(x) for x in bx['lower']];upper=[Q(x) for x in bx['upper']]
nominal=center_from_factors(bx['real_root'],bx['pairs']);dm=[nominal[j]-lower[j] for j in range(7)];dp=[upper[j]-nominal[j] for j in range(7)]
mks=[((a1bands[j][1]+a1bands[j+1][0])/2).limit_denominator(1000) for j in range(5)]
req=[((1,-1),(2,1)),((1,-1),(3,-1)),((0,1),(3,-1)),((0,1),(2,1)),((1,-1),(2,1))]
base=[(0,a1nodes[0]),(2,a1nodes[1]),(0,a1nodes[2]),(1,a1nodes[3])]
extra=[a1nodes[4],a1nodes[6],a1nodes[8],a1nodes[10]]
patterns=[(0,0,0,0),(2,1,2,1),(3,3,3,3)]
sparse_results=[]
for ip,pattern in enumerate(patterns):
 support=base+list(zip(pattern,extra));RE=z3.Real('spRE%d'%ip);RO=z3.Real('spRO%d'%ip);W=[z3.Real('spW%d_%d'%(ip,i)) for i in range(len(support))]
 lv=[zval(nominal[j])-(RE if j%2==0 else RO)*zval(dm[j]) for j in range(7)]
 uv=[zval(nominal[j])+(RE if j%2==0 else RO)*zval(dp[j]) for j in range(7)]
 S=z3.SolverFor('QF_NRA');S.set(timeout=12000)
 S.add(RE>zval(Q(1,10)),RO>zval(Q(1,10)),RE<zval(3),RO<zval(3))
 for j in range(7):S.add(lv[j]>0,uv[j]>lv[j])
 for t,rs in zip(mks,req):
  vals=oe(lv,uv,zval(t))
  for idx,sign in rs:S.add(sign*vals[idx]>0)
 for w in W:S.add(w>=0)
 S.add(sum(W)==1)
 for k in range(8):S.add(sum(w*actual_vector(lv,uv,ci,zval(t))[k]/zval((1+t)**7) for (ci,t),w in zip(support,W))<0)
 status=S.check();rec={'pattern':pattern,'support':[{'corner':ci,'t':str(t)} for ci,t in support],'solver_status':str(status),'timeout_ms':12000}
 if status==z3.sat:
  model=S.model()
  def rat(v,bits):
   v=model.eval(v,model_completion=True)
   if z3.is_rational_value(v):return Q(v.numerator_as_long(),v.denominator_as_long())
   if z3.is_algebraic_value(v):
    x=v.approx(bits);return Q(x.numerator_as_long(),x.denominator_as_long())
   raise ValueError('MODEL')
  for bits in (40,80,160,320,640):
   re,ro=rat(RE,bits),rat(RO,bits);weights=[rat(w,bits) for w in W];total=sum(weights)
   if total<=0 or any(w<0 for w in weights):continue
   weights=[w/total for w in weights];lo=[nominal[j]-(re if j%2==0 else ro)*dm[j] for j in range(7)];hi=[nominal[j]+(re if j%2==0 else ro)*dp[j] for j in range(7)]
   if not all(0<lo[j]<hi[j] for j in range(7)):continue
   if not all(sign*oe(lo,hi,t)[idx]>0 for t,rs in zip(mks,req) for idx,sign in rs):continue
   F=[sum(w*actual_vector(lo,hi,ci,t)[k]/(1+t)**7 for (ci,t),w in zip(support,weights)) for k in range(8)]
   if not all(v<0 for v in F):continue
   if not all(routh_ok(a) and integer_hurwitz(a) for a in local_corners(lo,hi)):raise ValueError('STABILITY')
   rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','even_scale':str(re),'odd_scale':str(ro),'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
     'weights':[str(w) for w in weights],'normalized_coefficient_sums':[str(v) for v in F],'precision':bits});break
  else:rec['status']='SAT_MODEL_RATIONAL_REPLAY_FAILED'
 elif status==z3.unsat:rec['status']='UNSAT_THIS_SUPPORT_AND_FAMILY'
 else:rec['status']='INCONCLUSIVE_'+S.reason_unknown()
 sparse_results.append(rec)
 if rec['status']=='STRICT_ACTUAL_BOX_CERTIFICATE':break
print('sparse two-parity search:',[{'pattern':r['pattern'],'status':r['status'],'solver_status':r['solver_status']} for r in sparse_results])
