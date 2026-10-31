#!/usr/bin/env python3
"""Cyclotomic resultant witnesses for 5 distinct supported eigenvalues."""
import collections,datetime,gzip,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(F(0),)*8;O=(F(1),)+(F(0),)*7;phi=[1,-1,0,1,-1,1,0,-1,1]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 q=[F(0)]*15
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:q[i+j]+=x*y
 for k in range(14,7,-1):
  v=q[k]
  if v:
   for j in range(8):q[k-8+j]-=v*phi[j]
 return tuple(q[:8])
r=(F(0),F(1))+(F(0),)*6;powers=[O]
for _ in range(15):powers.append(mul(powers[-1],r))
assert powers[15]==O and len(set(powers[:15]))==15
C=[add(O,powers[k])for k in range(15)];Inv=[]
for k in range(15):
 q=Z
 for j in range(15):q=add(q,powers[k*j%15]if j%2==0 else neg(powers[k*j%15]))
 q=tuple(x/2 for x in q);assert mul(C[k],q)==O;Inv.append(q)
def conj(x):
 q=Z
 for j,c in enumerate(x):
  if c:q=add(q,tuple(c*y for y in powers[-j%15]))
 return q
# Exact 4x4 determinants and cofactor kernel bases in Q(zeta15).
def ksum(vals):
 q=Z
 for x in vals:q=add(q,x)
 return q
def det(A):
 n=len(A);q=Z
 for perm in itertools.permutations(range(n)):
  v=O
  for i,j in enumerate(perm):v=mul(v,A[i][j])
  parity=sum(perm[i]>perm[j]for i in range(n)for j in range(i+1,n))%2;q=add(q,neg(v)if parity else v)
 return q
def kernel(S,exponents):
 V=[[powers[(d*a)%15]for a in S]for d in exponents]
 for piv in itertools.combinations(range(6),4):
  D=det([[V[i][j]for j in piv]for i in range(4)])
  if D!=Z:break
 else:raise AssertionError('rank deficient')
 free=[j for j in range(6)if j not in piv];N=[[Z,Z]for _ in range(6)]
 for k,f in enumerate(free):
  N[f][k]=D
  for i,col in enumerate(piv):
   t=list(piv);t[i]=f;N[col][k]=neg(det([[V[r][j]for j in t]for r in range(4)]))
 assert all(ksum(mul(V[r][j],N[j][k])for j in range(6))==Z for r in range(4)for k in range(2))
 return piv,N
def coefficients(S):
 pL,L=kernel(S,(0,5,-2,3));pM,M=kernel(S,(0,5,-7,-2));V=[[powers[(d*a)%15]for a in S]for d in (0,-7,2,-5)]
 R=[[mul(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)]
 out=[]
 for I in itertools.combinations(range(6),4):out.append((I,mul(det([[V[r][j]for j in I]for r in range(4)]),det([R[j]for j in I]))))
 return pL,pM,out
def atan_bounds(x,n):
 q=F(0)
 for k in range(n):q+=(-1)**k*x**(2*k+1)/(2*k+1)
 rem=(-1)**n*x**(2*n+1)/(2*n+1);return min(q,q+rem),max(q,q+rem)
a0,a1=atan_bounds(F(1,5),40);b0,b1=atan_bounds(F(1,239),20);pi_lo,pi_hi=16*a0-4*b1,16*a1-4*b0
def cos_bounds(x,n=45):
 q=F(0)
 for k in range(n):q+=(-1)**k*x**(2*k)/math.factorial(2*k)
 rem=(-1)**n*x**(2*n)/math.factorial(2*n);return min(q,q+rem),max(q,q+rem)
COS=[(F(1),F(1))]+[(cos_bounds(2*j*pi_hi/15)[0],cos_bounds(2*j*pi_lo/15)[1])for j in range(1,8)]
def positive(q):
 assert conj(q)==q;lo=F(0)
 for x,(l,h)in zip(q,COS):lo+=x*(l if x>=0 else h)
 return lo>0
def compositions(n,k):
 if n==1:return [((k,),1)]
 out=[]
 for a in range(k+1):
  for b,m in compositions(n-1,k-a):out.append(((a,)+b,math.comb(k,a)*m))
 return out
def expand(S,coef,L,orientation):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];ref=next(v for I,v in coef if v!=Z);out={}
 for I,v in coef:
  if v==Z:continue
  pair=[j for j in range(6)if j not in I];e=[0]*6
  for j in pair:e[j]+=1
  c=mul(v,conj(ref));c=c if orientation>0 else neg(c);assert conj(c)==c;pieces=[(e,c)]
  for group in groups:
   k=L-sum(e[j]for j in group);assert k>=0;new=[]
   for count,weight in compositions(len(group),k):
    for q,val in pieces:
     qq=q.copy()
     for i,w in zip(group,count):qq[i]+=w
     factor=weight*3**k;new.append((qq,tuple(factor*x for x in val)))
   pieces=new
  for q,val in pieces:
   key=tuple(q);out[key]=add(out.get(key,Z),val)
 return out
