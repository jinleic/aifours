# Exact rational rounding for the already found second-box numerator.
# Eval-only; each accepted proof receives independent direct Bernstein replay.
if harder_rounds[-1]['status']!='COMMON_NUMERATOR_PROVED':raise ValueError('NO_SOURCE_WITNESS')
harder_source_b=[Q(x) for x in harder_rounds[-1]['numerator']]
harder_denoms=[100,1000,10000,100000,1000000,10000000]
harder_rounding=[]
for den in harder_denoms:
    b=[Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den) for x in harder_source_b[:7]]+[Q(1)]
    rec={'denominator':den,'numerator':[str(x) for x in b]}
    if not all(x>0 for x in b):rec['status']='NONPOSITIVE_COEFFICIENT';harder_rounding.append(rec);continue
    polys=[pairing_polynomial(a,b) for a in harder_cs]
    proofs=[whole_halfline(p,max_depth=32,max_nodes=4000) for p in polys]
    for i,proof in enumerate(proofs):
        if proof['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=64,max_nodes=10000)
    rec['pairing_polynomials']=[[str(x) for x in p] for p in polys];rec['proofs']=proofs
    if all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in proofs):
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['independent_leaf_replay']=True
        rec['uniform_pairing_margin']=str(min(Q(x['margin']) for x in proofs))
        harder_rounding.append(rec);break
    rec['status']='NOT_CERTIFIED';harder_rounding.append(rec)
print('harder-box simplified numerator:',[{'denominator':x['denominator'],'status':x['status'],
 'numerator':x['numerator'],'proofs':[p['status'] for p in x.get('proofs',[])],
 'margin':x.get('uniform_pairing_margin')} for x in harder_rounding])
