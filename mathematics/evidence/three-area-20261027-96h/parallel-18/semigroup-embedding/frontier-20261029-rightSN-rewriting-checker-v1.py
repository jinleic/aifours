"""(1) Exact control: on all words of length <=7 over 3 letters, the rewriting rules
   (I) A x x B -> A x B,   (D) A x B -> A B  if A nonempty, x in c(B) and last(A) in c(B)
are sound for the candidate free-RIGHTSN normal form nf(w)=(first,last-new-letter-from-right,nf(suffix))
and greedy reduction reaches the canonical representative of every class (51 classes).
(2) Negative control: for S45 with its actor, label-adjacent consistency of words over labelled
letters (u,s) is NOT preserved by rule (D): many consistent words become inconsistent."""
from itertools import product
import random
def nf(w):
 c=set(w)
 if len(c)==1:return (w[0],)
 seen=set();j=len(w)-1
 while True:
  seen.add(w[j])
  if len(seen)==len(c):break
  j-=1
 return (w[0],w[j],nf(w[j+1:]))
def rep(k):
 if len(k)==1:return (k[0],)
 a,b,s=k;return ((a,) if a!=b else ())+(b,)+rep(s)
def reduce(w):
 ch=True
 while ch:
  ch=False
  for k in range(len(w)-1):
   if w[k]==w[k+1]:w=w[:k]+w[k+1:];ch=True;break
  if ch:continue
  for k in range(1,len(w)-1):
   if w[k] in w[k+1:] and w[k-1] in w[k+1:]:w=w[:k]+w[k+1:];ch=True;break
 return w
words=[w for L in range(1,8) for w in product('abc',repeat=L)]
for w in words:
 for k in range(len(w)-1):
  if w[k]==w[k+1]:assert nf(w)==nf(w[:k]+w[k+1:])
 for k in range(1,len(w)-1):
  if w[k] in w[k+1:] and w[k-1] in w[k+1:]:assert nf(w)==nf(w[:k]+w[k+1:])
 assert reduce(w)==rep(nf(w))
print('PASS rules (I),(D) sound for nf and greedy reduction gives the canonical representative for all',len(words),'words; classes',len({nf(w) for w in words}))
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));PP=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S=list(product(range(3),range(5),range(3)));ix={s:k for k,s in enumerate(S)}
M=[[ix[(a[0],T[T[a[1]][PP[a[2]][b[0]]]][b[1]],b[2])] for b in S] for a in S]
act=[(a[0],th[a[1]],a[2]) for a in S];Pq=[[th[PP[l][i]] for i in range(3)] for l in range(3)]
wt=lambda s,t:(act[s][1]+Pq[act[s][2]][act[t][0]])%2
def ev(w):
 u0,cur=w[0]
 for u,s in w[1:]:
  if u!=(u0+wt(cur,s))%2:return None
  cur=M[cur][s]
 return (u0,cur)
rnd=random.Random(0);broken=0;total=0
for _ in range(20000):
 al=rnd.sample(range(45),rnd.randint(2,4));u0=rnd.randrange(2);s=rnd.choice(al);w=[(u0,s)];cur=s
 for _ in range(rnd.randint(3,9)):
  t=rnd.choice(al);w.append(((u0+wt(cur,t))%2,t));cur=M[cur][t]
 assert ev(w) is not None
 for k in range(1,len(w)-1):
  A,x,B=w[:k],w[k],w[k+1:]
  if x in B and A[-1] in B:
   total+=1;broken+=ev(A+B) is None
assert broken>0
print('NEGATIVE CONTROL S45: rule (D) applied to consistent labelled words broke consistency in',broken,'of',total,'instances')
