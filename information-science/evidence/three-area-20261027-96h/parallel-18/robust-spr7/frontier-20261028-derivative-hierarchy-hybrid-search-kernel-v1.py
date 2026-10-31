# Exact original+derivative atom certificate search. The derivative rows are
# valid only via the written SPR-derivative preservation theorem. A positive
# finite-grid dual is not a full common-numerator proof.
from fractions import Fraction as Q
from math import lcm

def fall(n,k):
 out=1
 for j in range(k):out*=n-j
 return out
def dpoly(p,k):
 den=fall(7,k);return [Q(fall(j,k),den)*p[j] for j in range(k,8)]
def dvector(a,k,t):
 q=dpoly(a,k);E=sum(q[j]*(-t)**(j//2) for j in range(0,len(q),2));O=sum(q[j]*(-t)**((j-1)//2) for j in range(1,len(q),2));out=[Q(0)]*8;den=fall(7,k)
 for j in range(k,8):
  power=j-k;fac=Q(fall(j,k),den)
  out[j]=fac*((-t)**(power//2)*E if power%2==0 else t*(-t)**((power-1)//2)*O)
 return out

box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
grid={Q(0),Q(1,10),Q(1),Q(4),Q(8),Q(16),Q(25),Q(40),Q(81),Q(144),Q(289),Q(400)};hybrid=[]
for iteration in range(3):
 atoms=[]
 for order in range(7):
  n=7-order
  for ci,a in enumerate(cs):
   for t in sorted(grid):atoms.append((order,ci,t,[v/(1+t)**n for v in dvector(a,order,t)]))
 scale=lcm(*(v.denominator for atom in atoms for v in atom[3]));C=[[int(scale*a[3][k]) for a in atoms] for k in range(8)]
 sol=exact_minimax(C,pivot_cap=2400);rec={'iteration':iteration+1,'nodes':[str(t) for t in sorted(grid)],'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';hybrid.append(rec);break
 opt=sol['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  support=[]
  for i,w in enumerate(sol['lambda']):
   if w>0:
    order,ci,t,_=atoms[i];support.append((order,ci,t,w/(1+t)**(7-order)))
  den=lcm(*(w.denominator for order,ci,t,w in support));weights=[int(den*w) for order,ci,t,w in support]
  F=[sum(weights[i]*dvector(cs[ci],order,t)[k] for i,(order,ci,t,w) in enumerate(support)) for k in range(8)]
  if any(v>0 for v in F):raise ValueError('CERTIFICATE_REPLAY')
  rec.update({'status':'HYBRID_NONPOSITIVE_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
    'support':[{'derivative_order':order,'corner':ci,'t':str(t),'weight':weights[i]} for i,(order,ci,t,w) in enumerate(support)],
    'coefficient_sums':[str(v) for v in F]});hybrid.append(rec);break
 dual=sol['dual']
 if dual[7]<=0:raise ValueError('LEADING')
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
 for i,(order,ci,t,_) in enumerate(atoms):
  val=sum(dvector(cs[ci],order,t)[k]*b[k] for k in range(8))/(1+t)**(7-order)
  if val<=0 or sum(C[k][i]*b[k] for k in range(8))!=scale*val:raise ValueError('GRID_REPLAY')
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,pr in enumerate(proofs):
  if pr['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=12000)
 if all(p['status']=='STRICT_POSITIVITY' and 'leaves' in p for p in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'ORIGINAL_COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});hybrid.append(rec);break
 added={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}
 for p in proofs:
  if p['status']=='NONPOSITIVE_AT_DYADIC_X':
   x=Q(p['x'])
   if x<1:added.add(x/(1-x))
 added-=grid
 if not added:rec['status']='NO_NEW_ORIGINAL_VIOLATION';hybrid.append(rec);break
 rec.update({'status':'ADDED_ORIGINAL_VIOLATIONS','new_nodes':[str(t) for t in sorted(added)]});hybrid.append(rec);grid.update(added)
else:hybrid[-1]['terminal']='THREE_ITERATION_LIMIT'
print('hybrid derivative atom search:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in hybrid])
