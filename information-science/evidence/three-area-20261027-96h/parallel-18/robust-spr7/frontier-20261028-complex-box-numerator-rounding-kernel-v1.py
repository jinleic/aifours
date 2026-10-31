# Exact rational rounding; accepted numerator must replay on all four corners.
from fractions import Fraction as Q
if cx_cone_rounds[-1]['status']!='COMMON_NUMERATOR_PROVED':raise ValueError('NO_SOURCE_NUMERATOR')
cx_source=[Q(x) for x in cx_cone_rounds[-1]['numerator']];cx_round=[]
for den in (100,1000,10000,100000,1000000,10000000,100000000):
    b=[Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den) for x in cx_source[:7]]+[Q(1)]
    rec={'denominator':den,'numerator':[str(x) for x in b]}
    if not all(x>0 for x in b):rec['status']='NONPOSITIVE_COEFFICIENT';cx_round.append(rec);continue
    ps=[pairing_polynomial(a,b) for a in cx_cs];proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in ps]
    for i,p in enumerate(proofs):
        if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=64,max_nodes=10000)
    rec['pairing_polynomials']=[[str(x) for x in p] for p in ps];rec['proofs']=proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
        for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['margin']=str(min(Q(p['margin']) for p in proofs));cx_round.append(rec);break
    rec['status']='NOT_CERTIFIED';cx_round.append(rec)
print('complex-box exact rounding:',[{'denominator':r['denominator'],'status':r['status'],'numerator':r['numerator'],
      'pair_status':[p['status'] for p in r.get('proofs',[])],'margin':r.get('margin')} for r in cx_round])
