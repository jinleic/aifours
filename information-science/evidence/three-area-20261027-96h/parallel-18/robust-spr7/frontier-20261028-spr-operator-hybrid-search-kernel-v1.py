# Exact atom search augmented by D^k(I+hD) SPR-preserving operators.
# Nonpositive sums would contradict the written operator theorem; a positive
# finite-grid dual is not global synthesis.
from fractions import Fraction as Q
from math import lcm

def op_transform(a,k,h):
 out=[Q(ff(j,k),ff(7,k))*a[j] for j in range(k,8)]
 for j in range(k+1,8):out[j-k-1]+=h*Q(ff(j,k+1),ff(7,k))*a[j]
 return out
def op_vector(a,k,h,t):
 q=op_transform(a,k,h);E=sum(q[j]*(-t)**(j//2) for j in range(0,len(q),2));O=sum(q[j]*(-t)**((j-1)//2) for j in range(1,len(q),2));out=[Q(0)]*8
 def contrib(power):return (-t)**(power//2)*E if power%2==0 else t*(-t)**((power-1)//2)*O
 for j in range(k,8):
  out[j]+=Q(ff(j,k),ff(7,k))*contrib(j-k)
  if j>k:out[j]+=h*Q(ff(j,k+1),ff(7,k))*contrib(j-k-1)
 return out
box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
grid={Q(0),Q(1),Q(4),Q(16),Q(25),Q(81),Q(144),Q(289)};op_rounds=[]
for iteration in range(2):
 atoms=[]
 for k in range(7):
  for h in (Q(0),Q(1)):
   n=7-k
   for ci,a in enumerate(cs):
    for t in sorted(grid):atoms.append((k,h,ci,t,[v/(1+t)**n for v in op_vector(a,k,h,t)]))
 scale=lcm(*(v.denominator for a in atoms for v in a[4]));C=[[int(scale*a[4][j]) for a in atoms] for j in range(8)]
 sol=exact_minimax(C,pivot_cap=2200);rec={'iteration':iteration+1,'nodes':[str(t) for t in sorted(grid)],'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';op_rounds.append(rec);break
 opt=sol['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  support=[]
  for i,w in enumerate(sol['lambda']):
   if w>0:
    k,h,ci,t,_=atoms[i];support.append((k,h,ci,t,w/(1+t)**(7-k)))
  den=lcm(*(w.denominator for k,h,ci,t,w in support));weights=[int(den*w) for k,h,ci,t,w in support]
  F=[sum(weights[i]*op_vector(cs[ci],k,h,t)[j] for i,(k,h,ci,t,w) in enumerate(support)) for j in range(8)]
  if any(v>0 for v in F):raise ValueError('CERTIFICATE')
  rec.update({'status':'OPERATOR_NONPOSITIVE_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
   'support':[{'derivative_order':k,'h':str(h),'corner':ci,'t':str(t),'weight':weights[i]} for i,(k,h,ci,t,w) in enumerate(support)],
   'coefficient_sums':[str(v) for v in F]});op_rounds.append(rec);break
 dual=sol['dual']
 if dual[7]<=0:raise ValueError('LEADING')
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(x) for x in b]
 for i,(k,h,ci,t,_) in enumerate(atoms):
  value=sum(op_vector(cs[ci],k,h,t)[j]*b[j] for j in range(8))/(1+t)**(7-k)
  if value<=0 or sum(C[j][i]*b[j] for j in range(8))!=scale*value:raise ValueError('GRID_REPLAY')
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,pr in enumerate(proofs):
  if pr['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=12000)
 if all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'ORIGINAL_COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});op_rounds.append(rec);break
 added={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}
 for p in proofs:
  if p['status']=='NONPOSITIVE_AT_DYADIC_X':
   x=Q(p['x'])
   if x<1:added.add(x/(1-x))
 added-=grid
 if not added:rec['status']='NO_NEW_ORIGINAL_VIOLATION';op_rounds.append(rec);break
 rec.update({'status':'ADDED_ORIGINAL_VIOLATIONS','new_nodes':[str(t) for t in sorted(added)]});op_rounds.append(rec);grid.update(added)
else:op_rounds[-1]['terminal']='TWO_ITERATION_LIMIT'
print('operator-augmented atom search:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in op_rounds])
