# Exact minimax/linear-box alternation with both parity inversions forced.
# A finite-grid positive dual and an optimizer fixed point are not full results.
from fractions import Fraction as Q
from math import lcm
import z3
origin_lo=[Q(x) for x in five_frozen['boundary_lower']];origin_hi=[Q(x) for x in five_frozen['boundary_upper']]
center=[(origin_lo[j]+origin_hi[j])/2 for j in range(7)];rho=Q(999,1000)
lo=[center[j]-rho*(origin_hi[j]-origin_lo[j])/2 for j in range(7)];hi=[center[j]+rho*(origin_hi[j]-origin_lo[j])/2 for j in range(7)]
inv_alt=[]
for iteration in range(4):
    atoms=[(ci,t,[v/(1+t)**7 for v in actual_vector(lo,hi,ci,t)]) for ci,t in inv_atoms]
    scale=lcm(*(v.denominator for atom in atoms for v in atom[2]));C=[[int(scale*a[2][k]) for a in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1600);rec={'iteration':iteration+1,'atom_status':sol['status'],'atom_pivots':sol['pivots']}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';inv_alt.append(rec);break
    opt=sol['optimum']/scale;rec['grid_margin']=str(opt)
    lam=sol['lambda']
    if opt<=0:weights=[w/(1+t)**7 for w,(_,t,_) in zip(lam,atoms)]
    else:
        eta=Q(1,10000);weights=[((1-eta)*w+eta/Q(len(atoms)))/(1+t)**7 for w,(_,t,_) in zip(lam,atoms)]
    F=[sum(w*actual_vector(lo,hi,ci,t)[k] for (ci,t,_),w in zip(atoms,weights)) for k in range(8)]
    if opt<=0:
        if not all(v<=0 for v in F):raise ValueError('CERTIFICATE')
        rec.update({'status':'ACTUAL_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
         'support':[{'corner':ci,'t':str(t),'weight':str(w)} for (ci,t,_),w in zip(atoms,weights) if w>0],'coefficient_sums':[str(v) for v in F]});inv_alt.append(rec);break
    lv=[z3.Real('ival_l%d_%d'%(iteration,j)) for j in range(7)];uv=[z3.Real('ival_u%d_%d'%(iteration,j)) for j in range(7)];bound=z3.Real('ival_b%d'%iteration)
    S=z3.Optimize();S.set(timeout=10000)
    for j in range(7):S.add(lv[j]>=zval(Q(1,10**6)),uv[j]-lv[j]>=zval(Q(1,10**6)),uv[j]<=zval(1000))
    for t,req in markers:
        for idx,sgn in req:S.add(sgn*oe(lv,uv,zval(t))[idx]>=zval(Q(1,10**10)*(1+t)**3))
    for t,idx,sgn in inv_signs:S.add(sgn*oe(lv,uv,zval(t))[idx]>=zval(Q(1,10**10)*(1+t)**3))
    for k in range(8):S.add(sum(zval(w)*actual_vector(lv,uv,ci,zval(t))[k] for (ci,t,_),w in zip(atoms,weights))<=bound)
    S.minimize(bound);status=S.check();rec['box_status']=str(status)
    if status!=z3.sat:rec['status']='BOX_'+str(status);inv_alt.append(rec);break
    model=S.model();nlo=[frac(model.eval(v,model_completion=True)) for v in lv];nhi=[frac(model.eval(v,model_completion=True)) for v in uv]
    if not all(0<nlo[j]<nhi[j] for j in range(7)):raise ValueError('BOX')
    if not all(sgn*oe(nlo,nhi,t)[idx]>0 for t,req in markers for idx,sgn in req):raise ValueError('MARKER')
    if not all(sgn*oe(nlo,nhi,t)[idx]>0 for t,idx,sgn in inv_signs):raise ValueError('INVERSION')
    if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(nlo,nhi)):raise ValueError('STABILITY')
    F=[sum(w*actual_vector(nlo,nhi,ci,t)[k] for (ci,t,_),w in zip(atoms,weights)) for k in range(8)]
    rec.update({'box_bound':str(max(F)),'lower':[str(x) for x in nlo],'upper':[str(x) for x in nhi],
      'support':[{'corner':ci,'t':str(t),'weight':str(w)} for (ci,t,_),w in zip(atoms,weights)],'coefficient_sums':[str(v) for v in F]})
    if max(F)<=0:rec['status']='ACTUAL_CERTIFICATE';inv_alt.append(rec);break
    rec['status']='NO_CERTIFICATE_ON_FIXED_WEIGHTS';inv_alt.append(rec)
    if nlo==lo and nhi==hi:rec['terminal']='EXACT_FIXED_POINT';break
    lo,hi=nlo,nhi
else:inv_alt[-1]['terminal']='FOUR_ITERATION_LIMIT'
print('inversion-seeded exact alternation:',[{'iteration':r['iteration'],'status':r['status'],'grid_margin':r.get('grid_margin'),
 'box_bound':r.get('box_bound'),'box_status':r.get('box_status'),'terminal':r.get('terminal')} for r in inv_alt])
