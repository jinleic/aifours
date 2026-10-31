# Exact operator cut search with independently located negative frequencies.
# Each added row is an actual corner under D^k(I+hD); no grid verdict is global.
from fractions import Fraction as Q
from math import lcm
box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
grid={Q(0),Q(1),Q(4),Q(16),Q(81),Q(289)}
for r in adapt_op:grid.update(Q(t) for t in r.get('new_nodes',[]))
rows={(k,h,ci,t) for k in range(7) for h in (Q(0),Q(1)) for ci in range(4) for t in grid};opcuts=[]
for iteration in range(3):
 atoms=[(k,h,ci,t,[v/(1+t)**(7-k) for v in op_vector(cs[ci],k,h,t)]) for k,h,ci,t in sorted(rows)]
 scale=lcm(*(v.denominator for a in atoms for v in a[4]));C=[[int(scale*a[4][j]) for a in atoms] for j in range(8)]
 sol=exact_minimax(C,pivot_cap=2600);rec={'iteration':iteration+1,'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';opcuts.append(rec);break
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
   'support':[{'order':k,'h':str(h),'corner':ci,'t':str(t),'weight':weights[i]} for i,(k,h,ci,t,w) in enumerate(supp)],'coefficient_sums':[str(v) for v in F]});opcuts.append(rec);break
 dual=list(sol['dual'])
 if dual[7]<=0:
  lift=min(sum(row[4][j]*dual[j] for j in range(8))/(2*(1+abs(row[4][7]))) for row in atoms)
  if lift<=0:raise ValueError('LEADING_LIFT')
  dual[7]+=lift;rec['leading_lift']=str(lift)
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(v) for v in b]
 for i,(k,h,ci,t,_) in enumerate(atoms):
  v=sum(op_vector(cs[ci],k,h,t)[j]*b[j] for j in range(8))/(1+t)**(7-k)
  if v<=0 or sum(C[j][i]*b[j] for j in range(8))!=scale*v:raise ValueError('GRID')
 candidates=[];caps=0;original_proofs=[]
 for k in range(7):
  for h in (Q(0),Q(1),Q(10)):
   for ci,a in enumerate(cs):
    aa=op_transform(a,k,h);bb=op_transform(b,k,h);P=pv(aa,bb);test=exact_nonnegative_halfline(P,maxdepth=28,maxnodes=5000)
    if k==0 and h==0:original_proofs.append(test)
    if test['status']=='NEGATIVE':
     t=Q(test['t']);value=ev(P,t)
     if value<0:candidates.append((value/(1+t)**(7-k),k,h,ci,t,P))
    elif test['status']=='SUBDIVISION_CAP':caps+=1
    elif test['status']!='NONNEGATIVE_PROVED':raise ValueError('OP_PROOF_STATUS')
 candidates.sort(key=lambda x:x[0]);added=set()
 for _,k,h,ci,t,P in candidates[:24]:
  for den in (10,100,1000,10000,100000,1000000):
   q=nearest(t,den)
   if q>=0 and (k,h,ci,q) not in rows and ev(P,q)<0:added.add((k,h,ci,q));break
  else:
   if (k,h,ci,t) not in rows:added.add((k,h,ci,t))
 if not added:rec.update({'status':'NO_NEW_NEGATIVE_OPERATOR_ROW','proof_caps':caps});opcuts.append(rec);break
 rec.update({'status':'ADDED_NEGATIVE_OPERATOR_ROWS','added_count':len(added),'proof_caps':caps,
   'new_rows':[{'order':k,'h':str(h),'corner':ci,'t':str(t)} for k,h,ci,t in sorted(added)]});opcuts.append(rec);rows.update(added)
else:opcuts[-1]['terminal']='THREE_ITERATION_LIMIT'
print('operator-frequency exact cuts:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],'status':r['status'],
 'added_count':r.get('added_count'),'proof_caps':r.get('proof_caps'),'terminal':r.get('terminal')} for r in opcuts])
