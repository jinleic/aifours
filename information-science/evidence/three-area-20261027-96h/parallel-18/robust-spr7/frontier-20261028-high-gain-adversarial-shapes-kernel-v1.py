# Exact stress test of the five-contact high-gain criterion with widely
# separated root gaps and parameter choices close to admissible boundaries.
# A failed sufficient criterion is not an SPR counterexample.
from fractions import Fraction as Q
from random import Random
R=Random(20261101);edge=[Q(1,10000),Q(1,100),Q(1,2),Q(99,100),Q(9999,10000)]
adversarial={'proposals':0,'feasible_shapes':0,'strict_residual_success':0,'negative':[],'inconclusive':[]}
for trial in range(512):
 increments=[Q(R.randrange(1,21)*10**R.randrange(0,3)) for j in range(5)];ts=[];v=Q(0)
 for d in increments:v+=d;ts.append(v)
 t1,t2,t3,t4,t5=ts;adversarial['proposals']+=1
 vlo=max(t5,t1+t4+t5-t2-t3,t1*t4*t5/(t2*t3));vhi=(t1*t4+t1*t5+t4*t5-t2*t3)/(t2+t3)
 if vlo>=vhi:continue
 v=vlo+edge[R.randrange(len(edge))]*(vhi-vlo);u=t1*edge[R.randrange(len(edge))]
 qlo=max(Q(1),(t1*t2+t1*t5+t2*t5)/(u*t3+u*t4+t3*t4));qhi=min(t1*t2*t5/(u*t3*t4),(t1+t2+t5)/(u+t3+t4))
 if qlo>=qhi:continue
 lam=qlo+edge[R.randrange(len(edge))]*(qhi-qlo);design=(t1,t2,t3,t4,t5,v,str(u),str(lam),'','')
 try:lo,hi,center,vertices,contacts=five_box(design)
 except ValueError as e:
  adversarial['inconclusive'].append({'trial':trial+1,'reason':str(e)});continue
 adversarial['feasible_shapes']+=1;T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 b=[Q(0)]*8;b[6]=Q(1)
 try:vals=solve5([[row[j] for j in (1,2,3,4,5)] for row in T],[-row[6] for row in T])
 except ValueError as e:
  adversarial['inconclusive'].append({'trial':trial+1,'reason':str(e)});continue
 for j,x in zip((1,2,3,4,5),vals):b[j]=x
 if not all(v>0 for v in b[1:7]):
  adversarial['negative'].append({'trial':trial+1,'reason':'NONPOSITIVE_HIGH_GAIN_COEFFICIENT','design':[str(x) for x in design[:8]],'b':[str(x) for x in b]});break
 contactmap={i:[] for i in range(4)}
 for ci,t in contacts:contactmap[ci].append(t)
 good=True
 for ci,a in enumerate(vertices):
  P=pairing_polynomial(a,b);res=quotient_by_root(P,Q(0))
  for t in contactmap[ci]:res=quotient_by_root(quotient_by_root(res,t),t)
  pr=exact_nonnegative_halfline(res,maxdepth=36,maxnodes=6000)
  if pr['status']=='NEGATIVE':
   adversarial['negative'].append({'trial':trial+1,'reason':'NEGATIVE_HIGH_GAIN_RESIDUAL','corner':ci,'t':pr['t'],'design':[str(x) for x in design[:8]],'b':[str(x) for x in b],'residual':[str(x) for x in res]});good=False;break
  if pr['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in pr['leaves'] for v in leaf['coefficients']):
   adversarial['inconclusive'].append({'trial':trial+1,'corner':ci,'reason':pr['status']});good=False;break
 if good:adversarial['strict_residual_success']+=1
 if adversarial['negative']:break
 if adversarial['feasible_shapes']>=50:break
print('adversarial high-gain test:',adversarial)
