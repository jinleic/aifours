# Interior-seeking rational feasibility for the boundary tangent constraints.
# Shift each physical/unit column by epsilon*(1,...,1), leave +/- tangent
# columns unshifted. A zero optimum yields D*b=0 and every physical/unit
# grid value >=epsilon for b>=0,sum(b)=1; a negative optimum only rules out
# that chosen finite-grid margin, not the original problem.
from fractions import Fraction as Q
from math import lcm

centered_grid=set(limit_adapt_grid);centered_rounds=[];centered_done=False
for outer in range(4):
    rows=[]
    for ci,a in enumerate(limit_cs):
        for t in sorted(centered_grid):
            vector,den=pair_vector_t(a,t);rows.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in vector]})
    rows.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for j in range(8):rows.append({'kind':'unit','corner':None,'t':None,'vector':[Q(int(k==j)) for k in range(8)]})
    rows.extend(row for row in limit_atoms if row['kind']=='tangent')
    for eps in (Q(1,10**6),Q(1,10**8),Q(1,10**10),Q(1,10**12),Q(1,10**14),Q(1,10**16),Q(1,10**18),Q(1,10**20)):
        vectors=[[v-eps if row['kind']!='tangent' else v for v in row['vector']] for row in rows]
        scale=lcm(*(x.denominator for row in vectors for x in row));C=[[int(scale*vectors[i][k]) for i in range(len(rows))] for k in range(8)]
        cs=exact_minimax(C,pivot_cap=2200)
        item={'outer':outer+1,'epsilon':str(eps),'atoms':len(rows),'pivots':cs['pivots'],'solver_status':cs['status']}
        if cs['status']!='CERTIFIED_OPTIMUM':item['status']='PIVOT_CAP';centered_rounds.append(item);centered_done=True;break
        opt=cs['optimum']/scale;item['margin']=str(opt)
        if opt<0:item['status']='MARGIN_TOO_LARGE_ON_CURRENT_GRID';centered_rounds.append(item);continue
        if opt!=0:raise ValueError('TANGENT_ZERO')
        dual=cs['dual']
        if any(v<eps for v in dual):raise ValueError('UNIT_MARGIN')
        for row in rows:
            val=sum(row['vector'][k]*dual[k] for k in range(8))
            if row['kind']=='tangent' and val!=0:raise ValueError('TANGENT_EQ')
            if row['kind']!='tangent' and val<eps:raise ValueError('PHYSICAL_MARGIN')
        item['dual']=[str(v) for v in dual];contacts={1:[Q(15)],2:[Q(3),Q(65)]};new=set();boundary_checks=[];allpolys=[]
        for ci,a in enumerate(limit_cs):
            poly=pairing_polynomial(a,dual);allpolys.append(poly);residual=poly
            for t in contacts.get(ci,[]):residual=quotient_by_root(quotient_by_root(residual,t),t)
            result=exact_nonnegative_halfline(residual);boundary_checks.append(result)
            if result['status']=='NEGATIVE':new.add(limit_badpoint(poly,residual,contacts.get(ci,[]),result))
            elif result['status']!='NONNEGATIVE_PROVED':item['status']='BOUNDARY_CHECK_CAP';item['boundary_checks']=boundary_checks;centered_rounds.append(item);centered_done=True;break
        if centered_done:break
        item['boundary_checks']=boundary_checks
        if not new:
            cp=pairing_polynomial(cx_center,dual);proof=whole_halfline(cp,max_depth=45,max_nodes=20000)
            if proof['status']=='STRICT_POSITIVITY' and 'leaves' in proof:
                verify_leaves_by_power(cp,proof)
                item.update({'status':'ONE_NUMERATOR_FOR_ALL_RHO_LT_ONE','center_proof':proof,'boundary_polynomials':[[str(v) for v in p] for p in allpolys]})
            else:item.update({'status':'BOUNDARY_NONNEGATIVE_CENTER_UNRESOLVED','center_proof':proof})
            centered_rounds.append(item);centered_done=True;break
        new-=centered_grid
        if not new:raise ValueError('NO_NEW_NODE')
        item.update({'status':'ADDED_BOUNDARY_NEGATIVE_NODES','new_nodes':[str(t) for t in sorted(new)]});centered_rounds.append(item);centered_grid.update(new);break
    else:centered_rounds[-1]['terminal']='EPSILON_LIMIT';centered_done=True
    if centered_done:break
else:centered_rounds[-1]['terminal']='FOUR_OUTER_LIMIT'
print('centered tangent cone exact result:',[{'outer':r['outer'],'epsilon':r['epsilon'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in centered_rounds])