def realphase(a,d,k):
 phase=powers[(-8*k)%15];phase=phase if k%2==0 else neg(phase);v=mul(phase,powers[(-d*a)%15]);return tuple(x/2 for x in add(v,conj(v)))
def selfterms(S,d,k):
 piv,N=kernel(S,(0,5,-d,5-d));h=[realphase(a,d,k)for a in S];tr=[];de=[]
 for j in range(6):
  weight=ksum(mul(conj(N[j][a]),N[j][a])for a in range(2));tr.append((tuple(i for i in range(6)if i!=j),mul(h[j],weight)))
 for i,j in itertools.combinations(range(6),2):
  v=sub(mul(N[i][0],N[j][1]),mul(N[i][1],N[j][0]));de.append((tuple(k for k in range(6)if k not in (i,j)),mul(mul(h[i],h[j]),mul(v,conj(v)))))
 return piv,tr,de
# Branchwise combinations of short-pair imbalance, row collisions and positive planes.
assert 5*1920**2-4289**2==36479>0
def short_groups(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transformation(S,branch):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];short=short_groups(S);assert len(short)==len(branch);choice={tuple(g):lo for g,lo in zip(short,branch)};T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if tuple(g)in choice:
   lo=choice[tuple(g)];assert lo in g;hi=next(j for j in g if j!=lo);T[lo][lo]=F(7,240);T[hi][lo]=F(73,240);T[hi][hi]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 return T
def transform(S,terms,branch):
 T=transformation(S,branch);out={}
 for indices,val in terms:
  if val==Z:continue
  pieces=[([0]*6,val)]
  for i in indices:
   new=[]
   for arr,x in pieces:
    for j in range(6):
     if T[i][j]:bb=arr.copy();bb[j]+=1;new.append((bb,tuple(T[i][j]*v for v in x)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),x)
 return out
def homog(S,poly,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for exp,val in poly.items():
  if val==Z:continue
  pieces=[(list(exp),val)]
  for g in groups:
   power=L-sum(exp[j]for j in g);assert power>=0;new=[]
   for cnt,fac in compositions(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,tuple(fac*v for v in x)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),x)
 return out
def checked_poly(S,terms,branch,L):
 poly=homog(S,transform(S,terms,branch),L);out=[]
 for ex,val in sorted(poly.items()):
  if val==Z:continue
  assert positive(val);out.append([list(ex),[str(x)for x in val]])
 assert out;return {'degree_per_residue':L,'positive_coefficients':out}
# Closed dyadic box cover; strict actual populations stay inside each global simplex.
def boxexpand(S,poly,box):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];assert all(len(g)==2 for g in groups);out={}
 for exp,val in poly.items():
  if val==Z:continue
  pieces=[([0]*6,val)]
  for (i,j),(lo,hi)in zip(groups,box):
   e,f=exp[i],exp[j];new=[]
   for a in range(e+1):
    for b in range(f+1):
     coef=math.comb(e,a)*math.comb(f,b)*lo**a*hi**(e-a)*(1-lo)**b*(1-hi)**(f-b)
     if not coef:continue
     for arr,x in pieces:
      arr=arr.copy();arr[i]=a+b;arr[j]=e+f-a-b;new.append((arr,tuple(coef*q for q in x)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),x)
 return out
