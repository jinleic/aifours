# Exact bounded test of a possible derivative/integration lift. This is not a
# general theorem: seek a stable p and common c for p'/7 for which no additive
# integration constant makes b/p SPR. Every failure uses two exact frequencies.
from fractions import Fraction as Q
from math import comb

def pv(a,b):
 def part(v):return [v[j]*(-1)**(j//2) for j in range(0,len(v),2)],[v[j]*(-1)**((j-1)//2) for j in range(1,len(v),2)]
 E,O=part(a);F,G=part(b);ee=conv_exact(E,F);oo=conv_exact(O,G);out=ee+[Q(0)]*max(0,len(oo)+1-len(ee))
 for j,x in enumerate(oo):out[j+1]+=x
 return out
def ev(a,t):return sum(v*t**j for j,v in enumerate(a))
p=[Q(comb(7,j)) for j in range(8)];q=[Q(comb(6,j)) for j in range(7)];E=[p[0],-p[2],p[4],-p[6]]
grid=[Q(1,100),Q(1,20),Q(1,10),Q(1,4),Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(5),Q(10),Q(20),Q(50),Q(100)]
deriv_stress=[]
for power in range(6):
 for dv in (Q(-10),Q(-5),Q(-2),Q(-1),Q(-1,2),Q(-1,10),Q(1,10),Q(1,2),Q(1),Q(2),Q(5),Q(10),Q(20)):
  c=q[:];c[power]+=dv
  if not all(x>0 for x in c):continue
  H=pv(q,c);proof=exact_nonnegative_halfline(H,maxdepth=34,maxnodes=10000)
  if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in proof['leaves'] for v in leaf['coefficients']):continue
  b=[Q(0)]+[Q(7,j+1)*c[j] for j in range(7)];C=pv(p,b);lower=[];upper=[]
  for t in grid:
   e=ev(E,t);val=ev(C,t)
   if e>0:lower.append((-val/e,t))
   elif e<0:upper.append((-val/e,t))
  L=max(lower,default=(Q(0),Q(0)));U=min(upper,default=(None,None))
  if U[0] is not None and L[0]>=U[0]:
   deriv_stress.append({'power':power,'delta':str(dv),'status':'INTEGRATION_LINE_IMPOSSIBLE','c':[str(v) for v in c],
     'derivative_pairing_poly':[str(v) for v in H],'derivative_proof':proof,'lower_bound':str(L[0]),'lower_t':str(L[1]),
     'upper_bound':str(U[0]),'upper_t':str(U[1]),'b_without_constant':[str(v) for v in b]});break
 else:continue
 break
print('derivative/integration bounded stress:',{'status':deriv_stress[0]['status'] if deriv_stress else 'NO_FINITE_LINE_OBSTRUCTION_FOUND',
  'power':deriv_stress[0]['power'] if deriv_stress else None,'delta':deriv_stress[0]['delta'] if deriv_stress else None,
  'lower_bound':deriv_stress[0]['lower_bound'] if deriv_stress else None,'upper_bound':deriv_stress[0]['upper_bound'] if deriv_stress else None})
