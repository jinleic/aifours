# Direct physical-atom probes on the two stable near-four-contact boxes.
# All arithmetic is exact; finite positive grid dual is not global positivity.
from fractions import Fraction as Q
from math import lcm
actual_near_results=[]
for candidate in nf_results:
    if candidate['status']!='NO_STRICT_LIMIT_CERTIFICATE_ON_GRID':continue
    widths=[Q(x) for x in candidate['halfwidths']];rho=Q(candidate['rho']);ts=[Q(x) for x in candidate['contacts']];xl,xr=[Q(x) for x in candidate['near_fourth_bracket']]
    lo=[cx_center[j]-rho*widths[j] for j in range(7)];hi=[cx_center[j]+rho*widths[j] for j in range(7)];vv=corners(lo,hi)
    if not all(routh_ok(a) and integer_hurwitz(a) for a in vv):raise ValueError('STABILITY')
    grid=set(Q(x) for x in (0,1,2,4,7,8,9,10,12,14,16,20,25,30,40,50,60,70,80,100))
    grid.update((xl,xr,(xl+xr)/2))
    for t in ts:grid.update((t-Q(1,10000),t,t+Q(1,10000)))
    history=[]
    for iteration in range(2):
        at=[]
        for ci,a in enumerate(vv):
            for t in sorted(grid):
                vec,den=pair_vector_t(a,t);at.append((ci,t,[Q(v,den)/(1+t)**7 for v in vec]))
        at.append((None,None,[Q(0)]*7+[Q(1)]))
        scale=lcm(*(v.denominator for atom in at for v in atom[2]));Cphys=[[int(scale*atom[2][k]) for atom in at] for k in range(8)]
        solphys=exact_minimax(Cphys,pivot_cap=2200);rec={'iteration':iteration+1,'nodes':[str(t) for t in sorted(grid)]+['infinity'],'atoms':len(at),'pivots':solphys['pivots'],'solver_status':solphys['status']}
        if solphys['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';history.append(rec);break
        optimum=solphys['optimum']/scale;rec['margin']=str(optimum)
        if optimum<=0:
            support=[]
            for i,w in enumerate(solphys['lambda']):
                if w>0:
                    ci,t,_=at[i];raw=w/(1+t)**7 if t is not None else w;support.append((ci,t,raw))
            common=lcm(*(w.denominator for ci,t,w in support));weights=[int(common*w) for ci,t,w in support];vec=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1)
                value=sum(weights[i]*(independent_pair_t(vv[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(support));vec.append(value)
            if any(v>0 for v in vec):raise ValueError('CERTIFICATE_REPLAY')
            rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in vec]});history.append(rec);break
        dual=solphys['dual']
        if dual[0]<=0 or dual[7]<=0:raise ValueError('ENDPOINT')
        b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
        for i,(ci,t,_) in enumerate(at):
            value=independent_pair_t(vv[ci],b,t)/(1+t)**7 if t is not None else b[7]
            if value<=0 or sum(b[k]*Cphys[k][i] for k in range(8))!=scale*value:raise ValueError('DUAL_GRID')
        polys=[pairing_polynomial(a,b) for a in vv];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in polys]
        for i,p in enumerate(proofs):
            if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=58,max_nodes=12000)
        if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
            for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
            rec.update({'status':'COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(x) for x in p] for p in polys]});history.append(rec);break
        added={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}-grid
        if not added:rec['status']='NO_NEW_EXACT_VIOLATION';history.append(rec);break
        rec.update({'status':'ADDED_VIOLATING_NODES','new_nodes':[str(t) for t in sorted(added)]});history.append(rec);grid.update(added)
    else:history[-1]['terminal']='TWO_ITERATION_LIMIT'
    actual_near_results.append({'contacts':candidate['contacts'],'rho':str(rho),'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],'rounds':history})
    if history[-1]['status']=='ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE':break
print('actual near-four physical probes:',[{'contacts':r['contacts'],'rounds':[{'iteration':s['iteration'],'atoms':s['atoms'],'pivots':s['pivots'],
 'status':s['status'],'margin':s.get('margin'),'new_nodes':s.get('new_nodes'),'terminal':s.get('terminal')} for s in r['rounds']]} for r in actual_near_results])