def encode_poly(poly):
 entries=[]
 for exp,val in sorted(poly.items()):
  if val==Z:continue
  assert positive(val);entries.append([list(exp),[str(x)for x in val]])
 assert entries;return entries
# Rank-one cross-kernel discriminant.
def rank1_polynomial(S,pl,pm):
 L=kernel_fixed(S,(0,5,-2,3),pl);M=kernel_fixed(S,(0,5,-7,-2),pm);V=[[powers[(d*a)%15]for a in S]for d in (0,-7,2)]
 R=[[mul(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)];H=[]
 for col in range(4):
  poly={}
  for I in itertools.combinations(range(6),3):
   val=mul(det([[V[r][j]for j in I]for r in range(3)]),det([[R[j][c]for c in range(4)if c!=col]for j in I]));val=val if col%2==0 else neg(val);poly[tuple(int(j not in I)for j in range(6))]=val
  H.append(poly)
 def pmul(A,B):
  C={}
  for x,a in A.items():
   for y,b in B.items():
    e=tuple(i+j for i,j in zip(x,y));C[e]=add(C.get(e,Z),mul(a,b))
  return C
 A=pmul(H[0],H[3]);B=pmul(H[1],H[2]);return {e:sub(A.get(e,Z),B.get(e,Z))for e in set(A)|set(B)}
def kernel_fixed(S,exps,piv):
 V=[[powers[(d*a)%15]for a in S]for d in exps];D0=det([[V[i][j]for j in piv]for i in range(4)]);assert D0!=Z;free=[j for j in range(6)if j not in piv];N=[[Z,Z]for _ in range(6)]
 for c,f in enumerate(free):
  N[f][c]=D0
  for t,j in enumerate(piv):
   inds=list(piv);inds[t]=f;N[j][c]=neg(det([[V[r][q]for q in inds]for r in range(4)]))
 return N
def boundary_ok(S,poly,box):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];opts=[]
 for (i,j),(lo,hi)in zip(groups,box):
  o=[()]
  if lo>0:o.append((j,))
  if hi<1:o.append((i,))
  opts.append(o)
 for choice in itertools.product(*opts):
  zero={x for q in choice for x in q}
  if not any(v!=Z and all(ex[j]==0 for j in zero)for ex,v in poly.items()):return False
 return True
def realphase_poly(fp,k,sgn):
 ref=next(v for v in fp.values()if v!=Z);ph=powers[(-8*k)%15];ph=ph if k%2==0 else neg(ph);terms=[]
 for ex,val in fp.items():
  if val==Z:continue
  v=mul(mul(val,conj(ref)),ph);v=tuple(x/2 for x in add(v,conj(v)));v=v if sgn>0 else neg(v);terms.append((tuple(j for j,e in enumerate(ex)for _ in range(e)),v))
 return terms
def sign_poly(poly,sgn):return poly if sgn>0 else {k:neg(v)for k,v in poly.items()}
# Barycentric simplex covers for seven cyclic spectra; G tests kernel/self compatibility.
def pmul(A,B):
 C={}
 for x,a in A.items():
  if a==Z:continue
  for y,b in B.items():
   if b==Z:continue
   e=tuple(i+j for i,j in zip(x,y));C[e]=add(C.get(e,Z),mul(a,b))
 return C
def padd(A,B):
 C=dict(A)
 for k,v in B.items():C[k]=add(C.get(k,Z),v)
 return C
