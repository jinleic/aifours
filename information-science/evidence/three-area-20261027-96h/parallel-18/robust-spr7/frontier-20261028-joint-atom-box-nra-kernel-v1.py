# Exact joint atom-weight/box search on the fixed-point support of the
# preceding alternating LP. Strict sign markers prove a stable root ordering.
# QF_NRA solver timeout is 15 seconds; UNSAT/unknown is support-local only.
from fractions import Fraction as Q
import z3
support=[(int(x['corner']),Q(x['t'])) for x in alt_rounds[-1]['support']]
if len(support)<5:raise ValueError('SUPPORT')
lvars=[z3.Real('joint_l%d'%j) for j in range(7)];uvars=[z3.Real('joint_u%d'%j) for j in range(7)];wvars=[z3.Real('joint_w%d'%j) for j in range(len(support))]
solver=z3.SolverFor('QF_NRA');solver.set(timeout=15000)
for j in range(7):solver.add(lvars[j]>zval(Q(1,10**6)),uvars[j]-lvars[j]>zval(Q(1,10**6)),uvars[j]<zval(1000))
for t,requirements in markers:
    vals=oe(lvars,uvars,zval(t));rhs=zval(Q(1,10**10)*(1+t)**3)
    for index,sign in requirements:solver.add(sign*vals[index]>rhs)
for w in wvars:solver.add(w>0)
solver.add(sum(wvars)==1)
for k in range(8):solver.add(sum(w*actual_vector(lvars,uvars,ci,zval(t))[k] for w,(ci,t) in zip(wvars,support))<0)
status=solver.check();joint_result={'solver_status':str(status),'support':[{'corner':ci,'t':str(t)} for ci,t in support],
 'marker_values':[str(t) for t,req in markers],'timeout_ms':15000}
if status==z3.sat:
    model=solver.model()
    def rational(v,bits):
        v=model.eval(v,model_completion=True)
        if z3.is_rational_value(v):return Q(v.numerator_as_long(),v.denominator_as_long())
        if z3.is_algebraic_value(v):
            a=v.approx(bits);return Q(a.numerator_as_long(),a.denominator_as_long())
        raise ValueError('MODEL_TYPE')
    for bits in (40,80,160,320,640):
        lo=[rational(v,bits) for v in lvars];hi=[rational(v,bits) for v in uvars];w=[rational(v,bits) for v in wvars]
        total=sum(w)
        if total<=0:continue
        w=[x/total for x in w]
        if not all(Q(1,10**6)<lo[j]<hi[j]-Q(1,10**6) and hi[j]<1000 for j in range(7)):continue
        if not all(v>0 for v in w):continue
        if not all(sign*oe(lo,hi,t)[index]>Q(1,10**10)*(1+t)**3 for t,req in markers for index,sign in req):continue
        F=[sum(weight*actual_vector(lo,hi,ci,t)[k] for weight,(ci,t) in zip(w,support)) for k in range(8)]
        if not all(v<0 for v in F):continue
        if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(lo,hi)):raise ValueError('STABILITY_REPLAY')
        joint_result.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','lower':[str(v) for v in lo],'upper':[str(v) for v in hi],
          'weights':[str(v) for v in w],'coefficient_sums':[str(v) for v in F],'rational_precision':bits});break
    else:joint_result['status']='SAT_MODEL_RATIONAL_REPLAY_FAILED'
elif status==z3.unsat:joint_result['status']='UNSAT_ONLY_FOR_FROZEN_SUPPORT_AND_MARKER_REGION'
else:joint_result['status']='INCONCLUSIVE_'+solver.reason_unknown()
print('joint atom/box NRA search:',joint_result)
