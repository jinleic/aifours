# Exact limited search for a strict atom obstruction on analytically designed
# FIVE-contact rational boxes. The five contact points alternate E/O root-band
# boundaries; any actual certificate is rechecked on a rho<1 stable box.
from fractions import Fraction as Q
from math import lcm

def root_cubic(roots,scale):
    out=[Q(1)]
    for r in roots:
        nxt=[Q(0)]*(len(out)+1)
        for j,v in enumerate(out):nxt[j]-=r*v;nxt[j+1]+=v
        out=nxt
    return [-scale*v for v in out]

def five_box(design):
    t1,t2,t3,t4,t5,r6,r1s,qs,_,_=design;r1=Q(r1s);q=Q(qs)
    em=root_cubic([r1,Q(t3),Q(t4)],q);ep=root_cubic([Q(t1),Q(t2),Q(t5)],Q(1))
    om=root_cubic([Q(t1),Q(t4),Q(t5)],Q(1));op=root_cubic([Q(t2),Q(t3),Q(r6)],Q(1))
    lo=[em[0],om[0],-ep[1],-op[1],em[2],om[2],-ep[3]]
    hi=[ep[0],op[0],-em[1],-om[1],ep[2],op[2],-em[3]]
    if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('FIVE_BOX')
    center=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)]
    boundary=corners(lo,hi);contacts=[(2,Q(t1)),(3,Q(t2)),(1,Q(t3)),(0,Q(t4)),(2,Q(t5))]
    if not all(parity(boundary[ci],t)==(Q(0),Q(0)) for ci,t in contacts):raise ValueError('CONTACT')
    return lo,hi,center,boundary,contacts

five_limit_results=[]
for design in five_design[:12]:
    lo,hi,c0,vertices,contacts=five_box(design)
    grid={Q(0),Q(1,2),Q(3,2),Q(5,2),Q(4),Q(5),Q(7),Q(9),Q(12),Q(16)}
    for ci,t in contacts:grid.update((t-Q(1,10),t+Q(1,10)))
    atoms=[]
    for ci,a in enumerate(vertices):
        for t in sorted(grid):
            if t<0:continue
            vec,den=pair_vector_t(a,t);v=[Q(z,den)/(1+t)**7 for z in vec]
            if any(v):atoms.append({'kind':'physical','corner':ci,'t':t,'vector':v})
    atoms.append({'kind':'infinity','corner':None,'t':None,'vector':[Q(0)]*7+[Q(1)]})
    for ci,t in contacts:
        D=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);poly=pairing_polynomial(vertices[ci],unit)
            if sum(poly[j]*t**j for j in range(8))!=0:raise ValueError('CONTACT_ZERO')
            D.append(sum(j*poly[j]*t**(j-1) for j in range(1,8))/(1+t)**7)
        for sign in (1,-1):atoms.append({'kind':'tangent','corner':ci,'t':t,'sign':sign,'vector':[sign*v for v in D]})
    scale=lcm(*(v.denominator for a in atoms for v in a['vector']));Cfive=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
    solfive=exact_minimax(Cfive,pivot_cap=2000);rec={'design':[str(x) for x in design[:8]],'lower':[str(x) for x in lo],
       'upper':[str(x) for x in hi],'atoms':len(atoms),'pivots':solfive['pivots'],'solver_status':solfive['status']}
    if solfive['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';five_limit_results.append(rec);continue
    opt=solfive['optimum']/scale;rec['margin']=str(opt)
    if opt>0:raise ValueError('TANGENT_PAIR')
    witness=None
    if opt<0:
        witness=[w for w in solfive['lambda']];rec['limit_kind']='STRICT_NEGATIVE'
    else:
        dual=solfive['dual'];rec['dual_signs']=[0 if x==0 else 1 for x in dual]
        for k,v in enumerate(dual):
            if v==0:
                face=face_probe(Cfive,k,pivot_cap=2000)
                if face['status']=='NEGATIVE_FACE_WITNESS':witness=face['weights'];rec['limit_kind']='WEAK_NONPOSITIVE_NEGATIVE_COORDINATE';break
    if witness is None:
        rec['status']='NO_NEGATIVE_LIMIT_CERTIFICATE_ON_GRID';five_limit_results.append(rec);continue
    support=[(a,w) for a,w in zip(atoms,witness) if w>0]
    vals=[sum(w*a['vector'][k] for a,w in support) for k in range(8)]
    if not all(v<=0 for v in vals) or not any(v<0 for v in vals):raise ValueError('LIMIT_WITNESS')
    rec['limit_support']=[{'kind':a['kind'],'corner':a['corner'],'t':str(a['t']) if a['t'] is not None else 'infinity','sign':a.get('sign'),'weight':str(w)} for a,w in support]
    rec['limit_coefficient_sums']=[str(v) for v in vals]
    for power in range(2,13):
        eps=Q(1,10**power);rho=1-eps**3
        lower=[c0[j]-rho*(hi[j]-lo[j])/2 for j in range(7)];upper=[c0[j]+rho*(hi[j]-lo[j])/2 for j in range(7)];actual=corners(lower,upper)
        if not all(routh_ok(a) and integer_hurwitz(a) for a in actual):continue
        conv=[]
        for a,w in support:
            if a['kind']=='tangent':conv.append((a['corner'],a['t']+a['sign']*eps,w/eps))
            elif a['kind']=='physical':conv.append((a['corner'],a['t'],w))
            else:conv.append((None,None,w))
        f=[]
        for k in range(8):
            unit=[Q(0)]*8;unit[k]=Q(1);f.append(sum(w*(independent_pair_t(actual[ci],unit,t)/(1+t)**7 if t is not None else unit[7]) for ci,t,w in conv))
        if all(v<=0 for v in f):
            raw=[w/(1+t)**7 if t is not None else w for ci,t,w in conv];mult=lcm(*(v.denominator for v in raw));weight=[int(mult*v) for v in raw];check=[]
            for k in range(8):
                unit=[Q(0)]*8;unit[k]=Q(1);check.append(sum(weight[i]*(independent_pair_t(actual[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(conv)))
            if any(v>0 for v in check):raise ValueError('ACTUAL_CERTIFICATE')
            rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','rho':str(rho),'epsilon':str(eps),'actual_lower':[str(x) for x in lower],
             'actual_upper':[str(x) for x in upper],'actual_support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weight[i]} for i,(ci,t,w) in enumerate(conv)],
             'actual_coefficient_sums':[str(v) for v in check]});break
    else:rec['status']='LIMIT_ONLY_TRANSFER_NOT_FOUND'
    five_limit_results.append(rec)
    if rec['status']=='ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE':break
print('five-contact limit certificate probes:',[{'design':r['design'],'status':r['status'],'margin':r.get('margin'),
 'dual_signs':r.get('dual_signs'),'pivots':r['pivots'],'limit_kind':r.get('limit_kind'),'rho':r.get('rho')} for r in five_limit_results])
