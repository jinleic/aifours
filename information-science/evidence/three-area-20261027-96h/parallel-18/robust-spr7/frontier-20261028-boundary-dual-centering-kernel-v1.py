# Exact centering of distinct max-margin numerators on the same actual box.
# This avoids the already refuted b_H/G affine line. Eval only, no floats.
if len(unperturbed_rounds)<3 or any('numerator' not in r for r in unperturbed_rounds):raise ValueError('THREE_NUMERATORS_REQUIRED')
centering_inputs=[[Q(x) for x in r['numerator']] for r in unperturbed_rounds[:3]]
centering_weights=[(Q(1,3),Q(1,3),Q(1,3)),(Q(0),Q(1,2),Q(1,2)),
                   (Q(1,4),Q(1,4),Q(1,2)),(Q(1,6),Q(1,3),Q(1,2)),
                   (Q(1,2),Q(1,4),Q(1,4))]
centering_results=[]
for weights in centering_weights:
    if sum(weights)!=1 or not all(x>=0 for x in weights):raise ValueError('WEIGHTS')
    b=[sum(weights[i]*centering_inputs[i][j] for i in range(3)) for j in range(8)]
    if b[7]!=1 or any(x<0 for x in b):raise ValueError('NUMERATOR')
    polys=[pairing_polynomial(a,b) for a in boundary_cs];certs=[]
    for poly in polys:
        proof=whole_halfline(poly,max_depth=32,max_nodes=4000)
        if proof['status']=='SUBDIVISION_CAP':proof=locate_strict_failure(poly,max_depth=64,max_nodes=10000)
        certs.append(proof)
    rec={'weights':[str(x) for x in weights],'numerator':[str(x) for x in b],
         'polynomials':[[str(x) for x in p] for p in polys],'proofs':certs}
    if all(x['status']=='STRICT_POSITIVITY' and 'leaves' in x for x in certs):
        for poly,proof in zip(polys,certs):verify_leaves_by_power(poly,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['independent_leaf_replay']=True
        rec['margin']=str(min(Q(x['margin']) for x in certs));centering_results.append(rec);break
    rec['status']='NOT_CERTIFIED';centering_results.append(rec)
print('boundary exact dual centering:',[{'weights':r['weights'],'status':r['status'],
 'proof_status':[x['status'] for x in r['proofs']],
 'exact_failure_t':[x.get('t') for x in r['proofs'] if x['status']=='NONPOSITIVE_EXACT'],
 'margin':r.get('margin')} for r in centering_results])
