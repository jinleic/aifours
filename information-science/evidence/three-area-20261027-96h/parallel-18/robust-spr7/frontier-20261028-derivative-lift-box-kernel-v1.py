# Exact full-width septic box whose derivative sextics have one common SPR
# numerator that cannot be integrated into a common septic numerator.
from fractions import Fraction as Q
from math import comb
p0=[Q(comb(7,j)) for j in range(8)];q0=[Q(comb(6,j)) for j in range(7)];c=q0[:];c[0]+=2;r=Q(1,10**6)
lo=[p0[j]-r for j in range(7)];hi=[p0[j]+r for j in range(7)]
def c7(lo,hi):
 out=[]
 for e in (0,1):
  for o in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(e==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(o==0) else hi[j]
   out.append(a)
 return out
def c6(lo,hi):
 out=[]
 for e in (0,1):
  for o in (0,1):
   a=[Q(0)]*7;a[6]=Q(1)
   for j in (0,2,4):a[j]=lo[j] if ((j//2)%2==0)==(e==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(o==0) else hi[j]
   out.append(a)
 return out
pcs=c7(lo,hi);qlo=[Q(j+1,7)*lo[j+1] for j in range(6)];qhi=[Q(j+1,7)*hi[j+1] for j in range(6)];qcs=c6(qlo,qhi)
# Generic Gaussian minor helper is checked independently by frozen replay.
if not all(minor(a,k)>0 for a in pcs+qcs for k in range(1,len(a))):raise ValueError('HURWITZ')
H=pv(q0,c);hproof=exact_nonnegative_halfline(H,maxdepth=40,maxnodes=12000)
if hproof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in hproof['leaves'] for v in leaf['coefficients']):raise ValueError('DERIVATIVE_CENTER')
hdelta=min(Q(v) for leaf in hproof['leaves'] for v in leaf['coefficients']);margin=hdelta-sum(abs(v) for v in c)*3*r
pmargin=Q(1)-sum(abs(v) for v in p0)*7*r
if hdelta!=Q(5,1024) or margin<=0 or pmargin<=0:raise ValueError('MARGIN')
b0=[Q(0)]+[Q(7,j+1)*c[j] for j in range(7)];P=pv(p0,b0);Ep=[p0[0],-p0[2],p0[4],-p0[6]]
if ev(Ep,Q(1))!=8 or ev(P,Q(1))!=8 or ev(Ep,Q(1,2))!=Q(-13,8) or ev(P,Q(1,2))!=Q(-2421,128):raise ValueError('LINE_OBSTRUCTION')
pp=[pv(a,p0) for a in pcs];pproofs=[whole_halfline(v,max_depth=40,max_nodes=18000) for v in pp]
if not all(z['status']=='STRICT_POSITIVITY' for z in pproofs):raise ValueError('P_PROOF')
for v,pr in zip(pp,pproofs):verify_leaves_by_power(v,pr)
qh=[pv(a,c) for a in qcs];qproofs=[exact_nonnegative_halfline(v,maxdepth=40,maxnodes=18000) for v in qh]
if not all(z['status']=='NONNEGATIVE_PROVED' and all(Q(v)>0 for leaf in z['leaves'] for v in leaf['coefficients']) for z in qproofs):raise ValueError('Q_PROOF')
print('derivative lifting full-width counterexample:',{'radius':str(r),'p_center':[str(v) for v in p0],'derivative_center':[str(v) for v in q0],
 'derivative_common_c':[str(v) for v in c],'integrated_coeffs_without_constant':[str(v) for v in b0],
 'at_t_1_E_and_constant':[str(ev(Ep,Q(1))),str(ev(P,Q(1)))],
 'at_t_half_E_and_constant':[str(ev(Ep,Q(1,2))),str(ev(P,Q(1,2)))],
 'p_uniform_margin':str(pmargin),'derivative_uniform_margin':str(margin),'p_leaf_counts':[len(v['leaves']) for v in pproofs],
 'derivative_leaf_counts':[len(v['leaves']) for v in qproofs]})
