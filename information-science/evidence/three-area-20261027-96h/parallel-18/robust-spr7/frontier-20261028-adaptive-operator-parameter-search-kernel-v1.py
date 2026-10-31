# Exact cutting-plane search over operator parameter h>=0. A dual candidate
# is checked at the rational minimizing h of each quadratic on the current grid.
from fractions import Fraction as Q
from math import lcm
box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
grid={Q(0),Q(1),Q(4),Q(16),Q(81),Q(289)}
rows={(k,h,ci,t) for k in range(7) for h in (Q(0),Q(1)) for ci in range(4) for t in grid};adapt_op=[]
for iteration in range(5):
 atoms=[]
 for k,h,ci,t in sorted(rows):atoms.append((k,h,ci,t,[v/(1+t)**(7-k) for v in op_vector(cs[ci],k,h,t)]))
 scale=lcm(*(v.denominator for a in atoms for v in a[4]));C=[[int(scale*a[4][j]) for a in atoms] for j in range(8)]
 sol=exact_minimax(C,pivot_cap=2400);rec={'iteration':iteration+1,'atoms':len(atoms),'nodes':[str(t) for t in sorted(grid)],'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';adapt_op.append(rec);break
 opt=sol['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  supp=[]
  for i,w in enumerate(sol['lambda']):
   if w>0:
    k,h,ci,t,_=atoms[i];supp.append((k,h,ci,t,w/(1+t)**(7-k)))
  den=lcm(*(w.denominator for k,h,ci,t,w in supp));weights=[int(den*w) for k,h,ci,t,w in supp]
  F=[sum(weights[i]*op_vector(cs[ci],k,h,t)[j] for i,(k,h,ci,t,w) in enumerate(supp)) for j in range(8)]
  if any(v>0 for v in F):raise ValueError('CERT')
  rec.update({'status':'OPERATOR_NONPOSITIVE_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
    'support':[{'order':k,'h':str(h),'corner':ci,'t':str(t),'weight':weights[i]} for i,(k,h,ci,t,w) in enumerate(supp)],
    'coefficient_sums':[str(v) for v in F]});adapt_op.append(rec);break
 dual=list(sol['dual'])
 if dual[7]<=0:
  lift=min(sum(row[4][j]*dual[j] for j in range(8))/(2*(1+abs(row[4][7]))) for row in atoms)
  if lift<=0:raise ValueError('LEADING_LIFT')
  dual[7]+=lift;rec['leading_lift']=str(lift)
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(x) for x in b]
 for i,(k,h,ci,t,_) in enumerate(atoms):
  val=sum(op_vector(cs[ci],k,h,t)[j]*b[j] for j in range(8))/(1+t)**(7-k)
  if val<=0 or sum(C[j][i]*b[j] for j in range(8))!=scale*val:raise ValueError('GRID')
 candidates=[]
 for k in range(7):
  for ci,a in enumerate(cs):
   for t in grid:
    p0=sum(x*y for x,y in zip(op_vector(a,k,Q(0),t),b));p1t=sum(x*y for x,y in zip(op_vector(a,k,Q(1),t),b));p2t=sum(x*y for x,y in zip(op_vector(a,k,Q(2),t),b))
    quad=(p2t-2*p1t+p0)/2;linear=p1t-p0-quad
    if quad>0 and linear<0:
     h=-linear/(2*quad);value=p0+linear*h+quad*h*h
     if value<0:candidates.append((value/((1+t)**(7-k)*(1+h)**2),k,ci,t,h,p0,linear,quad))
 candidates.sort(key=lambda x:x[0]);added=set()
 for _,k,ci,t,h,p0,linear,quad in candidates[:12]:
  for den in (10,100,1000,10000,100000,1000000):
   hh=nearest(h,den)
   if hh>=0 and (k,hh,ci,t) not in rows and p0+linear*hh+quad*hh*hh<0:added.add((k,hh,ci,t));break
  else:
   if (k,h,ci,t) not in rows:added.add((k,h,ci,t))
 # Also find exact original-frequency failures and add both base h=0 and 1 rows.
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,pr in enumerate(proofs):
  if pr['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=12000)
 if all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'ORIGINAL_COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});adapt_op.append(rec);break
 newt={Q(p['t']) for p in proofs if p['status']=='NONPOSITIVE_EXACT'}
 for p in proofs:
  if p['status']=='NONPOSITIVE_AT_DYADIC_X':
   x=Q(p['x'])
   if x<1:newt.add(x/(1-x))
 newt-=grid
 for t in newt:
  for k in range(7):
   for h in (Q(0),Q(1)):
    for ci in range(4):added.add((k,h,ci,t))
 if not added:rec['status']='NO_NEW_OPERATOR_OR_FREQUENCY_ROW';adapt_op.append(rec);break
 rec.update({'status':'ADDED_VALID_ROWS','negative_h_rows':len([v for v in added if v[3] in grid]),'new_frequency_count':len(newt),'new_nodes':[str(t) for t in sorted(newt)]});adapt_op.append(rec);rows.update(added);grid.update(newt)
else:adapt_op[-1]['terminal']='FIVE_ITERATION_LIMIT'
print('adaptive operator-parameter search:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],'status':r['status'],
 'negative_h_rows':r.get('negative_h_rows'),'new_frequency_count':r.get('new_frequency_count'),'terminal':r.get('terminal')} for r in adapt_op])
