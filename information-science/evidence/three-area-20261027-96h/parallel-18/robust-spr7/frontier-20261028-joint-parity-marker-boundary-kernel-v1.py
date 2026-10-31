# Replace timed-out joint NRA with an exact outer-box construction. Marker
# constraints separately bound even and odd scale factors; their maximal outer
# box has one exact rational imaginary contact. Search one boundary tangent.
from fractions import Fraction as Q
from math import lcm
outerlo=[bn[j]-(BE[0] if j%2==0 else BO[0])*bdm[j] for j in range(7)]
outerhi=[bn[j]+(BE[0] if j%2==0 else BO[0])*bdp[j] for j in range(7)]
outercs=local_corners(outerlo,outerhi);contact=mm[4]
if oe(outerlo,outerhi,contact)[1]!=0 or oe(outerlo,outerhi,contact)[2]!=0:raise ValueError('CONTACT')
tangent=[]
for k in range(8):
 unit=[Q(0)]*8;unit[k]=Q(1);p=pairing_polynomial(outercs[2],unit)
 if sum(p[j]*contact**j for j in range(8))!=0:raise ValueError('CONTACT_PAIR')
 tangent.append(sum(j*p[j]*contact**(j-1) for j in range(1,8))/(1+contact)**7)
grid=set(a1nodes)|set(mm)|{Q(0),Q(1),Q(4),Q(10),Q(25),Q(50),Q(100),Q(200)}
grid.discard(contact)
joint_cone=[];done=False
for outer in range(6):
 rows=[]
 for ci,a in enumerate(outercs):
  for t in sorted(grid):
   vec,den=pair_vector_t(a,t);v=[Q(x,den)/(1+t)**7 for x in vec]
   if any(v):rows.append({'kind':'physical','vector':v})
 rows.append({'kind':'infinity','vector':[Q(0)]*7+[Q(1)]})
 for j in range(8):rows.append({'kind':'unit','vector':[Q(int(k==j)) for k in range(8)]})
 for sign in (-1,1):rows.append({'kind':'tangent','vector':[sign*v for v in tangent]})
 for eps in (Q(1,10**6),Q(1,10**8),Q(1,10**10),Q(1,10**12),Q(1,10**14),Q(1,10**16),Q(1,10**18),Q(1,10**20)):
  vectors=[[v-eps if row['kind']!='tangent' else v for v in row['vector']] for row in rows]
  scale=lcm(*(x.denominator for row in vectors for x in row));C=[[int(scale*vectors[i][k]) for i in range(len(rows))] for k in range(8)]
  sol=exact_minimax(C,pivot_cap=2500);rec={'outer':outer+1,'epsilon':str(eps),'atoms':len(rows),'pivots':sol['pivots'],'solver_status':sol['status']}
  if sol['status']!='CERTIFIED_OPTIMUM':rec['status']='PIVOT_CAP';joint_cone.append(rec);done=True;break
  opt=sol['optimum']/scale;rec['margin']=str(opt)
  if opt<0:rec['status']='MARGIN_TOO_LARGE_ON_GRID';joint_cone.append(rec);continue
  if opt!=0:raise ValueError('TANGENT_PAIR')
  b=sol['dual']
  if any(v<eps for v in b) or sum(tangent[k]*b[k] for k in range(8))!=0:raise ValueError('TANGENT')
  rec['numerator']=[str(v) for v in b];checks=[];polys=[];new=set()
  for ci,a in enumerate(outercs):
   poly=pairing_polynomial(a,b);polys.append(poly);res=poly
   if ci==2:res=quotient_by_root(quotient_by_root(res,contact),contact)
   test=exact_nonnegative_halfline(res,maxdepth=42,maxnodes=18000);checks.append(test)
   if test['status']=='NEGATIVE':
    t=Q(test['t']);pv=lambda x:sum(poly[j]*x**j for j in range(8))
    if pv(t)>=0:
     if ci!=2 or t!=contact:raise ValueError('RESIDUAL_SIGN')
     t=next((contact+sgn*Q(1,2**k) for k in range(1,61) for sgn in (-1,1) if contact+sgn*Q(1,2**k)>=0 and pv(contact+sgn*Q(1,2**k))<0),None)
     if t is None:raise ValueError('NO_NEAR_CONTACT_NEGATIVE')
    new.add(t)
   elif test['status']!='NONNEGATIVE_PROVED':rec.update({'status':'BOUNDARY_CHECK_CAP','checks':checks});joint_cone.append(rec);done=True;break
  if done:break
  rec['checks']=checks
  if not new:
   cp=pairing_polynomial(bn,b);pr=whole_halfline(cp,max_depth=45,max_nodes=18000)
   if pr['status']=='STRICT_POSITIVITY' and 'leaves' in pr:
    verify_leaves_by_power(cp,pr);rec.update({'status':'ALL_MARKER_REGION_COMMON_NUMERATOR','center_proof':pr,'boundary_polynomials':[[str(x) for x in p] for p in polys]})
   else:rec.update({'status':'BOUNDARY_NONNEGATIVE_CENTER_UNRESOLVED','center_proof':pr})
   joint_cone.append(rec);done=True;break
  new-=grid
  if not new:raise ValueError('NO_NEW_NODE')
  rec.update({'status':'ADDED_BOUNDARY_NEGATIVE_NODES','new_nodes':[str(t) for t in sorted(new)]});joint_cone.append(rec);grid.update(new);break
 else:joint_cone[-1]['terminal']='EPSILON_LIMIT';done=True
 if done:break
else:joint_cone[-1]['terminal']='SIX_OUTER_LIMIT'
print('joint parity marker-boundary synthesis:',[{'outer':r['outer'],'epsilon':r['epsilon'],'atoms':r['atoms'],'pivots':r['pivots'],
 'status':r['status'],'new_nodes':r.get('new_nodes'),'terminal':r.get('terminal')} for r in joint_cone])
