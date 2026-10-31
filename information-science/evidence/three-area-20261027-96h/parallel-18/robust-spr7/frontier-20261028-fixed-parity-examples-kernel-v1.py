# Exact illustrative fixed-parity boxes contained in the five-contact family.
# Search for explicit epsilon; every candidate is checked at all frequencies.
from fractions import Fraction as Q
rho=Q(1,2)
base_lo=[fcenter[j]-rho*(fu[j]-fl[j])/2 for j in range(7)]
base_hi=[fcenter[j]+rho*(fu[j]-fl[j])/2 for j in range(7)]
fixed_parity=[]
for fixed in ('odd','even'):
    lo=base_lo[:];hi=base_hi[:]
    for j in (1,3,5) if fixed=='odd' else (0,2,4,6):lo[j]=hi[j]=fcenter[j]
    vertices=corners(lo,hi)
    if not all(routh_ok(a) and integer_hurwitz(a) for a in vertices):raise ValueError('STABILITY')
    for k in range(1,11):
        eps=Q(1,10**k)
        if fixed=='odd':
            # O(t)=57-123t/2+31t²/2-t³; zeta=1/2; F=(t-zeta)O'.
            b=[eps*Q(123,4),Q(57),eps*77,Q(123,2),eps*Q(65,2),Q(31,2),eps*3,Q(1)]
        else:
            # E fixed at center, G=-E'-eta*t³, eta=1/10000.
            eta=Q(1,10000)
            b=[fcenter[0],eps*fcenter[2],fcenter[2],eps*2*fcenter[4],fcenter[4],eps*3*fcenter[6],fcenter[6],eps*eta]
        ps=[pairing_polynomial(a,b) for a in vertices];proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in ps]
        rec={'fixed':fixed,'epsilon':str(eps),'eta':str(Q(1,10000)) if fixed=='even' else None,'zeta':'1/2' if fixed=='odd' else None,
             'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],'numerator':[str(x) for x in b],'pairing_polynomials':[[str(x) for x in p] for p in ps],'proofs':proofs}
        if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
            for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
            rec.update({'status':'COMMON_NUMERATOR_PROVED','margin':str(min(Q(p['margin']) for p in proofs))});fixed_parity.append(rec);break
    else:fixed_parity.append({'fixed':fixed,'status':'EPSILON_LIMIT'})
print('fixed-parity exact examples:',[{'fixed':r['fixed'],'status':r['status'],'epsilon':r.get('epsilon'),'eta':r.get('eta'),
 'zeta':r.get('zeta'),'numerator':r.get('numerator'),'leaves':[len(p.get('leaves',[])) for p in r.get('proofs',[])],'margin':r.get('margin')} for r in fixed_parity])
