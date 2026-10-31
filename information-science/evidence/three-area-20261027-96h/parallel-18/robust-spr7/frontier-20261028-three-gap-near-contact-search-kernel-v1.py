# Bounded exact actual-atom search for the proven-stable three-gap family at
# rho=999999/1000000. Initial rational nodes straddle each contact. Eval only.
from fractions import Fraction as Q
from math import lcm
tg2_r=Q(999999,1000000);tg2_lo=[cx_center[j]-tg2_r*hh[j] for j in range(7)];tg2_hi=[cx_center[j]+tg2_r*hh[j] for j in range(7)];tg2_cs=corners(tg2_lo,tg2_hi)
if not all(0<tg2_lo[j]<tg2_hi[j] for j in range(7)) or not all(routh_ok(a) and integer_hurwitz(a) for a in tg2_cs):raise ValueError('NOT_STABLE')
tg2_grid={Q(0),Q(1,3),Q(1),Q(17,2),Q(30),Q(100)}
for t in (Q(3),Q(15),Q(65)):
    tg2_grid.update((t-Q(1,1000),t,t+Q(1,1000)))
tg2_rounds=[]
for iteration in range(4):
    atoms=[]
    for ci,a in enumerate(tg2_cs):
        for t in sorted(tg2_grid):
            vector,den=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,den)/(1+t)**7 for v in vector]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(v.denominator for atom in atoms for v in atom[2]));C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol2=exact_minimax(C,pivot_cap=1600)
    rec={'iteration':iteration+1,'nodes':[str(x) for x in sorted(tg2_grid)]+['infinity'],'atoms':len(atoms),'pivots':sol2['pivots'],'solver_status':sol2['status']}
    if sol2['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';tg2_rounds.append(rec);break
    opt=sol2['optimum'];rec['margin']=str(opt/common)
    if opt<=0:
        support=[]
        for i,w in enumerate(sol2['lambda']):
            if w>0:
                ci,t,_=atoms[i];raw=w*common/(1+t)**7 if t is not None else w*common;support.append((ci,t,raw))
        scale=lcm(*(v.denominator for ci,t,v in support));weights=[int(scale*v) for ci,t,v in support];sums=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            val=sum(weights[i]*(independent_pair_t(tg2_cs[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,v) in enumerate(support))
            if val>0:raise ValueError('CERTIFICATE_SIGN')
            sums.append(str(val))
        rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,v) in enumerate(support)],'coefficient_sums':sums});tg2_rounds.append(rec);break
    dual=sol2['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('DUAL_ENDPOINT')
    b=[v/dual[7] for v in dual];rec['numerator']=[str(v) for v in b]
    for i,(ci,t,_) in enumerate(atoms):
        val=independent_pair_t(tg2_cs[ci],b,t)/(1+t)**7 if t is not None else b[7]
        if val<=0 or sum(b[k]*C[k][i] for k in range(8))!=common*val:raise ValueError('GRID_DUAL')
    polys=[pairing_polynomial(a,b) for a in tg2_cs];proofs=[whole_halfline(p,max_depth=30,max_nodes=4000) for p in polys]
    for i,p in enumerate(proofs):
        if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=60,max_nodes=15000)
    rec['proofs']=proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        rec['status']='COMMON_NUMERATOR_PROVED';rec['pairing_polynomials']=[[str(x) for x in p] for p in polys];rec['pairing_margin']=str(min(Q(p['margin']) for p in proofs));tg2_rounds.append(rec);break
    new={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}-tg2_grid
    if not new:rec['status']='NO_NEW_EXACT_VIOLATION';tg2_rounds.append(rec);break
    rec['new_nodes']=[str(t) for t in sorted(new)];rec['status']='ADDED_VIOLATING_FREQUENCIES';tg2_rounds.append(rec);tg2_grid.update(new)
else:tg2_rounds[-1]['terminal']='FOUR_ITERATION_LIMIT'
print('near-contact physical atom search:',[{'iteration':r['iteration'],'nodes':len(r['nodes']),'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in tg2_rounds])
