# Actual stable box with three independently targeted near-critical gaps.
# Exact rational frequency exchange; no native optimizers or approximate values.
from fractions import Fraction as Q
from math import lcm
if threegap['shrunk_stable']!=1:raise ValueError('NO_DESIGNED_BOX')
tg_box=threegap['candidates'][0];tg_lo=[Q(v) for v in tg_box['lower']];tg_hi=[Q(v) for v in tg_box['upper']]
tg_cs=corners(tg_lo,tg_hi)
if not all(0<l<u for l,u in zip(tg_lo,tg_hi)) or not all(routh_ok(a) and integer_hurwitz(a) for a in tg_cs):raise ValueError('NOT_ELIGIBLE_BOX')
tg_grid={Q(0),Q(3),Q(15),Q(65)};tg_rounds=[]
for iteration in range(6):
    atoms=[]
    for ci,a in enumerate(tg_cs):
        for t in sorted(tg_grid):
            vector,den=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,den)/(1+t)**7 for v in vector]))
    atoms.append((None,None,[Q(0)]*7+[Q(1)]))
    common=lcm(*(v.denominator for atom in atoms for v in atom[2]));C=[[int(common*atom[2][k]) for atom in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1800)
    record={'iteration':iteration+1,'nodes':[str(x) for x in sorted(tg_grid)]+['infinity'],'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
    if sol['status']!='CERTIFIED_OPTIMUM':record['status']='PIVOT_CAP';tg_rounds.append(record);break
    opt=sol['optimum'];record['margin']=str(opt/common)
    if opt<=0:
        support=[]
        for i,w in enumerate(sol['lambda']):
            if w>0:
                ci,t,_=atoms[i];raw=w*common/(1+t)**7 if t is not None else w*common;support.append((ci,t,raw))
        scale=lcm(*(v.denominator for ci,t,v in support));weights=[int(scale*v) for ci,t,v in support];sums=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            value=sum(weights[i]*(independent_pair_t(tg_cs[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,v) in enumerate(support))
            if value>0:raise ValueError('CERTIFICATE_SIGN')
            sums.append(str(value))
        record.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,v) in enumerate(support)],'coefficient_sums':sums});tg_rounds.append(record);break
    dual=sol['dual']
    if dual[7]<=0 or dual[0]<=0:raise ValueError('DUAL_ENDPOINT')
    b=[v/dual[7] for v in dual];record['numerator']=[str(v) for v in b]
    for i,(ci,t,_) in enumerate(atoms):
        val=independent_pair_t(tg_cs[ci],b,t)/(1+t)**7 if t is not None else b[7]
        if val<=0 or sum(b[k]*C[k][i] for k in range(8))!=common*val:raise ValueError('GRID_DUAL')
    polys=[pairing_polynomial(a,b) for a in tg_cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=3500) for p in polys]
    for i,p in enumerate(proofs):
        if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=56,max_nodes=12000)
    record['proofs']=proofs
    if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
        for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
        record['status']='COMMON_NUMERATOR_PROVED';record['pairing_polynomials']=[[str(x) for x in p] for p in polys];record['pairing_margin']=str(min(Q(p['margin']) for p in proofs));tg_rounds.append(record);break
    new={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}-tg_grid
    if not new:record['status']='NO_NEW_EXACT_VIOLATION';tg_rounds.append(record);break
    record['new_nodes']=[str(t) for t in sorted(new)];record['status']='ADDED_VIOLATING_FREQUENCIES';tg_rounds.append(record);tg_grid.update(new)
else:tg_rounds[-1]['terminal']='SIX_ITERATION_LIMIT'
print('three-gap physical atom search:',[{'iteration':r['iteration'],'nodes':len(r['nodes']),'atoms':r['atoms'],'pivots':r['pivots'],
  'status':r['status'],'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in tg_rounds])
