# Bounded limit-certificate search on the five newly designed contact triples.
# If negative, transfer to a strictly stable actual box and replay each sum.
from fractions import Fraction as Q
from math import lcm
ct_limit_results=[]
for candidate in ct_results['candidates'][1:]:
    widths=[Q(v) for v in candidate['halfwidths']];contacts=[Q(t) for t in candidate['contacts']]
    vertices=corners([cx_center[j]-widths[j] for j in range(7)],[cx_center[j]+widths[j] for j in range(7)])
    grid=set(Q(x) for x in (0,1,2,4,7,8,9,10,12,14,16,20,25,30,40,50,60,70,80,100))
    for t in contacts:grid.update((t-Q(1,10),t+Q(1,10)))
    atoms=[]
    for ci,a in enumerate(vertices):
        for t in sorted(grid):
            direct,den=pair_vector_t(a,t);atoms.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in direct]})
    atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for ci,t in zip((2,1,2),contacts):
        deriv=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);poly=pairing_polynomial(vertices[ci],unit)
            if sum(poly[j]*t**j for j in range(8))!=0:raise ValueError('CONTACT')
            deriv.append(sum(j*poly[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
        for sign in (1,-1):atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in deriv]})
    scale=lcm(*(v.denominator for a in atoms for v in a['vector']));C=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
    solution=exact_minimax(C,pivot_cap=2000);rec={'contacts':candidate['contacts'],'halfwidths':candidate['halfwidths'],'solver_status':solution['status'],'pivots':solution['pivots'],'atoms':len(atoms)}
    if solution['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';ct_limit_results.append(rec);continue
    optimum=solution['optimum']/scale;rec['margin']=str(optimum)
    if optimum>0:raise ValueError('TANGENT_PAIR')
    if optimum==0:rec['status']='NO_STRICT_LIMIT_CERTIFICATE_ON_GRID';rec['dual']=[str(x) for x in solution['dual']];ct_limit_results.append(rec);continue
    support=[(atom,w) for atom,w in zip(atoms,solution['lambda']) if w>0]
    vec=[sum(w*a['vector'][k] for a,w in support) for k in range(8)]
    if not all(v<0 for v in vec):raise ValueError('LIMIT_SIGN')
    rec['limit_support']=[{'kind':a['kind'],'corner':a['corner'],'t':str(a['t']) if a['t'] is not None else 'infinity','sign':a.get('sign'),'weight':str(w)} for a,w in support]
    rec['limit_coefficient_sums']=[str(v) for v in vec]
    for power in range(2,13):
        eps=Q(1,10**power);rho=1-eps**3
        actual=corners([cx_center[j]-rho*widths[j] for j in range(7)],[cx_center[j]+rho*widths[j] for j in range(7)])
        if not all(routh_ok(a) and integer_hurwitz(a) for a in actual):continue
        converted=[]
        for atom,w in support:
            if atom['kind']=='tangent':converted.append((atom['corner'],atom['t']+atom['sign']*eps,w/eps))
            elif atom['kind']=='physical':converted.append((atom['corner'],atom['t'],w))
            else:converted.append((None,None,w))
        coeff=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            coeff.append(sum(w*(independent_pair_t(actual[ci],unit,t)/(1+t)**7 if t is not None else unit[7]) for ci,t,w in converted))
        if all(v<0 for v in coeff):
            raw=[w/(1+t)**7 if t is not None else w for ci,t,w in converted];common=lcm(*(v.denominator for v in raw));integer_weights=[int(common*v) for v in raw]
            exact=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1)
                exact.append(sum(integer_weights[i]*(independent_pair_t(actual[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(converted)))
            if not all(v<0 for v in exact):raise ValueError('ACTUAL_CERTIFICATE')
            rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','rho':str(rho),'epsilon':str(eps),
             'actual_support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':integer_weights[i]} for i,(ci,t,w) in enumerate(converted)],
             'actual_coefficient_sums':[str(v) for v in exact]});break
    else:rec['status']='STRICT_LIMIT_ONLY_NO_TRANSFER_IN_BUDGET'
    ct_limit_results.append(rec)
    if rec['status']=='STRICT_ACTUAL_BOX_CERTIFICATE':break
print('bounded contact-triple limit search:',[{'contacts':r['contacts'],'status':r['status'],'margin':r.get('margin'),'pivots':r['pivots'],'rho':r.get('rho')} for r in ct_limit_results])
