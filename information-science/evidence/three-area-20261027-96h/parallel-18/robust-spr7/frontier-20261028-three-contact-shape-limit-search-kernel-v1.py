# Bounded exact limit-obstruction search on four different admissible shapes
# with the same three boundary contacts. A strict limiting certificate, if
# found, is transferred to an explicitly stable rho<1 and replayed there.
from fractions import Fraction as Q
from math import lcm
shape_grid=[Q(x) for x in (0,1,2,4,7,8,9,10,12,14,16,20,25,30,40,50,60,70,80,100)]
shape_results=[]
for fraction in (Q(1,100),Q(1,4),Q(3,4),Q(99,100)):
    x=iv[0]+fraction*(iv[1]-iv[0]);ev=[ebase[k]+eder[k]*x for k in range(3)]+[x]
    widths=[ev[0],hh[1],ev[1],hh[3],ev[2],hh[5],ev[3]]
    if not all(0<widths[j]<cx_center[j] for j in range(7)):raise ValueError('WIDTH')
    lo=[cx_center[j]-widths[j] for j in range(7)];hi=[cx_center[j]+widths[j] for j in range(7)];vertices=corners(lo,hi)
    atoms=[]
    for ci,a in enumerate(vertices):
        for t in shape_grid:
            direct,den=pair_vector_t(a,t);atoms.append({'kind':'physical','corner':ci,'t':t,'vector':[Q(v,den)/(1+t)**7 for v in direct]})
    atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for ci,t in ((2,Q(3)),(1,Q(15)),(2,Q(65))):
        deriv=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);poly=pairing_polynomial(vertices[ci],unit)
            if sum(poly[j]*t**j for j in range(8))!=0:raise ValueError('CONTACT')
            deriv.append(sum(j*poly[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
        for sign in (1,-1):atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in deriv]})
    scale=lcm(*(v.denominator for a in atoms for v in a['vector']));C=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
    solshape=exact_minimax(C,pivot_cap=2000);rec={'fraction':str(fraction),'h6':str(x),'widths':[str(v) for v in widths],
      'solver_status':solshape['status'],'pivots':solshape['pivots'],'atoms':len(atoms)}
    if solshape['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';shape_results.append(rec);continue
    optimum=solshape['optimum']/scale;rec['margin']=str(optimum)
    if optimum>0:raise ValueError('TANGENT_ZERO')
    if optimum==0:rec['status']='NO_STRICT_LIMIT_CERTIFICATE_ON_GRID';rec['dual']=[str(v) for v in solshape['dual']];shape_results.append(rec);continue
    support=[(atom,w) for atom,w in zip(atoms,solshape['lambda']) if w>0]
    sums=[sum(w*atom['vector'][k] for atom,w in support) for k in range(8)]
    if not all(v<0 for v in sums):raise ValueError('LIMIT_SIGN')
    rec['limit_support']=[{'kind':a['kind'],'corner':a['corner'],'t':str(a['t']) if a['t'] is not None else 'infinity','sign':a.get('sign'),'weight':str(w)} for a,w in support]
    rec['limit_coefficient_sums']=[str(v) for v in sums]
    for power in range(2,13):
        eps=Q(1,10**power);rho=1-eps**3
        vlo=[cx_center[j]-rho*widths[j] for j in range(7)];vhi=[cx_center[j]+rho*widths[j] for j in range(7)];actual=corners(vlo,vhi)
        if not all(routh_ok(a) and integer_hurwitz(a) for a in actual):continue
        converted=[]
        for atom,w in support:
            if atom['kind']=='tangent':converted.append((atom['corner'],atom['t']+atom['sign']*eps,w/eps))
            elif atom['kind']=='physical':converted.append((atom['corner'],atom['t'],w))
            else:converted.append((None,None,w))
        actual_F=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1)
            z=sum(w*(independent_pair_t(actual[ci],unit,t)/(1+t)**7 if t is not None else unit[7]) for ci,t,w in converted);actual_F.append(z)
        if all(z<0 for z in actual_F):
            raw=[w/(1+t)**7 if t is not None else w for ci,t,w in converted];common=lcm(*(v.denominator for v in raw));integer_weights=[int(common*v) for v in raw]
            replay=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1)
                v=sum(integer_weights[i]*(independent_pair_t(actual[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(converted));replay.append(v)
            if not all(v<0 for v in replay):raise ValueError('ACTUAL_CERTIFICATE')
            rec.update({'status':'STRICT_ACTUAL_BOX_CERTIFICATE','rho':str(rho),'epsilon':str(eps),'lower':[str(v) for v in vlo],'upper':[str(v) for v in vhi],
             'actual_support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':integer_weights[i]} for i,(ci,t,w) in enumerate(converted)],
             'actual_coefficient_sums':[str(v) for v in replay]});break
    else:rec['status']='STRICT_LIMIT_ONLY_NO_TRANSFER_IN_BUDGET'
    shape_results.append(rec)
    if rec['status']=='STRICT_ACTUAL_BOX_CERTIFICATE':break
print('shape limit exact search:',[{'fraction':r['fraction'],'status':r['status'],'margin':r.get('margin'),'pivots':r['pivots'],'rho':r.get('rho')} for r in shape_results])
