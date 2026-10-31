"""Exact positive certificates (NOT a universal proof).  Builds the 748-element band Q4 from the
candidate free-RIGHTSN normal form nf(w)=(first letter, last-new-letter-from-right, nf(suffix)),
verifies it is a band with right-regular local monoids at EVERY element, then for random 2-generated
right-regular-local (RRL) original sources inside P(B5^1,D8) builds the presented band Q4/theta for
the canonical relations X_(u,sa)=X_(u,s)X_(u w(s,a),a), checks theta is invariant under the C2
relabelling automorphism, and verifies the induced physical host exactly: every source product and
injectivity on equal-actor pairs.  It also records that sources which are NOT RRL collapse here."""
import sys,random,importlib.util
from itertools import product
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('sn2',root/'frontier-20261029-SN-pattern-counterexample-search-v2.py');sn2=importlib.util.module_from_spec(sp);sp.loader.exec_module(sn2)
def nf(w):
 c=set(w)
 if len(c)==1:return w[0]
 seen=set();j=len(w)-1
 while True:
  seen.add(w[j])
  if len(seen)==len(c):break
  j-=1
 return (w[0],w[j],nf(w[j+1:]))
def rep(k):
 if not isinstance(k,tuple):return (k,)
 a,b,s=k;return ((a,) if a!=b else ())+(b,)+rep(s)
els=[nf((x,)) for x in 'abcd'];ix={e:i for i,e in enumerate(els)};fr=list(range(4))
while fr:
 new=[]
 for i in list(range(len(els))):
  for j in fr:
   for p,q in ((i,j),(j,i)):
    k=nf(rep(els[p])+rep(els[q]))
    if k not in ix:ix[k]=len(els);els.append(k);new.append(ix[k])
 fr=new
n=len(els);Q=np.array([[ix[nf(rep(els[i])+rep(els[j]))] for j in range(n)] for i in range(n)],dtype=np.int32)
assert n==748 and all(Q[x,x]==x for x in range(n))
assert all(np.array_equal(Q[Q[x]],Q[x][Q]) for x in range(n))
for e in range(n):
 u=Q[Q[e],e];U=Q[np.ix_(u,u)];assert np.array_equal(Q[U,u[:,None]],U.T)
REL={'a':'c','b':'d','c':'a','d':'b'};rl=np.array([ix[nf(tuple(REL[c] for c in rep(els[k])))] for k in range(n)])
assert all(np.array_equal(rl[Q[x]],Q[rl[x]][rl]) for x in range(n))
print('PASS Q4: 748 elements, band, associativity, right-regular local monoids at every element, relabelling automorphism')
L=[ix[nf((c,))] for c in 'abcd'];P=((0,0),(0,1))
def certify(M,act,gens):
 N=len(M);w=lambda s,t:act[s][1]^P[act[s][2]][act[t][0]]
 X={(u,j):L[u*2+j] for u in (0,1) for j in (0,1)};W={gens[0]:X[(0,0)],gens[1]:X[(0,1)]};rels=[];front=list(W)
 while front:
  new=[]
  for s in front:
   for j,a in enumerate(gens):
    t=M[s][a];c=int(Q[W[s],X[(w(s,a),j)]])
    if t not in W:W[t]=c;new.append(t)
    else:rels.append((W[t],c))
  front=new
 if len(W)!=N:return None
 rels+=[(int(rl[a]),int(rl[b])) for a,b in rels]
 par=list(range(n))
 def r(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 todo=list(rels)
 while todo:
  a,b=todo.pop();ra,rb=r(a),r(b)
  if ra==rb:continue
  par[rb]=ra
  for z in range(n):todo.append((int(Q[a,z]),int(Q[b,z])));todo.append((int(Q[z,a]),int(Q[z,b])))
 cls=[r(x) for x in range(n)]
 assert all(cls[rl[x]]==cls[rl[y]] for x in range(n) for y in (par[x],) )  # theta relabel-invariant on generators of classes
 beta={s:cls[W[s]] for s in range(N)};relab_cls={cls[x]:cls[rl[x]] for x in range(n)}
 for s,t in product(range(N),repeat=2):
  bt=relab_cls[beta[t]] if w(s,t) else beta[t]
  if beta[M[s][t]]!=cls[int(Q[W[s],[x for x in range(n) if cls[x]==bt][0]])]:return 'equation-fail'
 return all(beta[s]!=beta[t] for s in range(N) for t in range(s+1,N) if act[s]==act[t])
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 31);need=int(sys.argv[2]) if len(sys.argv)>2 else 60
cfg=[(d,a) for d in (False,True) for a in ('trivial','swap')];tab={c:sn2.make(*c) for c in cfg};done={'RRL_faithful':0,'RRL_collapsed':0,'nonRRL_collapsed':0,'nonRRL_faithful':0};rrl_with_localR=0
while done['RRL_faithful']+done['RRL_collapsed']<need:
 c=random.choice(cfg);H,T=tab[c];g=random.sample(range(48),2);S=sn2.closure(T,g)
 if sn2.analyse(H,T,S) is None:continue
 pos={s:k for k,s in enumerate(S)};M=[[pos[T[a][b]] for b in S] for a in S];act=[H[s][1] for s in S]
 E=[x for x in range(len(S)) if M[x][x]==x];C=[[x for x in E if M[M[e][x]][e]==x] for e in E]
 rrl=all(M[M[x][y]][x]==M[y][x] for K in C for x in K for y in K)
 res=certify(M,act,[pos[g[0]],pos[g[1]]])
 if res is None:continue
 assert res!='equation-fail'
 key=('RRL_' if rrl else 'nonRRL_')+('faithful' if res else 'collapsed');done[key]+=1
 if rrl and any(M[x][y]==y and M[y][x]==x and x!=y for K in C for x in K for y in K):rrl_with_localR+=1
assert done['RRL_collapsed']==0
print('PASS',done,'RRL sources with local R-pairs among them:',rrl_with_localR)
