# Exact outer-box search seeded by all six parity inversion bands. Because
# nested subboxes are contained in this stable outer box, a positive grid dual
# for the outer box excludes certificates on that grid in every subbox.
from fractions import Fraction as Q
from math import lcm
box=asym_results[0];lo=[Q(x) for x in box['lower']];hi=[Q(x) for x in box['upper']]
def local_corners(lower,upper):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lower[j] if ((j//2)%2==0)==(es==0) else upper[j]
   for j in (1,3,5):a[j]=lower[j] if ((j//2)%2==0)==(oside==0) else upper[j]
   out.append(a)
 return out
cs=local_corners(lo,hi)
if not all(routh_ok(a) and integer_hurwitz(a) for a in cs):raise ValueError('STABILITY')
grid=set(inv_grid_tenth)|{Q(0)};guided=[]
for iteration in range(8):
 atoms=[]
 for ci,a in enumerate(cs):
  for t in sorted(grid):
   vec,den=pair_vector_t(a,t);atoms.append((ci,t,[Q(v,den)/(1+t)**7 for v in vec]))
 atoms.append((None,None,[Q(0)]*7+[Q(1)]))
 scale=lcm(*(v.denominator for a in atoms for v in a[2]));C=[[int(scale*a[2][k]) for a in atoms] for k in range(8)]
 sol=exact_minimax(C,pivot_cap=2200);rec={'iteration':iteration+1,'grid':[str(t) for t in sorted(grid)]+['infinity'],'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
 if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';guided.append(rec);break
 opt=sol['optimum']/scale;rec['grid_margin']=str(opt)
 if opt<=0:
  support=[]
  for i,w in enumerate(sol['lambda']):
   if w>0:
    ci,t,_=atoms[i];support.append((ci,t,w/(1+t)**7 if t is not None else w))
  den=lcm(*(w.denominator for ci,t,w in support));weights=[int(den*w) for ci,t,w in support];values=[]
  for k in range(8):
   unit=[Q(0)]*8;unit[k]=Q(1);values.append(sum(weights[i]*(independent_pair_t(cs[ci],unit,t) if t is not None else unit[7]) for i,(ci,t,w) in enumerate(support)))
  if any(v>0 for v in values):raise ValueError('CERTIFICATE')
  rec.update({'status':'ACTUAL_NONPOSITIVE_ATOM_CERTIFICATE','lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
      'support':[{'corner':ci,'t':str(t) if t is not None else 'infinity','weight':weights[i]} for i,(ci,t,w) in enumerate(support)],'coefficient_sums':[str(v) for v in values]});guided.append(rec);break
 dual=sol['dual']
 if dual[0]<=0 or dual[7]<=0:raise ValueError('ENDPOINT')
 b=[v/dual[7] for v in dual];rec['dual_monic']=[str(x) for x in b]
 for i,(ci,t,_) in enumerate(atoms):
  value=independent_pair_t(cs[ci],b,t)/(1+t)**7 if t is not None else b[7]
  if value<=0 or sum(b[k]*C[k][i] for k in range(8))!=scale*value:raise ValueError('GRID_REPLAY')
 ps=[pairing_polynomial(a,b) for a in cs];proofs=[whole_halfline(p,max_depth=28,max_nodes=4000) for p in ps]
 for i,proof in enumerate(proofs):
  if proof['status']=='SUBDIVISION_CAP':proofs[i]=locate_strict_failure(ps[i],max_depth=58,max_nodes=14000)
 if all(v['status']=='STRICT_POSITIVITY' and 'leaves' in v for v in proofs):
  for p,pr in zip(ps,proofs):verify_leaves_by_power(p,pr)
  rec.update({'status':'COMMON_NUMERATOR_PROVED','proofs':proofs,'polynomials':[[str(v) for v in p] for p in ps]});guided.append(rec);break
 added=set()
 for ci,pr in enumerate(proofs):
  if pr['status']!='NONPOSITIVE_EXACT':continue
  raw=Q(pr['t'])
  if independent_pair_t(cs[ci],b,raw)>=0:continue
  for den in (10,100,1000,10000,100000,1000000,10000000):
   t=nearest(raw,den)
   if t>=0 and t not in grid and independent_pair_t(cs[ci],b,t)<0:added.add(t);break
  else:
   if raw not in grid:added.add(raw)
 if not added:rec['status']='NO_NEW_STRICT_NODE';guided.append(rec);break
 rec.update({'status':'ADDED_NEGATIVE_NODES','new_nodes':[str(t) for t in sorted(added)]});guided.append(rec);grid.update(added)
else:guided[-1]['terminal']='EIGHT_ITERATION_LIMIT'
print('band-guided outer-box exchange:',[{'iteration':r['iteration'],'atoms':r['atoms'],'pivots':r['pivots'],'status':r['status'],
 'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in guided])
