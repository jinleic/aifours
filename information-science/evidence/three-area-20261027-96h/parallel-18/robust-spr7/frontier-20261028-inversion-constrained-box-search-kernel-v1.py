# New support geometry: deliberately include both parity-band sign inversions.
# Deterministic exact fixed-weight QF_LRA box feasibility; no float arithmetic.
from fractions import Fraction as Q
from random import Random
import z3
rng_inv=Random(20261029)
inv_atoms=[(0,Q(3,5)),(2,Q(9,10)),(0,Q(11,10)),(1,Q(19,10)),
           (2,Q(21,10)),(0,Q(29,10)),(1,Q(16,5)),(0,Q(29,5)),
           (0,Q(31,5)),(2,Q(39,5)),(0,Q(41,5)),(1,Q(54,5))]
# Endpoint sign constraints enforce E and O inversions in all six bands.
inv_signs=[(Q(3,5),0,-1),(Q(9,10),1,1),(Q(11,10),2,-1),(Q(19,10),3,1),
           (Q(21,10),1,1),(Q(29,10),0,-1),(Q(16,5),3,1),(Q(29,5),2,-1),
           (Q(31,5),0,-1),(Q(39,5),1,1),(Q(41,5),2,-1),(Q(54,5),3,1)]
inv_results=[]
for trial in range(40):
    weights=[]
    for ci,t in inv_atoms:
        exponent=rng_inv.randrange(-3,4);factor=Q(10**exponent) if exponent>=0 else Q(1,10**(-exponent))
        weights.append(Q(rng_inv.randrange(1,10))*factor/(1+t)**7)
    lv=[z3.Real('inv_l%d_%d'%(trial,j)) for j in range(7)];uv=[z3.Real('inv_u%d_%d'%(trial,j)) for j in range(7)]
    solver=z3.SolverFor('QF_LRA');solver.set(timeout=2000)
    for j in range(7):solver.add(lv[j]>zval(Q(1,10**6)),uv[j]-lv[j]>zval(Q(1,10**6)),uv[j]<zval(1000))
    for t,requirements in markers:
        values=oe(lv,uv,zval(t));m=zval(Q(1,10**10)*(1+t)**3)
        for index,sign in requirements:solver.add(sign*values[index]>m)
    for t,index,sign in inv_signs:solver.add(sign*oe(lv,uv,zval(t))[index]>zval(Q(1,10**10)*(1+t)**3))
    for k in range(8):solver.add(sum(zval(w)*actual_vector(lv,uv,ci,zval(t))[k] for (ci,t),w in zip(inv_atoms,weights))<0)
    status=solver.check();rec={'trial':trial+1,'solver_status':str(status),'weights':[str(w) for w in weights]}
    if status==z3.sat:
        model=solver.model();lo=[frac(model.eval(v,model_completion=True)) for v in lv];hi=[frac(model.eval(v,model_completion=True)) for v in uv]
        F=[sum(w*actual_vector(lo,hi,ci,t)[k] for (ci,t),w in zip(inv_atoms,weights)) for k in range(8)]
        if not all(v<0 for v in F):raise ValueError('CERTIFICATE_SIGN')
        if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
        if not all(sign*oe(lo,hi,t)[index]>0 for t,requirements in markers for index,sign in requirements):raise ValueError('MARKERS')
        if not all(sign*oe(lo,hi,t)[index]>0 for t,index,sign in inv_signs):raise ValueError('INVERSION')
        if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(lo,hi)):raise ValueError('STABILITY')
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
                    'support':[{'corner':ci,'t':str(t),'weight':str(w)} for (ci,t),w in zip(inv_atoms,weights)],'coefficient_sums':[str(v) for v in F]});inv_results.append(rec);break
    rec['status']='UNSAT_FIXED_WEIGHTS_ONLY' if status==z3.unsat else 'INCONCLUSIVE_'+solver.reason_unknown()
    inv_results.append(rec)
print('inversion-constrained rational box search:',{'trials':len(inv_results),'statuses':{s:sum(r['status']==s for r in inv_results) for s in set(r['status'] for r in inv_results)},
 'found':next((r for r in inv_results if r['status']=='STRICT_ACTUAL_BOX_CERTIFICATE'),None)})
