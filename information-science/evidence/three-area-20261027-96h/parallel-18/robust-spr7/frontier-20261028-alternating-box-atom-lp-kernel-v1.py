# Different search representation: alternate exact atom minimax and an exact
# linear box optimization. Five rational sign markers force all-member parity
# interlacing. Z3 solves only QF_LRA for fixed atom weights, with a 10s bound.
from fractions import Fraction as Q
from math import lcm
import z3

def zval(x):
 x=Q(x);return z3.RealVal(str(x.numerator)+'/'+str(x.denominator))
def frac(v):
 if not z3.is_rational_value(v):raise ValueError('NONRATIONAL_Z3_MODEL')
 return Q(v.numerator_as_long(),v.denominator_as_long())
def oe(lo,hi,t):
 Eminus=lo[0]-hi[2]*t+lo[4]*t*t-hi[6]*t**3
 Eplus=hi[0]-lo[2]*t+hi[4]*t*t-lo[6]*t**3
 Ominus=lo[1]-hi[3]*t+lo[5]*t*t-t**3
 Oplus=hi[1]-lo[3]*t+hi[5]*t*t-t**3
 return Eminus,Eplus,Ominus,Oplus
markers=[(Q(1),((1,-1),(2,1))),(Q(2),((1,-1),(3,-1))),
         (Q(3),((0,1),(3,-1))),(Q(6),((0,1),(2,1))),(Q(8),((1,-1),(2,1)))]
def actual_vector(lo,hi,ci,t):
 em,ep,om,op=oe(lo,hi,t);e=(em,ep)[ci//2];o=(om,op)[ci%2]
 return [e,t*o,-t*e,-t*t*o,t*t*e,t**3*o,-t**3*e,-t**4*o]

v0,v1,cc,bc,contacts=five_box(five_design[0]);lo=[cc[j]-(v1[j]-v0[j])/4 for j in range(7)];hi=[cc[j]+(v1[j]-v0[j])/4 for j in range(7)]
if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(lo,hi)):raise ValueError('INITIAL_HURWITZ')
grid=sorted({Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(3),Q(4),Q(5),Q(6),Q(7),Q(8),Q(9),Q(12)})
alt_rounds=[]
for iteration in range(6):
    atoms=[]
    for ci in range(4):
        for t in grid:atoms.append((ci,t,[v/(1+t)**7 for v in actual_vector(lo,hi,ci,t)]))
    scale=lcm(*(v.denominator for a in atoms for v in a[2]));C=[[int(scale*a[2][k]) for a in atoms] for k in range(8)]
    sol=exact_minimax(C,pivot_cap=1400);rec={'iteration':iteration+1,'atom_solver_status':sol['status'],'atom_pivots':sol['pivots'],'grid':[str(t) for t in grid]}
    if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='ATOM_PIVOT_CAP';alt_rounds.append(rec);break
    opt=sol['optimum']/scale;rec['grid_margin']=str(opt)
    weights=[]
    for i,w in enumerate(sol['lambda']):
        if w:
            ci,t,_=atoms[i];weights.append((ci,t,w/(1+t)**7))
    currentF=[sum(w*actual_vector(lo,hi,ci,t)[k] for ci,t,w in weights) for k in range(8)]
    if max(currentF)!=opt:raise ValueError('CURRENT_PRIMAL')
    if opt<=0:
        rec.update({'status':'ACTUAL_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
                    'support':[{'corner':ci,'t':str(t),'weight':str(w)} for ci,t,w in weights],'coefficient_sums':[str(v) for v in currentF]});alt_rounds.append(rec);break
    zlo=[z3.Real('l%d_%d'%(iteration,j)) for j in range(7)];zhi=[z3.Real('u%d_%d'%(iteration,j)) for j in range(7)];bound=z3.Real('v_%d'%iteration)
    solver=z3.Optimize();solver.set(timeout=10000)
    for j in range(7):solver.add(zlo[j]>=zval(Q(1,10**6)),zhi[j]-zlo[j]>=zval(Q(1,10**6)),zhi[j]<=zval(1000))
    for t,requirements in markers:
        vals=oe(zlo,zhi,zval(t));rhs=zval(Q(1,10**10)*(1+t)**3)
        for index,sgn in requirements:solver.add(sgn*vals[index]>=rhs)
    for k in range(8):solver.add(sum(zval(w)*actual_vector(zlo,zhi,ci,zval(t))[k] for ci,t,w in weights)<=bound)
    goal=solver.minimize(bound);status=solver.check();rec['box_solver_status']=str(status)
    if status!=z3.sat:rec['status']='BOX_SOLVER_'+str(status);alt_rounds.append(rec);break
    model=solver.model();nlo=[frac(model.eval(v,model_completion=True)) for v in zlo];nhi=[frac(model.eval(v,model_completion=True)) for v in zhi]
    if not all(0<nlo[j]<nhi[j] for j in range(7)):raise ValueError('BOX_MODEL')
    for t,req in markers:
        vals=oe(nlo,nhi,t)
        if not all(sign*vals[index]>=Q(1,10**10)*(1+t)**3 for index,sign in req):raise ValueError('MARKER_MODEL')
    if not all(routh_ok(a) and integer_hurwitz(a) for a in corners(nlo,nhi)):raise ValueError('HURWITZ_REPLAY')
    nv=[sum(w*actual_vector(nlo,nhi,ci,t)[k] for ci,t,w in weights) for k in range(8)];v=max(nv)
    rec.update({'fixed_weight_box_bound':str(v),'box_lower':[str(x) for x in nlo],'box_upper':[str(x) for x in nhi],
                'support':[{'corner':ci,'t':str(t),'weight':str(w)} for ci,t,w in weights],'coefficient_sums':[str(x) for x in nv]})
    if v<=0:
        rec['status']='ACTUAL_CERTIFICATE';alt_rounds.append(rec);break
    rec['status']='NO_CERTIFICATE_FIXED_WEIGHTS';alt_rounds.append(rec);lo,hi=nlo,nhi
else:alt_rounds[-1]['terminal']='SIX_ITERATION_LIMIT'
print('alternating exact box/atom LP:',[{'iteration':r['iteration'],'status':r['status'],'grid_margin':r.get('grid_margin'),
 'fixed_weight_box_bound':r.get('fixed_weight_box_bound'),'box_solver':r.get('box_solver_status'),'terminal':r.get('terminal')} for r in alt_rounds])
