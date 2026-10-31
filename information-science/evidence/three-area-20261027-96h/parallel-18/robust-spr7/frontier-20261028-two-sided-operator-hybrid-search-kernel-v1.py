# Exact hybrid atom search using forward and reciprocal conjugate operators.
# Each row is from an actual septic member; finite-grid dual is not global.
from fractions import Fraction as Q
from math import lcm

def transform2(a,k,h,reverse):
 v=a[::-1] if reverse else a[:]
 z=op_transform(v,k,h)
 return z[::-1] if reverse else z

def coeff2(a,k,h,reverse,t,basis):
 q=transform2(a,k,h,reverse);E=sum(q[j]*(-t)**(j//2) for j in range(0,len(q),2));O=sum(q[j]*(-t)**((j-1)//2) for j in range(1,len(q),2))
 return [sum(v[j]*(-t)**(j//2)*E for j in range(0,len(v),2))+t*sum(v[j]*(-t)**((j-1)//2)*O for j in range(1,len(v),2)) for v in basis]

box=asym_results[3];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
base={}
for k in range(7):
 for h in (Q(0),Q(1)):
  for rev in (False,True):
   arr=[]
   for j in range(8):
    unit=[Q(0)]*8;unit[j]=Q(1);arr.append(transform2(unit,k,h,rev))
   base[k,h,rev]=arr
grid={Q(0),Q(1),Q(4),Q(16),Q(25),Q(81),Q(144),Q(289)};two_sided=[]
for it in range(2):
 atoms=[]
 for k in range(7):
  for h in (Q(0),Q(1)):
   for rev in (False,True):
    for ci,a in enumerate(cs):
     for t in sorted(grid):atoms.append((k,h,rev,ci,t,[v/(1+t)**(7-k) for v in coeff2(a,k,h,rev,t,base[k,h,rev])]))
 scale=lcm(*(v.denominator for a in atoms for v in a[5]));C=[[int(scale*a[5][j]) for a in atoms] for j in range(8)]
 sol2=exact_minimax(C,pivot_cap=2600);rec={'iteration':it+1,'nodes':[str(t) for t in sorted(grid)],'atoms':len(atoms),'pivots':sol2['pivots'],'solver_status':sol2['status']}
 if sol2['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';two_sided.append(rec);break
 opt=sol2['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  support=[]
  for i,w in enumerate(sol2['lambda']):
   if w>0:
    k,h,rev,ci,t,_=atoms[i];support.append((k,h,rev,ci,t,w/(1+t)**(7-k)))
  den=lcm(*(w.denominator for k,h,rev,ci,t,w in support));weights=[int(den*w) for k,h,rev,ci,t,w in support]
  F=[sum(weights[i]*coeff2(cs[ci],k,h,rev,t,base[k,h,rev])[j] for i,(k,h,rev,ci,t,w) in enumerate(support)) for j in range(8)]
  if any(v>0 for v in F):raise ValueError('CERT')
  rec.update({'status':'TWO_SIDED_OPERATOR_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
   'support':[{'order':k,'h':str(h),'reverse':rev,'corner':ci,'t':str(t),'weight':weights[i]} for i,(k,h,rev,ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in F]});two_sided.append(rec);break
 dual=list(sol2['dual'])
 if dual[7]<=0:
  lift=min(sum(a[5][j]*dual[j] for j in range(8))/(2*(1+abs(a[5][7]))) for a in atoms)
  if lift<=0:raise ValueError('LEADING')
  dual[7]+=lift;rec['leading_lift']=str(lift)
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
 for i,(k,h,rev,ci,t,_) in enumerate(atoms):
  val=sum(coeff2(cs[ci],k,h,rev,t,base[k,h,rev])[j]*b[j] for j in range(8))/(1+t)**(7-k)
  if val<=0 or sum(C[j][i]*b[j] for j in range(8))!=scale*val:raise ValueError('GRID')
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,pr in enumerate(proofs):
  if pr['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=12000)
 if all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'ORIGINAL_COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});two_sided.append(rec);break
 added={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}
 for p in proofs:
  if p['status']=='NONPOSITIVE_AT_DYADIC_X':
   x=Q(p['x'])
   if x<1:added.add(x/(1-x))
 added-=grid
 if not added:rec['status']='NO_NEW_ORIGINAL_VIOLATION';two_sided.append(rec);break
 rec.update({'status':'ADDED_ORIGINAL_VIOLATIONS','new_nodes':[str(t) for t in sorted(added)]});two_sided.append(rec);grid.update(added)
else:two_sided[-1]['terminal']='TWO_ITERATION_LIMIT'
print('two-sided operator hybrid search:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'margin':r.get('margin'),'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in two_sided])
