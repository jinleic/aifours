# Exact semi-infinite-in-h cut search at ten actual corner/frequency sites.
# Unit rows enforce a positive dual but are NOT actual pairing rows, so an LP
# obstruction using a unit row is inconclusive for the original problem.
from fractions import Fraction as Q
from math import lcm
box=asym_results[2];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']];cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
sites2=sites+[(0,Q(1021,3)),(2,Q(231,25)),(3,Q(235,21))]
ops={(i,Q(h)) for i in range(len(sites2)) for h in (0,1,10)}
cutrows=[]
for iteration in range(8):
 atoms=[]
 for i,h in sorted(ops):
  ci,t=sites2[i];atoms.append({'kind':'operator','site':i,'h':h,'vector':[v/(1+t)**7 for v in op_vector(cs[ci],0,h,t)]})
 for i,(ci,t) in enumerate(sites2):atoms.append({'kind':'derivative','site':i,'h':None,'vector':[49*v/(1+t)**7 for v in op_vector(cs[ci],1,Q(0),t)]})
 for j in range(8):atoms.append({'kind':'unit','site':None,'h':None,'index':j,'vector':[Q(int(k==j)) for k in range(8)]})
 scale=lcm(*(v.denominator for a in atoms for v in a['vector']));C=[[int(scale*a['vector'][k]) for a in atoms] for k in range(8)]
 sol=exact_minimax(C,pivot_cap=1800);rec={'iteration':iteration+1,'rows':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';cutrows.append(rec);break
 opt=sol['optimum']/scale;rec['margin']=str(opt)
 if opt<=0:
  supp=[(a,w) for a,w in zip(atoms,sol['lambda']) if w>0]
  if any(a['kind']=='unit' for a,w in supp):rec['status']='UNIT_ROW_OBSTRUCTION_NOT_VALID_CERTIFICATE';cutrows.append(rec);break
  F=[sum(w*a['vector'][k] for a,w in supp) for k in range(8)]
  if any(v>0 for v in F):raise ValueError('CERT')
  rec.update({'status':'ACTUAL_OPERATOR_CERTIFICATE','support':[{'kind':a['kind'],'site':a['site'],'h':str(a['h']) if a['h'] is not None else None,'weight':str(w)} for a,w in supp],
    'coefficient_sums':[str(v) for v in F]});cutrows.append(rec);break
 b=sol['dual'];rec['numerator']=[str(v) for v in b]
 if not all(v>0 for v in b):raise ValueError('POSITIVE_DUAL')
 new=[];triples=[]
 for i,(ci,t) in enumerate(sites2):
  P0=sum(x*y for x,y in zip(op_vector(cs[ci],0,Q(0),t),b));P1v=sum(x*y for x,y in zip(op_vector(cs[ci],0,Q(1),t),b));P2v=sum(x*y for x,y in zip(op_vector(cs[ci],0,Q(2),t),b))
  A=(P2v-2*P1v+P0)/2;B=P1v-P0-A
  if P0<=0 or A<=0:raise ValueError('ENDPOINT')
  triples.append((P0,B,A))
  if B<0 and B*B>=4*P0*A:
   h=-B/(2*A)
   if (i,h) not in ops:new.append((i,h))
 if not new:
  rec.update({'status':'ALL_H_FINITE_SITE_SEPARATOR','triples':[[str(v) for v in x] for x in triples]});cutrows.append(rec);break
 rec.update({'status':'ADDED_NEGATIVE_H','new_h':[{'site':i,'h':str(h)} for i,h in new]});cutrows.append(rec);ops.update(new)
else:cutrows[-1]['terminal']='EIGHT_ITERATION_LIMIT'
print('adaptive all-h site search:',[{'iteration':r['iteration'],'status':r['status'],'rows':r['rows'],'pivots':r['pivots'],
 'new_h':len(r.get('new_h',[])),'terminal':r.get('terminal')} for r in cutrows])
