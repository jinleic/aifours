# Bounded exact zero-plus-five-contact search. The boundary includes a0=0;
# at rho<1 all five sign markers and positive a0 establish strict stability.
# At t=0 the one-sided P derivative is included ONLY with positive sign.
from fractions import Fraction as Q
from math import lcm

def six_box(design):
    t1,t2,t3,t4,t5,r6,r1s,qs,_,_=design;q=Q(qs)
    em=root_cubic([Q(0),Q(t3),Q(t4)],q);ep=root_cubic([Q(t1),Q(t2),Q(t5)],Q(1))
    om=root_cubic([Q(t1),Q(t4),Q(t5)],Q(1));op=root_cubic([Q(t2),Q(t3),Q(r6)],Q(1))
    lo=[em[0],om[0],-ep[1],-op[1],em[2],om[2],-ep[3]];hi=[ep[0],op[0],-em[1],-om[1],ep[2],op[2],-em[3]]
    if lo[0]!=0 or not all(lo[j]<hi[j] for j in range(7)) or not all(lo[j]>0 for j in range(1,7)):raise ValueError('BOX')
    center=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)];verts=corners(lo,hi)
    contacts=[(2,Q(t1)),(3,Q(t2)),(1,Q(t3)),(0,Q(t4)),(2,Q(t5))]
    if not all(parity(verts[ci],t)==(Q(0),Q(0)) for ci,t in contacts):raise ValueError('CONTACT')
    if not parity(verts[0],Q(0))[0]==0 or not parity(verts[1],Q(0))[0]==0:raise ValueError('ZERO')
    return lo,hi,center,verts,contacts

six_results=[]
for design in six_design[:20]:
    lo,hi,c0,vertices,contacts=six_box(design)
    grid={Q(1,10000),Q(1,1000),Q(1,100),Q(1,10),Q(1,2),Q(3,2),Q(5,2),Q(4),Q(5),Q(7),Q(9),Q(12),Q(16)}
    for ci,t in contacts:grid.update((t-Q(1,10),t+Q(1,10)))
    atoms=[]
    for ci,a in enumerate(vertices):
        for t in sorted(grid):
            vec,den=pair_vector_t(a,t);v=[Q(z,den)/(1+t)**7 for z in vec]
            if any(v):atoms.append({'kind':'physical','corner':ci,'t':t,'vector':v})
    atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for ci,t in contacts:
        D=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);p=pairing_polynomial(vertices[ci],unit)
            if sum(p[j]*t**j for j in range(8))!=0:raise ValueError('CONTACT_ZERO')
            D.append(sum(j*p[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
        for sign in (1,-1):atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in D]})
    for ci in (0,1):
        D=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);p=pairing_polynomial(vertices[ci],unit)
            if p[0]!=0:raise ValueError('ZERO_PAIR')
            D.append(p[1])
        atoms.append({'kind':'zero_tangent','corner':ci,'t':Q(0),'sign':1,'vector':D})
    scale=lcm(*(v.denominator for a in atoms for v in a['vector']));C6=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
    sol6=exact_minimax(C6,pivot_cap=2400);rec={'design':[str(x) for x in design[:8]],'lower':[str(x) for x in lo],
      'upper':[str(x) for x in hi],'atoms':len(atoms),'pivots':sol6['pivots'],'solver_status':sol6['status']}
    if sol6['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';six_results.append(rec);continue
    opt=sol6['optimum']/scale;rec['margin']=str(opt)
    if opt>0:raise ValueError('TANGENT_PAIR')
    witness=None
    if opt<0:witness=sol6['lambda'];rec['limit_kind']='STRICT_NEGATIVE'
    else:
        dual=sol6['dual'];rec['dual_signs']=[0 if v==0 else 1 for v in dual]
        for k,v in enumerate(dual):
            if v==0:
                fs=face_probe(C6,k,pivot_cap=2500)
                if fs['status']=='NEGATIVE_FACE_WITNESS':witness=fs['weights'];rec['limit_kind']='WEAK_NONPOSITIVE';break
    if witness is None:rec['status']='NO_NEGATIVE_LIMIT_CERTIFICATE_ON_GRID';six_results.append(rec);continue
    support=[(a,w) for a,w in zip(atoms,witness) if w>0];vals=[sum(w*a['vector'][k] for a,w in support) for k in range(8)]
    if not all(v<=0 for v in vals) or not any(v<0 for v in vals):raise ValueError('LIMIT_WITNESS')
    rec['limit_support']=[{'kind':a['kind'],'corner':a['corner'],'t':str(a['t']) if a['t'] is not None else 'infinity','sign':a.get('sign'),'weight':str(w)} for a,w in support]
    rec['limit_coefficient_sums']=[str(v) for v in vals]
    for power in range(2,13):
        eps=Q(1,10**power);rho=1-eps**3
        lower=[c0[j]-rho*(hi[j]-lo[j])/2 for j in range(7)];upper=[c0[j]+rho*(hi[j]-lo[j])/2 for j in range(7)];actual=corners(lower,upper)
        if not all(routh_ok(a) and integer_hurwitz(a) for a in actual):continue
        converted=[]
        for a,w in support:
            if a['kind']=='tangent':converted.append((a['corner'],a['t']+a['sign']*eps,w/eps))
            elif a['kind']=='zero_tangent':converted.append((a['corner'],eps,w/eps))
            elif a['kind']=='physical':converted.append((a['corner'],a['t'],w))
            else:converted.append((None,None,w))
        F=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);F.append(sum(w*(independent_pair_t(actual[ci],unit,t)/(1+t)**7 if t is not None else unit[7]) for ci,t,w in converted))
        if all(v<=0 for v in F):
            raw=[w/(1+t)**7 if t is not None else w for ci,t,w in converted];common=lcm(*(v.denominator for v in raw));weights=[int(common*v) for v in raw];check=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1);check.append(sum(weights[i]*(independent_pair_t(actual[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(converted)))
            if any(v>0 for v in check):raise ValueError('ACTUAL_CERT')
            rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','rho':str(rho),'epsilon':str(eps),'actual_lower':[str(x) for x in lower],
             'actual_upper':[str(x) for x in upper],'actual_support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(converted)],'actual_coefficient_sums':[str(v) for v in check]});break
    else:rec['status']='LIMIT_ONLY_TRANSFER_NOT_FOUND'
    six_results.append(rec)
    if rec['status']=='ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE':break
print('zero-plus-five-contact bounded search:',[{'design':r['design'],'status':r['status'],'margin':r.get('margin'),
 'dual_signs':r.get('dual_signs'),'pivots':r['pivots'],'kind':r.get('limit_kind'),'rho':r.get('rho')} for r in six_results])
