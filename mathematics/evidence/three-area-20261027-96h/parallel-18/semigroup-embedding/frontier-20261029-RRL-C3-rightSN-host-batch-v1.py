"""Bounded exploration (NOT proof), different family: sources are regular subsemigroups of
P(C,D) with C = B012^1 (7-element non-globally-regular RIGHTSN band B012 with an adjoined identity,
hence NOT SN), C3 rotating the three u/v indices, D = M[C3;{0,1},{0,1};P].  Keep right-regular-local
(RRL) original sources with local R-pairs; Z3 searches a faithful RIGHTSN host over the GIVEN actor
with a C3 action (sigma^3=1); SAT models are exactly rechecked."""
import sys,json,random,time
from itertools import product
import z3
# B012: x=0, u_i=1+i, v_i=4+i ; identity 7
def bm(a,b):
 if a==7:return b
 if b==7:return a
 if b==0:return 0
 if a==0:return b+3 if 1<=b<=3 else b
 return a if 1<=b<=3 else b
def rot(b):
 if b in (0,7):return b
 off=1 if b<=3 else 4;return off+(b-off+1)%3
def act(g,b):
 for _ in range(g%3):b=rot(b)
 return b
def make(P):
 D=[(i,g,l) for i in range(2) for g in range(3) for l in range(2)]
 H=[(b,d) for b in range(8) for d in D];ix={h:k for k,h in enumerate(H)}
 def hm(x,y):
  b,(i,g,l)=x;c,(j,h,u)=y;w=(g+P[l][j])%3;return(bm(b,act(w,c)),(i,(w+h)%3,u))
 return H,[[ix[hm(x,y)] for y in H] for x in H]
def closure(T,gens,cap=60):
 S=set(gens);fr=list(gens)
 while fr:
  new=[]
  for x in fr:
   for y in list(S):
    for z in (T[x][y],T[y][x]):
     if z not in S:
      S.add(z);new.append(z)
      if len(S)>cap:return None
  fr=new
 return sorted(S)
def original_RRL(T,S,act_of):
 pos={s:k for k,s in enumerate(S)};n=len(S);M=[[pos[T[a][b]] for b in S] for a in S]
 if not all(any(M[M[x][y]][x]==x and M[M[y][x]][y]==y for y in range(n)) for x in range(n)):return None
 E=[x for x in range(n) if M[x][x]==x];fib={}
 for e in E:fib.setdefault(act_of[S[e]],[]).append(e)
 for F in fib.values():
  for a,b,c,d in product(F,repeat=4):
   if M[M[M[M[a][b]][c]][d]][a]!=M[M[M[M[M[M[a][b]][c]][a]][c]][d]][a]:return None
 C=[[x for x in E if M[M[g][x]][g]==x] for g in E]
 if not all(M[M[x][y]][x]==M[y][x] for K in C for x in K for y in K):return None
 locR=sum(1 for K in C for x in K for y in K if x<y and M[x][y]==y and M[y][x]==x)
 return locR
def find_host(S,mul,actor,n,P,tmo):
 tag=str(random.random());Bs,el=z3.EnumSort('B'+tag,['e%d_%s'%(k,tag) for k in range(n)])
 m=z3.Function('m'+tag,Bs,Bs,Bs);sg=z3.Function('s'+tag,Bs,Bs);beta={s:z3.Const('b%d_%s'%(s,tag),Bs) for s in S}
 so=z3.Solver();so.set('timeout',tmo)
 A=lambda w,v:v if w==0 else (sg(v) if w==1 else sg(sg(v)))
 for x in el:so.add(m(x,x)==x,sg(sg(sg(x)))==x)
 for x,y in product(el,repeat=2):so.add(sg(m(x,y))==m(sg(x),sg(y)))
 for x,y,z in product(el,repeat=3):
  so.add(m(m(x,y),z)==m(x,m(y,z)))
  so.add(m(m(m(m(m(m(x,y),x),z),x),y),x)==m(m(m(m(x,z),x),y),x))
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];w=(g+P[l][j])%3
  so.add(beta[mul[(s,t)]]==m(beta[s],A(w,beta[t])))
 for s,t in product(S,repeat=2):
  if s<t and actor[s]==actor[t]:so.add(beta[s]!=beta[t])
 r=so.check()
 if r!=z3.sat:return str(r),None
 md=so.model();idx={str(e):k for k,e in enumerate(el)};ev=lambda t:idx[str(md.eval(t,model_completion=True))]
 return 'sat',([[ev(m(x,y)) for y in el] for x in el],[ev(sg(x)) for x in el],{s:ev(beta[s]) for s in S})
def recheck(S,mul,actor,P,Mv,sv,bv):
 n=len(Mv);R=range(n);mm=lambda *xs:__import__('functools').reduce(lambda a,b:Mv[a][b],xs)
 a3=lambda w,v:v if w==0 else (sv[v] if w==1 else sv[sv[v]])
 assert all(Mv[x][x]==x for x in R) and all(Mv[Mv[x][y]][z]==Mv[x][Mv[y][z]] for x,y,z in product(R,repeat=3))
 assert all(mm(e,x,e,y,e,x,e)==mm(e,y,e,x,e) for e,x,y in product(R,repeat=3))
 assert all(sv[sv[sv[x]]]==x and sv[Mv[x][y]]==Mv[sv[x]][sv[y]] for x,y in product(R,repeat=2))
 for s,t in product(S,repeat=2):
  i,g,l=actor[s];j,h,u=actor[t];w=(g+P[l][j])%3
  assert bv[mul[(s,t)]]==Mv[bv[s]][a3(w,bv[t])]
 assert len({(bv[s],actor[s]) for s in S})==len(S)
if __name__=='__main__':
 seed,count,NMAX,tmo=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]);random.seed(seed);done=0;tried=0
 while done<count:
  P=[[0,0],[0,random.randrange(1,3)]];H,T=make(P);act_of={k:H[k][1] for k in range(len(H))}
  tried+=1;gens=random.sample(range(len(H)),random.randint(2,4));S=closure(T,gens)
  if S is None:continue
  locR=original_RRL(T,S,act_of)
  if not locR:continue
  mul={(s,t):T[s][t] for s in S for t in S};actor={s:H[s][1] for s in S}
  rec={'P':P,'size':len(S),'local_R_pairs':locR,'gens':[str(H[g]) for g in gens],'runs':[]}
  for n in range(2,NMAX+1):
   t0=time.time();r,sol=find_host(S,mul,actor,n,P,tmo);rec['runs'].append((n,r,round(time.time()-t0,1)))
   if r=='sat':recheck(S,mul,actor,P,*sol);rec['rightSN_host_band_size']=n;break
  done+=1;print(json.dumps(rec));sys.stdout.flush()
 print(json.dumps({'seed':seed,'sources':done,'generated':tried}))