def pconj(A):return {k:conj(v)for k,v in A.items()}
def Hpolys(S,pl,pm):
 L=kernel_fixed(S,(0,5,-2,3),pl);M=kernel_fixed(S,(0,5,-7,-2),pm);V=[[powers[(d*a)%15]for a in S]for d in (0,-7,2)];R=[[mul(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)];H=[]
 for col in range(4):
  h={}
  for I in itertools.combinations(range(6),3):
   v=mul(det([[V[r][j]for j in I]for r in range(3)]),det([[R[j][c]for c in range(4)if c!=col]for j in I]));h[tuple(int(j not in I)for j in range(6))]=v if col%2==0 else neg(v)
  H.append(h)
 return L,M,H
def Gpolys(S,pl,pm):
 L,M,H=Hpolys(S,pl,pm)
 def Mt(N,d):return {(a,c):{tuple(int(k!=j)for k in range(6)):mul(mul(conj(N[j][a]),N[j][c]),powers[(-d*S[j])%15])for j in range(6)}for a in range(2)for c in range(2)}
 Mx=Mt(L,2);My=Mt(M,7);out=[]
 for b in range(2):
  G={}
  for a in range(2):
   for c in range(2):G=padd(G,pmul(pmul(H[a*2+b],Mx[a,c]),pconj(H[c*2+b])))
  out.append(G)
 for a in range(2):
  G={}
  for b in range(2):
   for c in range(2):G=padd(G,pmul(pmul(pconj(H[a*2+b]),My[b,c]),H[a*2+c]))
  out.append(G)
 return out
def multinom(n,k):
 if n==1:
  yield (k,),1;return
 for a in range(k+1):
  for rest,c in multinom(n-1,k-a):yield (a,)+rest,math.comb(k,a)*c
def simplex_expand(poly,groups,verts):
 out={}
 for exps,val in poly.items():
  if val==Z:continue
  pieces=[([0]*6,F(1))]
  for g,V in zip(groups,verts):
   m=len(g);ex={tuple([0]*m):F(1)}
   for c in range(m):
    e=exps[g[c]]
    if not e:continue
    new={}
    for loc,coef in ex.items():
     for cnt,mult in multinom(m,e):
      w=F(mult)
      for k in range(m):
       if cnt[k]:w*=V[k][c]**cnt[k]
      if not w:continue
      nl=tuple(loc[k]+cnt[k]for k in range(m));new[nl]=new.get(nl,F(0))+coef*w
    ex=new
   newp=[]
   for arr,v in pieces:
    for loc,coef in ex.items():
     if not coef:continue
     bb=arr.copy()
     for k in range(m):bb[g[k]]=loc[k]
     newp.append((bb,v*coef))
   pieces=newp
  for arr,v in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),tuple(v*x for x in val))
 return out
def faces_ok(keys,groups,verts):
 opts=[]
 for g,V in zip(groups,verts):
  m=len(g);o=[]
  for r in range(1,m+1):
   for W in itertools.combinations(range(m),r):
    if all(any(V[k][c]>0 for k in W)for c in range(m)):o.append({g[k]for k in range(m)if k not in W})
  opts.append(o)
 for ch in itertools.product(*opts):
  zero=set().union(*ch)
  if not any(all(k[j]==0 for j in zero)for k in keys):return False
 return True
def realphase_ref(poly,ref,k):
 ph=powers[(-8*k)%15];ph=ph if k%2==0 else neg(ph);out={}
 for e,val in poly.items():
  if val==Z:continue
  v=mul(mul(val,conj(ref)),ph);out[e]=tuple(x/2 for x in add(v,conj(v)))
 return out
def hom_p(S,ppoly,L):return homog(S,transform(S,[(tuple(j for j,c in enumerate(e)for _ in range(c)),v)for e,v in ppoly.items()if v!=Z],()),L)
def certify(Q,groups,verts):
 nz={k:v for k,v in Q.items()if v!=Z};enc=encode_poly(nz);assert faces_ok(list(nz),groups,verts);return enc
