from itertools import product
from collections import Counter
D=list(product(range(2),repeat=3));S=list(product(range(2),[-1,0,1],range(2)));H=list(product(range(2),D))
def dm(x,y):
 i,g,l=x;j,h,m=y;return(i,g^(l&j)^h,m)
def sm(x,y):
 if x is None:return y
 if y is None:return x
 i,a,l=x;j,b,m=y;return(i,-1 if a==-1 or b==-1 else a^(l&j)^b,m)
def hm(x,y):return(min(x[0],y[0]),dm(x[1],y[1]))
def cover(x):
 t,(i,g,l)=x;return(i,g if t else -1,l)
ES={s for s in S if sm(s,s)==s};EH={s for s in H if hm(s,s)==s}
assert len(S)==12 and len(H)==16 and len(ES)==len(EH)==8
assert set(map(cover,H))==set(S) and len({cover(e) for e in EH})==8
assert all(cover(hm(x,y))==sm(cover(x),cover(y)) for x,y in product(H,repeat=2))
assert all(sm(sm(x,y),z)==sm(x,sm(y,z)) for x,y,z in product(S,repeat=3))
assert all(any(sm(sm(x,y),x)==x and sm(sm(y,x),y)==y for y in S) for x in S)
for e in ES:
 C={sm(sm(e,s),e) for s in S};EC=C&ES
 assert all(sm(x,y)==sm(y,x) in EC for x,y in product(EC,repeat=2))
 U={f for f in ES if sm(e,f)==sm(f,e)==e}
 assert all(sm(x,y)==sm(y,x) in U for x,y in product(U,repeat=2))
z=(0,-1,0);a=(0,1,0)
assert z in ES and a not in ES and sm(z,a)==sm(a,z)==z
# Full idempotence contexts, including both formal absent-factor cases.
X=[None]+S
sig={s:tuple(sm(sm(x,s),y) in ES for x,y in product(X,repeat=2)) for s in S}
def q(s):return 'zero' if s[1]==-1 else s
Q=D+['zero']
def qm(x,y):return 'zero' if x=='zero' or y=='zero' else dm(x,y)
assert len(set(sig.values()))==9
assert all((sig[s]==sig[t])==(q(s)==q(t)) for s,t in product(S,repeat=2))
assert all(q(sm(s,t))==qm(q(s),q(t)) for s,t in product(S,repeat=2))
assert all((s in ES)==(qm(q(s),q(s))==q(s)) for s in S)
EQ={e for e in Q if qm(e,e)==e}
assert qm((0,0,0),(1,1,1)) not in EQ and all(qm('zero',e)==qm(e,'zero')=='zero' for e in EQ)
def rectangular_e_blocks(V,m):
 n=len(V);ix={v:i for i,v in enumerate(V)};T=[[ix[m(x,y)] for y in V] for x in V];pr=list(range(n));pc=list(range(n))
 def root(p,x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for x,y in product(range(n),repeat=2):pr[root(pr,T[x][y])]=root(pr,x);pc[root(pc,T[x][y])]=root(pc,y)
 B={}
 for e in range(n):
  if T[e][e]==e:B.setdefault((root(pr,e),root(pc,e)),[]).append(e)
 bad=[(V[e],V[f],V[T[e][f]]) for b in B.values() for e,f in product(b,repeat=2) if T[T[e][f]][T[e][f]]!=T[e][f]]
 return len({root(pr,e) for e in range(n)}),len({root(pc,e) for e in range(n)}),sorted(map(len,B.values())),bad
rS=rectangular_e_blocks(S,sm);rQ=rectangular_e_blocks(Q,qm)
assert rS[:3]==(2,2,[2,2,2,2]) and not rS[3]
assert rQ[:3]==(1,1,[5]) and rQ[3]
print('PASS physical SL2-by-D8 host16 ->source12 onto/idempotent-separating; ALL256products')
print('PASS source12:1728associativity,regular,locallyinverse,ALLupperconesSL,butNONORTH andNONWEU')
print('PASS actual syntactic quotient9=D8^zero:2028fullcontexttests,all144quotientproducts,andpurity')
print('PASS source finestRECT2x2:Eblocks2,2,2,2; quotient finestRECT1:Eblock5NOTclosed')
print('RESULT Q2 eligibility is NOTpreserved by ACTUALidempotent-pure syntacticquotients: positive12->negative9')
