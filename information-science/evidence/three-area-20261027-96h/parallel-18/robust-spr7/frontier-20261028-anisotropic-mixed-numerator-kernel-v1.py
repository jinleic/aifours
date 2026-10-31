# Exact new-numerator search only for the four eligible anisotropic cases with
# unresolved b* in the prior scan. Runs inside Python Eval, no native solver.
# Uses previously defined own kernels, and independently verifies each accepted
# Bernstein leaf by direct power-to-Bernstein conversion on its actual interval.

def verify_leaves_by_power(poly,proof):
    if proof['status']!='STRICT_POSITIVITY':return False
    q=[sum(poly[k]*((-1)**(n-k))*comb(7-k,n-k) for k in range(n+1)) for n in range(8)]
    leaves=sorted(proof['leaves'],key=lambda x:Q(x['left']))
    at=Q(0)
    for leaf in leaves:
        left,right=Q(leaf['left']),Q(leaf['right'])
        if left!=at or not left<right<=1:raise ValueError('LEAF_COVERAGE')
        d=[sum(q[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,8)) for j in range(8)]
        beta=[sum(d[j]*Q(comb(i,j),comb(7,j)) for j in range(i+1)) for i in range(8)]
        if beta!=[Q(v) for v in leaf['coefficients']] or not all(x>0 for x in beta):raise ValueError('LEAF_BERNSTEIN_REPLAY')
        at=right
    if at!=1:raise ValueError('LEAF_COVERAGE')
    return True

mix_weights=[Q(1,8),Q(1,4),Q(1,2),Q(3,4)]
mix_report=[]
for rec in aniso_report:
    if not rec['status'].startswith('GRID_'):continue
    lo=[Q(x) for x in rec['lower']];hi=[Q(x) for x in rec['upper']];cs=corners(lo,hi)
    dual=[Q(x) for x in rec['grid_dual']]
    if dual[7]<=0:raise ValueError('NONPOSITIVE_LEADING_GRID_DUAL')
    guide=[x/dual[7] for x in dual]
    trials=[]
    for eta in mix_weights:
        b=[(1-eta)*x+eta*y for x,y in zip(ray_b,guide)]
        if b[7]!=1 or not all(x>0 for x in b):raise ValueError('NUMERATOR_NORMALIZATION')
        polys=[pairing_polynomial(a,b) for a in cs]
        proofs=[whole_halfline(p) for p in polys]
        for i,p in enumerate(proofs):
            if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i])
        success=all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs)
        if success:
            for p,cert in zip(polys,proofs):verify_leaves_by_power(p,cert)
        trials.append({'eta':str(eta),'numerator':[str(x) for x in b],
            'pairing_polynomials':[[str(x) for x in p] for p in polys], 'proofs':proofs,
            'independent_leaf_replay':success})
        if success:break
    mix_report.append({'wide':rec['wide'],'narrow_j':rec['narrow_j'],'lower':rec['lower'],'upper':rec['upper'],
        'corner_hurwitz':rec['corner_hurwitz'],'trials':trials,
        'status':'COMMON_NUMERATOR_PROVED' if success else 'NOT_RESOLVED_BY_FOUR_MIXTURES'})
print('exact mixed-numerator summary:',[{'wide':r['wide'],'narrow_j':r['narrow_j'],'status':r['status'],
  'trials':[{'eta':x['eta'],'status':[p['status'] for p in x['proofs']],
   'negatives':[p.get('t') for p in x['proofs'] if p['status']=='NONPOSITIVE_EXACT']} for x in r['trials']]} for r in mix_report])
