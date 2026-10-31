#!/usr/bin/env python3
"""Independent Q(sqrt5)[omega,eta] replay of the seven-spectrum simplex covers."""
import collections,datetime,gzip,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-simplex-cover-proof-v1.json.gz';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='9c7914fb7bbd1e89ff9c423fb4b65e17f1c604a88a4ed38bfb48550580c6b29d'
with gzip.open(src,'rt',encoding='utf8')as f:D=json.load(f)
manifest=P/'frontier-20261029-cyclic15-7-residual-spectra-v1.json';mr=manifest.read_bytes();assert hashlib.sha256(mr).hexdigest()=='176b424095a49fea70959cb313d85a5c4fd46ec693d5bfc1a0dbe10ce3a8c49a';MM=json.loads(mr)
z=(F(0),F(0));o=(F(1),F(0))
def a(x,y):return(x[0]+y[0],x[1]+y[1])
def n(x):return(-x[0],-x[1])
def s(x,y):return a(x,n(y))
def m(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def oa(x,y):return(a(x[0],y[0]),a(x[1],y[1]))
def on(x):return(n(x[0]),n(x[1]))
def om(x,y):
 ac=m(x[0],y[0]);bd=m(x[1],y[1]);return(s(ac,bd),s(a(m(x[0],y[1]),m(x[1],y[0])),bd))
c=(F(-1,2),F(1,2))
def km(x,y):
 ac=om(x[:2],y[:2]);bd=om(x[2:],y[2:]);bc=om(x[2:],y[:2]);ad=om(x[:2],y[2:]);cbd=(m(c,bd[0]),m(c,bd[1]));return oa(ac,on(bd))+oa(oa(ad,bc),cbd)
Z=(z,z,z,z);O=(o,z,z,z)
def ka(x,y):return tuple(a(v,w)for v,w in zip(x,y))
def kn(x):return tuple(n(v)for v in x)
def conj(x):
 A,B,C,D=x;return(s(a(s(A,B),m(c,C)),m(c,D)),s(n(B),m(c,D)),s(D,C),D)
def scale(x,k):return tuple((v[0]*k,v[1]*k)for v in x)
zeta=(o,o,n(c),n(c));powers=[O]
for _ in range(15):powers.append(km(powers[-1],zeta))
assert powers[15]==O and conj(zeta)==powers[14]
def summ(xs):
 q=Z
 for x in xs:q=ka(q,x)
 return q
def det(A):
 N=len(A);q=Z
 for perm in itertools.permutations(range(N)):
  v=O
  for i,j in enumerate(perm):v=km(v,A[i][j])
  parity=sum(perm[i]>perm[j]for i in range(N)for j in range(i+1,N))%2;q=ka(q,kn(v)if parity else v)
 return q
def kernel(S,exps,piv):
 assert len(piv)==4 and len(set(piv))==4;V=[[powers[(d*x)%15]for x in S]for d in exps];D=det([[V[i][j]for j in piv]for i in range(4)]);assert D!=Z
 free=[j for j in range(6)if j not in piv];N=[[Z,Z]for _ in range(6)]
 for k,f in enumerate(free):
  N[f][k]=D
  for i,j in enumerate(piv):
   q=list(piv);q[i]=f;N[j][k]=kn(det([[V[r][x]for x in q]for r in range(4)]))
 assert all(summ(km(V[r][j],N[j][k])for j in range(6))==Z for r in range(4)for k in range(2));return N
def coeffs(S,pL,pM):
 L=kernel(S,(0,5,-2,3),pL);M=kernel(S,(0,5,-7,-2),pM);E=[[powers[(d*x)%15]for x in S]for d in (0,-7,2,-5)]
 R=[[km(conj(L[j][a0]),M[j][b])for a0 in range(2)for b in range(2)]for j in range(6)]
 return [(I,km(det([[E[r][j]for j in I]for r in range(4)]),det([R[j]for j in I])))for I in itertools.combinations(range(6),4)]

def ks(x,y):return ka(x,kn(y))
def comps(n,k):
 if n==1:return [((k,),1)]
 q=[]
 for i in range(k+1):
  for rest,v in comps(n-1,k-i):q.append(((i,)+rest,math.comb(k,i)*v))
 return q
def expand(S,coef,L,orient):
 groups=[[j for j,x in enumerate(S)if x%3==r]for r in range(3)];ref=next(v for I,v in coef if v!=Z);out={}
 for I,v in coef:
  if v==Z:continue
  ex=[0]*6
  for j in range(6):
   if j not in I:ex[j]+=1
  val=km(v,conj(ref));val=val if orient>0 else kn(val);assert conj(val)==val;pieces=[(ex,val)]
  for g in groups:
   power=L-sum(ex[j]for j in g);assert power>=0;new=[]
   for cs,weight in comps(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cs):arr[j]+=k
     new.append((arr,scale(x,weight*3**power)))
   pieces=new
  for arr,x in pieces:
   key=tuple(arr);out[key]=ka(out.get(key,Z),x)
 return out
# Rational enclosures via Machin's identity and alternating Taylor bounds.
def atan_bound(x,N):
 total=sum(((-1)**k*x**(2*k+1)/(2*k+1)for k in range(N)),F(0));rem=(-1)**N*x**(2*N+1)/(2*N+1);return min(total,total+rem),max(total,total+rem)
a0,a1=atan_bound(F(1,5),42);b0,b1=atan_bound(F(1,239),22);pl,ph=16*a0-4*b1,16*a1-4*b0
def cb(x,N=47):
 total=sum(((-1)**k*x**(2*k)/math.factorial(2*k)for k in range(N)),F(0));rem=(-1)**N*x**(2*N)/math.factorial(2*N);return min(total,total+rem),max(total,total+rem)
cos=[(F(1),F(1))]+[(cb(2*j*ph/15)[0],cb(2*j*pl/15)[1])for j in range(1,8)]
def positive_phi(v):
 lo=F(0)
 for x,(l,h)in zip(v,cos):lo+=x*(l if x>=0 else h)
 return lo>0
def phase_real(a0,d,k):
 ph=powers[(-8*k)%15];ph=ph if k%2==0 else kn(ph);v=km(ph,powers[(-d*a0)%15]);return scale(ka(v,conj(v)),F(1,2))
def selfterms(S,d,k,piv):
 N=kernel(S,(0,5,-d,5-d),piv);h=[phase_real(x,d,k)for x in S];tr=[];de=[]
 for j in range(6):tr.append((tuple(x for x in range(6)if x!=j),km(h[j],summ(km(conj(N[j][b]),N[j][b])for b in range(2)))))
 for i,j in itertools.combinations(range(6),2):
  v=ks(km(N[i][0],N[j][1]),km(N[i][1],N[j][0]));de.append((tuple(x for x in range(6)if x not in(i,j)),km(km(h[i],h[j]),km(v,conj(v)))))
 return tr,de
assert 5*1920**2-4289**2==36479>0
def short_groups(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transform(S,terms,branch):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];ss=short_groups(S);assert len(ss)==len(branch);choices={tuple(g):lo for g,lo in zip(ss,branch)};T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if tuple(g)in choices:
   lo=choices[tuple(g)];assert lo in g;hi=next(j for j in g if j!=lo);T[lo][lo]=F(7,240);T[hi][lo]=F(73,240);T[hi][hi]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 out={}
 for indices,val in terms:
  if val==Z:continue
  pieces=[([0]*6,val)]
  for i in indices:
   new=[]
   for arr,x in pieces:
    for j in range(6):
     if T[i][j]:bb=arr.copy();bb[j]+=1;new.append((bb,scale(x,T[i][j])))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=ka(out.get(tuple(arr),Z),x)
 return out
def homog(S,poly,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for exp,val in poly.items():
  if val==Z:continue
  pieces=[(list(exp),val)]
  for g in groups:
   power=L-sum(exp[j]for j in g);assert power>=0;new=[]
   for cnt,fac in comps(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,scale(x,fac)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=ka(out.get(tuple(arr),Z),x)
 return out
def check_poly(S,terms,branch,record):
 global signs
 poly=homog(S,transform(S,terms,branch),record['degree_per_residue']);expect={}
 for ex,phi in record['positive_coefficients']:
  key=tuple(ex);assert key not in expect;v=[F(x)for x in phi];assert len(v)==8 and positive_phi(v)
  expect[key]=summ(scale(powers[i],x)for i,x in enumerate(v));assert expect[key]!=Z and conj(expect[key])==expect[key];signs+=1
 assert expect and {k:v for k,v in poly.items()if v!=Z}==expect
def rank1(S,pl,pm):
 L=kernel(S,(0,5,-2,3),pl);M=kernel(S,(0,5,-7,-2),pm);V=[[powers[(d*a)%15]for a in S]for d in(0,-7,2)];R=[[km(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)];H=[]
 for col in range(4):
  h={}
  for I in itertools.combinations(range(6),3):
   v=km(det([[V[r][j]for j in I]for r in range(3)]),det([[R[j][c]for c in range(4)if c!=col]for j in I]));h[tuple(int(j not in I)for j in range(6))]=v if col%2==0 else kn(v)
  H.append(h)
 out={}
 for (A,B),sgn in [((H[0],H[3]),1),((H[1],H[2]),-1)]:
  for x,a0 in A.items():
   for y,b in B.items():
    e=tuple(i+j for i,j in zip(x,y));v=km(a0,b);out[e]=ka(out.get(e,Z),v if sgn>0 else kn(v))
 return out
def first_pivot(S,exps):
 V=[[powers[(d*a)%15]for a in S]for d in exps]
 for piv in itertools.combinations(range(6),4):
  if det([[V[i][j]for j in piv]for i in range(4)])!=Z:return piv
 raise AssertionError
def pm_(A,B):
 C={}
 for x,a in A.items():
  if a==Z:continue
  for y,b in B.items():
   if b==Z:continue
   e=tuple(i+j for i,j in zip(x,y));C[e]=ka(C.get(e,Z),km(a,b))
 return C
def pa_(A,B):
 C=dict(A)
 for k,v in B.items():C[k]=ka(C.get(k,Z),v)
 return C
def pc_(A):return {k:conj(v)for k,v in A.items()}
def Hset(S,pl,pm):
 L=kernel(S,(0,5,-2,3),pl);M=kernel(S,(0,5,-7,-2),pm);V=[[powers[(d*a)%15]for a in S]for d in(0,-7,2)];R=[[km(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)];H=[]
 for col in range(4):
  h={}
  for I in itertools.combinations(range(6),3):
   v=km(det([[V[r][j]for j in I]for r in range(3)]),det([[R[j][c]for c in range(4)if c!=col]for j in I]));h[tuple(int(j not in I)for j in range(6))]=v if col%2==0 else kn(v)
  H.append(h)
 return L,M,H
def Gset(S,pl,pm):
 L,M,H=Hset(S,pl,pm)
 def Mt(N,d):return {(a,c):{tuple(int(k!=j)for k in range(6)):km(km(conj(N[j][a]),N[j][c]),powers[(-d*S[j])%15])for j in range(6)}for a in range(2)for c in range(2)}
 Mx=Mt(L,2);My=Mt(M,7);out=[]
 for b in range(2):
  G={}
  for a in range(2):
   for c in range(2):G=pa_(G,pm_(pm_(H[a*2+b],Mx[a,c]),pc_(H[c*2+b])))
  out.append(G)
 for a in range(2):
  G={}
  for b in range(2):
   for c in range(2):G=pa_(G,pm_(pm_(pc_(H[a*2+b]),My[b,c]),H[a*2+c]))
  out.append(G)
 return out
def mn(n,k):
 if n==1:
  yield (k,),1;return
 for a in range(k+1):
  for rest,c in mn(n-1,k-a):yield (a,)+rest,math.comb(k,a)*c
def sexp(poly,groups,verts):
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
     for cnt,mult in mn(m,e):
      w=F(mult)
      for k in range(m):
       if cnt[k]:w*=V[k][c]**cnt[k]
      if not w:continue
      nl=tuple(loc[k]+cnt[k]for k in range(m));new[nl]=new.get(nl,F(0))+coef*w
    ex=new
   np_=[]
   for arr,v in pieces:
    for loc,coef in ex.items():
     if not coef:continue
     bb=arr.copy()
     for k in range(m):bb[g[k]]=loc[k]
     np_.append((bb,v*coef))
   pieces=np_
  for arr,v in pieces:out[tuple(arr)]=ka(out.get(tuple(arr),Z),scale(val,v))
 return out
def faces(keys,groups,verts):
 opts=[]
 for g,V in zip(groups,verts):
  m=len(g);o=[]
  for r in range(1,m+1):
   for W in itertools.combinations(range(m),r):
    if all(any(V[k][c]>0 for k in W)for c in range(m)):o.append({g[k]for k in range(m)if k not in W})
  opts.append(o)
 for ch in itertools.product(*opts):
  zero=set().union(*ch)
  assert any(all(k[j]==0 for j in zero)for k in keys)
def rphase(poly,ref,k):
 ph=powers[(-8*k)%15];ph=ph if k%2==0 else kn(ph);out={}
 for e,val in poly.items():
  if val==Z:continue
  v=km(km(val,conj(ref)),ph);out[e]=scale(ka(v,conj(v)),F(1,2))
 return out
def homp(S,pp,L):return homog(S,transform(S,[(tuple(j for j,c in enumerate(e)for _ in range(c)),v)for e,v in pp.items()if v!=Z],()),L)
def compare(Q,entries):
 global signs
 exp={}
 for e,phi in entries:
  k=tuple(e);assert k not in exp;v=[F(x)for x in phi];assert len(v)==8 and positive_phi(v);exp[k]=summ(scale(powers[i],x)for i,x in enumerate(v));assert exp[k]!=Z and conj(exp[k])==exp[k];signs+=1
 assert exp and {k:v for k,v in Q.items()if v!=Z}==exp;return list(exp)
def tri_xy(V):return [(v[0],v[1])for v in V]
def cross2(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def separated(P1,P2):
 for poly in (P1,P2):
  n=len(poly)
  for i in range(n):
   a,b=poly[i],poly[(i+1)%n];s1=[cross2(a,b,q)for q in P1];s2=[cross2(a,b,q)for q in P2]
   if (all(x>=0 for x in s1)and all(x<=0 for x in s2))or(all(x<=0 for x in s1)and all(x>=0 for x in s2)):return True
 return False
def measure(g,V):
 if len(g)==1:return F(1)
 if len(g)==2:return abs(V[0][0]-V[1][0])
 a,b,c=tri_xy(V);return abs(cross2(a,b,c))/2
def disjoint(g,V1,V2):
 if len(g)==1:return False
 if len(g)==2:
  l1=sorted((V1[0][0],V1[1][0]));l2=sorted((V2[0][0],V2[1][0]));return l1[1]<=l2[0]or l2[1]<=l1[0]
 return separated(tri_xy(V1),tri_xy(V2))
allowed={tuple(q['representative'])for q in MM['remaining_spectrum_classes']};assert len(allowed)==7;signs=0;regions_total=0;kinds=collections.Counter();seen=set()
for rec in D['records']:
 S=tuple(rec['spectrum']);assert S in allowed and S not in seen and not short_groups(S);seen.add(S);groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];pl,pm=tuple(rec['pivot_L']),tuple(rec['pivot_M'])
 assert pl==first_pivot(S,(0,5,-2,3)) and pm==first_pivot(S,(0,5,-7,-2))
 co=coeffs(S,pl,pm);crossp={tuple(int(j not in I)for j in range(6)):v for I,v in co};cref=crossp[tuple(rec['cross_ref'])];assert cref!=Z
 F0=rank1(S,pl,pm);fref=F0[tuple(rec['F_ref'])];assert fref!=Z
 Gs=Gset(S,pl,pm);grefs=[G[tuple(k)]for G,k in zip(Gs,rec['G_refs'])];assert all(x!=Z for x in grefs)
 cache={};allv=[]
 for reg in rec['regions']:
  verts=[[tuple(F(c)for c in vtx)for vtx in Vg]for Vg in reg['verts']];allv.append(verts);regions_total+=1
  for g,V in zip(groups,verts):assert len(V)==len(g)and all(len(v)==len(g)and min(v)>=0 and sum(v)==1 for v in V)
  cert=reg['cert'];kind=cert[0];kinds[kind]+=1;polys=reg['polys']
  if kind=='cross':
   if 'c' not in cache:cache['c']=homp(S,{e:km(v,conj(cref))for e,v in crossp.items()},2)
   Q=sexp(cache['c'],groups,verts);Q=Q if cert[1]>0 else {k:kn(v)for k,v in Q.items()};faces(compare(Q,polys[0]),groups,verts)
  elif kind=='self':
   d,k=cert[1],cert[2];ck=('s',d,k)
   if ck not in cache:
    tr,de=selfterms(S,d,k,first_pivot(S,(0,5,-d,5-d)));cache[ck]=(homog(S,transform(S,tr,()),3),homog(S,transform(S,de,()),3))
   t,dd=cache[ck];faces(compare(sexp(t,groups,verts),polys[0]),groups,verts);faces(compare(sexp(dd,groups,verts),polys[1]),groups,verts)
  elif kind=='rank1':
   ck=('r',cert[1])
   if ck not in cache:cache[ck]=homp(S,rphase(F0,fref,cert[1]),6)
   faces(compare(sexp(cache[ck],groups,verts),polys[0]),groups,verts)
  else:
   assert kind=='G';gi,k=cert[1],cert[2];ck=('G',gi,k)
   if ck not in cache:cache[ck]=homp(S,rphase(Gs[gi],grefs[gi],k),9)
   faces(compare(sexp(cache[ck],groups,verts),polys[0]),groups,verts)
 total=F(1)
 for g in groups:total*=measure(g,[tuple(F(int(i==k))for i in range(len(g)))for k in range(len(g))])
 assert sum(math.prod(measure(g,V)for g,V in zip(groups,vv))for vv in allv)==total
 for v1,v2 in itertools.combinations(allv,2):assert any(disjoint(g,a,b)for g,a,b in zip(groups,v1,v2))
 print('replayed',S,len(allv),flush=True)
assert seen==allowed
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),'manifest_sha256':hashlib.sha256(mr).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'classes_checked':len(seen),'regions_checked':regions_total,'methods':dict(kinds),'strict_positive_coefficients':signs,
 'exact_measure_tiling_and_face_strictness':True,'remaining_cyclic_classes':0,'status':'PASS'}
(P/'frontier-20261029-cyclic15-simplex-cover-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
