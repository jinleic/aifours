# Exact rational simplification of the already discovered common numerator.
# Eval only; deterministic rounding is a proposal, never proof. Every accepted
# candidate must pass both de Casteljau and independent power-to-Bernstein checks.
from fractions import Fraction as Q
if endpoint_rounds[-1]['status']!='COMMON_NUMERATOR_PROVED':raise ValueError('NO_SOURCE_WITNESS')
source_b=[Q(x) for x in endpoint_rounds[-1]['numerator']]
rounding_denominators=[100,1000,10000,100000,1000000,10000000]
rounding_trials=[]
for den in rounding_denominators:
    b=[Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den) for x in source_b[:7]]+[Q(1)]
    rec={'denominator':den,'numerator':[str(x) for x in b]}
    if not all(x>0 for x in b):rec['status']='NONPOSITIVE_COEFFICIENT';rounding_trials.append(rec);continue
    polynomials=[pairing_polynomial(a,b) for a in cs]
    proofs=[whole_halfline(p,max_depth=32,max_nodes=4000) for p in polynomials]
    for i,proof in enumerate(proofs):
        if proof['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polynomials[i],max_depth=64,max_nodes=10000)
    rec['pairing_polynomials']=[[str(x) for x in p] for p in polynomials];rec['proofs']=proofs
    if all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in proofs):
        for p,proof in zip(polynomials,proofs):verify_leaves_by_power(p,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['independent_leaf_replay']=True
        rec['uniform_pairing_margin']=str(min(Q(x['margin']) for x in proofs))
        rounding_trials.append(rec);break
    rec['status']='NOT_CERTIFIED';rounding_trials.append(rec)
print('exact numerator simplification:',[{'denominator':x['denominator'],'status':x['status'],
 'numerator':x['numerator'],'pair_status':[p['status'] for p in x.get('proofs',[])],
 'margin':x.get('uniform_pairing_margin')} for x in rounding_trials])
