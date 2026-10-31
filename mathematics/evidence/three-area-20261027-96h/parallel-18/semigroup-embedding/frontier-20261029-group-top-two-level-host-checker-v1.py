"""Exact finite check of the explicit RIGHTSN host for RRL sources S = H ⊔ K
(H a subgroup with identity h, K a completely simple ideal) over D8 = M[C2;2,2;P], P=((0,0),(0,1)).
C2 is written additively.  The construction is the written one in
frontier-20261029-group-top-two-level-host-v1.md; this program only checks finite instances.
It rebuilds sources as 2-generated regular subsemigroups of P(B5,D8) (B5 with its involutory
automorphism), keeps those of the form H ⊔ K, builds the band B = (C2xC2 rectangular) ⊔ Const(Omega),
and checks: band laws, right-regular local monoids at every element, C2 acts by automorphisms,
every source/host product equation, and separation of every same-fibre R-pair."""
import random,sys
from itertools import product
P8=((0,0),(0,1))
B5=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));SW=(0,3,4,1,2)
PB=[(b,(i,g,l)) for b in range(5) for i in range(2) for g in range(2) for l in range(2)];PIX={x:k for k,x in enumerate(PB)}
def pmul(x,y):
 b,(i,g,l)=x;c,(j,h,m)=y;w=g^P8[l][j]
 return (B5[b][SW[c] if w else c],(i,w^h,m))
PT=[[PIX[pmul(x,y)] for y in PB] for x in PB];PACT=[x[1] for x in PB]
def closure(gens):
 S=set(gens);todo=list(gens)
 while todo:
  x=todo.pop()
  for y in list(S):
   for z in (PT[x][y],PT[y][x]):
    if z not in S:S.add(z);todo.append(z)
 return sorted(S)
def analyse(M,act):
 N=len(M);E=[x for x in range(N) if M[x][x]==x]
 if not all(any(M[M[x][y]][x]==x for y in range(N)) for x in range(N)):return None
 if not all((M[x][x]==x)==(act[x][1]==P8[act[x][2]][act[x][0]]) for x in range(N)):return None
 # minimal ideal K: elements x with SxS minimal
 ideal=lambda x:frozenset(M[M[a][x]][b] for a in range(N) for b in range(N))
 sizes={x:len(ideal(x)) for x in range(N)};mn=min(sizes.values());K=sorted(x for x in range(N) if sizes[x]==mn and x in ideal(x))
 Kset=set(K);Hs=[x for x in range(N) if x not in Kset]
 hs=[x for x in Hs if M[x][x]==x]
 if len(hs)!=1:return None
 h=hs[0]
 if not all(M[h][x]==x==M[x][h] for x in Hs):return None
 if not all(M[x][y] in Hs for x in Hs for y in Hs):return None
 if not all(any(M[x][y]==h for y in Hs) for x in Hs):return None   # H is a group
 # K completely simple: every element of K lies in a subgroup of K
 if not all(any(M[M[x][y]][x]==x and M[M[y][x]][y]==y and M[x][y]==M[y][x] for y in K) for x in K):return None
 return K,Hs,h
