# Exact rounding of Bernstein inner-cone result on actual boundary box.
# Eval-only; every accepted candidate receives an independent exact leaf replay.
if adaptive_bern[-1]['status']!='COMMON_NUMERATOR_PROVED':raise ValueError('NO_SOURCE_WITNESS')
bound_source=[Q(x) for x in adaptive_bern[-1]['numerator']]
bound_denoms=[100,1000,10000,100000,1000000,10000000,100000000]
bound_round=[]
for den in bound_denoms:
    b=[Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den) for x in bound_source[:7]]+[Q(1)]
    rec={'denominator':den,'numerator':[str(x) for x in b]}
    if not all(x>0 for x in b):rec['status']='NONPOSITIVE_COEFFICIENT';bound_round.append(rec);continue
    ps=[pairing_polynomial(a,b) for a in boundary_cs]
    proofs=[whole_halfline(p,max_depth=40,max_nodes=10000) for p in ps]
    for i,x in enumerate(proofs):
        if x['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=64,max_nodes=10000)
    rec['pairing_polynomials']=[[str(x) for x in p] for p in ps];rec['proofs']=proofs
    if all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in proofs):
        for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['independent_leaf_replay']=True
        rec['uniform_pairing_margin']=str(min(Q(x['margin']) for x in proofs));bound_round.append(rec);break
    rec['status']='NOT_CERTIFIED';bound_round.append(rec)
print('boundary simplified numerator:',[{'denominator':r['denominator'],'status':r['status'],'numerator':r['numerator'],
 'pair_status':[p['status'] for p in r.get('proofs',[])],'margin':r.get('uniform_pairing_margin')} for r in bound_round])
