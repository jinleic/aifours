# Bounded exact search: tune E+ to the right endpoint of a rational bracket
# on the remaining O+ root, creating a near-fourth boundary contact.
# Strict limiting certificates are transferred to actual stable boxes.
from fractions import Fraction as Q
from math import lcm
nf_results=[]
for candidate in ct_results['candidates']:
    ts=[Q(t) for t in candidate['contacts']];old=[Q(v) for v in candidate['halfwidths']]
    op=[cx_center[1]+old[1],-cx_center[3]+old[3],cx_center[5]+old[5],Q(-1)]
    left=ts[0];right=None
    for j in range(1,65):
        r=ts[0]+(ts[1]-ts[0])*Q(j,64)
        if cx_eval(op,r)<0:right=r;break
        left=r
    if right is None:continue
    for _ in range(20):
        mid=(left+right)/2
        if cx_eval(op,mid)>0:left=mid
        else:right=mid
    t4=right;base=quad_interpolate(ts,[abs(cx_eval(ct_E,t)) for t in ts]);slope=quad_interpolate(ts,[-t**3 for t in ts])
    A=sum(base[j]*t4**j for j in range(3));B=sum(slope[j]*t4**j for j in range(3))+t4**3
    if not B or cx_eval(ct_E,t4)>=0:continue
    x=(-cx_eval(ct_E,t4)-A)/B;ev=[base[j]+slope[j]*x for j in range(3)]+[x]
    widths=[ev[0],old[1],ev[1],old[3],ev[2],old[5],ev[3]]
    if not all(0<widths[j]<cx_center[j] for j in range(7)):continue
    rho=1-Q(1,10**9);actual=corners([cx_center[j]-rho*widths[j] for j in range(7)],[cx_center[j]+rho*widths[j] for j in range(7)])
    rec={'contacts':[str(t) for t in ts],'near_fourth_bracket':[str(left),str(right)],'halfwidths':[str(v) for v in widths],'rho':str(rho)}
    if not all(routh_ok(a) and integer_hurwitz(a) for a in actual):rec['status']='ACTUAL_BOX_UNSTABLE';nf_results.append(rec);continue
    vertices=corners([cx_center[j]-widths[j] for j in range(7)],[cx_center[j]+widths[j] for j in range(7)])
    if parity(vertices[3],t4)[0]!=0 or not cx_eval(op,left)>0>cx_eval(op,right):raise ValueError('NEAR_CONTACT')
    grid=set(Q(v) for v in (0,1,2,4,7,8,9,10,12,14,16,20,25,30,40,50,60,70,80,100))
    grid.update((left,right,left-Q(1,1000),right+Q(1,1000)))
    atoms=[]
    for ci,a in enumerate(vertices):
        for t in sorted(grid):
            vec,den=pair_vector_t(a,t);atoms.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in vec]})
    atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for ci,t in zip((2,1,2),ts):
        D=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);poly=pairing_polynomial(vertices[ci],unit)
            if sum(poly[j]*t**j for j in range(8))!=0:raise ValueError('EXACT_CONTACT')
            D.append(sum(j*poly[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
        for sign in (1,-1):atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in D]})
    scale=lcm(*(v.denominator for a in atoms for v in a['vector']));C=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
    solution=exact_minimax(C,pivot_cap=2400);rec.update({'solver_status':solution['status'],'pivots':solution['pivots'],'atoms':len(atoms)})
    if solution['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';nf_results.append(rec);continue
    opt=solution['optimum']/scale;rec['margin']=str(opt)
    if opt>0:raise ValueError('TANGENT_PAIR')
    if opt==0:rec['status']='NO_STRICT_LIMIT_CERTIFICATE_ON_GRID';rec['dual']=[str(v) for v in solution['dual']];nf_results.append(rec);continue
    support=[(a,w) for a,w in zip(atoms,solution['lambda']) if w>0];vals=[sum(w*a['vector'][k] for a,w in support) for k in range(8)]
    if not all(v<0 for v in vals):raise ValueError('LIMIT_SIGN')
    rec['limit_support']=[{'kind':a['kind'],'corner':a['corner'],'t':str(a['t']) if a['t'] is not None else 'infinity','sign':a.get('sign'),'weight':str(w)} for a,w in support]
    rec['limit_coefficient_sums']=[str(v) for v in vals]
    for power in range(2,15):
        eps=Q(1,10**power);rho=1-eps**3;ac=corners([cx_center[j]-rho*widths[j] for j in range(7)],[cx_center[j]+rho*widths[j] for j in range(7)])
        if not all(routh_ok(a) and integer_hurwitz(a) for a in ac):continue
        converted=[]
        for a,w in support:
            if a['kind']=='tangent':converted.append((a['corner'],a['t']+a['sign']*eps,w/eps))
            elif a['kind']=='physical':converted.append((a['corner'],a['t'],w))
            else:converted.append((None,None,w))
        vals=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);vals.append(sum(w*(independent_pair_t(ac[ci],unit,t)/(1+t)**7 if t is not None else unit[7]) for ci,t,w in converted))
        if all(v<0 for v in vals):
            raw=[w/(1+t)**7 if t is not None else w for ci,t,w in converted];common=lcm(*(v.denominator for v in raw));weights=[int(common*v) for v in raw]
            exact=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1);exact.append(sum(weights[i]*(independent_pair_t(ac[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(converted)))
            if not all(v<0 for v in exact):raise ValueError('ACTUAL_CERTIFICATE')
            rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','rho':str(rho),'epsilon':str(eps),
             'actual_support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(converted)],'actual_coefficient_sums':[str(v) for v in exact]});break
    else:rec['status']='STRICT_LIMIT_ONLY_NO_TRANSFER_IN_BUDGET'
    nf_results.append(rec)
    if rec['status']=='STRICT_ACTUAL_BOX_CERTIFICATE':break
print('near-four-contact exact search:',[{'contacts':r['contacts'],'status':r['status'],'margin':r.get('margin'),'pivots':r.get('pivots'),'atoms':r.get('atoms'),'rho':r['rho']} for r in nf_results])
