# New representation: deterministic asymmetric boxes around six distinct
# stable conjugate-root centers. Bounded exact rational actual-atom search.
# No floating arithmetic, random floats, native optimizer or subprocess.
from fractions import Fraction as Q
from math import lcm
from random import Random
rng=Random(20261028)
profiles=[(1,((1,2),(1,5),(1,11))),(2,((1,3),(2,7),(1,13))),
          (3,((1,4),(1,9),(2,17))),(1,((2,3),(1,7),(2,12))),
          (2,((1,1),(1,6),(1,14))),(3,((2,5),(1,8),(1,15)))]
asym_results=[]
for real,pairs in profiles:
    nominal=center_from_factors(real,pairs);wl=[Q(rng.randrange(2,21),20) for _ in range(7)];wh=[Q(rng.randrange(2,21),20) for _ in range(7)]
    def box(r):return [nominal[j]*(1-r*wl[j]) for j in range(7)],[nominal[j]*(1+r*wh[j]) for j in range(7)]
    def stable(r):
        lo,hi=box(r)
        return all(0<lo[j]<hi[j] for j in range(7)) and all(routh_ok(a) for a in corners(lo,hi))
    low=Q(1,65536);rec={'real_root':real,'pairs':pairs,'lower_weights':[str(x) for x in wl],'upper_weights':[str(x) for x in wh]}
    if not stable(low):rec['status']='INITIAL_UNSTABLE';asym_results.append(rec);continue
    high=Q(1,4)
    if stable(high):low=high;high=None
    else:
        for _ in range(12):
            mid=(low+high)/2
            if stable(mid):low=mid
            else:high=mid
    lo,hi=box(low);vv=corners(lo,hi)
    if not all(integer_hurwitz(a) for a in vv):raise ValueError('STABILITY_MISMATCH')
    rec.update({'stable_scale':str(low),'next_checked_unstable_scale':str(high) if high else None,'lower':[str(x) for x in lo],'upper':[str(x) for x in hi]})
    grid={Q(0),Q(1,4),Q(1),Q(4)}
    for damping,w in pairs:grid.update((Q(w*w,4),Q(w*w),Q(4*w*w)))
    rounds=[]
    for it in range(2):
        atoms=[]
        for ci,a in enumerate(vv):
            for t in sorted(grid):
                vec,den=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,den)/(1+t)**7 for v in vec]))
        atoms.append((None,None,[Q(0)]*7+[Q(1)]))
        sc=lcm(*(v.denominator for atom in atoms for v in atom[2]));matrix=[[int(sc*atom[2][j]) for atom in atoms] for j in range(8)]
        sol=exact_minimax(matrix,pivot_cap=2000);row={'iteration':it+1,'nodes':[str(t) for t in sorted(grid)]+['infinity'],'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
        if sol['status']!='CERTIFIED_OPTIMUM':row['status']='PIVOT_CAP';rounds.append(row);break
        opt=sol['optimum']/sc;row['margin']=str(opt)
        if opt<=0:
            support=[]
            for i,w in enumerate(sol['lambda']):
                if w>0:
                    ci,t,_=atoms[i];support.append((ci,t,w/(1+t)**7 if t is not None else w))
            den=lcm(*(w.denominator for ci,t,w in support));weights=[int(den*w) for ci,t,w in support];sums=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1);sums.append(sum(weights[i]*(independent_pair_t(vv[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(support)))
            if any(v>0 for v in sums):raise ValueError('CERTIFICATE_REPLAY')
            row.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in sums]});rounds.append(row);break
        dual=sol['dual']
        if dual[0]<=0 or dual[7]<=0:raise ValueError('ENDPOINT')
        b=[v/dual[7] for v in dual];row['dual_monic']=[str(v) for v in b]
        for i,(ci,t,_) in enumerate(atoms):
            v=independent_pair_t(vv[ci],b,t)/(1+t)**7 if t is not None else b[7]
            if v<=0 or sum(b[k]*matrix[k][i] for k in range(8))!=sc*v:raise ValueError('GRID_DUAL')
        ps=[pairing_polynomial(a,b) for a in vv];proofs=[whole_halfline(p,max_depth=28,max_nodes=3500) for p in ps]
        for i,p in enumerate(proofs):
            if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=56,max_nodes=10000)
        if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
            for p,proof in zip(ps,proofs):verify_leaves_by_power(p,proof)
            row.update({'status':'COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(x) for x in p] for p in ps]});rounds.append(row);break
        add={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}-grid
        if not add:row['status']='NO_NEW_EXACT_VIOLATION';rounds.append(row);break
        row.update({'status':'ADDED_VIOLATING_NODES','new_nodes':[str(t) for t in sorted(add)]});rounds.append(row);grid.update(add)
    else:rounds[-1]['terminal']='TWO_ITERATION_LIMIT'
    rec['rounds']=rounds;rec['status']=rounds[-1]['status'];asym_results.append(rec)
    if rec['status']=='ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE':break
print('asymmetric exact actual-box search:',[{'pairs':r['pairs'],'status':r['status'],'scale':r.get('stable_scale'),
 'rounds':[{'atoms':s['atoms'],'pivots':s['pivots'],'status':s['status'],'terminal':s.get('terminal')} for s in r.get('rounds',[])]} for r in asym_results])
