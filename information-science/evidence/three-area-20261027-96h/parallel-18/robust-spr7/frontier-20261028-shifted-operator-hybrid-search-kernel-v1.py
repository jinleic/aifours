# Exact hybrid atom search with right-half-plane shifts f(s+r) composed with
# D^k(I+hD). Shifted rows are necessary by harmonic extension of SPR.
from fractions import Fraction as Q
from math import comb,lcm

def shift7(a,r):return [sum(Q(comb(j,k))*r**(j-k)*a[j] for j in range(k,8)) for k in range(8)]
def transformed(a,r,k,h):return op_transform(shift7(a,r),k,h)
def coef(a,r,k,h,t,basis):
 q=transformed(a,r,k,h);E=sum(q[j]*(-t)**(j//2) for j in range(0,len(q),2));O=sum(q[j]*(-t)**((j-1)//2) for j in range(1,len(q),2))
 return [sum(v[j]*(-t)**(j//2)*E for j in range(0,len(v),2))+t*sum(v[j]*(-t)**((j-1)//2)*O for j in range(1,len(v),2)) for v in basis]
box=asym_results[4];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
basis={}
for r in (Q(0),Q(1),Q(10)):
 for k in range(3):
  for h in (Q(0),Q(1)):
   arr=[]
   for j in range(8):
    unit=[Q(0)]*8;unit[j]=Q(1);arr.append(transformed(unit,r,k,h))
   basis[r,k,h]=arr
grid={Q(0),Q(1),Q(4),Q(16),Q(25),Q(81),Q(144),Q(289)};shift_rounds=[]
for it in range(2):
 atoms=[]
 for r in (Q(0),Q(1),Q(10)):
  for k in range(3):
   for h in (Q(0),Q(1)):
    for ci,a in enumerate(cs):
     for t in sorted(grid):atoms.append((r,k,h,ci,t,[v/(1+t)**(7-k) for v in coef(a,r,k,h,t,basis[r,k,h])]))
 scale=lcm(*(v.denominator for atom in atoms for v in atom[5]));C=[[int(scale*a[5][j]) for a in atoms] for j in range(8)]
 sol=exact_minimax(C,pivot_cap=2400);rec={'iteration':it+1,'atoms':len(atoms),'nodes':[str(t) for t in sorted(grid)],'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';shift_rounds.append(rec);break
 opt=sol['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  support=[]
  for i,w in enumerate(sol['lambda']):
   if w>0:
    r,k,h,ci,t,_=atoms[i];support.append((r,k,h,ci,t,w/(1+t)**(7-k)))
  den=lcm(*(w.denominator for r,k,h,ci,t,w in support));weights=[int(den*w) for r,k,h,ci,t,w in support]
  F=[sum(weights[i]*coef(cs[ci],r,k,h,t,basis[r,k,h])[j] for i,(r,k,h,ci,t,w) in enumerate(support)) for j in range(8)]
  if any(v>0 for v in F):raise ValueError('CERT')
  rec.update({'status':'SHIFT_OPERATOR_NONPOSITIVE_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
   'support':[{'shift':str(r),'order':k,'h':str(h),'corner':ci,'t':str(t),'weight':weights[i]} for i,(r,k,h,ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in F]});shift_rounds.append(rec);break
 dual=list(sol['dual'])
 if dual[7]<=0:
  lift=min(sum(row[5][j]*dual[j] for j in range(8))/(2*(1+abs(row[5][7]))) for row in atoms)
  if lift<=0:raise ValueError('LIFT')
  dual[7]+=lift;rec['leading_lift']=str(lift)
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
 for i,(r,k,h,ci,t,_) in enumerate(atoms):
  v=sum(coef(cs[ci],r,k,h,t,basis[r,k,h])[j]*b[j] for j in range(8))/(1+t)**(7-k)
  if v<=0 or sum(C[j][i]*b[j] for j in range(8))!=scale*v:raise ValueError('GRID')
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,pr in enumerate(proofs):
  if pr['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=12000)
 if all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'ORIGINAL_COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});shift_rounds.append(rec);break
 added={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}
 for p in proofs:
  if p['status']=='NONPOSITIVE_AT_DYADIC_X':
   x=Q(p['x'])
   if x<1:added.add(x/(1-x))
 added-=grid
 if not added:rec['status']='NO_NEW_ORIGINAL_VIOLATION';shift_rounds.append(rec);break
 rec.update({'status':'ADDED_ORIGINAL_VIOLATIONS','new_nodes':[str(t) for t in sorted(added)]});shift_rounds.append(rec);grid.update(added)
else:shift_rounds[-1]['terminal']='TWO_ITERATION_LIMIT'
print('shifted operator hybrid search:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],'status':r['status'],
 'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in shift_rounds])
