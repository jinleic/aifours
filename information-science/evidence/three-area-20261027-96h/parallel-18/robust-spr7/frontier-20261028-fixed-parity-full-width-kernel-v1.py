# Expand every formerly fixed parity coefficient by rational radius 1e-8.
# General compactified bound and independent direct corner proofs, exact only.
from fractions import Fraction as Q
fp_expanded=[];radius=Q(1,10**8)
for ex in fixed_parity:
    if ex['status']!='COMMON_NUMERATOR_PROVED':raise ValueError('SOURCE')
    fixed=(1,3,5) if ex['fixed']=='odd' else (0,2,4,6)
    lo=[Q(x) for x in ex['lower']];hi=[Q(x) for x in ex['upper']];b=[Q(x) for x in ex['numerator']]
    for j in fixed:lo[j]-=radius;hi[j]+=radius
    if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('NOT_FULL_WIDTH')
    B=sum(abs(x) for x in b);delta0=Q(ex['margin']);delta=delta0-len(fixed)*radius*B
    if delta<=0:raise ValueError('MARGIN')
    cs=corners(lo,hi)
    if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('HURWITZ')
    polys=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=45,max_nodes=20000) for p in polys]
    if not all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):raise ValueError('PAIRING_PROOF')
    for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
    S=1+sum(hi)
    fp_expanded.append({'fixed':ex['fixed'],'radius':str(radius),'lower':[str(v) for v in lo],'upper':[str(v) for v in hi],
       'numerator':[str(v) for v in b],'B':str(B),'original_margin':str(delta0),'perturbation_bound':str(len(fixed)*radius*B),
       'extended_margin':str(delta),'coefficient_sum_bound':str(S),'ratio_margin':str(delta/S**2),
       'direct_pairing_polynomials':[[str(v) for v in p] for p in polys],'direct_proofs':proofs,
       'direct_margin':str(min(Q(p['margin']) for p in proofs))})
print('full-width exact parity neighborhoods:',[{'fixed':r['fixed'],'radius':r['radius'],'B':r['B'],'delta0':r['original_margin'],
 'perturbation_bound':r['perturbation_bound'],'delta':r['extended_margin'],'ratio':r['ratio_margin'],
 'direct_leaf_counts':[len(p['leaves']) for p in r['direct_proofs']],'direct_margin':r['direct_margin']} for r in fp_expanded])
