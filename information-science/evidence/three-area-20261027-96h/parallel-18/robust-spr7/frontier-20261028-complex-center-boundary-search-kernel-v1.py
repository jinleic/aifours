# Bounded exact search over five explicitly listed complex-root centers.
# Eval-only, rational arithmetic, no native optimizer or numerical roots.
from fractions import Fraction as Q
from math import lcm

def center_from_factors(real_root,pairs):
    poly=[Q(real_root),Q(1)]
    for damping,frequency in pairs:
        poly=conv_exact(poly,[Q(damping*damping+frequency*frequency),Q(2*damping),Q(1)])
    if len(poly)!=8 or poly[-1]!=1:raise ValueError('CENTER')
    return poly

def fast_stable(a,r):
    lower,upper=centered_box(a,r)
    if not all(0<l<u for l,u in zip(lower,upper)):return False
    return all(routh_ok(v) for v in corners(lower,upper))

def complex_grid(pairs):
    frequencies={Q(1,2),Q(1),Q(2)}
    for damping,frequency in pairs:
        frequencies.update((Q(frequency,2),Q(frequency),Q(2*frequency)))
    return sorted(frequencies)

complex_profiles=[(1,((1,1),(1,2),(1,4))),(1,((1,2),(1,4),(1,8))),
 (1,((1,3),(2,5),(1,9))),(2,((1,4),(2,8),(1,16))),
 (1,((1,1),(1,3),(1,8)))]
complex_results=[]
for real_root,pairs in complex_profiles:
    center=center_from_factors(real_root,pairs);low=Q(1,65536)
    rec={'real_root':real_root,'pairs':pairs,'center':[str(x) for x in center]}
    if not fast_stable(center,low):rec['status']='INITIAL_WIDTH_UNSTABLE';complex_results.append(rec);continue
    high=Q(1,4)
    if fast_stable(center,high):low=high;high=None
    else:
        for _ in range(10):
            mid=(low+high)/2
            if fast_stable(center,mid):low=mid
            else:high=mid
    lower,upper=centered_box(center,low);vertices=corners(lower,upper)
    if not all(integer_hurwitz(v) for v in vertices):raise ValueError('INDEPENDENT_STABILITY_REPLAY')
    rec.update({'stable_halfwidth_ratio':str(low),'next_checked_unstable_ratio':str(high) if high is not None else None,
                'lower':[str(x) for x in lower],'upper':[str(x) for x in upper]})
    polys=[pairing_polynomial(v,center) for v in vertices]
    proofs=[whole_halfline(p,max_depth=28,max_nodes=2500) for p in polys]
    for i,p in enumerate(proofs):
        if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=50,max_nodes=5000)
    rec['center_proofs']=proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        rec['status']='CENTER_COMMON_NUMERATOR_PROVED';rec['margin']=str(min(Q(x['margin']) for x in proofs));complex_results.append(rec);continue
    grid=sorted(set([Q(0)]+[w*w for w in complex_grid(pairs)]+[Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT']))
    atoms=[]
    for ci,v in enumerate(vertices):
        for t in grid:
            direct,scale=pair_vector_t(v,t);atoms.append((ci,t,[Q(x,scale)/(1+t)**7 for x in direct]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(x.denominator for atom in atoms for x in atom[2]));C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1000);rec['grid_status']=sol['status'];rec['pivots']=sol['pivots'];rec['grid_nodes']=[str(x) for x in grid]+['infinity']
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP_UNRESOLVED';complex_results.append(rec);continue
    opt=sol['optimum'];rec['grid_margin']=str(opt/common)
    if opt<0:
        raw=[sol['lambda'][i]*Q(common)/(1+atom[1])**7 if atom[1] is not None else sol['lambda'][i]*common for i,atom in enumerate(atoms)]
        L=lcm(*(x.denominator for x in raw));weights=[int(L*x) for x in raw];sums=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            value=sum(weights[i]*(independent_pair_t(vertices[atom[0]],unit,atom[1]) if atom[1] is not None else unit[7]) for i,atom in enumerate(atoms))
            if value>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(value))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','weights':weights,'strict_sums':sums});complex_results.append(rec);break
    if opt==0:rec['status']='GRID_ZERO_MARGIN_UNRESOLVED';complex_results.append(rec);continue
    dual=sol['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT_DUAL')
    b=[x/dual[7] for x in dual];rec['grid_dual_numerator']=[str(x) for x in b]
    for i,(ci,t,vec) in enumerate(atoms):
        v=independent_pair_t(vertices[ci],b,t)/(1+t)**7 if t is not None else b[7]
        if v<=0 or sum(b[k]*C[k][i] for k in range(8))!=common*v:raise ValueError('DUAL_GRID_REPLAY')
    bp=[pairing_polynomial(v,b) for v in vertices];bp_proofs=[whole_halfline(p,max_depth=28,max_nodes=2500) for p in bp]
    for i,p in enumerate(bp_proofs):
        if p['status']=='SUBDIVISION_CAP':bp_proofs[i]=locate_strict_failure(bp[i],max_depth=50,max_nodes=5000)
    rec['dual_proofs']=bp_proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in bp_proofs):
        for p,proof in zip(bp,bp_proofs):verify_leaves_by_power(p,proof)
        rec['status']='GRID_DUAL_COMMON_NUMERATOR_PROVED';rec['margin']=str(min(Q(x['margin']) for x in bp_proofs))
    else:rec['status']='NO_STRICT_GRID_CERTIFICATE_OR_GLOBAL_WITNESS'
    complex_results.append(rec)
print('complex-center exact search:',[{'real_root':r['real_root'],'pairs':r['pairs'],'status':r['status'],
 'stable_ratio':r.get('stable_halfwidth_ratio'),'next_unstable':r.get('next_checked_unstable_ratio'),
 'center_status':[x['status'] for x in r.get('center_proofs',[])],'grid_margin':r.get('grid_margin'),'pivots':r.get('pivots')} for r in complex_results])
