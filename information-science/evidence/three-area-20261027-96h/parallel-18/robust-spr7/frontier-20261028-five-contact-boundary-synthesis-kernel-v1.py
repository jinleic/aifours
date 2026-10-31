# Exact five-tangency inner feasibility and full boundary pairing test.
# Positive output is a numerator for ALL rho<1 of one analytically stable
# five-contact box family; finite-grid failures are not global no-gos.
from fractions import Fraction as Q
from math import lcm
fl,fu,fcenter,fvertices,fcontacts=five_box(five_design[0])
fgrid={Q(0),Q(1,2),Q(3,2),Q(5,2),Q(4),Q(5),Q(7),Q(9),Q(12),Q(16)}
for ci,t in fcontacts:fgrid.update((t-Q(1,10),t+Q(1,10)))
ftang=[]
for ci,t in fcontacts:
    D=[]
    for k in range(8):
        unit=[Q(0)]*8;unit[k]=Q(1);p=pairing_polynomial(fvertices[ci],unit)
        if sum(p[j]*t**j for j in range(8))!=0:raise ValueError('CONTACT')
        D.append(sum(j*p[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
    for sign in (-1,1):ftang.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*x for x in D]})
froots={ci:[] for ci in range(4)}
for ci,t in fcontacts:froots[ci].append(t)
fsolve_rounds=[];fdone=False
for outer in range(6):
    rows=[]
    for ci,a in enumerate(fvertices):
        for t in sorted(fgrid):
            if t<0:continue
            vec,den=pair_vector_t(a,t);v=[Q(x,den)/(1+t)**7 for x in vec]
            if any(v):rows.append({'kind':'physical','vector':v})
    rows.append({'kind':'infinity','vector':[Q(0)]*7+[Q(1)]})
    for j in range(8):rows.append({'kind':'unit','vector':[Q(int(k==j)) for k in range(8)]})
    rows.extend(ftang)
    for eps in (Q(1,10**6),Q(1,10**8),Q(1,10**10),Q(1,10**12),Q(1,10**14),Q(1,10**16)):
        vectors=[[v-eps if row['kind']!='tangent' else v for v in row['vector']] for row in rows]
        sc=lcm(*(x.denominator for row in vectors for x in row));Ccent=[[int(sc*vectors[i][k]) for i in range(len(rows))] for k in range(8)]
        sl=exact_minimax(Ccent,pivot_cap=2000);rec={'outer':outer+1,'epsilon':str(eps),'atoms':len(rows),'pivots':sl['pivots'],'solver_status':sl['status']}
        if sl['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';fsolve_rounds.append(rec);fdone=True;break
        opt=sl['optimum']/sc;rec['margin']=str(opt)
        if opt<0:rec['status']='MARGIN_TOO_LARGE_ON_GRID';fsolve_rounds.append(rec);continue
        if opt!=0:raise ValueError('TANGENT_PAIR')
        b=sl['dual']
        if any(v<eps for v in b):raise ValueError('UNIT_MARGIN')
        for row in rows:
            val=sum(row['vector'][k]*b[k] for k in range(8))
            if (row['kind']=='tangent' and val!=0) or (row['kind']!='tangent' and val<eps):raise ValueError('GRID_MARGIN')
        rec['numerator']=[str(v) for v in b];checks=[];polys=[];new=set()
        for ci,a in enumerate(fvertices):
            p=pairing_polynomial(a,b);polys.append(p);res=p
            for t in froots[ci]:res=quotient_by_root(quotient_by_root(res,t),t)
            result=exact_nonnegative_halfline(res,maxdepth=38,maxnodes=14000);checks.append(result)
            if result['status']=='NEGATIVE':
                t=Q(result['t']);value=sum(p[j]*t**j for j in range(8))
                if value>=0:
                    if t not in froots[ci]:raise ValueError('RESIDUAL_SIGN')
                    t=next((t+sign*Q(1,2**k) for k in range(1,61) for sign in (-1,1) if t+sign*Q(1,2**k)>=0 and sum(p[j]*(t+sign*Q(1,2**k))**j for j in range(8))<0),None)
                    if t is None:raise ValueError('NO_NEAR_CONTACT_NEGATIVE')
                new.add(t)
            elif result['status']!='NONNEGATIVE_PROVED':rec['status']='BOUNDARY_CHECK_CAP';rec['boundary_checks']=checks;fsolve_rounds.append(rec);fdone=True;break
        if fdone:break
        rec['boundary_checks']=checks
        if not new:
            cp=pairing_polynomial(fcenter,b);proof=whole_halfline(cp,max_depth=45,max_nodes=18000)
            if proof['status']=='STRICT_POSITIVITY' and 'leaves' in proof:
                verify_leaves_by_power(cp,proof);rec.update({'status':'ALL_RHO_LT_ONE_COMMON_NUMERATOR','center_proof':proof,'boundary_polynomials':[[str(x) for x in p] for p in polys]})
            else:rec.update({'status':'BOUNDARY_NONNEGATIVE_CENTER_UNRESOLVED','center_proof':proof})
            fsolve_rounds.append(rec);fdone=True;break
        new-=fgrid
        if not new:raise ValueError('NO_NEW_NODE')
        rec.update({'status':'ADDED_BOUNDARY_NEGATIVE_NODES','new_nodes':[str(t) for t in sorted(new)]});fsolve_rounds.append(rec);fgrid.update(new);break
    else:fsolve_rounds[-1]['terminal']='EPSILON_LIMIT';fdone=True
    if fdone:break
else:fsolve_rounds[-1]['terminal']='SIX_OUTER_LIMIT'
print('five-contact full boundary synthesis:',[{'outer':r['outer'],'epsilon':r['epsilon'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in fsolve_rounds])