def build(M,act,K,H,h):
 Kset=set(K)
 col={k:frozenset(x for x in K if {M[z][x] for z in K}=={M[z][k] for z in K}) for k in K}
 cols=sorted(set(col.values()),key=lambda c:min(c))
 def cdot(c,t):return col[M[min(c)][t]]
 mu={c:act[min(c)][2] for c in cols}
 ih,lh=act[h][0],act[h][2];ph=P8[lh][ih]
 ghat={t:act[t][1]^ph for t in H}
 Hhat=set(ghat.values())
 vof=lambda w:w[0]^P8[mu[w[1]]][ih]
 hfixed=lambda c:cdot(c,h)==c
 def orbit(w):
  v=vof(w);return frozenset((b^ph,cdot(w[1],t)) for t in H for b in [v^ghat[t]])
 def act_pt(p,a,b):
  if p[0]=='R':
   w=p[1];v=vof(w)
   ts=[t for t in H if v^ghat[t]==b]
   if hfixed(w[1]):
    if ts:return ('R',(b^ph,cdot(w[1],ts[0])))
    return ('O',orbit(w),b)
   if a==v:
    if ts:return ('R',(b^ph,cdot(w[1],ts[0])))
    return ('O',orbit((v^ph,cdot(w[1],h))),b)
   return ('M',w,a,b)
  if p[0]=='O':
   w0=min(p[1],key=str);return act_pt(('R',w0),vof(w0),b)
  return act_pt(('R',p[1]),p[2],b)
 def gact_pt(p):
  if p[0]=='R':return ('R',(p[1][0]^1,p[1][1]))
  if p[0]=='O':return ('O',frozenset((m^1,c) for m,c in p[1]),p[2]^1)
  return ('M',(p[1][0]^1,p[1][1]),p[2]^1,p[3]^1)
 real=[('R',(m,c)) for m in (0,1) for c in cols]
 pts=list(real);seen=set(pts);i=0
 while i<len(pts):
  p=pts[i];i+=1
  for a,b in product((0,1),repeat=2):
   for q in (act_pt(p,a,b),gact_pt(p)):
    if q not in seen:seen.add(q);pts.append(q)
 tops=[(a,b) for a in (0,1) for b in (0,1)]
 elems=[('T',x) for x in tops]+[('C',p) for p in pts];ix={e:k for k,e in enumerate(elems)}
 def mul(x,y):
  if y[0]=='C':return y
  if x[0]=='T':return ('T',(x[1][0],y[1][1]))
  return ('C',act_pt(x[1],*y[1]))
 Bt=[[ix[mul(x,y)] for y in elems] for x in elems]
 def gact(x):return ('T',(x[1][0]^1,x[1][1]^1)) if x[0]=='T' else ('C',gact_pt(x[1]))
 alpha=[ix[gact(e)] for e in elems]
 def beta(s):
  if s in Kset:return ix[('C',('R',(act[s][1],col[s])))]
  return ix[('T',(0,ghat[s]))]
 return Bt,alpha,beta,len(real),len(pts)
def check(M,act,K,H,h):
 Bt,alpha,beta,nreal,npts=build(M,act,K,H,h);n=len(Bt);R=range(n)
 assert all(Bt[x][x]==x for x in R)
 assert all(Bt[Bt[x][y]][z]==Bt[x][Bt[y][z]] for x in R for y in R for z in R)
 for e in R:
  loc=[Bt[Bt[e][x]][e] for x in R];loc=sorted(set(loc))
  assert all(Bt[Bt[x][y]][x]==Bt[y][x] for x in loc for y in loc)
 assert all(alpha[alpha[x]]==x for x in R)
 assert all(alpha[Bt[x][y]]==Bt[alpha[x]][alpha[y]] for x in R for y in R)
 N=len(M)
 for s,t in product(range(N),repeat=2):
  w=act[s][1]^P8[act[s][2]][act[t][0]];bt=alpha[beta(t)] if w else beta(t)
  assert beta(M[s][t])==Bt[beta(s)][bt],('host equation',s,t)
 E=[x for x in range(N) if M[x][x]==x]
 Rp=[(e,f) for e in E for f in E if e<f and act[e]==act[f] and M[e][f]==f and M[f][e]==e]
 assert Rp and all(beta(e)!=beta(f) for e,f in Rp)
 return n,nreal,npts,len(Rp)
def main(seed,want):
 random.seed(seed);done=0;tried=0;seenT=set()
 while done<want and tried<200000:
  tried+=1;g=random.sample(range(40),2);S=closure(g)
  pos={s:k for k,s in enumerate(S)};M=[[pos[PT[a][b]] for b in S] for a in S];act=[PACT[s] for s in S]
  if len(set(act))<8:continue
  key=tuple(map(tuple,M))
  if key in seenT:continue
  seenT.add(key)
  r=analyse(M,act)
  if r is None:continue
  K,H,h=r
  E=[x for x in range(len(M)) if M[x][x]==x]
  if not any(e<f and act[e]==act[f] and M[e][f]==f and M[f][e]==e for e in E for f in E):continue
  n,nreal,npts,nR=check(M,act,K,H,h)
  print('source',len(M),'|H|',len(H),'|K|',len(K),'band',n,'real columns',nreal,'points',npts,'R-pairs separated',nR)
  done+=1
 print('PASS',done,'distinct H-plus-CS-ideal sources: band, RIGHTSN locals, C2 automorphism, all host equations, all same-fibre R-pairs separated')
 print('LIMIT finite instances only; the universal statement is the written proof')
if __name__=='__main__':
 main(int(sys.argv[1]) if len(sys.argv)>1 else 1,int(sys.argv[2]) if len(sys.argv)>2 else 10)