planfile=P/'frontier-20261029-cyclic15-simplex-cover-plan-v1.json';planraw=planfile.read_bytes();assert hashlib.sha256(planraw).hexdigest()=='5ebe39d3408cf9cef8b384868e3fe6e3f29d3032336388c73c60c5c93cbe734b';PLAN=json.loads(planraw)
manifest=P/'frontier-20261029-cyclic15-7-residual-spectra-v1.json';raw=manifest.read_bytes();assert hashlib.sha256(raw).hexdigest()=='176b424095a49fea70959cb313d85a5c4fd46ec693d5bfc1a0dbe10ce3a8c49a';MAN=json.loads(raw);allowed={tuple(q['representative'])for q in MAN['remaining_spectrum_classes']};assert len(allowed)==7
records=[]
for key,item in PLAN.items():
 S=tuple(item['spectrum']);assert S in allowed and not short_groups(S);groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];pl,pm=tuple(item['pivot_L']),tuple(item['pivot_M'])
 pl0,pm0,co=coefficients(S);assert tuple(pl0)==pl and tuple(pm0)==pm
 crossp={tuple(int(j not in I)for j in range(6)):v for I,v in co};cref=crossp[tuple(item['cross_ref'])];assert cref!=Z
 Fp=rank1_polynomial(S,pl,pm);fref=Fp[tuple(item['F_ref'])];assert fref!=Z
 Gs=Gpolys(S,pl,pm);grefs=[G[tuple(k)]for G,k in zip(Gs,item['G_refs'])];assert all(g!=Z for g in grefs)
 cache={};regions=[]
 for reg in item['regions']:
  verts=[[tuple(F(c)for c in vtx)for vtx in Vg]for Vg in reg['verts']];cert=reg['cert'];kind=cert[0];entry={'verts':reg['verts'],'cert':cert}
  for g,V in zip(groups,verts):
   assert len(V)==len(g) and all(len(v)==len(g) and all(c>=0 for c in v) and sum(v)==1 for v in V)
  if kind=='cross':
   if 'cross' not in cache:cache['cross']=hom_p(S,{e:mul(v,conj(cref))for e,v in crossp.items()},2)
   Q=simplex_expand(cache['cross'],groups,verts)
   if cert[1]<0:Q={k:neg(v)for k,v in Q.items()}
   entry['polys']=[certify(Q,groups,verts)]
  elif kind=='self':
   d,k=cert[1],cert[2];ck=('self',d,k)
   if ck not in cache:
    piv,tr,de=selfterms(S,d,k);cache[ck]=(homog(S,transform(S,tr,()),3),homog(S,transform(S,de,()),3))
   t,dd=cache[ck];entry['polys']=[certify(simplex_expand(t,groups,verts),groups,verts),certify(simplex_expand(dd,groups,verts),groups,verts)]
  elif kind=='rank1':
   k=cert[1];ck=('rank1',k)
   if ck not in cache:cache[ck]=hom_p(S,realphase_ref(Fp,fref,k),6)
   entry['polys']=[certify(simplex_expand(cache[ck],groups,verts),groups,verts)]
  else:
   assert kind=='G';gi,k=cert[1],cert[2];ck=('G',gi,k)
   if ck not in cache:cache[ck]=hom_p(S,realphase_ref(Gs[gi],grefs[gi],k),9)
   entry['polys']=[certify(simplex_expand(cache[ck],groups,verts),groups,verts)]
  regions.append(entry)
 records.append({'spectrum':S,'pivot_L':pl,'pivot_M':pm,'cross_ref':item['cross_ref'],'F_ref':item['F_ref'],'G_refs':item['G_refs'],'G_names':item['G_names'],'regions':regions})
 print('certified',S,len(regions),flush=True)
assert {tuple(r['spectrum'])for r in records}==allowed
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_sha256':hashlib.sha256(planraw).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':records,'scope':'seven cyclic spectra; barycentric simplex covers by cross determinant, self-plane, rank-one and kernel-self compatibility tests','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-simplex-cover-proof-v1.json.gz'
with gzip.open(out,'wt',encoding='utf8')as f:json.dump(obj,f,separators=(',',':'))
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'clock_finish':obj['clock_finish'],'classes':len(records),'regions':sum(len(r['regions'])for r in records),'status':'PRODUCED_UNREPLAYED'},indent=2))
