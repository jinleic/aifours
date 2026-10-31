# Four bounded direct actual-atom LP probes on different five-contact designs.
# Exact physical nodes only; all candidate denominators are four-corner checked.
from fractions import Fraction as Q
from math import lcm
five_actual_results=[]
for idx in (0,100,200,350):
    design=five_design[idx];lo1,hi1,center,bc,contacts=five_box(design);rho=1-Q(1,10**9)
    lo=[center[j]-rho*(hi1[j]-lo1[j])/2 for j in range(7)];hi=[center[j]+rho*(hi1[j]-lo1[j])/2 for j in range(7)];vertices=corners(lo,hi)
    if not all(routh_ok(a) and integer_hurwitz(a) for a in vertices):raise ValueError('STABILITY')
    grid={Q(0),Q(1,2),Q(3,2),Q(5,2),Q(4),Q(5),Q(7),Q(9),Q(12),Q(16),Q(25)}
    for ci,t in contacts:grid.update((t-Q(1,1000),t,t+Q(1,1000),t-Q(1,10000),t+Q(1,10000)))
    rounds=[]
    for iteration in range(2):
        atoms=[]
        for ci,a in enumerate(vertices):
            for t in sorted(grid):
                if t<0:continue
                vec,den=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,den)/(1+t)**7 for v in vec]))
        atoms.append((None,None,[Q(0)]*7+[Q(1)]))
        scale=lcm(*(v.denominator for a in atoms for v in a[2]));CM=[[int(scale*a[2][k]) for a in atoms] for k in range(8)]
        solA=exact_minimax(CM,pivot_cap=2200);rec={'iteration':iteration+1,'nodes':[str(t) for t in sorted(grid)]+['infinity'],'atoms':len(atoms),'pivots':solA['pivots'],'solver_status':solA['status']}
        if solA['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';rounds.append(rec);break
        opt=solA['optimum']/scale;rec['margin']=str(opt)
        if opt<=0:
            support=[]
            for i,w in enumerate(solA['lambda']):
                if w>0:
                    ci,t,_=atoms[i];support.append((ci,t,w/(1+t)**7 if t is not None else w))
            den=lcm(*(w.denominator for ci,t,w in support));weights=[int(den*w) for ci,t,w in support];sums=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1);sums.append(sum(weights[i]*(independent_pair_t(vertices[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(support)))
            if any(v>0 for v in sums):raise ValueError('CERTIFICATE_SIGN')
            rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in sums]});rounds.append(rec);break
        dual=solA['dual']
        if dual[0]<=0 or dual[7]<=0:raise ValueError('ENDPOINT')
        b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
        for i,(ci,t,_) in enumerate(atoms):
            v=independent_pair_t(vertices[ci],b,t)/(1+t)**7 if t is not None else b[7]
            if v<=0 or sum(b[k]*CM[k][i] for k in range(8))!=scale*v:raise ValueError('GRID_DUAL')
        polys=[pairing_polynomial(a,b) for a in vertices];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in polys]
        for i,p in enumerate(proofs):
            if p['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(polys[i],max_depth=58,max_nodes=12000)
        if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
            for p,proof in zip(polys,proofs):verify_leaves_by_power(p,proof)
            rec.update({'status':'COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(x) for x in p] for p in polys]});rounds.append(rec);break
        add={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}-grid
        if not add:rec['status']='NO_NEW_EXACT_VIOLATION';rounds.append(rec);break
        rec.update({'status':'ADDED_VIOLATING_NODES','new_nodes':[str(t) for t in sorted(add)]});rounds.append(rec);grid.update(add)
    else:rounds[-1]['terminal']='TWO_ITERATION_LIMIT'
    five_actual_results.append({'design_index':idx,'design':[str(v) for v in design[:8]],'rho':str(rho),'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],'rounds':rounds})
    if rounds[-1]['status']=='ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE':break
print('five-contact actual atom searches:',[{'index':r['design_index'],'design':r['design'],'rounds':[{'atoms':s['atoms'],'pivots':s['pivots'],'status':s['status'],'margin':s.get('margin'),'new_nodes':s.get('new_nodes'),'terminal':s.get('terminal')} for s in r['rounds']]} for r in five_actual_results])
