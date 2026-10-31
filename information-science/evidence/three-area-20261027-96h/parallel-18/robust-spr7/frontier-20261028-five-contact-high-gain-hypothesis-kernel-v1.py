# Test a NEW constructive hypothesis on the 436 bounded five-contact designs:
# solve the 5 tangencies with b0=b7=0,b6=1, then exactly check all four
# residuals after removing t and contact squares. A grid pass is not a theorem.
from fractions import Fraction as Q
def parity(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
hyp={'tested':0,'strict_all_residuals':0,'nonpositive_coefficients':0,'negative_residual':[],'inconclusive':[]}
for idx,design in enumerate(five_design):
 lo,hi,center,vertices,contacts=five_box(design);T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 b=[Q(0)]*8;b[6]=Q(1)
 try:sol=solve5([[row[j] for j in (1,2,3,4,5)] for row in T],[-row[6] for row in T])
 except ValueError as e:
  if str(e)!='SINGULAR':raise
  hyp['tested']+=1;hyp['inconclusive'].append({'index':idx,'reason':'SINGULAR'});continue
 for j,v in zip((1,2,3,4,5),sol):b[j]=v
 if any(sum(row[k]*b[k] for k in range(8)) for row in T):raise ValueError('TANGENT')
 hyp['tested']+=1
 if not all(v>0 for v in b[1:7]):hyp['nonpositive_coefficients']+=1;hyp['negative_residual'].append({'index':idx,'design':[str(x) for x in design[:8]],'reason':'NONPOSITIVE_NUMERATOR_COEFFICIENT','b':[str(v) for v in b]});break
 rr={i:[] for i in range(4)}
 for ci,t in contacts:rr[ci].append(t)
 okay=True
 for ci,a in enumerate(vertices):
  P=pairing_polynomial(a,b);res=quotient_by_root(P,Q(0))
  for t in rr[ci]:res=quotient_by_root(quotient_by_root(res,t),t)
  proof=exact_nonnegative_halfline(res,maxdepth=32,maxnodes=4000)
  if proof['status']=='NEGATIVE':
   hyp['negative_residual'].append({'index':idx,'design':[str(x) for x in design[:8]],'reason':'NEGATIVE_RESIDUAL','corner':ci,'t':proof['t'],'residual':[str(x) for x in res],'b':[str(v) for v in b]});okay=False;break
  if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in proof['leaves'] for v in leaf['coefficients']):
   hyp['inconclusive'].append({'index':idx,'corner':ci,'reason':proof['status']});okay=False;break
 if okay:hyp['strict_all_residuals']+=1
 if hyp['negative_residual']:break
print('five-contact high-gain hypothesis screen:',hyp)
