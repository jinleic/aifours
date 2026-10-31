# Inversion-bearing joint search with rational snapping to bound bit growth.
# Every snapped box, support and coefficient sum is checked exactly.
from fractions import Fraction as Q
from math import lcm
import z3
olo=[Q(x) for x in five_frozen['boundary_lower']];ohi=[Q(x) for x in five_frozen['boundary_upper']];center=[(olo[j]+ohi[j])/2 for j in range(7)];rho=Q(999,1000)
seedlo=[center[j]-rho*(ohi[j]-olo[j])/2 for j in range(7)];seedhi=[center[j]+rho*(ohi[j]-olo[j])/2 for j in range(7)]
lo=seedlo[:];hi=seedhi[:];bit_rounds=[]
def nearest(x,den):return Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den)
def valid_box(l,u):
 return (all(Q(1,10**6)<l[j]<u[j]-Q(1,10**6) and u[j]<1000 for j in range(7))
   and all(sgn*oe(l,u,t)[idx]>Q(1,10**10)*(1+t)**3 for t,req in markers for idx,sgn in req)
   and all(sgn*oe(l,u,t)[idx]>Q(1,10**10)*(1+t)**3 for t,idx,sgn in inv_signs))
if not valid_box(lo,hi):raise ValueError('SEED')
for iteration in range(6):
 atoms=[(ci,t,[v/(1+t)**7 for v in actual_vector(lo,hi,ci,t)]) for ci,t in inv_atoms]
 scale=lcm(*(v.denominator for atom in atoms for v in atom[2]));C=[[int(scale*a[2][k]) for a in atoms] for k in range(8)]
 sol=exact_minimax(C,pivot_cap=1600);rec={'iteration':iteration+1,'atom_status':sol['status'],'atom_pivots':sol['pivots']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';bit_rounds.append(rec);break
 opt=sol['optimum']/scale;rec['grid_margin']=str(opt)
 if opt<=0:
  lam=sol['lambda'];weights=[w/(1+t)**7 for w,(_,t,_) in zip(lam,atoms)]
  F=[sum(w*actual_vector(lo,hi,ci,t)[k] for (ci,t,_),w in zip(atoms,weights)) for k in range(8)]
  if not all(v<=0 for v in F):raise ValueError('CERT')
  rec.update({'status':'ACTUAL_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
   'support':[{'corner':ci,'t':str(t),'weight':str(w)} for (ci,t,_),w in zip(atoms,weights) if w>0],'coefficient_sums':[str(v) for v in F]});bit_rounds.append(rec);break
 # Snap simplex weights to a bounded denominator and add strictly positive mass.
 approx=[max(1,(v.numerator*10**8)//v.denominator) for v in sol['lambda']];total=sum(approx)
 weights=[Q(q,total)/(1+t)**7 for q,(_,t,_) in zip(approx,atoms)]
 lv=[z3.Real('bbit_l%d_%d'%(iteration,j)) for j in range(7)];uv=[z3.Real('bbit_u%d_%d'%(iteration,j)) for j in range(7)];bound=z3.Real('bbit_v%d'%iteration)
 S=z3.Optimize();S.set(timeout=10000)
 for j in range(7):S.add(lv[j]>=zval(Q(1,10**6)),uv[j]-lv[j]>=zval(Q(1,10**6)),uv[j]<=zval(1000))
 for t,req in markers:
  for idx,sgn in req:S.add(sgn*oe(lv,uv,zval(t))[idx]>=zval(Q(1,10**10)*(1+t)**3))
 for t,idx,sgn in inv_signs:S.add(sgn*oe(lv,uv,zval(t))[idx]>=zval(Q(1,10**10)*(1+t)**3))
 for k in range(8):S.add(sum(zval(w)*actual_vector(lv,uv,ci,zval(t))[k] for (ci,t,_),w in zip(atoms,weights))<=bound)
 S.minimize(bound);status=S.check();rec['box_status']=str(status)
 if status!=z3.sat:rec['status']='BOX_'+str(status);bit_rounds.append(rec);break
 model=S.model();rawlo=[frac(model.eval(v,model_completion=True)) for v in lv];rawhi=[frac(model.eval(v,model_completion=True)) for v in uv]
 # Mix with the strictly feasible seed, then snap; try higher exact precision.
 tau=Q(1,1000);mixlo=[(1-tau)*rawlo[j]+tau*seedlo[j] for j in range(7)];mixhi=[(1-tau)*rawhi[j]+tau*seedhi[j] for j in range(7)]
 for den in (10**8,10**10,10**12,10**14,10**16,10**18):
  nlo=[nearest(v,den) for v in mixlo];nhi=[nearest(v,den) for v in mixhi]
  if valid_box(nlo,nhi):break
 else:rec['status']='SNAP_NO_VALID_BOX';bit_rounds.append(rec);break
 if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(nlo,nhi)):raise ValueError('STABILITY')
 F=[sum(w*actual_vector(nlo,nhi,ci,t)[k] for (ci,t,_),w in zip(atoms,weights)) for k in range(8)]
 rec.update({'box_bound':str(max(F)),'snap_denominator':den,'lower':[str(v) for v in nlo],'upper':[str(v) for v in nhi],
   'support':[{'corner':ci,'t':str(t),'weight':str(w)} for (ci,t,_),w in zip(atoms,weights)],'coefficient_sums':[str(v) for v in F]})
 if max(F)<=0:rec['status']='ACTUAL_CERTIFICATE';bit_rounds.append(rec);break
 rec['status']='NO_CERTIFICATE_ON_FIXED_WEIGHTS';bit_rounds.append(rec)
 if nlo==lo and nhi==hi:rec['terminal']='EXACT_FIXED_POINT';break
 lo,hi=nlo,nhi
else:bit_rounds[-1]['terminal']='SIX_ITERATION_LIMIT'
print('bounded-bit inversion search:',[{'iteration':r['iteration'],'status':r['status'],'atom_pivots':r['atom_pivots'],
 'box_status':r.get('box_status'),'box_bound':r.get('box_bound'),'snap_denominator':r.get('snap_denominator'),'terminal':r.get('terminal')} for r in bit_rounds])
