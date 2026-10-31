# Exact feasibility and boundary-residual diagnostics at four w<8 slices.
# Positive vertices do not prove a continuum; a negative residual disproves
# only this gain-1000 ansatz, not septic synthesis.
from fractions import Fraction as Q

def bndry(u,lam,v,w):
 E0=root_cubic([u,Q(3),Q(6)],lam);E1=root_cubic([Q(1),Q(2),w],Q(1));O0=root_cubic([Q(1),Q(6),w],Q(1));O1=root_cubic([Q(2),Q(3),v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]
subeight={'tested':0,'all_residuals_positive':0,'negative':[],'inconclusive':[]}
for w in (Q(13,2),Q(7),Q(15,2),Q(79,10)):
 ul=(9*w-36)/(6*w+25);um=min(Q(1),w-6,w/9,w/(w+1));ua=(3*w-16)/9;us=9*w/(8*w+27)
 cuts=sorted(set([ul,um]+[v for v in (ua,us) if ul<v<um]))
 for u in cuts:
  low=max(Q(1),(2+3*w)/(9*u+18));high=min((w+3)/(u+9),w/(9*u))
  if low>high:raise ValueError('LAMBDA_DOMAIN')
  for lam in sorted(set((low,high))):
   for v in (w+2,7*w/5):
    vertices=bndry(u,lam,v,w);contacts=[(2,Q(1)),(3,Q(2)),(1,Q(3)),(0,Q(6)),(2,w)];T=[]
    for ci,t in contacts:
     a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
     T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
    A=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(A);subeight['tested']+=1
    if not D:subeight['inconclusive'].append({'w':str(w),'u':str(u),'lambda':str(lam),'v':str(v),'reason':'SINGULAR'});continue
    sgn=1 if D>0 else -1;rhs=[-row[0]-1000*row[6]-row[7] for row in T];b=[Q(0)]*8;b[0]=sgn*D;b[6]=sgn*D*1000;b[7]=sgn*D
    for col,j in enumerate((1,2,3,4,5)):
     M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=sgn*det5(M)
    if not all(x>0 for x in b):subeight['negative'].append({'w':str(w),'u':str(u),'lambda':str(lam),'v':str(v),'reason':'NONPOSITIVE_NUMERATOR'});break
    good=True;groups={i:[] for i in range(4)}
    for ci,t in contacts:groups[ci].append(t)
    for ci,a in enumerate(vertices):
     p=pairing_polynomial(a,b)
     for t in groups[ci]:p=quotient_by_root(quotient_by_root(p,t),t)
     proof=exact_nonnegative_halfline(p,maxdepth=40,maxnodes=10000)
     if proof['status']=='NEGATIVE':subeight['negative'].append({'w':str(w),'u':str(u),'lambda':str(lam),'v':str(v),'corner':ci,'t':proof['t'],'reason':'NEGATIVE_RESIDUAL'});good=False;break
     if proof['status']!='NONNEGATIVE_PROVED' or not all(Q(x)>0 for leaf in proof['leaves'] for x in leaf['coefficients']):subeight['inconclusive'].append({'w':str(w),'u':str(u),'corner':ci,'reason':proof['status']});good=False;break
    if good:subeight['all_residuals_positive']+=1
   if subeight['negative']:break
  if subeight['negative']:break
 if subeight['negative']:break
print('sub-eight node diagnostics:',subeight)
