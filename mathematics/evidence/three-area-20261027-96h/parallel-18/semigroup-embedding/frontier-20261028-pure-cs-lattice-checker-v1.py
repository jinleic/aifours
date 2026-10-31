from itertools import product
S=list(product(range(2),range(2),range(3)))
def mul(x,y):return x[0],x[1]^y[1],y[2]
def partitions(n):
 out=[]
 def go(seq):
  if len(seq)==n:out.append(tuple(seq));return
  for v in range(max(seq)+2):go(seq+[v])
 go([0]);return out
R=partitions(2);C=partitions(3)
assert len(R)==2 and len(C)==5
sigs={}
contexts=[None]+S
for s in S:
 sig=[]
 for x,y in product(contexts,repeat=2):
  t=s if x is None else mul(x,s)
  if y is not None:t=mul(t,y)
  sig.append(mul(t,t)==t)
 sigs[s]=tuple(sig)
assert len(set(sigs.values()))==2
assert all((sigs[x]==sigs[y])==(x[1]==y[1]) for x,y in product(S,repeat=2))
kernels=set()
for rr,cc in product(R,C):
 def actor(s):return rr[s[0]],s[1],cc[s[2]]
 def amul(x,y):return x[0],x[1]^y[1],y[2]
 assert all(actor(mul(x,y))==amul(actor(x),actor(y)) for x,y in product(S,repeat=2))
 assert all((amul(actor(s),actor(s))==actor(s))==(mul(s,s)==s) for s in S)
 kernel=frozenset((i,j) for i,x in enumerate(S) for j,y in enumerate(S) if actor(x)==actor(y))
 kernels.add(kernel)
assert len(kernels)==10
print('PASS rectangular-group source12, actual q=C2, Bell(2)*Bell(3)=10 distinct pure CS quotient kernels')
print('checked all actor product equations and idempotent purity; not a proof of the universal theorem')
