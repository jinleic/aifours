"""Bounded exploratory search (NOT a proof).  Host P(C,D) with C=B5^1 x Y4 (Y4=P({1,2}) meet),
D=M[C2;I,L;P].  C2 acts by the u/v swap on B5^1 (optional) and by swapping the two atoms of Y4,
so letters with identity B5-coordinate need NOT lie in subgroups.  Seeds realize the B5^1 SN failure
(u0,x,1,u1) in the first coordinate; second coordinates random.  Filters: regular, every idempotent
actor fibre SN.  Pattern abcda!=abcacda with prefix conditions modulo nu'."""
import random,json,sys,time
from itertools import product
from functools import reduce
def b5(a,b):
 if a==5:return b
 if b==5:return a
 if b==0:return 0
 if a==0:return b+2 if b in (1,2) else b
 if a in (1,2):return a if b in (1,2) else b
 return a if b in (1,2) else b
SW=[0,2,1,4,3,5];YS=[0,2,1,3]
class Host:
 def __init__(s,I,L,P,swapB):
  s.I,s.L,s.P,s.swapB=I,L,P,swapB
  s.C=[(b,y) for b in range(6) for y in range(4)]
  s.D=[(i,g,l) for i in range(I) for g in range(2) for l in range(L)]
  s.H=[(c,d) for c in s.C for d in s.D];s.ix={h:n for n,h in enumerate(s.H)};s.memo={}
 def act(s,g,c):
  if not g:return c
  b,y=c;return(SW[b] if s.swapB else b,YS[y])
 def dm(s,x,y):
  i,g,l=x;j,h,m=y;return(i,g^s.P[l][j]^h,m)
 def mul(s,x,y):
  k=(x,y)
  if k in s.memo:return s.memo[k]
  (c1,d1),(c2,d2)=s.H[x],s.H[y];w=d1[1]^s.P[d1[2]][d2[0]]
  c3=s.act(w,c2);z=s.ix[((b5(c1[0],c3[0]),c1[1]&c3[1]),s.dm(d1,d2))];s.memo[k]=z;return z
def closure(h,gens,cap=300):
 S=set(gens);fr=list(gens)
 while fr:
  new=[]
  for x in fr:
   for y in list(S):
    for z in (h.mul(x,y),h.mul(y,x)):
     if z not in S:
      S.add(z);new.append(z)
      if len(S)>cap:return None
  fr=new
 return sorted(S)
def analyse(h,S):
 m=h.mul;E=[x for x in S if m(x,x)==x]
 for x in S:
  if not any(m(m(x,y),x)==x and m(m(y,x),y)==y for y in S):return None,'nonregular'
 fib={}
 for e in E:fib.setdefault(h.H[e][1],[]).append(e)
 for F in fib.values():
  for a,b,c,d in product(F,repeat=4):
   if m(m(m(m(a,b),c),d),a)!=m(m(m(m(m(m(a,b),c),a),c),d),a):return None,'badfibre'
 par={x:x for x in S}
 def root(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 todo=[(e,f) for e in E for f in E if e!=f and m(e,f)==m(f,e)==e]
 while todo:
  a,b=todo.pop();ra,rb=root(a),root(b)
  if ra!=rb:
   par[rb]=ra
   for z in S:todo.append((m(a,z),m(b,z)));todo.append((m(z,a),m(z,b)))
 return {x:root(x) for x in S},'ok'
def pattern(h,S,cls,quads):
 m=h.mul
 for a,b,c,d in quads:
  abc=m(m(a,b),c)
  if cls[m(abc,a)]!=cls[a] or cls[abc]!=cls[m(a,c)]:continue
  u=m(m(abc,d),a)
  if cls[u]!=cls[a]:continue
  v=m(m(m(m(abc,a),c),d),a)
  if u!=v:return (a,b,c,d,u,v)
 return None
if __name__=='__main__':
 seed=int(sys.argv[1]);budget=float(sys.argv[2]);random.seed(seed)
 t0=time.time();stats={};hits=0
 while time.time()-t0<budget:
  I,L=random.choice([(2,2),(2,3),(3,2)]);swapB=random.random()<0.5
  P=[[random.randrange(2) for _ in range(I)] for _ in range(L)];P[0]=[0]*I
  for r in P:r[0]=0
  if all(P[l][i]==0 for l in range(L) for i in range(I)):continue
  h=Host(I,L,P,swapB);D=h.D
  ds=[random.choice(D) for _ in range(4)];ys=[random.randrange(4) for _ in range(4)]
  gens=[h.ix[((bb,yy),dd)] for bb,yy,dd in zip((1,0,5,2),ys,ds)]
  key=str((I,L,swapB));st=stats.setdefault(key,{'tried':0,'closed':0,'nonregular':0,'badfibre':0,'ok':0,'hits':0});st['tried']+=1
  if random.random()<0.7:
   extra=[]
   for g in gens:
    inv=[y for y in range(len(h.H)) if h.mul(h.mul(g,y),g)==g and h.mul(h.mul(y,g),y)==y]
    if inv:extra.append(random.choice(inv))
   gens=gens+extra
  S=closure(h,gens)
  if S is None:continue
  st['closed']+=1
  cls,status=analyse(h,S);st[status]+=1
  if status!='ok':continue
  quads=[tuple(gens[:4])]
  if len(S)<=30:quads=list(product(S,repeat=4))
  w=pattern(h,S,cls,quads)
  if w:
   st['hits']+=1;hits+=1
   print(json.dumps({'shape':key,'P':P,'size':len(S),'gens':[str(h.H[g]) for g in gens],'witness':[str(h.H[z]) for z in w]}));sys.stdout.flush()
   if hits>=3:break
 print(json.dumps({'seed':seed,'seconds':round(time.time()-t0,1),'stats':stats,'hits':hits}))
