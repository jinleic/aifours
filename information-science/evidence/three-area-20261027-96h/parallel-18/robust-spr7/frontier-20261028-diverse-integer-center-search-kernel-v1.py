# Bounded diverse-center actual-box search in Python Eval only.
# Five deterministic integer-root centers, exact width bracketing, and at most
# one exact normalized grid LP per center if its own numerator fails.
# No author checker, numerical optimizer, floats, subprocess or hidden fallback.
from fractions import Fraction as Q
from math import lcm

def root_product(roots):
    a=[Q(1)]
    for r in roots:
        nxt=[Q(0)]*(len(a)+1)
        for i,v in enumerate(a):nxt[i]+=r*v;nxt[i+1]+=v
        a=nxt
    if len(a)!=8 or a[-1]!=1:raise ValueError('CENTER')
    return a

def centered_box(a,r):return [a[j]*(1-r) for j in range(7)],[a[j]*(1+r) for j in range(7)]
def center_stability(a,r):
    lower,upper=centered_box(a,r)
    if not all(0<l<u for l,u in zip(lower,upper)):return False,[False]*4
    vv=corners(lower,upper);rr=[routh_ok(v) for v in vv];dd=[integer_hurwitz(v) for v in vv]
    if rr!=dd:raise ValueError('STABILITY_REPLAY_MISMATCH')
    return all(rr),rr

def center_frequency_grid(roots):
    mn=min(roots);mx=max(roots)
    values={Q(mn,2),Q(mn),Q(2*mn),Q(mx,4),Q(mx,2),Q(mx),Q(2*mx),Q(4*mx)}
    for i in range(1,33):
        if len(values)>=8:break
        values.add(Q(mx*i,9))
    return sorted(values)[:8]

profiles=[(1,1,2,3,5,8,13),(1,2,3,4,5,6,7),(1,1,1,2,5,8,13),
          (1,3,3,3,7,7,11),(1,2,4,8,16,32,64)]
diverse_results=[]
for roots in profiles:
    a=root_product(roots); low=Q(1,65536); ok,_=center_stability(a,low)
    if not ok:
        diverse_results.append({'roots':roots,'status':'INITIAL_WIDTH_UNSTABLE'});continue
    high=Q(1,4);high_ok,_=center_stability(a,high)
    if high_ok:low=high;high=None
    else:
        for _ in range(5):
            m=(low+high)/2;stable,_=center_stability(a,m)
            if stable:low=m
            else:high=m
    l,u=centered_box(a,low);vv=corners(l,u)
    rec={'roots':roots,'stable_halfwidth_ratio':str(low),'next_checked_unstable_ratio':str(high) if high is not None else None,
         'lower':[str(x) for x in l],'upper':[str(x) for x in u],'center':[str(x) for x in a]}
    polys=[pairing_polynomial(v,a) for v in vv];proofs=[whole_halfline(p,max_depth=28,max_nodes=2500) for p in polys]
    for i,p in enumerate(proofs):
        if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=50,max_nodes=5000)
    rec['center_proofs']=proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        rec['status']='CENTER_COMMON_NUMERATOR_PROVED';rec['margin']=str(min(Q(x['margin']) for x in proofs));diverse_results.append(rec);continue
    grid=sorted(set([Q(0)]+[w*w for w in center_frequency_grid(roots)]+[Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT']))
    atoms=[]
    for ci,v in enumerate(vv):
        for t in grid:
            direct,scale=pair_vector_t(v,t);atoms.append((ci,t,[Q(x,scale)/(1+t)**7 for x in direct]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(x.denominator for atom in atoms for x in atom[2]))
    C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=600);rec['grid_solver_status']=sol['status'];rec['pivots']=sol['pivots'];rec['grid_nodes']=[str(t) for t in grid]+['infinity']
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP_UNRESOLVED';diverse_results.append(rec);continue
    opt=sol['optimum'];rec['grid_margin']=str(opt/common)
    if opt<0:
        raw=[sol['lambda'][i]*Q(common)/(1+atom[1])**7 if atom[1] is not None else sol['lambda'][i]*common for i,atom in enumerate(atoms)]
        L=lcm(*(x.denominator for x in raw));weights=[int(L*x) for x in raw];sums=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            z=sum(weights[i]*(independent_pair_t(vv[atom[0]],unit,atom[1]) if atom[1] is not None else unit[7]) for i,atom in enumerate(atoms))
            if z>=0:raise ValueError('STRICT_CERTIFICATE_REPLAY')
            sums.append(str(z))
        rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','weights':weights,'strict_sums':sums});diverse_results.append(rec);break
    if opt==0:rec['status']='GRID_ZERO_MARGIN_UNRESOLVED';diverse_results.append(rec);continue
    dual=sol['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('ENDPOINT_DUAL')
    b=[x/dual[7] for x in dual]
    rec['grid_dual_numerator']=[str(x) for x in b]
    for i,(ci,t,vec) in enumerate(atoms):
        val=independent_pair_t(vv[ci],b,t)/(1+t)**7 if t is not None else b[7]
        if val<=0 or sum(b[k]*C[k][i] for k in range(8))!=common*val:raise ValueError('DUAL_GRID_REPLAY')
    ps=[pairing_polynomial(v,b) for v in vv];bp=[whole_halfline(p,max_depth=28,max_nodes=2500) for p in ps]
    for i,p in enumerate(bp):
        if p['status']=='SUBDIVISION_CAP':bp[i]=locate_strict_failure(ps[i],max_depth=50,max_nodes=5000)
    rec['dual_proofs']=bp
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in bp):
        for p,proof in zip(ps,bp):verify_leaves_by_power(p,proof)
        rec['status']='GRID_DUAL_COMMON_NUMERATOR_PROVED';rec['margin']=str(min(Q(x['margin']) for x in bp))
    else:rec['status']='NO_STRICT_GRID_CERTIFICATE_OR_GLOBAL_WITNESS'
    diverse_results.append(rec)
print('diverse-center exact search:',[{'roots':r['roots'],'status':r['status'],'stable_ratio':r.get('stable_halfwidth_ratio'),
 'next_unstable':r.get('next_checked_unstable_ratio'),'center_status':[x['status'] for x in r.get('center_proofs',[])],
 'grid_margin':r.get('grid_margin'),'pivots':r.get('pivots')} for r in diverse_results])
